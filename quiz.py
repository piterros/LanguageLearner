from load_files import LoadFiles
import random
from sys import exit

class Quiz:
    """
    Main class for performing quiz.
    """
    def __init__(self):
        self.correct_answer: str = ''

    def get_questions(self) -> tuple:
        """
        Get category, questions and answers from CSV file.
        :returns:
            category, questions and answers
        """
        load_files = LoadFiles()
        for key, value in load_files.load_csv_files().items():
            yield key, list(value.items()), len(list(value.items()))

    def get_questions_data(self) -> None:
        """
        Print number of category, category name, and number of questions.
        """
        for question in list(enumerate(self.get_questions())):
            print(f"{question[0]} {question[1][0]} [questions: {question[1][2]}]")

    def select_category_and_number_of_questions(self):
        """
        Select category from available categories.
        :returns:
            number of category or Exception of specified number of questions os too large.
        """
        self.get_questions_data()
        category = int(input('Select category: '))
        print(f'Chosen category: {list(self.get_questions())[category][0]}')

        try:
            number_of_questions = int(input('Set number of questions: '))
            randomized_questions = random.sample(list(enumerate(self.get_questions()))[category][1][1],
                                                 number_of_questions)
            return randomized_questions
        except ValueError:
            exit('ERROR! Specified number of questions is larger than number of questions in CSV files!')

    def perform_quiz(self):
        """
        Main method to run quiz.
        """
        selected_questions = self.select_category_and_number_of_questions()
        wrong_language = True
        while wrong_language:
            wrong_language = False
            language = input('Select language: ')
            for questions in selected_questions:
                if language == 'es_pl':
                    self.correct_answer = questions[1]
                    print(questions[0])
                    self.send_answer()
                elif language == 'pl_es':
                    self.correct_answer = questions[0]
                    print(questions[1])
                    self.send_answer()
                else:
                    print('Wrong language!')
                    wrong_language = True
                    break

    def send_answer(self) -> None:
        """
        Send answer and check if it's correct.
        """
        answer = input('answer: ').encode('utf-8').strip()
        if answer.lower() == self.correct_answer.lower().encode('utf-8').strip():
            print('GOOD!')
        else:
            print('WRONG! Correct answer:', self.correct_answer)

