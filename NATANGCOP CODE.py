
t1 = float(input( "Enter Tentative Q1 Score: " ) )
t2 = float(input( "Enter Tentative Q2 Score: " ) )
t3 = float(input( "Enter Tentative Q3 Score: : " ) )
average = (t1 + t2 + t3) / 3

print(average)

# Q1 = Tentative Q1
q1 = t1

#Q2 = (Q1 + 2*Tentative Q2)

def get_gwa(average)
if average >= 96:  print(1.00)
elif average >= 90: print(1.25)
elif average >= 84: print(1.50)
elif average >= 78: print(1.75)
elif average >= 72: print(2.00)
elif average >= 66: print(2.25)
elif average >= 60: print(2.50)
elif average >= 55: print(2.75)
elif average >= 50: print(3.00)
elif average >= 40: print(4.00)
else: print(5.00)
