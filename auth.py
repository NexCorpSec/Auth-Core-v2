import bcrypt

def register_user(username, password):
    if database.find(username):
        return "Error: User already exists"

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    database.save({
        "username": username,
        "password": hashed_password
    })
    return "Success: User registered"

def login_user(username, provided_password):
    user_record = database.find(username)

    if not user_record:
        return "Error: Invalid credentials" # Keep it vague for security

    if bcrypt.checkpw(provided_password.encode('utf-8'), user_record['password']):
        token = generate_token(username)
        return {"status": "Login successful", "token": token}
    else:
        return "Error: Invalid credentials"
