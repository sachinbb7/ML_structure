import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig():
    raw_data_path: str = os.path.join("artifacts", "raw.csv")
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config=  DataIngestionConfig()   

    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df= pd.read_csv("Users/sachinbb/Downloads/stud.csv")
            logging.info("Imported the dataset as DataFrame using pandas")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path) , exist_ok= True )
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header= True)

            logging.info("train test split initiated")
            train_test, test_split = train_test_split(df, test_size=0.2 , random_state= 11)
            train_test.to_csv(self.ingestion_config.train_data_path, index=False, header= True)
            test_split.to_csv(self.ingestion_config.test_data_path, index=False, header= True)
            logging.info("Data ingestion completed")

            return self.ingestion_config.train_data_path , self.ingestion_config.test_data_path

        except Exception as e:
            logging.info("Error occured during Data ingestion")
            raise CustomException(e , sys)
        

        


        
    