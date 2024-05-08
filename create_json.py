import json


def main():
    print("Starting...") 
    raw_dict = read_txt()
    print("File Read!")
    print("Parsing words...")
    parsed_dict = parse_words(raw_dict)
    print("Creating new file")
    create_file(parsed_dict)
    print("New file created!")


def read_txt():
    path = "words_dictionary.txt"
    file = open(path, 'r')
    words = file.readlines()
    file.close()

    return words


def parse_words(words):
    json_dict = {}
    for word in words:
        stripped_word = word.rstrip()
        word_length = len(stripped_word)
        
        if word_length not in json_dict:
            json_dict[word_length] = {}
        key = len(json_dict[word_length])
        json_dict[word_length][key] = stripped_word
    
    return json_dict


def create_file(json_dict):
    json_object = json.dumps(json_dict, indent=4)
    with open("dictionary.json", "w") as outfile:
        outfile.write(json_object)
    outfile.close()


main()
