import pyotp

secret_key = ""


def main(secret_key) -> str:
    totp = pyotp.TOTP(secret_key)
    otp = totp.now()
    return otp


if __name__ == "__main__":
    print(main(secret_key=secret_key))
