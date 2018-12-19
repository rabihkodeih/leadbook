def preprend_zws(plural_model_name, num_zws):
    '''
    Preprends a number of zero-width-spaces to the plural
    name of a model. This is mainly used to arrange
    models in the admin user interface. Example usage:

    class Model(models.model):
        ...
        class Meta:
            ...
            verbose_name_plural = prepend_zws("...", 4)
    '''
    prefix = '\u200b' * num_zws
    return '%s%s' % (prefix, plural_model_name)


def tryCatchEval(lambda_expression, default_value, exception_type=None):
    '''
    Evaluates a lambda expression and returns the corresponding result within a try-catch block.
    If exception_type is thrown then a default value is returned.
    @param lambda_expression: The lambda expression to be evaluated
    @param default_value: The default value to be returned on raising the exception
    @param exception_type: The exception type to be checked if provided
    @return: the evaluated lambda expression
    '''
    if exception_type is None:
        exception_type = Exception
    try:
        result = lambda_expression()
    except exception_type:
        result = default_value
    return result


def get_from_query_string(qs, param, default_value=None, type_cast=None):
    result = tryCatchEval(lambda: qs.get(param)[0], default_value)
    if type_cast:
        result = type_cast(result)
    return result


# end of file
