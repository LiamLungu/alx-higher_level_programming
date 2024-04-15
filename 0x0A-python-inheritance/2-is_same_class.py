def is_same_class(obj, a_class):
    """Checks if the obj is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.

    Returns:
        True if the object is exactly an instance of the specified class, otherwise False.
    """
    return type(obj) == a_class
