def name_sorter(name_list):
    dict_names = {}
    male_list = []
    female_list = []
    for name in name_list:
        if name[-1] == 'a':
            female_list.append(name)
        else:
            male_list.append(name)
    print(male_list)
    print(female_list)
    dict_names['female'] = sorted(female_list)
    dict_names['male'] = sorted(male_list)
    return dict_names


names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
print(name_sorter(names))
