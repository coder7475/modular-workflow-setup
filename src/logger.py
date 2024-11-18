# Import required libraries
import os
import sys 
import logging
from datetime import datetime

# Create a log file name with current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Create path for log directory and file
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create logs directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)
# Set complete log file path
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure basic logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify log file location
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Define log message format
    level=logging.INFO  # Set logging level to INFO
)