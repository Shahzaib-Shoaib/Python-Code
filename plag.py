def validate_score(score):
    try:
        score = int(score)
        if 0 <= score <= 10:
            return True
        else:
            return False
    except ValueError:
        return False

def calculate_average(scores):
    return sum(scores) / len(scores)

def main():
    scores = []
    for i in range(10):
        score = input(f"Enter score {i+1}: ")
        while not validate_score(score):
            print("Please enter a valid score between 0 and 10.")
            score = input(f"Enter score {i+1}: ")
        scores.append(int(score))
    average = calculate_average(scores)
    print(f"The average score is: {average:.2f}")

if __name__ == "__main__":
    main()
