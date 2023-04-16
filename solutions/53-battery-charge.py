# https://www.hackinscience.org/exercises/print-battery-charge

def battery_charge(charge):
    _charge = round(charge/10)
    print("[" + _charge * "❚" + (10 - _charge) * " " + "]")
    print(f"{charge}%")

if __name__ == "__main__":
    for i in range(0, 101, 25):
        battery_charge(i)