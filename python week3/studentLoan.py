# Input variables
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: "))
income = float(input("Enter your monthly income: "))
gpa = float(input("Enter your GPA (0.0 - 4.0): "))
is_enrolled = input("Are you currently enrolled in school? (yes/no): ").lower()

# Decision logic
if age>=19 and credit_score >= 700 and income >= 3000 and gpa >= 3.0 and is_enrolled == "yes":
    print(f"Hi {name}, you are eligible for a full student loan.")
elif age>=19 and credit_score >= 650 and income >= 2000 and gpa >= 2.5 and is_enrolled == "yes":
    print(f"Hi {name}, you qualify for a partial student loan.")
elif age>=19 and credit_score < 650 and gpa >= 2.0 and is_enrolled == "yes":
    print(f"Hi {name}, you may need a co-signer to apply for a loan.")
else:
    print(f"Sorry {name}, you are currently not eligible for a student loan. Please review your eligibility requirements.")