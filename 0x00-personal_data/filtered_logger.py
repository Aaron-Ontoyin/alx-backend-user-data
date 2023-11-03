#!/usr/bin/env python3
"""This module is about logging"""

import logging
import re


def filter_datum(fields, redaction, message, separator):
    """Returns log message obfuscated"""
    for field in fields:
        message = re.sub(
            f"{field}=(.*?){separator}", f"{field}={redaction}{separator}", message
        )
    return message
