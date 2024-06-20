from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = [Question(dict['text'], dict['answer']) for dict in question_data]

def main():
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()

main()