import os
import pandas as pd
import pymongo as mongo
from sklearn.model_selection import train_test_split
from pathlib import Path
from src.books_recommender.entity import DataIngestionConfig
from src.books_recommender.logger import logging
from src.books_recommender.utils.common import get_data
from dotenv import load_dotenv

load_dotenv()


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def downloadfile(self):
        host = os.getenv("host")
        port = os.getenv("port")
        connection_str = "mongodb://"+host+":"+port
        df = get_data(connection_str=connection_str)
        df.to_csv(self.config.data_file)
        logging.info(f"data saved successfully at {self.config.data_file}")

        df_train, df_test = train_test_split(df, test_size=0.2)
        df_train.to_csv(self.config.train_data_file)
        logging.info(f"training data saved successfully at {self.config.train_data_file}")
        df_test.to_csv(self.config.test_data_file)
        logging.info(f"test data saved successfully at {self.config.test_data_file}")

