import hashlib
import secrets

def generate_hash():
    random_string = secrets.token_bytes(16)
    hash_object = hashlib.sha256()
    hash_object.update(random_string)
    hex_dig = hash_object.hexdigest()
    return hex_dig

