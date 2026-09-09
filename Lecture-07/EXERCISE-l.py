survey_results = [
    ["Python","JavaScript","C++"],
    ["Python","JavaScript","C#"],
    ["Python","Java"],
    ["Python","JavaScript","C++"],
    ["Python","JavaScript","C++","Java"]
]


choices_sets = [set(x) for x in survey_results]
# print(choices_sets)
common_languages = set.intersection(*choices_sets)
print("1. Languages chosen by all respondents:", common_languages)


all_languages = set.union(*choices_sets)
repeatedly_languages = set()
for i in range(len(choices_sets)):
    for j in range(i+1,len(choices_sets)):
        repeatedly_languages.update(choices_sets[i] & choices_sets[j])
unique_languages = all_languages - repeatedly_languages
# print(unique_languages)   
print("2. Languages only chosen by one participant:", unique_languages)


len_all_languages = len(all_languages)
print("3. Number of unique languages:", len_all_languages)


language_chosen_two = set()
for l in all_languages:
    count = sum(l in word for word in choices_sets)
    if count == 2:
        language_chosen_two.add(l)
print("4. Languages chosen by exactly two participants:", language_chosen_two)



partivipants_have_same_of_fav_languages = []
for i in range(len(choices_sets)):
    for j in range(i+1,len(choices_sets)):
        if choices_sets[i] == choices_sets[j]:
            partivipants_have_same_of_fav_languages.append([i+1,j+1])
print("5. Participants with the same set of languages:",partivipants_have_same_of_fav_languages)