from load_files import LoadFiles
import random

class Quiz:

    def quiz(self, number_of_questions=3):
        load_files = LoadFiles()
        for key, value in load_files.load_csv_files().items():
            yield key, random.sample(list(value.items()), number_of_questions)
            # if language == 'pl':
            #     yield key, random.sample(list(value.values()), 3)
            # else:
            #     yield key, random.sample(list(value.items()), 3)

    def test(self):
        quiz = Quiz()
        es = 'antes'
        pl = 'kiedyś'

        for x in quiz.quiz(number_of_questions=1):
            for y in x[1]:
                print(y[0])
                answer = input('answer: ')
                if answer.lower() == y[1].lower():
                    print('good!')
                else:
                    print('bad! correct:', y[1])
