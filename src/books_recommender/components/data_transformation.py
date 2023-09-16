import os
import sys
from pathlib import Path
import shutil
import numpy as np
import pandas as pd
from src.books_recommender.entity import DataTransformerConfig
from src.books_recommender.logger import logging
from src.books_recommender.exception import CustomException


class DataTransformer:
    def __init__(self, config: DataTransformerConfig):
        self.config = config


    def transform_data(self):
        try:
            books_df = pd.read_csv(r'artifacts/data_ingestion/books.csv')
            ratings_df = pd.read_csv(r'artifacts/data_ingestion/ratings.csv')
            total_ratings = ratings_df.groupby('ISBN').count()['Book-Rating'].reset_index()
            books_with_rating = books_df.merge(total_ratings,on='ISBN', how='inner')
            books_with_rating.to_csv(self.config.books_df_dir, index=False)
            logging.info(f"books data saved to {self.config.books_df_dir} successfully")


            books_with_ratings = pd.merge(books_df, ratings_df,on='ISBN')
            x = books_with_ratings.groupby('User-ID').count()['Book-Rating'] > 100
            knowledgeable_reader = x[x].index
            knowledgeable_reader_df = books_with_ratings[books_with_ratings['User-ID'].isin(knowledgeable_reader)]
            y = knowledgeable_reader_df.groupby('Book-Title').count()['Book-Rating']>=50
            famous_books = y[y].index
            final_df = knowledgeable_reader_df[knowledgeable_reader_df['Book-Title'].isin(famous_books)]

            final_df.to_csv(self.config.final_df_dir, index=False)
            logging.info(f"final_dataframe saved at {self.config.final_df_dir} successfully")
        except Exception as e:
            raise CustomException(e, sys)
