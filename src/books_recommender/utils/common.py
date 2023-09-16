import os
import sys
import yaml
import pandas as pd
import pymongo as mongo
from pathlib import Path
from box import ConfigBox
from src.books_recommender.logger import logging
from src.books_recommender.exception import CustomException
from dotenv import load_dotenv
import pickle as pkl


load_dotenv()


def db_conn():
    try:
        host = os.getenv("host")
        port = os.getenv("port")
        connection_str = "mongodb://"+host+":"+port
        client = mongo.MongoClient(connection_str)
        logging.info("database connection established successfully...")

        return client
    except Exception as e:
        raise CustomException(e, sys)
        


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


def get_data(coll_name):
    try:
        client = db_conn()
        database = os.getenv("database")
        db = client[database]
        coll_df = db[coll_name]
        data = list(coll_df.find())
        df = pd.DataFrame(data, index = None)
        df.drop(['_id'], axis=1, inplace=True)
        logging.info(f"{coll_name} collection converted into dataframe successfully.")

        return df    
    except Exception as e:
        raise CustomException(e, sys)
    
    
def pickled_loader(filepath:Path):
    with open(filepath, 'rb') as file:
        obj = pkl.load(file)
    return obj

