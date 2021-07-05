"""Example module."""


def do_something(x: bool) -> str:
    """Perform stuff.

    This function does something very interesting.

    Args:
        x: the boolean argument.

    Returns:
        A string that depends on the argument.
    """
    if x:
        return "hello"
    else:
        return "world"


# do_something(5) # should make type error
