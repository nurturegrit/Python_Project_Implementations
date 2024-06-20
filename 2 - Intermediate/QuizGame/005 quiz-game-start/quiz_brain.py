class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.player_points = 0

    def still_has_questions(self):
        if self.question_number + 1 <= len(self.question_list):
            return True
        return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        ans = input(f"Q.{self.question_number + 1}:{current_question.text} (True/False): ")
        if ans == current_question.answer:
            self.player_points += 1
            print(f"Correct! You guessed right! ({self.player_points}/{self.question_number+1})")
        else:
            print(f"Incorrect! You guessed wrong. ({self.player_points}/{self.question_number+1})")
        self.question_number += 1