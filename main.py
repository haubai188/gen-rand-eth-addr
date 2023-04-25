from web3.auto import w3
from eth_account import Account

# Generate a random private key
private_key = w3.eth.account.create().privateKey.hex()

# Derive the Ethereum address from the private key
account = Account.from_key(private_key)
address = account.address

print("Private key: ", private_key)
print("Ethereum address: ", address)
