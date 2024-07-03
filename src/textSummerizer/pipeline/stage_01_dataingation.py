from textSummerizer.config.configuration import ConfigurationManager
from textSummerizer.components.data_ingestion import DataIngetion



class DataIngestionTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngetion(config=data_ingestion_config)
        data_ingestion.Download_file()
        data_ingestion.extract_zip_file()
       