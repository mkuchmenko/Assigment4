def  get_grade(*score):
    for i in score:
        if i<=100 and i>=90:
            print("A", end=", ")
        elif i<=89 and i>=80:
            print("B",end=", ")
        elif i<=79 and i>=70:
            print("C",end=", ")
        elif i<=69 and i>=0:
            print("F",end=", ")
        else: print("Please, Print a score from 0-100", end=", ")
get_grade(95, 45, 78, 82, 60)