import re

from tracardi_custom_string_validator.model.configuration import Configuration


class Validator:
    def __init__(self, config: Configuration):
        self.config = config

    def check(self) -> bool:
        """Check the validation"""
        return re.match(self.config.validation_regex,self.config.data)


