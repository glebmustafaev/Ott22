def introspection_info(obj):
    type_ = type(obj).__name__
    atr_ = dir(obj)
    module = obj.__class__.__module__
    my_dict = {'type': type_, 'attributes and methods': atr_, 'module': module}
    return my_dict



number_info = introspection_info(42)
print(number_info)
