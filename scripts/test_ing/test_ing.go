package main

import (
	"crypto"
	"crypto/rand"
	"crypto/rsa"
	"crypto/sha256"
	"crypto/tls"
	"crypto/x509"
	"encoding/base64"
	"encoding/json"
	"encoding/pem"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
	"strings"
	"time"
)

type TokenResponse struct {
	AccessToken string `json:"access_token"`
	ExpiresIn   int    `json:"expires_in"`
	TokenType   string `json:"token_type"`
	Scope       string `json:"scope"`
}

func main() {
	cert, err := tls.LoadX509KeyPair("certs/example_client_tls.cer", "certs/example_client_tls.key")
	if err != nil {
		panic(err)
	}

	transport := &http.Transport{
		TLSClientConfig: &tls.Config{
			Certificates: []tls.Certificate{cert},
		},
	}
	client := &http.Client{
		Transport: transport,
		Timeout:   10 * time.Second,
	}

	// 1. Fetch OAuth token
	form := url.Values{}
	form.Set("grant_type", "client_credentials")
	form.Set("client_id", "5ca1ab1e-c0ca-c01a-cafe-154deadbea75")

	req, err := http.NewRequest("POST", "https://api.sandbox.ing.com/oauth2/token", strings.NewReader(form.Encode()))
	if err != nil {
		panic(err)
	}
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")
	req.Header.Set("Accept", "application/json")

	resp, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	fmt.Printf("Token status: %d\n", resp.StatusCode)
	var tokenResp TokenResponse
	if err := json.Unmarshal(body, &tokenResp); err != nil {
		panic(err)
	}
	fmt.Printf("Access Token acquired: %s...\n", tokenResp.AccessToken[:20])

	// 2. Test PS256 signing
	keyBytes, err := os.ReadFile("certs/example_client_signing.key")
	if err != nil {
		panic(err)
	}
	block, _ := pem.Decode(keyBytes)
	privKey, err := x509.ParsePKCS8PrivateKey(block.Bytes)
	if err != nil {
		privKey, err = x509.ParsePKCS1PrivateKey(block.Bytes)
		if err != nil {
			panic(err)
		}
	}
	rsaKey := privKey.(*rsa.PrivateKey)

	now := time.Now().UTC().Format(time.RFC3339)
	headerObj := map[string]interface{}{
		"b64":     false,
		"x5t#S256": "6sBLIUdEk-O9ULSwrTkDECfA6CO0mrzeLc0tXXyjxgM",
		"crit":    []string{"sigT", "sigD", "b64"},
		"sigT":    now,
		"sigD": map[string]interface{}{
			"pars": []string{"(request-target)", "digest", "content-type"},
			"mId":  "http://uri.etsi.org/19182/HttpHeaders",
		},
		"alg": "PS256",
	}
	hdrJSON, _ := json.Marshal(headerObj)
	hdrB64 := base64.RawURLEncoding.EncodeToString(hdrJSON)

	payloadJSON := `{"instructedAmount":{"currency":"EUR","amount":"149.00"},"creditorAccount":{"iban":"NL99INGB0001234567"},"creditorName":"CM Payments B.V.","remittanceInformationUnstructured":"Order 123"}`
	h := sha256.Sum256([]byte(payloadJSON))
	digestB64 := base64.StdEncoding.EncodeToString(h[:])
	digestHeader := "SHA-256=" + digestB64

	signingString := fmt.Sprintf("(request-target): post /v1/payments/sepa-credit-transfers\ndigest: %s\ncontent-type: application/json", digestHeader)
	dataToSign := fmt.Sprintf("%s.%s", hdrB64, signingString)

	hData := sha256.Sum256([]byte(dataToSign))
	sigBytes, err := rsa.SignPSS(rand.Reader, rsaKey, crypto.SHA256, hData[:], &rsa.PSSOptions{
		SaltLength: rsa.PSSSaltLengthEqualsHash,
	})
	if err != nil {
		panic(err)
	}
	sigB64 := base64.RawURLEncoding.EncodeToString(sigBytes)
	jws := fmt.Sprintf("%s..%s", hdrB64, sigB64)
	fmt.Printf("JWS Signature generated successfully: len=%d\n", len(jws))

	// 3. Test Payment Creation
	reqID := fmt.Sprintf("req-%d", time.Now().UnixNano())
	payReq, err := http.NewRequest("POST", "https://api.sandbox.ing.com/v1/payments/sepa-credit-transfers", strings.NewReader(payloadJSON))
	if err != nil {
		panic(err)
	}
	payReq.Header.Set("Authorization", "Bearer "+tokenResp.AccessToken)
	payReq.Header["x-jws-signature"] = []string{jws}
	payReq.Header.Set("Digest", digestHeader)
	payReq.Header.Set("Date", time.Now().UTC().Format(http.TimeFormat))
	payReq.Header.Set("X-Request-ID", reqID)
	payReq.Header.Set("PSU-IP-Address", "82.161.45.12")
	payReq.Header.Set("TPP-Redirect-URI", "http://localhost:8088/#success")
	payReq.Header.Set("Content-Type", "application/json")
	payReq.Header.Set("Accept", "application/json")

	payResp, err := client.Do(payReq)
	if err != nil {
		panic(err)
	}
	defer payResp.Body.Close()
	payBody, _ := io.ReadAll(payResp.Body)
	fmt.Printf("Payment HTTP status: %d\n", payResp.StatusCode)
	for k, v := range payResp.Header { fmt.Println(k, ":", v) }
fmt.Printf("Payment response body: %s\n", string(payBody))
}
