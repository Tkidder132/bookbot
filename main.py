import operator;

character_dict = {};
path_to_file = "books/frankenstein.txt";
words_found_count = 0;

def add_to_character_dict(word):
    for character in list(word.lower()):
        if character.isalpha():
            try:
                character_dict[character] += 1;
            except KeyError:
                character_dict[character] = 1;

def read_contents():
    with open(path_to_file) as f:
        file_contents = f.read();
        words = file_contents.split();
        words_found_count = len(words);
        for word in words:
            add_to_character_dict(word);

def print_report():
    print(f"--- Begin report of {path_to_file} ---");
    print(f"{words_found_count} words found in the document\n");
    for character in dict(sorted(character_dict.items(), key=operator.itemgetter(1), reverse=True)):
        print(f"The '{character}' character was found {character_dict[character]} times");
    print("--- End report ---");

read_contents();
print_report();