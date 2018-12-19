# -*- coding: utf-8 -*-

import re


def validate_fields(item, fields, spider, check_null_values=True):
    '''
    This function validates fields according to their regex validators
    and logs validation warning messages using the supplied spider logger.
    '''
    null_values = ['nill', 'none', 'null', 'n/a']
    for field, validator in fields:
        value = str(item[field])
        value_is_null = check_null_values and value.lower() in null_values
        if value_is_null or not re.match(validator, value, re.MULTILINE):  # @UndefinedVariable
            log_msg = "BAD_FIELD: invalid item field:\nitem:%s\nfield:%s\nvalue:%s"
            log_msg = log_msg % (repr(item), field, item[field])
            spider.logger.warn(log_msg)


# end of file
