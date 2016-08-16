# def sort1(languages):
    # val_list = languages.values()
    # val_list.sort()
    # for key in val_list:
    #     print(key)
    # return sorted(sorted_byval, key=)
    
# def sort1a(langauges):
#     lst = sorted(sorted(langauges), key = languages.__getitem__)
#     for x in lst:
#         print("\t" + x)
def sort1b(d):
    import operator
    lst = sorted(sorted(d.items()), key=operator.itemgetter(1))
    print("1:")
    for language, type_ in lst:
        print("\t"+language)


def sort2(langauges):
    lst = sorted(langauges, key=len)
    print("2:")
    for item in lst:
        print("\t"+item)

def sort3(d):
    
    lst = sorted(sorted(d), key=last_char, reverse=True)
    print(sorted(d))
    print("3:")
    for item in lst:
        print("\t"+item)

def last_char(string):
    return string[-1].lower()

"""
Write three functions:

sort1(langauges)
sort2(languages)
sort3(langauges)
Goal: Print exactly the below w/ three functions:
1:
    Arabic
    English
    Koine Greek
    Latin
    Romanian
    C++
    JavaScript
    Python
    R
2:
    R
    C++
    Latin
    Arabic
    Python
    English
    Romanian
    JavaScript
    Koine Greek
3:
    JavaScript
    R
    Latin
    Python
    Romanian
    Koine Greek
    English
    Arabic
    C++
"""
def main():

    languages = {'JavaScript': 'P',
                 'Arabic': 'N',
                 'R': 'P',
                 'Python': 'P',
                 'C++': 'P',
                 'Koine Greek': 'N',
                 'Latin': 'N',
                 'Romanian': 'N',
                 'English': 'N'}
    sort1b(languages)
    sort2(languages)
if __name__ == '__main__':
    main()
