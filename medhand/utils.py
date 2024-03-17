def add(tuple1, tuple2):
    return tuple(x + y for x, y in zip(tuple1, tuple2))

def sign(x):
    if x == 0:
        return 0
    return 1 if x > 0 else -1

def signed_power(x, a):
    return sign(x) * abs(x)**a
