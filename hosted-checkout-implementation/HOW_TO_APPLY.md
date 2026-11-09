# Applying these changes

Unzip next to your clone, then from the repo root:

    git checkout -b feature/hosted-checkout-card-bancontact
    cp -R ../pay-by-bank-pisp-changes/public/. public/
    node --test public/card-utils.test.js
    git add public
    git commit -m "Hosted checkout: card form with live card, Bancontact screen, single Back button"
    git push -u origin feature/hosted-checkout-card-bancontact

Then open a PR and paste PR_DESCRIPTION.md as the description.
Note: public/checkout.html is replaced in full (the pay-by-bank flow and API calls are preserved).
