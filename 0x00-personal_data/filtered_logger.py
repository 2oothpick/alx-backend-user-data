#!/usr/bin/env python3
"""
Filter logger module
"""
import re
from typing import List
import logging
import mysql.connector
from os import getenv

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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


def get_logger() -> logging.Logger:
    """
    Creates a Logger object with RedactingFrormatter
    as formatter which obsfucates PII_FIELDS fields
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.propagate = False
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to DB using env variables
    """
    username = getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = getenv('PERSONAL_DATA_DB_NAME')
    connection = mysql.connector.connect(
        user=username, database=db_name, password=password, host=host)
    return connection


def main() -> None:
    """
    Main function
    """
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute('select * from users')
    logger = get_logger()
    for row in cursor:
        message = f"name={row[0]};email={row[1]};phone={\
            row[2]};ssn={row[3]};password={row[4]};ip={row[5]};last_login={\
                row[6]};user_agent={row[7]};"
        logger.info(message)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
