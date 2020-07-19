import json
import os
from difflib import get_close_matches

lexicon_data = None

def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as data_file:
            global lexicon_data
            lexicon_data = json.load(data_file)
            return lexicon_data            
    else:
        print("Please give me the correct file path for data")
        return None

def find_meaning(word):
    word = word.lower()
    if word in lexicon_data:
        return lexicon_data[word]
    elif word.title() in lexicon_data:
        return lexicon_data[word.title()]
    elif word.upper() in lexicon_data:
        return lexicon_data[word.upper()]
    elif len(get_close_matches(word, lexicon_data.keys())) > 0:
        user_answer = input("Did you mean %s? press y for yes or n for no. " % get_close_matches(word, lexicon_data.keys())[0] )
        if user_answer.lower() == "y":
            return lexicon_data[get_close_matches(word, lexicon_data.keys())[0] ]
        elif user_answer.lower() == 'n':
            return ["The word does not exist in our lexicon!!!"]
        else:
            return ["We could not understand your response"]
    else:
        return ["The word does not exist in our lexicon!!!"]


if __name__=="__main__":
    load_data("data.json")

    word = input("Please enter word to find it's meaning: ")

    print("\n".join(find_meaning(word)))