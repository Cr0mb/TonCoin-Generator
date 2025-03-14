# TonCoin-Generator
This script generates Toncoin wallets and checks their balances using the [TonCenter API](https://toncenter.com/api/v2/getAddressInformation?address={}). If a wallet contains a balance greater than zero, it is saved to a text file. The script uses the tonsdk library to generate wallets and requests to fetch wallet balance data.
