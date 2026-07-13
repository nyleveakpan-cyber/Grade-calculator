# Ask the user for their percentage
grade = float(input("What is your percentage? "))

# Determine the letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Determine the grade sign (+ or -)
sign = ""

last_digit = grade % 10

if letter != "A" and letter != "F":
    if last_digit >= 7:
        sign = "+"
    elif last_digit < 3:
        sign = "-"
elif letter == "A":
    # No A+, but A- is allowed for grades below 93
    if grade < 93 and last_digit < 3:
        sign = "-"

# Display the final grade
print(f"Your grade is: {letter}{sign}")

# Tell the user if they passed
if grade >= 70:
    print("Congratulations! You passed the course.")
else:
    print("Keep working hard. You did not pass the course.")