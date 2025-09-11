def get_word_count(path_to_file):
    with open(path_to_file) as f:
        content=f.read()
        word_list = content.split()
        return len(word_list)

def get_char_count(path_to_file):
    with open(path_to_file) as f:
        content=f.read().lower()
        counts={}
        for c in content:
            if c not in counts:
                counts[c]=1
            else:
                counts[c] = counts[c]+1 
    return counts

def char_list(dict):
    char_dict=[]
    for count in dict:
       char_dict.append({"char" : count, "num" : dict[count]})
    return char_dict

def sort_on(items):
    return items["num"]

