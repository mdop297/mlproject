import logging
import os, sys
from datetime import datetime

logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,"running_logs.log")

logging.basicConfig(
    format="[ %(asctime)s ] line number: %(lineno)d; module: %(name)s - %(levelname)s: %(module)s: %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]

)

log = logging.getLogger("mlproject")

