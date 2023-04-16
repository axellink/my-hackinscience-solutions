# https://www.hackinscience.org/exercises/distance

def dist(points):
    return max(points) - min(points)

if __name__ == "__main__":
    print(dist([1, 2, 3]))
    print(dist([1, 2, 3, 2.5, 3.5, 120, -1000]))