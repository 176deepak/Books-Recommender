import sys
from src.books_recommender.logger import logging
from src.books_recommender.exception import CustomException
import pandas as pd
from src.books_recommender.entity import ModelTrainerConfig
import pickle
from sklearn.metrics.pairwise import cosine_similarity


class ModelTrainer:
    def __init__(self, config:ModelTrainerConfig):
        self.config = config

    def train_model(self):
        try:
            df = pd.read_csv(r'artifacts\data_transformation\final.csv')
            pickle.dump(df,open(self.config.data_path,'wb'))
            logging.info(f"data file dumped successfully at {self.config.data_path}")

            model = df.pivot_table(index='Book-Title',columns='User-ID',values='Book-Rating')
            model.fillna(0,inplace=True)
            pickle.dump(model,open(self.config.model_path,'wb'))
            logging.info(f"model trained successfully and dumped at location {self.config.model_path}")

            similarity_scores = cosine_similarity(model)
            pickle.dump(similarity_scores,open(self.config.similarity_score,'wb'))
            logging.info(f"models similarity scores dummped successfully at {self.config.similarity_score}")
            
        except Exception as e:
            raise CustomException(e, sys)