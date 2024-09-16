from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "DATA INGESTION STAGE"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<\n\nx=========================x")
    except Exception as e:
        logger.exception(e)
        raise e