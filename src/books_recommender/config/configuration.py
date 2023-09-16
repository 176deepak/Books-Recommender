from src.books_recommender.constants import *
from src.books_recommender.entity import (DataIngestionConfig, DataValidationConfig, DataTransformerConfig)
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
            books_data_file = config.books_data_file,
            ratings_data_file = config.ratings_data_file,
            users_data_file = config.users_data_file,
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_dirs([config.validation_dir])

        data_validation_config = DataValidationConfig(
            validation_dir = config.validation_dir,
            status_filepath = config.status_filepath,
            required_files = config.required_files  
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformerConfig:
        config = self.config.data_transformation

        create_dirs([config.transformation_dir])

        data_transformation_config = DataTransformerConfig(
            transformer_dir=config.transformation_dir,
            books_df_dir=config.books_df_dir,
            final_df_dir=config.final_df_dir
        )
        
        return data_transformation_config