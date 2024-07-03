import os
import urllib.request as request
import zipfile
from textSummerizer.utils.common import get_size
from textSummerizer.logging import logger
from textSummerizer.entity import DataIngestionConfig
from pathlib import Path

class DataIngetion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def Download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_url,
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} download1! with following info:\n{headers}")
        else:
            logger.info(f"file already exits of size: {get_size(Path(self.config.local_data_file))}")



    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        if not zipfile.is_zipfile(self.config.local_data_file):
            raise zipfile.BadZipFile(f"File {self.config.local_data_file} is not a zip file")
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)