import json

with open('text_7.txt', 'r', encoding='utf8') as tf7_r:
    with open('text_77.json', 'w', encoding='utf8') as tf7_w:
        my_dict = {s.split()[0]: int(s.split()[2]) - int(s.split()[3]) for s in tf7_r}
        average = [my_dict, {'average': round(sum([int(n) for n in my_dict.values() if int(n) > 0]) / len([int(n) for n in my_dict.values() if int(n) > 0]))}]
        json.dump(average, tf7_w, ensure_ascii=False, indent=4)
