import os
import sys
from pathlib import Path
from src.books_recommender.logger import logging
from src.books_recommender.exception import CustomException
from src.books_recommender.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_files(self):
        validation_status = None

        try:
            data_files = os.listdir(os.path.join("artifacts", "data_ingestion"))
            for data_file in data_files:
                if data_file not in self.config.required_files:
                    validation_status = False
                    with open(self.config.status_filepath, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_filepath, 'w')   as f:
                        f.write(f"Validation status: {validation_status}")
        
            return validation_status

        except Exception as e:
            raise CustomException(e, sys)
        