#!/usr/bin/env python3
"""This module is about logging"""

import logging
import re


def filter_datum(fields, redaction, message, separator):
    """
        Returns log message obfuscated
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating
        all fields in the log line (message)
    """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message
