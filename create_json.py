import json


def main():
    print("Starting...") 
    raw_dict = read_txt()
    print("File Read!")
    print("Creating new file")
    create_file(raw_dict)
    print("New file created!")


def read_txt():
    path = "words_dictionary.txt"
    file = open(path, 'r')
    words = file.readlines()
    file.close()

    json_dict = {}
    for word in words:
        stripped_word = word.rstrip()
        json_dict[stripped_word] = len(stripped_word)
    
    return json_dict


def create_file(json_dict):
    json_object = json.dumps(json_dict, indent=4)
    with open("dictionary.json", "w") as outfile:
        outfile.write(json_object)
    outfile.close()


main()
