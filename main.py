import sys
from src.exception import NetworkSecurityException
from src.logging.logger import logging

from src.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == '__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        
        # 1. Data Ingestion
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        
        # 2. Data Validation
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)

        # 3. Data Transformation
        data_trans_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info("Initiate the data transformation..")
        data_transformation = DataTransformation(data_validation_artifact, data_trans_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("data Transformation Completed")
        print(data_transformation_artifact)

        # 4. Model Training
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        logging.info("Initiate the Model Training..")
        model_trainer = ModelTrainer(model_trainer_config, data_transformation_artifact)
        model_artifacts = model_trainer.initiate_model_trainer()
        logging.info("Model Training Completed")
        print(model_artifacts)

    except Exception as e:
        raise NetworkSecurityException(e, sys)