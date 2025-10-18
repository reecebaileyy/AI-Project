def vector_add(a, b):
    """Add two tuples or lists elementwise."""
    return tuple(x + y for x, y in zip(a, b))
