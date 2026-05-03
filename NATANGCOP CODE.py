# Inputs
t1 = float(input("Enter Tentative Q1 Score: "))
t2 = float(input("Enter Tentative Q2 Score: "))
t3 = float(input("Enter Tentative Q3 Score: "))
t4 = float(input("Enter Tentative Q4 Score: "))

# Quarter grades calculation (Cumulative)
q1 = t1
q2 = (q1 + 2 * t2) / 3
q3 = (q2 + 2 * t3) / 3
q4 = (q3 + 2 * t4) / 3

def get_equivalent(grade):
    # Data stored in a list of tuples (Threshold, Equivalent, Adjective)
    # Ordered from highest to lowest
    grading_scale = [
        (96, 1.00, "EXCELLENT"),
        (90, 1.25, "VERY GOOD"),
        (84, 1.50, "VERY GOOD"),
        (78, 1.75, "GOOD"),
        (72, 2.00, "GOOD"),
        (66, 2.25, "SATISFACTORY"),
        (60, 2.50, "SATISFACTORY"),
        (55, 2.75, "FAIR"),
        (50, 3.00, "FAIR"),
        (40, 4.00, "FAILED ON CONDITION")
    ]
    
    for threshold, equiv, adj in grading_scale:
        if grade >= threshold:
            return equiv, adj
            
    return 5.00, "FAILED" # Default if below 40

# Get results
equivalent, adjective = get_equivalent(q4)

# Outputs
print(f"\nFinal Quarter Grade: {q4:.2f}")
print(f"Equivalent: {equivalent:.2f}")
print(f"Adjectival Equivalent: {adjective}")
