import re

def check_password_strength(password):
    """Check the strength of a given password."""
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def main():
    password = input("Enter your password: ")
    if check_password_strength(password):
        print("Password is strong.")
    else:
        print("Password is weak. Make sure it is at least 8 characters long, contains upper and lower case letters, includes a digit, and has a special character.")

if __name__ == "__main__":
    main()
