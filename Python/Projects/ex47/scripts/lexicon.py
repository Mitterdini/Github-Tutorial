direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
noun = ['door', 'bear', 'princess', 'cabine']
verb = ['go', 'stop', 'kill', 'eat']
stop = ['the', 'in', 'of', 'from', 'at', 'it']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

dictionaries = [direction, noun, verb, stop, number]

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]

def dict_get(word):
    for i in range(len(dictionaries)):
        if word in dictionaries[i]:
            return(namestr(dictionaries[i], globals())[0])
        else:
            pass
    raise ValueError("Invalid Dictionary, word not in dictionaries")

def extractor():
    answer = input('> ')
    words = answer.split()
    return words

def tuple_creator(word_list):
    listed_tuples = []
    word_num = len(word_list)
    for i in range(word_num):
        listed_tuples.append((dict_get(word_list[i]), word_list[i]))
    return listed_tuples

def scan():
    tuple_list = []
    sentence_list = extractor()

    tuple_list.extend(tuple_creator(sentence_list))
    return(tuple_list)
