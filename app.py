import logging
from datetime import datetime, timezone

# Configure logging to output to a file with basic format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='a'  # Append mode to preserve previous logs
)

# Get the current UTC datetime
current_time = datetime.now(timezone.utc)

# Log the required message
logging.info(f"this message was logged at {current_time}")

# The script exits cleanly after logging