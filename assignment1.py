'''
Part 1: Python Introduction and Data Types
1. Personal Information
'''
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
student = input("Are you a student? (yes/no): ").strip().lower() == "yes"

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", student,"\n")



'''
2. Identify the Data Types
'''
name = 'abcdef'
age = 25
height = 5.9
is_student = True


print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Is Student:", is_student, type(is_student),"\n")  



'''
Part 2: Lists
3. Favourite Foods
'''
foods = ['Pizza', 'Burger', 'Pasta', 'Firfir', 'injera']

# 1 Print the entire list
print("List of foods:", foods)
# 2 Print the first and last food. 
print("First food:", foods[0])
print("Last food:", foods[-1])

# 3 Add one more food. 
foods.append('Salad')

# 4 Remove one food. 
foods.remove('Burger')

# 5 Change one food to another food. 
foods[1] = 'Cake'

# 6 Print the final list. 
print("Updated list of foods:", foods,"\n")



'''
4. Student Scores
'''

scores = [75, 80, 65, 90, 85] 
# 1 Print all the scores. 
print("List of scores:", scores)
# 2 Print the highest score. 
print("Highest score:", max(scores))

# 3 Print the lowest score. 
print("Lowest score:", min(scores))

# 4 Add a new score of 95. 
scores.append(95)

# 5 Print the updated list. 
print("Updated list of scores:", scores,"\n")




'''
Part 3: Tuples
5. Days of the Week 
'''
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# 1 Print the entire tuple. 
print("Days of the week:", days)
# 2  Print the first day. 
print("First day:", days[0])

# 3 Print the last day. 
print("Last day:", days[-1],"\n")

# 4 Attempt to change one of the values and explain what happens.
#  
# days[1] = "Funday"  
'''
This will raise an error because tuples are immutable 

TypeError: 'tuple' object does not support item assignment
'''

'''
Question: Why is a tuple different from a list?  

a tuple is different from a list in Python because tuples are immutable, means once created , their elements cannot be changed, added, or removed. 
but lists are mutable - we are allowed to modify them by adding, removing, or changing elements.
'''

'''
Part 4: Sets
6. Remove Duplicate Values
'''

numbers = [1, 2, 3, 4, 2, 5, 3, 6, 1] 

# 1 Convert the list into a set. 
unique_numbers = set(numbers)
#2 Print the result. 
print("Unique numbers:", unique_numbers,"\n")
 
'''
3. Explain why some values disappeared. 
This is because a set in Python only contains unique elements. 
When we convert the list to a set, any duplicate values are automatically removed.
'''

'''
7. Unique Programming Languages
'''

languages = ["Python", "Java", "Python", "C++", "JavaScript", "Python"]

# 1 Convert the list into a set 
unique_languages = set(languages)
# 2 and print the unique programming languages.
print("Unique programming languages:", unique_languages)

# 3 Then add "Django" to the set.

unique_languages.add("Django")
print("Updated unique programming languages:", unique_languages,"\n") 

'''
Part 5: Dictionaries
8. Student Profile 

'''
student_profile = {
    "Name" : "Abigiya",
    "Age" : 25,
    "Course" : "Backend",
    "Level" : "Intermediate",
    "Skills" : ["Python", "FastAPI", "MySQL"],

}

# 1  Print the entire dictionary
print("Student Profile:" , student_profile)

# 2 print student names
print("Name:", student_profile["Name"])

# 3 add email as key
student_profile["Email"] = "abc123@gmail.com"

# 4 change student level
student_profile["Level"] = "Advanced"

# 5 remove age key
student_profile.pop("Age")

#6 print updated profile
print("Updated Student Profile:", student_profile,"\n")


'''
Final Challenge
9. Student Management Data
'''
students = {
    "student1" : {
        "name" : "Abebe",
        "age" : 21,
        "course" : "Backend Development",
        "skills" : ["Python", "C++", "SQL"]
    },
    "student2" : {
        "name" : "John",
        "age" : 20,
        "course" : "Computer Science",
        "skills" : ["Python", "Java", "C++"]
    },
    "student3" : {
        "name" : "Mary",
        "age" : 22,
        "course" : "Data Analysis",
        "skills" : ["Excel", "SQL", "Python"]
    }
}

print("Student Management Data:" , students,"\n")


'''
Assignment: Student Information Manager
Objective
    - Create a Python program that stores and displays information about a student using different Python data types and data structures.
'''


'''
1. List
'''
# 1. Variables with appropriate data types
name = "John"
age = 25
height = 1.75
is_enrolled = True

# 2. List of 5 programming languages or subjects the student is interested in
skills = ["Python", "HTML", "CSS", "JavaScript", "SQL"]
# 1 print the 1st item
print("First skill:", skills[0])
# 2 add new item
skills.append("Git")
# 3 remove an item
skills.remove("HTML")
# 4 print the updated list
print("Updated skills:", skills,"\n")

'''
2. Tuple
'''

# Tuple of favorite numbers then print the second number
favorite_numbers = (7, 10, 25)
print("Second favorite number:", favorite_numbers[1],"\n")

'''
3. set
'''
# Set of hobbies with duplicate value
hobbies = {"Reading", "Gaming", "Football", "Reading"}
# 1 print the set
print("Hobbies:", hobbies)
# 2. explain  through the program output what happened to the duplicate value. 
print("Duplicate value was removed because sets store only unique values.")
# add a new hobby 
hobbies.add("Cycling")
print("Updated hobbies:", hobbies,"\n")

'''
5. Dictionary
'''

# 5. Dictionary with all student details
student = {
    "name": "John",
    "age": 22,
    "height": 1.75,
    "is_enrolled": True,
    "skills": ["Python", "HTML", "CSS", "JavaScript", "SQL"],
    "favorite_numbers": [7,10,25,30,100],
    "hobbies": ["Reading","Basketball","Sleeping"],
}
# Print the student's name. 
print("Student name:", student["name"])
# Print their skills. 
print("Student skills:", student["skills"])
# Add a new key called "country". 
student["country"] = "Ethiopia"
# Update the student's age. 
student["age"] = 26
# print the complete student dictionary.
print("Complete student dictionary:", student,"\n")


# bonus 
name = "Abigiya"
age = 22
fav_programming_language = "Python"

my_data_dict = {
    "name": name,
    "age": age,
    "skill": fav_programming_language
}

print(f"Hello {my_data_dict['name']}!! \nyou are {my_data_dict['age']} years old. \nyour favorite programming language is {my_data_dict['skill']}.")

'''
A short explanation of the difference between:
    o List
    o Tuple
    o Set
    o Dictionary

List: An ordered, changeable collection of items written in square brackets [].
Tuple: An ordered, unchangeable collection of items written in parentheses ().
Set: An unordered collection of unique items written in curly braces {}.
Dictionary: A collection of key-value pairs used to store related data.
'''