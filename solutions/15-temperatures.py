# https://www.hackinscience.org/exercises/temperatures

def fahrenheit_to_celsius(temp):
    return (temp - 32.0)*(5.0/9.0)


def celsius_to_fahrenheit(temp):
    return (temp * (9.0/5.0)) + 32.0

if __name__ == "__main__":
    print(f"20°C = {celsius_to_fahrenheit(20)}°F")
    print(f"100°F = {fahrenheit_to_celsius(100)}°C")