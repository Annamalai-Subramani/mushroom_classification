import os
import sys
from mushroom_classification.exception import customexception
from mushroom_classification.logger import logging
import pandas as pd
import numpy as np
from mushroom_classification.components.data_ingestion import DataIngestion
from mushroom_classification.components.data_transformation import DataTransformation
from mushroom_classification.components.model_trainer import ModelTrainer
from mushroom_classification.components.model_evaluation import ModelEvaluation

logging.info('Training Pipeline has started')

try:
    obj=DataIngestion()
    train_data_path,test_data_path=obj.Initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)
    
    model_trainer_obj=ModelTrainer()
    model_trainer_obj.initate_model_training(train_arr,test_arr)

    model_eval_obj = ModelEvaluation()
    model_eval_obj.initiate_model_evaluation(train_arr,test_arr)


except Exception as e:
    raise customexception(e,sys)