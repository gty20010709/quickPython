import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


quizNum = 1
for i in range(35):
    # create one quiz
    quizFile = open(f'Quiz{quizNum}.q','w')
    answerFile = open(f'Answer{quizNum}.a','w')


    # header of the quiz
    quizFile.write('Name:\n\nData:\n\nPeriod:\n\n')
    quizFile.write(' '*20 + f'State Capitals Quiz (Form {quizNum})\n')

    status = list(capitals.keys())
    random.shuffle(status)

    # Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        correctAnswer = capitals[status[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOption = wrongAnswers + [correctAnswer]
        random.shuffle(answerOption)
    
    # write the question and the answer options to the quiz file.
        quizFile.write(f'{questionNum+1}. What is tha capital of {status[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f'{"ABCD"[i]}. {answerOption[i]}\n')
        quizFile.write('\n')

        # write the answer key to a file
        answerFile.write(f'{questionNum+1}. {"ABCD"[answerOption.index(correctAnswer)]}\n')
    
    quizNum += 1
    quizFile.close()
    answerFile.close()