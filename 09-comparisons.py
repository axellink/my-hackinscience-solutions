# https://www.hackinscience.org/exercises/comparisons

the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]

m = the_list[0]
for n in the_list[1:]:
    m = n if n>m else m

print(m)