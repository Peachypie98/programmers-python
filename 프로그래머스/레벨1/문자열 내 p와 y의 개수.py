def solution (input_string):
    p_count = 0
    y_count = 0
    for char in input_string:
        if char == "p" or char == "P":
            p_count = p_count + 1
        if char == "y" or char == "Y":
            y_count = y_count + 1
    return p_count == y_count