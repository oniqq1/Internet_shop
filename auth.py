import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password=password.encode(),salt=salt)
    return hashed

def check_password(password , hashed):
    return bcrypt.checkpw(password.encode(),hashed)