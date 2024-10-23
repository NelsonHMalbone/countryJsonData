# this is the project for the udemy course
# Learn Python by Doing with 100 Projects
import requests

url = 'https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json'
response = requests.get(url)
content = response.json()


question_id = int(input('Enter the question ID: '))

# vars to track question correct answer and whether question was found

question_correct = None
question_found = False



for x in content['quizzes']:
    for questions in x['questions']:
        if questions['id'] == question_id:
            question_found = True
            for choice, is_correct in questions['choices'].items():
                if is_correct:
                    question_correct = choice

# check question with given id found
if question_found:
    # check if there was a correct answer
    if question_correct:
        print(f"The correct answer is: {question_correct}")
    else:
        print("No correct answer found for the given question ID.")
else:
    print("Question ID not found.")
