from src.books_recommender.config import configuration
from src.books_recommender.components.data_validation import DataValidation
from src.books_recommender.logger import logging

class DataValidator:
    def __init__(self):
        pass

    def main(self):
        config = configuration.ConfigurationManager()
        data_ingestion_config = config.get_data_validation_config()
        validatior = DataValidation(data_ingestion_config)
        validatior.validate_files()

