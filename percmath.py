
def mapping(value, valueRangeMax, valueRangeMin, desiredRangeMax, desiredRangeMin):
    startScaled = valueRangeMax - valueRangeMin
    desiredScaled = desiredRangeMax - desiredRangeMin

    valueScaled = float(value-valueRangeMin) / float(startScaled)

    return desiredRangeMin + (valueScaled * desiredScaled)


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def f(x):
    return 1 * x + 0.0
