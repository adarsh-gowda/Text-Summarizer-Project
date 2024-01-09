from textSummarizer.config.configuration import configurationManager
from textSummarizer.conponents.data_validation import DataValidation
from textSummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = configurationManager()
        data_validatiion_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validatiion_config)
        data_validation.validate_all_files_exist()