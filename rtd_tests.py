"""
Tests for read-the-docs.
"""

__version__ = "0.1.0"


class CustomException(Exception):
    """Some custom exception."""
    pass


def get_random_data(kind=None):
    """
    Return a list of random data.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise rtd_tests.CustomException: If the kind is invalid.
    :return: the list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
