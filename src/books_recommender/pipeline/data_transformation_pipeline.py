from src.books_recommender.logger import logging
from src.books_recommender.config.configuration import ConfigurationManager
from src.books_recommender.components.data_transformation import DataTransformer


class DataTransformationPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformer(data_transformation_config)
        data_transformation.transform_data()