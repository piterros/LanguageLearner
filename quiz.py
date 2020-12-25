from load_files import LoadFiles
import random

class Quiz:

    def quiz(self, number_of_questions=3):
        load_files = LoadFiles()
        for key, value in load_files.load_csv_files().items():
            yield key, random.sample(list(value.items()), number_of_questions)

    def test(self, language='es_pl', number_of_questions=3):

        for x in self.quiz(number_of_questions=number_of_questions):
            for y in x[1]:
                if language == 'es_pl':
                    question = y
                    correct_answer = y[1]
                    print(question[0])
                else:
                    question = y
                    correct_answer = y[0]
                    print(question[1])

                answer = input('answer: ').encode('utf-8').rstrip()
                if answer.lower() == correct_answer.lower().encode('utf-8'):
                    print('good!')
                else:
                    print('bad! correct:', correct_answer)
