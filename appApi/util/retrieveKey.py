from typing import Literal
from django.http import HttpResponse, JsonResponse
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization
import os
import base64


def get_JWT_key(key_name: Literal["public_key", "private_key"]):
    """ 
    Retrieve key based on what has been passed via argument 
    
    Parameters:
        key_name (str): Must be the following value: "private_key" or "public_key"
    
    Return:
        key (str): avaliable for jwt token

    """

    print("IT ENTERED GET TOKEN KEY")
    load_dotenv()
    if key_name == "private_key" or key_name == "public_key":
        if key_name == "private_key":
            private_key_base64_format = os.getenv("PRIVATE_KEY")
            private_key_pem_format = base64.b64decode(private_key_base64_format)
            formatted_key = serialization.load_pem_private_key(private_key_pem_format)
            print("Now it about to exit")
            return formatted_key
        else:
            public_key_base64_format = os.getenv("PUBLIC_KEY")
            public_key_pem_format = base64.b64decode(public_key_base64_format)
            formatted_key = serialization.load_pem_public_key(public_key_pem_format)
            print("Now it about to exit")
            return formatted_key
    else:
        print("Now it about to exit")
        return ""
