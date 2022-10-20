import Task01_check_password


def main():
    password = input("Input password: ")

    result = Task01_check_password.check_password(password)

    msg = f"Your password is {result}" if isinstance(result, str) \
        else "User data invalid"

    print(msg)


if __name__ == "__main__":
    main()
