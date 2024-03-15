def add(tuple1, tuple2):
    return (x + y for x, y in zip(tuple1, tuple2))

def button_name(is_right):
    return "right" if is_right else "left"
