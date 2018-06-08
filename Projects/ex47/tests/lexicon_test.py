directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
nouns = ['door', 'bear', 'princess', 'cabine']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def show(dictor):
    return type(dictor)


def test_show():
    show(nouns) == list
