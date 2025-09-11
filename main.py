from stats import *
import sys


def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    dict = get_char_count(sys.argv[1])
    char_dict=char_list(dict)
    char_dict.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(sys.argv[1])} total words")
    print("--------- Character Count -------")
    for char in char_dict:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")
main()