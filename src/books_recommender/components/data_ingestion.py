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
        books_df = get_data(coll_name="books_data")
        books_df.to_csv(self.config.books_data_file, index=False)
        logging.info(f"books data saved successfully at {self.config.books_data_file}")

        ratings_df = get_data(coll_name="ratings_data")
        ratings_df.to_csv(self.config.ratings_data_file, index=False)
        logging.info(f"ratings data saved successfully at {self.config.ratings_data_file}")

        users_df = get_data(coll_name="users_data")
        users_df.to_csv(self.config.users_data_file, index=False)
        logging.info(f"users data saved successfully at {self.config.users_data_file}")


        # df_train, df_test = train_test_split(df, test_size=0.2)
        # df_train.to_csv(self.config.train_data_file)
        # logging.info(f"training data saved successfully at {self.config.train_data_file}")
        # df_test.to_csv(self.config.test_data_file)
        # logging.info(f"test data saved successfully at {self.config.test_data_file}")

