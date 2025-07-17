import os
import sys
import hashlib
import json
import hmac
import keyring
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

SERVICE_NAME = "obsidian_vault_encryptor"
USERNAME = "jonahmakowski"  # Change as needed

# === Keychain integration ===
def get_password_from_keychain():
    pw = keyring.get_password(SERVICE_NAME, USERNAME)
    if pw is None:
        print(f"[!] No password found in Keychain for service '{SERVICE_NAME}' user '{USERNAME}'.")
        print("Please add it with:\n\n  keyring.set_password('"+SERVICE_NAME+"', '"+USERNAME+"', 'your-password')\n")
        sys.exit(1)
    return pw

# === Crypto helpers ===

def derive_key(password: str) -> bytes:
    return hashlib.sha256(password.encode()).digest()

def encrypt_data(data: bytes, key: bytes) -> bytes:
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(pad(data, AES.block_size))

def decrypt_data(data: bytes, key: bytes) -> bytes:
    iv = data[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(data[16:]), AES.block_size)

def encrypt_file(path: str, key: bytes):
    try:
        with open(path, 'rb') as f:
            data = f.read()
        encrypted = encrypt_data(data, key)
        with open(path, 'wb') as f:
            f.write(encrypted)
    except (PermissionError, OSError) as e:
        print(f"[!] Skipping encrypt (no permission): {path} ({e})")

def decrypt_file(path: str, key: bytes):
    try:
        with open(path, 'rb') as f:
            data = f.read()
        decrypted = decrypt_data(data, key)
        with open(path, 'wb') as f:
            f.write(decrypted)
    except (PermissionError, OSError, ValueError) as e:
        print(f"[!] Skipping decrypt (error): {path} ({e})")

# === Name encryption using HMAC-SHA256 ===

def encrypt_name(name: str, key: bytes) -> str:
    return hmac.new(key, name.encode(), hashlib.sha256).hexdigest()

def save_map(path: str, data: dict, key: bytes):
    try:
        with open(path + '.enc', 'wb') as f:
            f.write(encrypt_data(json.dumps(data).encode(), key))
    except Exception as e:
        print(f"[!] Failed saving map {path}.enc: {e}")

def load_map(path: str, key: bytes) -> dict:
    try:
        with open(path + '.enc', 'rb') as f:
            decrypted = decrypt_data(f.read(), key)
        return json.loads(decrypted.decode())
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"[!] Failed loading map {path}.enc: {e}")
        return {}

def delete_map(path: str):
    try:
        os.remove(path + '.enc')
    except FileNotFoundError:
        pass

# === Folder processing ===

def process_folder(folder: str, key: bytes, mode: str):
    print(f"[DEBUG] Walking folder: {folder}")
    for root, dirs, files in os.walk(folder, topdown=False):
        print(f"[DEBUG] In directory: {root}")
        print(f"  Files: {files}")
        print(f"  Dirs: {dirs}")

        file_map_path = os.path.join(root, '.filename_map.json')
        folder_map_path = os.path.join(root, '.folder_map.json')

        if mode == 'decrypt':
            file_map = load_map(file_map_path, key)
            folder_map = load_map(folder_map_path, key)
        else:
            file_map = {}
            folder_map = {}

        # --- Process files ---
        for name in files:
            if name in {'.filename_map.json.enc', '.folder_map.json.enc'}:
                continue
            full_path = os.path.join(root, name)

            if mode == "encrypt":
                encrypt_file(full_path, key)
                encrypted_name = encrypt_name(name, key)
                new_path = os.path.join(root, encrypted_name)
                try:
                    os.rename(full_path, new_path)
                    file_map[encrypted_name] = name
                    print(f"[+] Encrypted file: {name} → {encrypted_name}")
                except Exception as e:
                    print(f"[!] Failed renaming file {full_path}: {e}")

            elif mode == "decrypt":
                if name not in file_map:
                    print(f"[!] Skipping unknown file: {name}")
                    continue
                original_name = file_map[name]
                new_path = os.path.join(root, original_name)
                try:
                    os.rename(full_path, new_path)
                    decrypt_file(new_path, key)
                    print(f"[+] Decrypted file: {name} → {original_name}")
                except Exception as e:
                    print(f"[!] Failed renaming/decrypting file {full_path}: {e}")

        # Save or remove file map
        if mode == "encrypt":
            save_map(file_map_path, file_map, key)
        elif mode == "decrypt":
            delete_map(file_map_path)

        # --- Process folders ---
        for name in dirs:
            full_path = os.path.join(root, name)

            if mode == "encrypt":
                encrypted_name = encrypt_name(name, key)
                new_path = os.path.join(root, encrypted_name)
                try:
                    os.rename(full_path, new_path)
                    folder_map[encrypted_name] = name
                    print(f"[+] Encrypted folder: {name} → {encrypted_name}")
                except Exception as e:
                    print(f"[!] Failed renaming folder {full_path}: {e}")

            elif mode == "decrypt":
                if name not in folder_map:
                    print(f"[!] Skipping unknown folder: {name}")
                    continue
                original_name = folder_map[name]
                new_path = os.path.join(root, original_name)
                try:
                    os.rename(full_path, new_path)
                    print(f"[+] Decrypted folder: {name} → {original_name}")
                except Exception as e:
                    print(f"[!] Failed renaming folder {full_path}: {e}")

        # Save or remove folder map
        if mode == "encrypt":
            save_map(folder_map_path, folder_map, key)
        elif mode == "decrypt":
            delete_map(folder_map_path)


# === Main entry ===


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["encrypt", "decrypt"])
    parser.add_argument("folder")
    parser.add_argument("--password", help="Password to use for encryption/decryption (optional)")
    args = parser.parse_args()

    print(f"[DEBUG] Mode: {args.mode}")
    print(f"[DEBUG] Folder: {args.folder}")
    print(f"[DEBUG] Password received: {'Yes' if args.password else 'No'}")

    if args.password:
        password = args.password
    else:
        # fallback to keyring or prompt
        password = "fallbackpassword"  # just for testing

    key = derive_key(password)

    print("[DEBUG] Starting processing...")
    process_folder(args.folder, key, args.mode)
    print("[DEBUG] Processing finished.")

if __name__ == "__main__":
    main()
