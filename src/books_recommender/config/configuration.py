from src.books_recommender.constants import *
from src.books_recommender.entity import DataIngestionConfig
from src.books_recommender.utils.common import read_yaml, create_dirs


class ConfigurationManager:
    def __init__(
            self, 
            config_filepath = CONFIG_YAML_FILE,
            ):
        #params_filepath = PARAMS_YAML_FILE
        self.config = read_yaml(config_filepath)
        #self.params = read_yaml(params_filepath)

        create_dirs([self.config.artifacts_dir])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_dirs([config.ingestion_dir])

        data_ingestion_config = DataIngestionConfig(
            ingestion_dir = config.ingestion_dir,
            data_file = config.data_file,
            train_data_file = config.train_data_file,
            test_data_file = config.test_data_file,
        )

        return data_ingestion_config