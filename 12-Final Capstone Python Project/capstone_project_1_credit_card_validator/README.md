# Application Description

* Application takes in a credit card number
* Optional: Use a package to pass in arguments to the main script
* Application verifies if number is valid
* Application returns the credit card type
* Extra credit: Validate CCV2 number

## Validation algorithm
Credit card validation will be done using an implementation of the Luhn algorithm: https://www.geeksforgeeks.org/luhn-algorithm/

> The Luhn algorithm, also known as the modulus 10 or mod 10 algorithm, is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, Canadian Social Insurance Numbers. The LUHN formula was created in the late 1960s by a group of mathematicians. Shortly thereafter, credit card companies adopted it. Because the algorithm is in the public domain, it can be used by anyone. Most credit cards and many government identification numbers use the algorithm as a simple method of distinguishing valid numbers from mistyped or otherwise incorrect numbers. It was designed to protect against accidental errors, not malicious attacks.

## Credit card types
The following credit card types will be identified:
AMERICAN_EXPRESS
DINERS_CLUB
DISCOVER
ELO
HIPERCARD
HIPER
JCB
MAESTRO
MASTERCARD
MIR
UNIONPAY
VISA

The source object to identify cards is based on https://github.com/braintree/credit-card-type/blob/master/lib/card-types.js. This list also identifies the lenght of the security code and the name of the security code.