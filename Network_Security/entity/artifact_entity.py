from dataclasses import dataclass #like a decorator

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str