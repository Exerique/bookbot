def get_num_words(content):
    word_split = content.split()
    return len(word_split)

def count_char(texts):
    dictionary_alph = {}
    lowered_case = texts.lower()
    for t in lowered_case:
        if t in dictionary_alph:
            dictionary_alph[t] += 1
        else:
            dictionary_alph[t] = 1
    return dictionary_alph
        

def store_count(dicti):
    dict_to_list = []
    for d, k in dicti.items():
        dict_to_list.append({"char": d, "num": k})
    dict_to_list.sort(key=lambda item: item["num"], reverse=True)
    return dict_to_list