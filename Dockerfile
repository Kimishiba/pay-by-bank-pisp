# Production Dockerfile for Pay by Bank Gateway
FROM alpine:3.20

RUN apk --no-cache add ca-certificates tzdata curl

WORKDIR /app

COPY pay-by-bank-gateway /app/pay-by-bank-gateway
COPY public /app/public
COPY certs /app/certs

EXPOSE 8088
ENV PORT=8088

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8088/api/v1/banks || exit 1

ENTRYPOINT ["/app/pay-by-bank-gateway"]
