import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Fix: Combine paths correctly
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create logs directory if it doesn't exist
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# Rest of your logging configuration
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

