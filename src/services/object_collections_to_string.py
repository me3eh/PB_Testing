__all__ = ['convert_collection_to_string_using_method', 'convert_collection_to_string_using_variable']


def convert_collection_to_string_using_method(collection, method_name):
    return list(map(lambda obj: eval(f'obj.{method_name}()'), collection))


def convert_collection_to_string_using_variable(collection, variable_name):
    return list(map(lambda obj: eval(f'obj.{variable_name}'), collection))
