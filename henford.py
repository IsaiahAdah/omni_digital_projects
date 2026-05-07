# ALGORITHM - Henford High School Result Computation App
# 1. Display welcome message
# 2. Ask lecturer to enter username and password
# 3. Check if credentials match any account in the database
# 4. If wrong, deny access and exit
# 5. If correct, welcome the lecturer by name
# 6. Ask for student name
# 7. Ask for MTH scores (CAT1, CAT2, Exam)
# 8. Ask for GNS scores (CAT1, CAT2, Exam)
# 9. Calculate total for each subject
# 10. Calculate average of both subjects
# 11. Determine grade from average
# 12. Display the result

# Database of registered lecturers
users = [
    {"name": "Adeyemi Adeyemo", "age": 36, "email": "adeyemiadeyemo@henfordschools.com", "role": "Lecturer 1", "username": "Adeson", "pass": "adeson0123LEC"},
    {"name": "Adamu Abdullahi", "age": 40, "email": "adamuabdul@henfordschools.com", "role": "Lecturer", "username": "Adamu", "pass": "adamu2030LEC"},
    {"name": "Judith Okonkwo", "age": 26, "email": "judithOkonkwo@henfordschools.com", "role": "Lecturer 3", "username": "JudithOko", "pass": "judith0023LEC"}
]

# Login system
username = input("Enter username: ")
password = input("Enter password: ")

# Check credentials
logged_in_user = None
for user in users:
    if user["username"] == username and user["pass"] == password:
        logged_in_user = user
        break

# Grant or deny access
if logged_in_user is None:
    print("Access denied.")
else:
    print(f"Welcome, {logged_in_user['name']}")

    # Ask for student name
    student_name = input("Enter student name: ")

    # Ask for MTH scores
    mth_cat1 = float(input("Enter MTH CAT1 score: "))
    mth_cat2 = float(input("Enter MTH CAT2 score: "))
    mth_exam = float(input("Enter MTH Exam score: "))

    # Ask for GNS scores
    gns_cat1 = float(input("Enter GNS CAT1 score: "))
    gns_cat2 = float(input("Enter GNS CAT2 score: "))
    gns_exam = float(input("Enter GNS Exam score: "))

    # Calculate totals
    mth_total = mth_cat1 + mth_cat2 + mth_exam
    gns_total = gns_cat1 + gns_cat2 + gns_exam

    # Calculate average of both subjects
    average = (mth_total + gns_total) / 2

    # Determine grade
    if average >= 70:
        grade = "A - Excellent"
    elif average >= 60:
        grade = "B - Very Good"
    elif average >= 50:
        grade = "C - Good"
    elif average >= 40:
        grade = "D - Pass"
    elif average <= 39:
        grade = "F - Fair"
    else:
        grade = "Invalid Input"

    # Display result
    print(f"Student Name: {student_name}")
    print(f"MTH Total: {mth_total}")
    print(f"GNS Total: {gns_total}")
    print(f"Average Score: {average}")
    print(f"Grade: {grade}")
