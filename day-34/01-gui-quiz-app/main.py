# ----------------------------------------------------------------------------------------------------------------------
# > Day 34 - GUI Quiz App Project --------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# > File: main.py
# > Module: Main Module
# > Description: Entry point of the application; initializes and runs the main logic.
# > Author: Fabio Chippari
# > Created: 2025-10-27
# ----------------------------------------------------------------------------------------------------------------------
# > Imports ------------------------------------------------------------------------------------------------------------

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# > Main ---------------------------------------------------------------------------------------------------------------

def main():
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)

if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
