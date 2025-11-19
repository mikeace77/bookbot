def how_many_words(file):
    split_word = file.split()
    total_count = len(split_word)
    return f"Found {total_count} total words" 

def each_word_counter(text):
    x = text.lower()
    word_lists = []
    the_dict = {}
    counter = 0
    for ch in x:
        if ch not in the_dict:
            the_dict[ch] = 1
        else:
            the_dict[ch] = the_dict[ch] + 1
    return the_dict

def sort_progress(items):
    my_list = []
    for item in items:
        count = items[item]
        new_dict = {"char": item, "num": count}
        my_list.append(new_dict)
    my_list.sort(reverse=True, key=sort_on)
    return my_list

def sort_on(d):
    return d["num"]