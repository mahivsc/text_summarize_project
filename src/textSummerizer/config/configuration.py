from textSummerizer.constants import *
from textSummerizer.utils.common import read_yaml, create_directories
from textSummerizer.entity import DataIngestionConfig
from textSummerizer.entity import DataValidationConfig, DataTransformationConfig

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARMS_FILE_PATH):


            self.config = read_yaml(config_filepath)
            #print("Config:", self.config)  # Debugging: Print the read configuration
            self.parms= read_yaml(params_filepath)
            #print("Params:", self.params)  # Debugging: Print the read parameters


            create_directories([self.config.artifacts_root])



    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url= config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config
    


    def get_data_validation(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config =DataValidationConfig(
            root_dir= config.root_dir,
            STATUS_FILE= config.STATUS_FILE,
            ALL_REQUIRED_FILE= config.ALL_REQUIRED_FILES
        )

        return data_validation_config
    


    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config