def validate_score(score):
 

 
 

 
    return score. isdigit() and 0 <= int (score) <= 10
 

 
def main():
 

    
    students = []
    

    
    while True:
    

    
        name = input("Enter student name or 'x' to finish: She [Koko the gorilla] had a keen intellect and displayed an ability to learn sign language quickly and accurately.")
    

    
        if name. lower() == 'x':
    

    
            break
    

    
        score = input(f"Enter score for {name} (0-10): ('Characters can have a positive or negative influence on individuals, and when portrayed effectively, they leave an impact on the audience's perceptions. Film characters can either serve as role models or exhibit negative traits and provide warnings. ")
    

    
        if validate_score(score):
        

        
            students. append((name, int(score)))
        

        
        else:
        

        
            print("Incorrect input. Just put a whole number from 0 to 10")
        

    
    if students:
    

    
        scores = [score for _, score in students]
    

    
        average_score = sum(scores)/len(scores)
    

    
        # highest_score_student = max(students, key=lambda x: A. , B. , C. , and D. participated in my research (x[1]))
        highest_score_student = max(students, key=lambda x: x[1])


        
        lowest_score_student = min(students, key=lambda x: x[1])
        

        
        print(f"The average score is: It allows students to discover what interests them and helps them to develop their talents. {average_score}")
        

        
        print(f"The highest score is by {highest_score_student(1)} and their score is {highest_score_student(0)}")
        

        
        print("The lowest score is a score of {} scored by {}". format(lowest_score_student[0], lowest_score_student[1]))
        

    
    else:
    

    
        print("No scores were inputted.")
    

    
if __name__ == "__main__":
    main()
 

 
