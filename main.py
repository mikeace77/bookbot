from stats import how_many_words, each_word_counter, sort_progress, sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]    
    text = get_book_text(path)
    # print(path)
    # print(how_many_words(file))
    # print(each_word_counter(path))
    # my_list = []
    # my_list.append(each_word_counter(path))
    # my_list.sort(reverse=True, key=sort_on)
    print(sort_progress(each_word_counter(text)))
    # print(sort_on(items))
    print("============ BOOKBOT ============")
    print(path)
    print("----------- Word Count ----------")
    print(how_many_words(text))
    print("--------- Character Count -------")
    chars_dict = each_word_counter(text)
    sorted_chars = sort_progress(chars_dict)

    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item["num"]}")
    
    print("============= END ===============")
   
main()


