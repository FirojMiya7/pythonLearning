#Simple Quiz Game using Functions (Practice)

#Requirements:
"""
1. Minimum 3 Questions define garney (question + correct answer)
2. askQuestion function:
    a.Question user lai sodhne.
    b.User ko answer correct cha bhane 1 point add garney , wrong bhaye 0 point add garney.
3. showScore function: Total score print garney
4. User le case insensitive answer haley pani thik answer ma count garney
"""


#Goal:
"""
Functions practice (askQuestion , showScore)
Conditonal logic (correct / incorrect check garney) practice.
"""


#Implementation:
"""
def askQuestion():
    score = 0
    
    ans = input("What is the capital of Nepal: ")
    if ans.strip().lower() == "kathmandu":
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
    
    try:
        ans2 = int(input("\n5 + 2 = "))
        if ans2 == 7:
            print("Correct Answer")
            score += 1
        else:
            print("Incorrect Answer")
    except ValueError:
        print("Please Enter Integer value.")
        
    ans3 = input("\nWhat is the largest planet in our solar system? ")
    if ans3.strip().lower() == "jupiter":
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
    
    return score

def showScore(totalScore):
    print("\nYour total score is:", totalScore)

totalScore = askQuestion()
showScore(totalScore)
"""



#OR 
# In a professional way:


#Implementation

def askQuestion(question, correctAnswer):
    """Function to ask question and return score based on answer"""
    userAnswer = input(question + " ")
    if userAnswer.strip().lower() == correctAnswer.strip().lower():
        print("Correct Answer!\n")
        return 1
    else:
        print("Incorrect Answer!\n")
        return 0
    
def showScore(totalScore):
    """Function to show total score"""
    print(f"Your total score is: {totalScore}\n")

questions = [
    ("What is the capital of Nepal?", "Kathmandu"),
    ("5 + 2 = ?", "7"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What is the chemical symbol for water?", "H2O"),
    ("Who wrote 'Romeo and Juliet'?", "Shakespeare"),
    ("What is the capital of United States?", "Washington, D.C."),
]

totalScore = 0

for quest, ans in questions:
    totalScore += askQuestion(quest, ans)
    
showScore(totalScore)
