import bcrypt
import logging

# Set up debug logging to see what's happening behind the scenes
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("AuthDebug")

def login_user_debug(username, provided_password):
    logger.debug(f"Attempting login for user: {username}")

    # 1. Database Retrieval
    user_record = database.find(username)
    
    if not user_record:
        logger.warning(f"Login Failed: User '{username}' not found in DB.")
        return "Invalid credentials"

    # 2. Password Verification
    logger.debug("User found. Proceeding to hash comparison...")
    
    # In debug mode, we check if the stored hash is valid
    if not user_record['password'].startswith(b'$2b$'):
        logger.error("Critical: Stored password hash is corrupted or in wrong format!")
        return "Internal Error"

    if bcrypt.checkpw(provided_password.encode('utf-8'), user_record['password']):
        logger.info(f"Login Success: {username} authenticated.")
        return {"status": "Success", "token": "DEBUG_TOKEN_123"}
    else:
        logger.warning(f"Login Failed: Incorrect password for {username}.")
        return "Invalid credentials"
