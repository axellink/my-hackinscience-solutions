# https://www.hackinscience.org/exercises/sort-students

def sort_by_mark(my_class):
    return sorted(my_class, key=lambda x : x[0], reverse = True)


def sort_by_name(my_class):
    return sorted(my_class, key=lambda x : x[1])