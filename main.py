from textSummerizer.pipeline.stage_01_data_ingation import DataIngestionTrainingPipeline
from textSummerizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummerizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummerizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Trasformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e