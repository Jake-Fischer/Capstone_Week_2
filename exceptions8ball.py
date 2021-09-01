import requests

question = input('Enter your question for the magic 8 ball: ')

magic_8_ball_url = f'https://8ball.delegator.com/magic/JSON/{question}'

try:
    responce = requests.get(magic_8_ball_url).json()
    answer = responce['magic']['answer']
    print(f'that magic 8 ball says.... {answer}')
except Exception as e:
    print(e)
    print('Sorry, something went wrong.')

