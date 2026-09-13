# Unified Receiving Policy

All BizXtreme game purchase flows use the following receiving configuration:

- **Primary crypto receiver:** `0x0B4fF3fc6AE19fAF9A0d2628a646ABD9636B1162` on Ethereum.
- **Primary PayPal receiver:** `amer.hwaitat@gmail.com`.
- Default payment method: Ethereum.
- PayPal is the fallback/alternative checkout method.
- The game must present the payment method and amount clearly and require the buyer's explicit approval before a production transaction.

## Security

This file contains receiving identifiers only. It must never contain wallet private keys, seed phrases, PayPal client secrets, OAuth tokens, API keys, or webhook signing secrets.

PayPal production integration must use server-side credentials stored in deployment secrets/environment variables. PayPal's current Checkout documentation requires a client ID and server-side credentials for order creation/capture; credentials must not be committed to source control.

Crypto transfers remain non-custodial: the game prepares the transaction and the user's wallet explicitly authorizes/signs it.
