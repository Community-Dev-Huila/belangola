from regex import match, compile

true_bi = compile("[1-9]*[A-Z]*2[1-9]*")


def validate_bi(_bi_number: str) -> bool:
    if match(true_bi, _bi_number):
        return True
    return False
