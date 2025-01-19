import requests

def question_bank():
    response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
    response.raise_for_status()
    return response.json()["results"]
