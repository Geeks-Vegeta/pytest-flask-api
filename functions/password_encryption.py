from passlib.hash import sha256_crypt


def generate_passwords(list_password):
    for x in list_password:
        password = sha256_crypt.hash(x)
        print(f"{x} {password}")

passwords = ["shreyas123", "shreyas!123"]
generate_passwords(passwords)