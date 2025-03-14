![image](https://github.com/user-attachments/assets/c7f71731-62bd-4727-af65-c3a50eaf9311)


# TonCoin-Generator
This script generates Toncoin wallets and checks their balances using the [TonCenter API](https://toncenter.com/api/v2/getAddressInformation?address={}). If a wallet contains a balance greater than zero, it is saved to a text file. The script uses the tonsdk library to generate wallets and requests to fetch wallet balance data.


## Features
1. Generate Toncoin Wallets: Creates wallets with mnemonics, private keys, and addresses.
2. Balance Checking: Fetches the wallet balance from the TonCenter API.
3. Save Wallets with Positive Balances: If a wallet has a non-zero balance, it is saved to a file.
4. Rate Limit Handling: Implements rate limit handling with automatic retries.

## Requirements
Python 3.7 or higher
```
pip install tonsdk requests colorama pyfiglet
```


## How It Works
- Wallet Generation: The script generates a new Toncoin wallet using the tonsdk library, creating a public address, private key, and mnemonic phrase.
- Balance Fetching: The script uses the TonCenter API to fetch the balance of the generated wallet address. If the balance is greater than 0 TON, it saves the wallet data.
- Output: The script outputs the wallet information (address, private key, mnemonic, and balance) in the terminal and saves any wallet with a balance to the wallets_with_balance.txt file.

