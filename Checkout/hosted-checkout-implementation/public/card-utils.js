/*
 * card-utils.js
 * Pure helpers for the hosted checkout card forms (card + Bancontact card).
 * No DOM access and no dependencies, so it runs in the browser and under `node --test`.
 *
 * SECURITY NOTE: these helpers only format and validate what the user types for
 * display purposes. In production the PAN / CVC must be captured by the PSP's
 * hosted fields (PCI SAQ-A). Never send raw card data to the gateway in this repo.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.CardUtils = factory();
  }
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var digitsOf = function (v) {
    return String(v == null ? '' : v).replace(/\D/g, '');
  };

  /** 'visa' | 'mastercard' | 'amex' | '' (unknown) from the leading digits. */
  function detectBrand(digits) {
    var d = digitsOf(digits);
    if (/^4/.test(d)) return 'visa';
    if (/^(5[1-5]|222[1-9]|22[3-9]\d|2[3-6]\d\d|27[01]\d|2720)/.test(d)) return 'mastercard';
    if (/^3[47]/.test(d)) return 'amex';
    return '';
  }

  function groupsFor(brand) {
    return brand === 'amex' ? [4, 6, 5] : [4, 4, 4, 4];
  }

  function maxLength(brand) {
    return brand === 'amex' ? 15 : 16;
  }

  function cvcLength(brand) {
    return brand === 'amex' ? 4 : 3;
  }

  /** "4242424242424242" -> "4242 4242 4242 4242" (Amex 4-6-5). Truncates to max length. */
  function formatNumber(raw, brand) {
    var b = brand === undefined ? detectBrand(raw) : brand;
    var d = digitsOf(raw).slice(0, maxLength(b));
    var out = [];
    var i = 0;
    groupsFor(b).forEach(function (g) {
      if (i < d.length) out.push(d.slice(i, i + g));
      i += g;
    });
    return out.join(' ');
  }

  /** Same grouping, padded with bullets for the card face: "4242 •••• •••• ••••". */
  function maskedDisplay(raw, brand) {
    var b = brand === undefined ? detectBrand(raw) : brand;
    var d = digitsOf(raw).slice(0, maxLength(b));
    var groups = groupsFor(b);
    var start = 0;
    return groups
      .map(function (g) {
        var part = d.slice(start, start + g);
        start += g;
        return part + '•'.repeat(g - part.length);
      })
      .join(' ');
  }

  function luhn(raw) {
    var d = digitsOf(raw);
    var sum = 0;
    var alt = false;
    for (var i = d.length - 1; i >= 0; i--) {
      var n = Number(d[i]);
      if (alt) {
        n *= 2;
        if (n > 9) n -= 9;
      }
      sum += n;
      alt = !alt;
    }
    return d.length > 0 && sum % 10 === 0;
  }

  /** Complete (right length for the brand) and passes Luhn. */
  function isNumberValid(raw) {
    var d = digitsOf(raw);
    return d.length === maxLength(detectBrand(d)) && luhn(d);
  }

  /** "1" -> "01", "13" -> "12", "1234" -> "12/34". Used on every keystroke. */
  function formatExpiry(raw) {
    var d = digitsOf(raw).slice(0, 4);
    if (d.length >= 1 && d[0] > '1') d = '0' + d;
    if (d.length >= 2 && Number(d.slice(0, 2)) > 12) d = '12' + d.slice(2);
    d = d.slice(0, 4);
    return d.length > 2 ? d.slice(0, 2) + '/' + d.slice(2) : d;
  }

  function isExpiryComplete(raw) {
    return digitsOf(raw).length === 4;
  }

  /** MM/YY is a real month and not in the past (valid through the last day of the month). */
  function isExpiryValid(raw, now) {
    var d = digitsOf(raw);
    if (d.length !== 4) return false;
    var m = Number(d.slice(0, 2));
    var y = 2000 + Number(d.slice(2));
    var ref = now || new Date();
    return m >= 1 && m <= 12 && (y > ref.getFullYear() || (y === ref.getFullYear() && m >= ref.getMonth() + 1));
  }

  function sanitizeName(v) {
    return String(v == null ? '' : v).replace(/[0-9]/g, '').slice(0, 26);
  }

  function isNameValid(v) {
    return String(v == null ? '' : v).trim().length > 1;
  }

  function sanitizeCvc(v, brand) {
    return digitsOf(v).slice(0, cvcLength(brand));
  }

  return {
    digitsOf: digitsOf,
    detectBrand: detectBrand,
    groupsFor: groupsFor,
    maxLength: maxLength,
    cvcLength: cvcLength,
    formatNumber: formatNumber,
    maskedDisplay: maskedDisplay,
    luhn: luhn,
    isNumberValid: isNumberValid,
    formatExpiry: formatExpiry,
    isExpiryComplete: isExpiryComplete,
    isExpiryValid: isExpiryValid,
    sanitizeName: sanitizeName,
    isNameValid: isNameValid,
    sanitizeCvc: sanitizeCvc
  };
});
