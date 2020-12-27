from dataclasses import dataclass
from load_files import LoadFiles
import random
from sys import exit

@dataclass
class Quiz:
    """
    Main class for performing quiz.
    :argument:
        number_of_questions - number of questions to run.
    """
    number_of_questions: int

    def get_questions(self) -> tuple:
        """
        Get category, questions and answers from CSV file.
        :returns:
            category, questions and answers or Exception of specified number of questions os too large.
        """
        load_files = LoadFiles()
        try:
            for key, value in load_files.load_csv_files().items():
                yield key, random.sample(list(value.items()), self.number_of_questions)
        except ValueError:
            exit('Specified number of questions is larger than number of questions in CSV files!')

    def select_category(self) -> int:
        """
        Select category from available categories
        :returns:
            number of category
        """
        for question in self.iterate():
            print(question[0], question[1][0])
        return int(input('Select category:'))

    def perform_quiz(self, language='es_pl') -> None:
        """
        Main method to run quiz.
        :param:
            language: language that should be as a question and answer.
        """
        selected_category = self.select_category()
        for questions in self.iterate():
            if questions[0] == selected_category:
                print('Chosen:', questions[1][0])
                for question in questions[1][1]:
                    if language == 'es_pl':
                        correct_answer = question[1]
                        print(question[0])
                    else:
                        correct_answer = question[0]
                        print(question[1])

                    answer = input('answer: ').encode('utf-8').rstrip()
                    if answer.lower() == correct_answer.lower().encode('utf-8'):
                        print('GOOD!')
                    else:
                        print('WRONG! Correct answer:', correct_answer)

    def iterate(self) -> tuple:
        """
        Iterate over questions.
        :returns:
            Tuple with category number, question and answer from CSV file.
        """
        for question in list(enumerate(self.get_questions())):
            yield question
