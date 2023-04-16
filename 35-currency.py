# https://www.hackinscience.org/exercises/currency

def how_to_pay(amount, currency):
    res = dict()
    _currency = sorted(currency, reverse=True)
    for i in _currency:
        res[i], amount = divmod(amount, i)
    if amount == 0:
        return res
    else:
        raise ValueError("Impossible to pay that amount with such currency")