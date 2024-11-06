import logging
import os
from datetime import datetime

LogFile = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path =  os.path.join(os.getcwd(), "logs", LogFile)
os.makedirs(logs_path, exist_ok= True)

LogFilePath = os.path.join(logs_path, LogFile)

logging.basicConfig(

    filename= LogFilePath,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO

)

