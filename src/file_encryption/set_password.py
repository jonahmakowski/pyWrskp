import keyring

SERVICE_NAME = "obsidian_vault_encryptor"
USERNAME = "jonahmakowski"
PASSWORD = input("Enter the password to save: ")

keyring.set_password(SERVICE_NAME, USERNAME, PASSWORD)
print("Password saved to Keychain.")
