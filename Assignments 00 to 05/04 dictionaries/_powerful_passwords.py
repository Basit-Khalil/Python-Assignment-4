
import hashlib

def hash_password(password):
    """Given a password, return its SHA-256 hash."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Check if the given password's hash matches the stored hash.

    :param email: User's email
    :param password_to_check: Password entered by the user
    :param stored_logins: Dictionary of email -> hashed password
    :return: True if login is successful, otherwise False
    """
    hashed_password = hash_password(password_to_check)
    return stored_logins.get(email) == hashed_password

# Example usage:
stored_logins = {
    "user@example.com": hash_password("securepassword"),
    "admin@example.com": hash_password("faizee123"),
    "faizee956@gmail.com": hash_password("faizee123"),  # ✅ Add this entry
}

# Simulating user login
email = input("Enter your email: ")
password = input("Enter your password: ")

if login(email, password, stored_logins):
    print("Login successful!")
else:
    print("Invalid credentials.")