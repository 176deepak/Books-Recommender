from src.books_recommender.pipeline.data_ingestion_pipeline import DataIngestionTraining
from src.books_recommender.pipeline.data_validation_pipeline import DataValidator
from src.books_recommender.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.books_recommender.pipeline.model_training import ModelTrainerPipeline
from src.books_recommender.logger import logging
from src.books_recommender.exception import CustomException


STAGE_NAME = "Data Ingestion"
try:
    logging.info(f"--------------------{STAGE_NAME} start--------------------")
    obj = DataIngestionTraining()
    obj.main()
    logging.info(f"------------------------{STAGE_NAME} end--------------------")
except Exception as e:
    raise e


STAGE_NAME = "Data Validation"
try:
    logging.info(f"--------------------{STAGE_NAME} start--------------------")
    obj = DataValidator()
    obj.main()
    logging.info(f"------------------------{STAGE_NAME} end--------------------")
except Exception as e:
    raise e

STAGE_NAME = "Data Transformation"
try:
    logging.info(f"--------------------{STAGE_NAME} start--------------------")
    obj = DataTransformationPipeline()
    obj.main()
    logging.info(f"------------------------{STAGE_NAME} end--------------------")
except Exception as e:
    raise e

STAGE_NAME = "Model Trainer"
try:
    logging.info(f"--------------------{STAGE_NAME} start--------------------")
    obj = ModelTrainerPipeline()
    obj.main()
    logging.info(f"------------------------{STAGE_NAME} end--------------------")
except Exception as e:
    raise e
