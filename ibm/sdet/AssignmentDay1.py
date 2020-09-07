# Write a program to prompt for a score between 0.0 and 1.0.
# # If the score is out of range, print an error message.
# # If the score is between 0.0 and 1.0, print a grade using the following table:
# #Score   Grade
# #>= 0.9     A
# #>= 0.8     B
# #>= 0.7     C
# #>= 0.6     D
# #< 0.6      F
# # print 'Bad score' if the score is not between 0.0 and 1.0 or if the
# #score is not numeric   value entered


import sys

score = (input("Please prompt for a score between 0.0 and 1.0"))
score = float(score)
if score > 1.0 or score < 0.0:
    print("Bad score")
    sys.exit()
else:
    print("Valid score")

if score >= 0.9:
    print("Grade A")
elif score >= 0.8:
    print("Grade B")
elif score >= 0.7:
    print("Grade C")
elif score >= 0.6:
    print("Grade D")
else:
    print("Grade F")