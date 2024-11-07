import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


from src.components.data_transform import DataTransformation
from src.components.data_transform import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer




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
            df= pd.read_csv("notebook/stud.csv")
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
        

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()


    data_transformation = DataTransformation()
    train_arr , test_arr , _ = data_transformation.initiate_data_transformation(train_data, test_data)


    model_trainer = ModelTrainer()
    r2_score = model_trainer.initiate_model_trainer(train_arr , test_arr)
    print(r2_score)









        




        
    
