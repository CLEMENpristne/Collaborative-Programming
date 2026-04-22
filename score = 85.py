def get_adjectival (grade):
    if grade >= 96:
        return "EXCELLENT"
    elif grade >= 90:
        return "VERY GOOD"
    elif grade >= 84:
        return "VERY GOOD"
    elif grade >= 78:
        return "GOOD"
    elif grade >= 72:
        return "GOOD"
    elif grade >= 66:
        return "SATISFACTORY"
    elif grade >= 60: 
        return "SATISFACTORY"
    elif grade >= 55:
        return "FAIR"
    elif grade >= 50:
        return "FAIR"
    elif grade >= 40:
        return "FAILED ON CONDITION"
    else:
        return "FAILED"

#Input tentative grades 

q1 = float(input("Enter tentative grade for Q1: "))
q2 = float(input("Enter tentative grade for Q2: "))
q3 = float(input("Enter tentative grade for Q3: "))
q4 = float(input("Enter tentative grade for Q4: "))

#Compute quarters 
q1 = q1 *      