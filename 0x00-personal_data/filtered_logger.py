#!/usr/bin/env python3
"""This module is about logging"""

import logging
import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Returns log message obfuscated
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating
    all fields in the log line (message)
    """
    p = "|".join([f"{f}=([^{separator}]*)" for f in fields])
    return re.sub(
        p, lambda m: f"{m.group().split('=')[0]}=" f"{redaction}", message
    )
