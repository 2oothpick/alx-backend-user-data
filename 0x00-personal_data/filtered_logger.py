#!/usr/bin/env python3
"""
Filter logger module
"""
import re
from typing import List
import logging


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Filters out all PIIs
    """
    for field in fields:
        message = re.sub(f"((?<={field}=)[^{separator}]*)", redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Obfuscates personal data fields from record
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
