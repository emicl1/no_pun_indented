list_from_the_file = []
list_of_commas = []
internal_index = 0
internal_lenght = 0
internal_latest_index = 0
with open("input.in", "r") as file:
    for line in file:
        list_from_the_file.append(line)
        if line[-2:-1] == ":":
            list_of_commas.append([internal_index, -1])
            internal_latest_index += 1
            internal_lenght = 0
        if len(list_of_commas) > 0:
            list_of_commas[internal_latest_index-1][1] += 1
        internal_index += 1
        internal_lenght += 1

print(list_of_commas)
n = 3
levely = n-2
posloupnost_sum = 11/2 *(1+11)



def calculate_number_of_posibilities_for_one_comma(max_level, number_of_neutral_commands):
    """
    from the original list of list take specific index of the comma and the num of commands after it
    :param max_level: index of the commas
    :param number_of_neutral_commands: the seconds number in the list of lists
    :return:
    """
    if number_of_neutral_commands == 0:
        return 0
    if number_of_neutral_commands == 1:
        return max_level
    if number_of_neutral_commands == 2:
        return max_level/2 * (1+max_level)
    if number_of_neutral_commands >= 3:
        a = 0
        for j in range(1, number_of_neutral_commands+1):
            b = 0
            for i in range(1, max_level+1):
                b += calculate_number_of_posibilities_for_one_comma(i, j)
            a = b
        return a

print(calculate_number_of_posibilities_for_one_comma(3, 3))









