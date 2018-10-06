#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
stocksense/controllers/validators.py

"""

from PyInquirer import (Token, ValidationError, Validator, print_json, prompt,
                        style_from_dict)


class EmptyValidator(Validator):
    def validate(self, value):
        if len(value.text):
            return True
        else:
            raise ValidationError(
                message="You can't leave this blank",
                cursor_position=len(value.text))
