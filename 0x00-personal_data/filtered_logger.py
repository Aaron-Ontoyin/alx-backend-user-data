#!/usr/bin/env python3
"""This module is about logging"""

import logging
import re


def filter_datum(fields, redaction, message, separator):
    """Returns log message obfuscated"""
    p = "|".join([f"{f}=([^{separator}]*)" for f in fields])
    return re.sub(p, lambda m: f"{m.group().split('=')[0]}=" f"{redaction}",
                  message)
