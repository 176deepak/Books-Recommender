from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    ingestion_dir: Path
    books_data_file: Path
    ratings_data_file: Path
    users_data_file: Path 
    # train_data_file: Path
    # test_data_file: Path

@dataclass
class DataValidationConfig:
    validation_dir: Path
    status_filepath: Path
    required_files: list