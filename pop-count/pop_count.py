def egg_count(display_value):
    """
    Count the '1' bits in the binary representation of the `display_value` 
    (without using "that bit-count functionality" (or any bitwise operators)).
    
    """
    if display_value == 0: 
        return 0
    return display_value % 2 + egg_count(display_value // 2)