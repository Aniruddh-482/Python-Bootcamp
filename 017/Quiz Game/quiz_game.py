from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # Question_Text = question["text"]
    # Question_Answer = question["answer"]
    Question_Text = question["question"]
    Question_Answer = question["correct_answer"]
    New_Question = Question(Question_Text, Question_Answer)
    question_bank.append(New_Question)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

