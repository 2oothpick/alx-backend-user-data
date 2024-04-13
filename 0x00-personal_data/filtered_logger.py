#!/usr/bin/env python3
"""
Filter logger module
"""
import re


def filter_datum(
    fields: list[str], redaction: str, message: str, separator: str
) -> str:
    """
    Filters out all PIIs
    """
    for field in fields:
        message = re.sub(f"((?<={field}=)[^{separator}]*)", redaction, message)
    return message
