def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    """
    # get a list of all attribute names of the object
    attribute_names = dir(obj)
    
    # filter out attributes that start with '__' (these are usually internal attributes)
    public_attribute_names = [attr_name for attr_name in attribute_names if not attr_name.startswith('__')]
    
    # get the value of each attribute and append it to the result list
    result = []
    for attr_name in public_attribute_names:
        try:
            attr_value = getattr(obj, attr_name)
            result.append((attr_name, attr_value))
        except Exception:
            pass
    
    return result
