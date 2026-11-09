// Run with: node --test public/card-utils.test.js
const test = require('node:test');
const assert = require('node:assert/strict');
const C = require('./card-utils.js');

test('detectBrand', () => {
  assert.equal(C.detectBrand('4242'), 'visa');
  assert.equal(C.detectBrand('5555'), 'mastercard');
  assert.equal(C.detectBrand('2221'), 'mastercard');
  assert.equal(C.detectBrand('2720'), 'mastercard');
  assert.equal(C.detectBrand('2721'), '');
  assert.equal(C.detectBrand('3782'), 'amex');
  assert.equal(C.detectBrand('3400'), 'amex');
  assert.equal(C.detectBrand('6703'), '');
  assert.equal(C.detectBrand(''), '');
});

test('formatNumber groups 4-4-4-4 and Amex 4-6-5, truncating extra digits', () => {
  assert.equal(C.formatNumber('4242424242424242'), '4242 4242 4242 4242');
  assert.equal(C.formatNumber('42424242424242429999'), '4242 4242 4242 4242');
  assert.equal(C.formatNumber('378282246310005'), '3782 822463 10005');
  assert.equal(C.formatNumber('4242 42'), '4242 42');
  assert.equal(C.formatNumber('abc'), '');
});

test('maskedDisplay pads each group with bullets', () => {
  assert.equal(C.maskedDisplay(''), '•••• •••• •••• ••••');
  assert.equal(C.maskedDisplay('42424'), '4242 4••• •••• ••••');
  assert.equal(C.maskedDisplay('3782'), '3782 •••••• •••••');
});

test('luhn and isNumberValid', () => {
  assert.equal(C.luhn('4242424242424242'), true);
  assert.equal(C.luhn('4242424242424241'), false);
  assert.equal(C.luhn(''), false);
  assert.equal(C.isNumberValid('4242 4242 4242 4242'), true);
  assert.equal(C.isNumberValid('4242 4242 4242 424'), false); // incomplete
  assert.equal(C.isNumberValid('4242 4242 4242 4241'), false); // bad checksum
  assert.equal(C.isNumberValid('378282246310005'), true); // Amex, 15 digits
  assert.equal(C.isNumberValid('5555555555554444'), true);
});

test('cvcLength and sanitizeCvc follow the brand', () => {
  assert.equal(C.cvcLength('visa'), 3);
  assert.equal(C.cvcLength('amex'), 4);
  assert.equal(C.sanitizeCvc('12a345', 'visa'), '123');
  assert.equal(C.sanitizeCvc('12345', 'amex'), '1234');
});

test('formatExpiry auto-prefixes, clamps the month and inserts the slash', () => {
  assert.equal(C.formatExpiry('1'), '1');
  assert.equal(C.formatExpiry('2'), '02');
  assert.equal(C.formatExpiry('13'), '12');
  assert.equal(C.formatExpiry('1228'), '12/28');
  assert.equal(C.formatExpiry('12/28999'), '12/28');
  assert.equal(C.formatExpiry('0'), '0');
});

test('isExpiryValid is valid through the end of the month', () => {
  const now = new Date(2026, 10, 9); // 9 Nov 2026
  assert.equal(C.isExpiryValid('11/26', now), true);
  assert.equal(C.isExpiryValid('10/26', now), false);
  assert.equal(C.isExpiryValid('01/27', now), true);
  assert.equal(C.isExpiryValid('13/30', now), false);
  assert.equal(C.isExpiryValid('1', now), false);
  assert.equal(C.isExpiryComplete('11/26'), true);
  assert.equal(C.isExpiryComplete('11/2'), false);
});

test('name helpers', () => {
  assert.equal(C.sanitizeName('Ann3 Smith'), 'Ann Smith');
  assert.equal(C.sanitizeName('x'.repeat(40)).length, 26);
  assert.equal(C.isNameValid(' A '), false);
  assert.equal(C.isNameValid('Al'), true);
});
