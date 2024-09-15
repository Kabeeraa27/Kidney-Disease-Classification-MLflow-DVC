import os
import sys
import logging

# Define the logging format
logging_str = "[%(asctime)s] %(levelname)s: %(module)s: %(message)s"

# Define the directory and file path for log files
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format=logging_str,  # Set the logging format
    handlers=[
        logging.FileHandler(log_filepath),  # Log to a file
        logging.StreamHandler(sys.stdout)    # Log to the console
    ]
)

# Get a logger instance
logger = logging.getLogger("cnnClassifierLogger")

