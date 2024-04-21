grocery_items = input("Enter your items, please use ',' after each item: ").split(',')

remove = input("Do you want to remove some items? Enter 'yes' otherwise 'no': ")

if remove == "no":
    print(f"This is your grocery items list: {grocery_items}")
  

elif remove == "yes":
    remove_items = input("Enter the items you want to remove, please use ',' after each item: ").split(',')

    for item in remove_items:
        if item in grocery_items:
            grocery_items.remove(item)
            print(f"This is your remove items list: {grocery_items}")
        else:
            print(f"{item} not found in the items list.")

else:
    print("Invalid input. Bye bye.")            

add = input("if do you eant to add items? Enter 'add' otherwise 'no': ") 

if add == 'add':
    add_items = input("Enter your items: ")
    grocery_items.append(add_items)
    print(f"This is your add items list{grocery_items}")

elif add == 'no':
    print(grocery_items)

else:
    print("Invalid input. Bye bye.")     



print(f"This is your final grocery list{grocery_items}")



#Scenario 2: Student Grades 

student_grades = {}
total_students = int(input("Enter student frequency: "))
total_percentage = 0

for student in range(total_students):
    name_of_student = input("Enter your name here: ")

    subjects = ['maths', 'economics', 'accounting', 'P_O_C', 'statistics']
    
    student_grades[name_of_student] = {}
    total_numbers = 0 

    for subject in subjects:
        numbers = float(input(f"Enter your {subject} numbers: "))
        student_grades[name_of_student][subject] = numbers
        total_numbers += numbers
    
    percentage = total_numbers / len(subjects)
    student_grades[name_of_student]['percentage'] = percentage
    total_percentage += percentage

average_percentage = total_percentage / total_students

print(f"Student Grades: {student_grades}")
print(f"Average Percentage is: {average_percentage}")





#Scenario 3: Word Frequency Counter

word_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]

word_frequency = {}

for word in word_list:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Word Frequencies:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency} times")


#Scenario 3: Password Strength Checker

password_input = input("Enter your password: ")
letter = any(alphabet.isalpha() for alphabet in password_input)
number = any(digit.isdigit() for digit in password_input)

if len(password_input) >= 8 and letter and number:
    print(password_input)
else:
    print("Invalid password. Please ensure the following:")
    if len(password_input) < 8:
        print("• Password should be at least 8 characters long.")
    if not number:
        print("• Password should contain at least one digit.")
    if not letter:
        print("• Password should contain at least one letter.")




#Scenario 04: Voting System (Annual Employee Recognition Awards)

                            #LOGIC (1)

Employees_of_the_Year = {}
Team_player_of_the_Year = {}
Innovation_award = {}

num_of_nominees = int(input("Enter how many nominees participate in Annual Employee Recognition Awards:"))

for nominee in range(num_of_nominees):
    categories = input('''
           If you participate in 'Employee of the Year', press 'A': 
           If you participate in 'Team Player of the Year', press 'B': 
           If you participate in 'Innovation Award', press 'C': 
           ''')
    
    if categories == 'A':
        names_of_A = input("Enter your name here: ")
        categories_A = "Employees of the Year"
        Employees_of_the_Year[names_of_A] = {'category': categories_A, 'votes': 0}

    elif categories == 'B':
        names_of_B = input("Enter your name here: ")
        categories_B = "Team player of the Year"
        Team_player_of_the_Year[names_of_B] = {'category': categories_B, 'votes': 0}

    elif categories == 'C':
        names_of_C = input("Enter your name here: ")
        categories_C = "Innovation award"
        Innovation_award[names_of_C] = {'category': categories_C, 'votes': 0}

    else:
        print("We don't have this category")

                                 #LOGIC (2)

voters = int(input("Enter voters frequency: "))

for vote in range(voters):
    voting_for_A = input(f"{Employees_of_the_Year.keys()} Name the employee from the given names whom you want to vote: ")
    
    if voting_for_A in Employees_of_the_Year:
        Employees_of_the_Year[voting_for_A]['votes'] += 1
        vote_recorded = True
    else:
        print("Invalid vote. Please choose a valid employee.")

    voting_for_B = input(f"{Team_player_of_the_Year.keys()} Name the employee from the given names whom you want to vote: ")

    if voting_for_B in Team_player_of_the_Year:
        Team_player_of_the_Year[voting_for_B]['votes'] += 1
        vote_recorded = True
    else:
        print("Invalid vote. Please choose a valid employee.")

    voting_for_C = input(f"{Innovation_award.keys()} Name the employee from the given names whom you want to vote: ")

    if voting_for_C in Innovation_award:
        Innovation_award[voting_for_C]['votes'] += 1
        vote_recorded = True
    else:
        print("Invalid vote. Please choose a valid employee.")

if vote_recorded:
    print("All VOTES HAS BEEN RECORDED")

                                    #LOGIC (3)

employee_award = -1
name_employee = None
player_award = -1
name_player = None
innovation_award = -1
name_innovation = None

print("Final vote counts for 'Employees of the Year':")
for employee, award in Employees_of_the_Year.items():
    print(f"{employee}: {award['votes']} votes")
    votes_count_A = award['votes']
    if votes_count_A > employee_award:
        employee_award = votes_count_A
        name_employee = employee

print("Final vote counts for 'Team of the year':")
for player, Award in Team_player_of_the_Year.items():
    print(f"{player}: {Award['votes']} votes")
    votes_count_B = Award['votes']
    if votes_count_B > player_award:
        player_award = votes_count_B
        name_player = player

print("Final vote counts for 'Innovation award':")
for innovation, AwArd in Innovation_award.items():
    print(f"{innovation}: {AwArd['votes']} votes")
    votes_count_C = AwArd['votes']
    if votes_count_C > innovation_award:
        innovation_award = votes_count_C
        name_innovation = innovation

if name_employee and name_player and name_innovation is not None:
 print(f"{name_employee} is the Winner of 'Employees of the Year AWARD' they got {employee_award} votes")
 print(f"{name_player} is the Winner of 'Employees of the Year AWARD' they got {player_award} votes")
 print(f"{name_innovation} is the Winner of 'Employees of the Year AWARD' they got {innovation_award} votes")
else:
    print("\nNo votes recorded.")