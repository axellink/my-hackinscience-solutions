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
    
if __name__ == "__main__":
    euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    print(how_to_pay(500, euro))
    print(how_to_pay(123, euro))