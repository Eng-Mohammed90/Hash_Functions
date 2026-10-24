import hashlib
import secrets
import hmac
from pathlib import Path

DATA_FILE = Path("users.txt")
SALT_BYTES = 16


def hash_password(password: str, salt: str) -> str:
    """Return the SHA-256 hash of password concatenated with salt."""
    combined = password + salt
    return hashlib.sha256(combined.encode("utf-8")).hexdigest()


def load_users() -> dict:
    """Load users from a text file: username|salt|password_hash."""
    users = {}
    if not DATA_FILE.exists():
        return users

    with DATA_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) == 3:
                username, salt, password_hash = parts
                users[username] = {"salt": salt, "hash": password_hash}
    return users


def register() -> None:
    username = input("Choose a username: ").strip()
    if not username or "|" in username:
        print("Invalid username. Please enter a non-empty name without '|'.")
        return

    users = load_users()
    if username in users:
        print("Registration failed: username already exists.")
        return

    password = input("Choose a password: ")
    if not password:
        print("Registration failed: password cannot be empty.")
        return

    salt = secrets.token_hex(SALT_BYTES)
    password_hash = hash_password(password, salt)

    with DATA_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{username}|{salt}|{password_hash}\n")

    print("Registration successful!")


def login() -> None:
    username = input("Username: ").strip()
    password = input("Password: ")

    users = load_users()
    user = users.get(username)
    if user is None:
        print("Login failed: invalid username or password.")
        return

    entered_hash = hash_password(password, user["salt"])
    if hmac.compare_digest(entered_hash, user["hash"]):
        print("Login successful. Welcome!")
    else:
        print("Login failed: invalid username or password.")


def main() -> None:
    while True:
        print("\n=== Password Hashing Authentication ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()