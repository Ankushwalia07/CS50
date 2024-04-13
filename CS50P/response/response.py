import validators

def validate_email(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

def main():
    user_email = input("Please enter your email address: ")
    result = validate_email(user_email)
    print(result)

if __name__ == "__main__":
    main()
