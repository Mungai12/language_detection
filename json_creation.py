import json


def add_english_dict(words):
    filename = 'dictionary.json'

    with open(filename) as f:
        data = json.load(f)

    for key, value in data.items():
        corpus = {'text': value, 'lang_id': 'en'}
        words.append(corpus)

    return words


def add_swahili_dict(words):
    filename = 'swahili.json'
    with open(filename) as f:
        data = json.load(f)

    for key, value in data.items():
        text = ''
        for k, v in value.items():
            if v is not None:
                text += v
        corpus = {'text': text, 'lang_id': 'sw'}
        words.append(corpus)
    return words


def create_json(words):
    filename = 'corpora.json'
    with open(filename, 'w') as f_obj:
        json.dump(words, f_obj)


words = []
words = add_english_dict(words)
words = add_swahili_dict(words)
create_json(words)