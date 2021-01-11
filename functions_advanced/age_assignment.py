def age_assignment(*args, **kwargs):
    new_data = {}
    for n in args:
        if n[0] in kwargs:
            new_data[n] = kwargs[n[0]]
    return new_data

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
