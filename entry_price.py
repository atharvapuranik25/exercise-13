cost = 0    #stores the cost
group=[]    #empty list for ages

print("Enter Your Age: ")
while True:     #loop for taking user input for ages
    try:
        age = int(input(""))
    except ValueError:
        break
    group.append(int(age))

for i in group:     #loop for calculating the total cost
    if i <= 5:
        pass
    elif 5 < i <= 15:
        cost += 20
    elif 15 < i < 60:
        cost += 60
    elif i > 60:
        cost += 40

print("Amount to be paid: %.2f" %cost)
