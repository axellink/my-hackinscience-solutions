# https://www.hackinscience.org/exercises/select-students

def select_student(students, threshold):
    _students = sorted(students, key = lambda x : x[1], reverse=True)
    accepted = []
    i = 0
    try:
        while(_students[i][1] >= threshold):
            accepted.append(_students[i])
            i += 1
    except ValueError:
        pass
    return {'Accepted': accepted, 'Refused': list(reversed(_students[i:]))}