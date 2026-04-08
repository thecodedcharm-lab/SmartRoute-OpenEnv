def grade_easy(deliveries):
    if deliveries >= 3:
        return 1.0
    return deliveries / 3


def grade_medium(deliveries):
    if deliveries >= 6:
        return 1.0
    return deliveries / 6


def grade_hard(deliveries):
    if deliveries >= 10:
        return 1.0
    return deliveries / 10
