#!/usr/bin/python3
"""class instance checker documentation"""

def is_same_class(obj, a_class):
    """Checks if the obj is exactly an instance of the specified class.
    
    Args:
        obj: The object to check.
        a_class: The class to check against.
        
    Returns:
        True if the object is an instance, otherwise, False.
    """
    # This line compares the type of obj with the specified class
    # If they are the same, it means obj is exactly an instance of a_class
    return type(obj) == a_class  # This is the checking part, it's like saying "Are you the same as this class?"
