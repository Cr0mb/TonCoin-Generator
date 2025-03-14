import secrets
from tonsdk.contract.wallet import Wallets, WalletVersionEnum
import requests
import time
import json
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

API_URL = 'https://toncenter.com/api/v2/getAddressInformation?address={}'
OUTPUT_FILE = "wallets_with_balance.txt"

def print_title():
    title = pyfiglet.figlet_format("TonCoin Generator")
    print(Fore.CYAN + title)
    print(Fore.GREEN + "Made by Cr0mb\n")

def clear_screen():
    print("\033[H\033[J", end="")

def get_ton_balance(address):
    print(f"{Fore.CYAN}Fetching balance for address: {address}\n")
    
    try:
        response = requests.get(API_URL.format(address))
        data = response.json()

        if not data.get("ok"):
            print(f"{Fore.RED}Error: {data.get('result', 'Unknown error')}")
            if data.get('code') == 429:
                print(f"{Fore.YELLOW}Rate limit exceeded. Sleeping for 10 seconds...\n")
                time.sleep(10)
            return None
        
        if isinstance(data, dict) and 'result' in data:
            print(f"{Fore.GREEN}Pretty response:")
            print(f"{Style.BRIGHT}{json.dumps(data['result'], indent=4)}\n")
            balance = data['result']['balance']
            return balance / 10**9
        
        else:
            print(f"{Fore.RED}Error: Unexpected response structure for address {address}\n")
            return None

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Request error: {e}\n")
        return None
    except ValueError as e:
        print(f"{Fore.RED}JSON decode error: {e}\n")
        return None

def generate_wallet():
    print(f"{Fore.MAGENTA}Generating wallet...\n")
    mnemonics, pub_key, priv_key, wallet = Wallets.create(WalletVersionEnum.v4r2, workchain=0)
    address = wallet.address.to_string(True, True, False)
    return address, priv_key.hex(), mnemonics

def save_wallet_to_file(address, private_key, mnemonics, balance):
    with open(OUTPUT_FILE, "a") as file:
        file.write(f"Address: {address}\n")
        file.write(f"Private Key: {private_key}\n")
        file.write(f"Mnemonic: {' '.join(mnemonics)}\n")
        file.write(f"Balance: {balance} TON\n")
        file.write("-" * 40 + "\n")
    print(f"{Fore.GREEN}Wallet saved to {OUTPUT_FILE}\n")

def generate_wallets():
    while True:
        clear_screen()
        print_title()
        
        address, private_key, mnemonics = generate_wallet()
        
        print(f"{Fore.YELLOW}Address: {address}")
        print(f"{Fore.YELLOW}Private Key: {private_key}")
        print(f"{Fore.YELLOW}Mnemonic: {' '.join(mnemonics)}\n")
        
        balance = get_ton_balance(address)
        if balance is not None:
            print(f"{Fore.GREEN}Toncoin Balance: {balance} TON\n")
            if balance > 0:
                save_wallet_to_file(address, private_key, mnemonics, balance)
        else:
            print(f"{Fore.RED}Error fetching balance.\n")
        
        time.sleep(1)

if __name__ == "__main__":
    print_title()
    print(f"{Fore.BLUE}{Style.BRIGHT}Wallet Generator and Balance Checker\n")
    generate_wallets()
