import os
import sys
import yaml
import pandas as pd
import pymongo as mongo
from pathlib import Path
from box import ConfigBox
from src.books_recommender.logger import logging
from src.books_recommender.exception import CustomException


def read_yaml(path):
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise e
    

def create_dirs(paths:list):
    for path in paths:
        path = Path(path)
        os.makedirs(path, exist_ok=True)
        logging.info(f"Created directory at {path}")


def get_data(connection_str):
    try:
        client = mongo.MongoClient(connection_str)
        logging.info("Connection to mongodb is established")

        db = client.recommender_app_data
        collection = db.books_data
        cursor = collection.find()
        data = list(cursor)
        df = pd.DataFrame(data)
        df.drop(['_id'], axis=1, inplace = True)
        logging.info("collection's data extracted successfully")
        
        return df
    except Exception as e:
        raise CustomException(e, sys)
    



