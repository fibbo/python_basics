def is_between(x, y, z):
    if x <= y and y <= z:
        return True
    else:
        return False


def is_between2(x, y, z):
    if x <= y <= z:
        return True
    return False


def is_between3(x, y, z):
    return x <= y <= z
