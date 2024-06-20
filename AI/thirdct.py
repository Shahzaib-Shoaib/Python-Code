def validate_score(score):
    """Validate that the score is a whole number between 0 and 10 inclusive."""
    return score.isdigit() and 0 <= int(score) <= 10

def main():
    students = []
    while True:
        name = input("Enter student name or 'x' to finish: ")
        if name.lower() == 'x':
            break
        score = input(f"Enter score for {name} (0-10): ")
        if validate_score(score):
            students.append((name, int(score)))
        else:
            print("Invalid score. Please enter a whole number between 0 and 10.")

    if students:
        scores = [score for _, score in students]
        average_score = sum(scores) / len(scores)
        highest_score_student = max(students, key=lambda x: x[1])
        lowest_score_student = min(students, key=lambda x: x[1])

        print(f"The average score is: {average_score}")
        print(f"The highest score is by {highest_score_student[0]} with a score of {highest_score_student[1]}")
        print(f"The lowest score is by {lowest_score_student[0]} with a score of {lowest_score_student[1]}")
    else:
        print("No scores were entered.")

if __name__ == "__main__":
    main()
