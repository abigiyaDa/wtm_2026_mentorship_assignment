# 1.  Interactive Terminal E-Commerce Cart & Inventory Tracker 

catalog = {"laptop": 1000, "mouse": 25 , "keyboard": 75,"monitor": 200, "phone": 500, "tablet": 300}
order = []
grand_total = 0

print(f"Currently in stock {catalog}")

while True:
    item = input("Enter item name or 'checkout' to finish or 'exit' to cancel: ").lower()
    if item == "checkout":
        if grand_total >= 500:
            discount = grand_total * 0.1
            grand_total -= discount
        elif grand_total >= 200 and grand_total < 500:
            discount = grand_total * 0.05
            grand_total -= discount
        else: 
            discount = 0

        print(f"\nCHECKOUT RECEIPT \n{20*'='}\nSubtotal: ${grand_total + discount:.1f}\nDiscount: ${discount:.1f}\nTotal: ${grand_total:.1f}\n{20*'='}")
        break
    if item == "exit":
        order.clear()
        break
    if item in catalog:
        order.append(item)
        grand_total += catalog[item]
        print(f"--> Added {item} (${catalog[item]}) to order.")
    else:
        print("Item not found in catalog. Try again.")



# 2. Student Grade Evaluator & Class Performance Tracker 

count = int(input("How many student entries do you want to create? ")) 
student_records = {}

for i in range(count):
    name = input(f"Enter the name of student {i+1}: ")
    while True:
        score = float(input(f"Enter the grade of student {i+1}: "))
        if score > 100 or score <0:
            print("score must be between 0 and 100")
        else :
            break
    student_records[name] = score

total_score = 0
passed = 0
failed = 0

print(f"{20*'='}\nEVALUATION RESULTS \n{20*'='}")
for name, score in student_records.items():
    total_score += score
    if score >= 70:
        grade = "A"
        passed += 1
        print(f"{name}: Score {score:.1f} | Grade {grade} | Passed with Distinction.")
    elif score >= 50:
        grade = "B"
        passed += 1
        print(f"{name}: Score {score:.1f} | Grade {grade} | Passed.")
    else:
        grade = "F"
        failed += 1
        print(f"{name}: Score {score:.1f} | Grade {grade} | Needs Improvement.")


print(f"{20*'='}\nCLASS PERFORMANCE  \n{20*'='}")

average_score = total_score / count 
print(f"Average Score: {average_score:.1f} \nTotal Passed: {passed} \nTotal Failed: {failed} ")


# 3. Backend Data Processing & User Audit Tool 
# Raw user records: (User ID, Name, Role, Is_Active, Login_Attempts) 
users = [ (101, "Alice", "admin", True, 1),  
         (102, "Bob", "member", True, 4),  
         (103, "Charlie", "editor", False, 0),  
         (104, "Diana", "admin", False, 6), 
         (105, "Evan", "member", True, 2),  
         (106, "Fiona", "guest", True, 0), ] 

active = 0
inactive = 0    
for user in users:
    if user[3] == True :
        active += 1
        if user[2] == "admin":
            print(f"[GRANT] Full system access granted to {user[1]} (ID:{user[0]})")
        elif user[2] =="member" or user[2] =="editor":
            print(f"[GRANT] Standard access granted to {user[1]} (ID:{user[0]})")
    elif user[3] == False:
        inactive += 1
        print(f"[DENIED] Account {user[1]} is inactive.")
    

flagged = 0

# b audit 
length = len(users)
i = 0
while i < length:
    if users[i][4] >= 5:
        flagged += 1
        print(f"[ALERT] Account {users[i][1]} is LOCKED due to excessive failed logins ({users[i][4]} attempts).")
    i += 1

print(f"\n{20*'='}\nAUDIT SUMMARY REPORT \n{20*'='}\nTotal Active Users Granted: {active} \nTotal Inactive Accounts: {inactive} \nTotal Security Alerts: {flagged}")