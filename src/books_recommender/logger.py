import os
import logging
from datetime import datetime

log_filename = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
log_dir = os.path.join(os.getcwd(), 'LOGS\Project_Logs')
os.makedirs(log_dir, exist_ok=True)
logfile_path = os.path.join(log_dir,log_filename)

with open(logfile_path, 'w') as log:
    pass

logging.basicConfig(
    filename=logfile_path,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)