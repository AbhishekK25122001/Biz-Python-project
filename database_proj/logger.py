import logging

def setup_logger(username):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Set logging level for the logger
    
    # Clear any existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Create a FileHandler with the username as the file name
    file_handler = logging.FileHandler(filename=f"{username}_logs.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    
    # Add the FileHandler to the logger
    logger.addHandler(file_handler)