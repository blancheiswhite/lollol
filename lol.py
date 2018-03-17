def positive(sequence):
    total = 0
    for element in sequence:
        if element > 0:
            total = total + 1
    return total

positive ([1,0])