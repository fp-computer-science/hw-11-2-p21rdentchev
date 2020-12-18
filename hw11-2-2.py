# Ryan Dentchev

def odds(lst):
    for index, values in enumerate(lst):
        if values % 2 != 0:
            print(index, values)


odds([1, 2, 3, 4, 5, 6, 7, 8])
