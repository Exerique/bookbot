from stats import count_char,store_count,get_num_words
import sys

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}")
    with open(filepath) as fe:
        file_content = fe.read()   
    return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        characters_all = get_book_text(sys.argv[1])
        print("----------- Word Count ----------")
        word_num = get_num_words(characters_all)
        print(f"Found {word_num} total words")
        print("--------- Character Count -------")
        char_num = count_char(characters_all)
        sorted_char = store_count(char_num)
        for items in sorted_char:
            if items["char"].isalpha():
                print(f"{items['char']}: {items['num']}")
        print("============= END ===============")

main()