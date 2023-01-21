#################################################################
# For a competition, you need to find a competitor who is second place.
# Points are: 2, 3, 6, 6, 5
# Example input: 2, 3, 6, 6, 5
# Example output: 5
#################################################################

competition = [2, 3, 6, 6, 5]


def second_one(list_x):
    # This list is not contain max(list_x
    second_max_list = list()
    # Now, func. finds the maximum value of list_x, then if element is not equal to maximum value,
    # element goes to second_max_list
    for element in list_x:
        if element == max(list_x):
            continue
        else:
            second_max_list.append(element)
    # func. takes the maximum value of second_max_list, at the same time second max. score of list_x
    second_one_list_x = max(second_max_list)
    return second_one_list_x


second_one(competition)