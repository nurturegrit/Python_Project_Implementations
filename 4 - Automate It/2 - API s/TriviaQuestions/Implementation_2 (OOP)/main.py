from data import question_bank
from question_model import Question
from quiz_brain import QuizBrain


question_bank = [Question(dict['question'], dict['correct_answer']) for dict in question_bank()]

def main():
    quiz = QuizBrain(question_bank())
    while quiz.still_has_questions():
        quiz.next_question()

main()