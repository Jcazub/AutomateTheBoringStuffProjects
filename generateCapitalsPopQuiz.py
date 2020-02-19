import os
import sys
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
                'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
                'New York': 'Albany', 'North Carolina': 'Raleigh',
                'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
                'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
                'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


def main():
    quizzes_num = 5
    questions_num = 5

    if len(sys.argv) > 1:
        quizzes_num = sys.argv[1]
    if len(sys.argv) > 2:
        questions_num = sys.argv[2]
        if questions_num > 50:
            sys.exit('questions exceeded limit allowed')

    create_quizzes(quizzes_num, questions_num)




def create_quizzes(quizzes, questions):

    # create the number of quizzes
    for i in range(quizzes):
        current_quiz = str(i + 1)

        quiz = open('quiz' + current_quiz, 'w')
        answer_key = open('answerkey' + current_quiz, 'w')

        quizBoilerPlate(quiz)
        answerkeyBoilerPlate(answer_key, current_quiz)

        states_list = list(capitals.keys())
        random.shuffle(states_list)

        capitals_list = list(capitals.values())

        for i in range(questions):
            answer = capitals[states_list[i]]
            answer_key.write('Question ' + str(i + 1) + ' answer: ' + answer + '\n')

            random.shuffle(capitals_list)
            choices = [answer]

            while len(choices) < 5:
                wrong_answer_num = random.randint(0, len(choices))
                if capitals_list[wrong_answer_num] not in choices:
                    choices.append(capitals_list[wrong_answer_num])
            random.shuffle(choices)

            quiz.write('Question ' + str(i + 1) + ': ' + states_list[i] + '\n')
            for choice in choices:
                quiz.write(choice + ', ')
            quiz.write('\n')

        quiz.close()
        answer_key.close()


def quizBoilerPlate(quiz):
    quiz.write('Welcome to my quiz student!\n')
    quiz.write('Here are the questions!\n')


def answerkeyBoilerPlate(answer_key, current_quiz):
    answer_key.write('The answer key for quiz ' + current_quiz + '\n')


if __name__ == '__main__':
    main()
