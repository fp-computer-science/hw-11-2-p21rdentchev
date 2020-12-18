# Ryan Dentchev

lst = ['Cat', 'Dog', 'Moose', 'Cow']


def find_thing(lst, element):
    for words in lst:
        for index, letters in enumerate(words):
            if letters == element:
                print(index, element)


find_thing(['Cat', 'Dog', 'Moose', 'Cow'], 'o')
