from src.books_recommender.logger import logging
from src.books_recommender.components.model_trainer import ModelTrainer
from src.books_recommender.config.configuration import ConfigurationManager


class ModelTrainerPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train_model()