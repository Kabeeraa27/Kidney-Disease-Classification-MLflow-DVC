from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


STAGE_NAME = "DATA INGESTION STAGE"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> {STAGE_NAME} STARTED <<<<<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> {STAGE_NAME} COMPLETED <<<<<<<<<<\n\nx=========================x")
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME = "PREPARE BASE MODEL"
    
if __name__ == "__main__":
    try:
        logger.info(f"************************************************")
        logger.info(f">>>>>>>>>> {STAGE_NAME} STARTED <<<<<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> {STAGE_NAME} COMPLETED <<<<<<<<<<\n\nx=========================x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "TRAINING"

if __name__ == "__main__":
    try:
        logger.info(f"************************************************")
        logger.info(f">>>>>>>>>> {STAGE_NAME} STARTED <<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> {STAGE_NAME} COMPLETED <<<<<<<<<<\n\nx=========================x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "EVALUATION"

if __name__ == "__main__":
    try:
        logger.info(f"************************************************")
        logger.info(f">>>>>>>>>> {STAGE_NAME} STARTED <<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> {STAGE_NAME} COMPLETED <<<<<<<<<<\n\nx=========================x")
    except Exception as e:
        logger.exception(e)
        raise e
