from src.books_recommender.config import configuration
from src.books_recommender.components.data_ingestion import DataIngestion
from src.books_recommender.logger import logging


class DataIngestionTraining:
    def __init__(self):
        pass


    def main(self):
        config = configuration.ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.downloadfile()


if __name__ == '__main__':
    obj = DataIngestionTraining()
    obj.main()