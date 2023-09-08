from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    ingestion_dir: Path
    connection_str: str
    data_file: Path 
    train_data_file: Path
    test_data_file: Path
