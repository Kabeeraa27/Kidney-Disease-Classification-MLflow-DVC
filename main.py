from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


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
    

STAGE_NAME = "PREPARE BASE MODEL"
    
if __name__ == "__main__":
    try:
        logger.info(f"************************************************")
        logger.info(f">>>>>>>>>> STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<\n\nx=========================x")
    except Exception as e:
        logger.exception(e)
        raise e
