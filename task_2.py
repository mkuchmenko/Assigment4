def  get_grade(*score):
    a=[]
    for i in score:
        if i<=100 and i>=90:
            a.append("A")
        elif i<=89 and i>=80:
            a.append("B")
        elif i<=79 and i>=70:
            a.append("C")
        elif i<=69 and i>=0:
            a.append("F")
        else: a.append("Please, Print a score from 0-100", end=", ")
    return a
print(get_grade(95, 45, 78, 82, 60))