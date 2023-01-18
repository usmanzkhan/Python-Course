input_score=input("Enter a score between 0.0 and 1.0: ")

try:
    score=float(input_score)
except ValueError:
    print("Please Enter a score between 0.0 and 1.0: ")
    quit()
if score >=0.0 and score <=1.0:
    if score < 0.6:
        print("Grade is F")
    elif score >=0.6:
        print("Grade is D")
    elif score >=0.7:
        print("Grade is C")
    elif score >=0.8:
        print("Grade is B")
    elif score >=0.9:
        print("Grade is A")
else:
    print("Please Enter a score between 0.0 and 1.0: ")
