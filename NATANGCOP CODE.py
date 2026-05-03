t1 = float(input("Enter Tentative Q1 Score: "))
t2 = float(input("Enter Tentative Q2 Score: "))
t3 = float(input("Enter Tentative Q3 Score: "))
t4 = float(input("Enter Tentative Q4 Score: "))

# Quarter grades
q1 = t1
q2 = (q1 + 2 * t2) / 3
q3 = (q2 + 2 * t3) / 3
q4 = (q3 + 2 * t4) / 3

def get_equivalent(grade):
    if grade >= 96:
        return 1.00, "EXCELLENT"
    elif grade >= 90:
        return 1.25, "VERY GOOD"
    elif grade >= 84:
        return 1.50, "VERY GOOD"
    elif grade >= 78:
        return 1.75, "GOOD"
    elif grade >= 72:
        return 2.00, "GOOD"
    elif grade >= 66:
        return 2.25, "SATISFACTORY"
    elif grade >= 60:
        return 2.50, "SATISFACTORY"
    elif grade >= 55:
        return 2.75, "FAIR"
    elif grade >= 50:
        return 3.00, "FAIR"
    elif grade >= 40:
        return 4.00, "FAILED ON CONDITION"
    else:
        return 5.00, "FAILED"

equivalent, adjective = get_equivalent(q4)

print(f"\nFinal Quarter Grade: {q4:.2f}")
print(f"Equivalent: {equivalent:.2f}")
print(f"Adjectival Equivalent: {adjective}")
