from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    ingestion_dir: Path
    books_data_file: Path
    ratings_data_file: Path
    users_data_file: Path 

@dataclass
class DataValidationConfig:
    validation_dir: Path
    status_filepath: Path
    required_files: list

@dataclass 
class DataTransformerConfig:
    transformer_dir: Path
    books_df_dir: Path
    final_df_dir: Path

@dataclass
class ModelTrainerConfig:
    model_trainer_dir: Path
    model_path: Path
    similarity_score: Path
    data_path: Path