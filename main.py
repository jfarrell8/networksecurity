from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        dataingestion=DataIngestion(dataingestionconfig)

        logging.info("Initiate data ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiation Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed")
        print(data_validation_artifact)

        logging.info('Initiating Data Transformation')
        data_transformation_config=DataTransformationConfig(training_pipeline_config=trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info('Data Transformation Completed')

        logging.info("Model Training started")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()
        logging.info("Model Training completed")
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)