import base64
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


def generateJWTKey():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    # convert into private_key into pem block 
    privatekey_pem_format = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    publickey_pem_format = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # convert into base64
    privatekey_base64_format = base64.b64encode(privatekey_pem_format).decode("utf-8")
    publickey_base64_format = base64.b64encode(publickey_pem_format).decode("utf-8")

    with open("../../.env", "a") as env_file:
        env_file.write(f"PRIVATE_KEY={privatekey_base64_format}\n")
        env_file.write(f"PUBLIC_KEY={publickey_base64_format}\n")


    print("Key successfully Generated")

