
l = [2, 3, 6, 6, 5]

def second_place(l):

    l.sort(reverse=True)

    first_place_score = l[0]

    for elem in l:
        if elem < first_place_score:
            return_string = "Congratulations second place with score {}!".format(elem)
            return return_string



print(second_place(l))