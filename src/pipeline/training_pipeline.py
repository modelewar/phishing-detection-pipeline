from src.entity.config_entity import TrainingPipelineConfig

from src.entity.artifacts_entity import DataIngestionArtifact
from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig

from src.entity.artifacts_entity import DataValidationArtifact
from src.components.data_validation import DataValidation
from src.entity.config_entity import DataValidationConfig

from src.entity.artifacts_entity import DataTransformationArtifact
from src.components.data_transformation import DataTransformation
from src.entity.config_entity import DataTransformationConfig

from src.entity.artifacts_entity import ModelTrainerArtifact
from src.components.model_trainer import ModelTrainer
from src.entity.config_entity import ModelTrainerConfig
from src.entity.artifacts_entity import ClassificationMetricArtifact
from src.logging import logging
from src.exception import NetworkSecurityException
# from src.constant.training_pipeline import TRAINING_BUCKET_NAME
import sys

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config=TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            data_ingestion_config=DataIngestionConfig(self.training_pipeline_config)
            logging.info("Start data ingestion..")

            data_ingestion=DataIngestion(data_ingestion_config)
            
            data_ingestion_artifacts=data_ingestion.initiate_data_ingestion()

            logging.info("Data Ingestion Completed & artifact : ",data_ingestion_artifacts)

            return data_ingestion_artifacts
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        try:
            data_validation_config=DataValidationConfig(self.training_pipeline_config)

            logging.info("Start data Validation...")
            data_validation=DataValidation(data_ingestion_artifact,data_validation_config)
    
            data_validation_artifacts=data_validation.initiate_data_validation()

            logging.info("Data validation Completed & artifact : ",data_validation_artifacts)

            return data_validation_artifacts
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_transformation(self,data_validation_artifacts:DataValidationArtifact):
        try:
          
            data_trans_config=DataTransformationConfig(self.training_pipeline_config)
            logging.info("Initiate the data transformation..")
            data_transformation=DataTransformation(data_validation_artifacts,data_trans_config)
            logging.info("data Transformation Completed")
            data_transformation_artifact=data_transformation.initiate_data_transformation()

            return data_transformation_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    
    def start_data_model_tariner(self,data_transformation_artifact:DataTransformationArtifact):
        try:
          
            model_trainer_config=ModelTrainerConfig(self.training_pipeline_config)
            logging.info("Initiate the Model Training..")
            model_trainer=ModelTrainer(model_trainer_config,data_transformation_artifact)
            logging.info("Model Training Completed")
            model_artifacts=model_trainer.initiate_model_trainer()
        

            return model_artifacts
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def run_pipeline(self):
        try:
            logging.info("Runing Training Pipeline...")
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(data_validation_artifacts=data_validation_artifact)
            model_trainer_artifact=self.start_data_model_tariner(data_transformation_artifact=data_transformation_artifact)

           
           
            return model_trainer_artifact

        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
