def is_decreasing(number:int) -> bool:
    '''
    Function checks if numbers are decreasing
    :param number: int. number to be checked
    :return: bool
    '''
    number_str = str(number)
    lenghth_number = len(number_str)
    for i in range(1, lenghth_number):
        if int(number_str[i]) < int(number_str[i-1]):
            return False
    return True

def check_is_2_adjacent_groups(number:int) -> bool:
    '''
    Function checks if there are at least 2 groups of adjacent numbers
    :param number: int. number to be checked
    :return: bool
    '''
    already_used_number = []
    number_str = str(number)
    lenghth_number = len(number_str)
    for i in range(1, lenghth_number):
        if number_str[i] == number_str[i-1]:
            if number_str[i] not in already_used_number:
                already_used_number.append(number_str[i])
    if len(already_used_number) >=2:
        return True

#playground

match = []
for i in range(372**2, 809**2+1):
    if not is_decreasing(i):
        continue
    elif check_is_2_adjacent_groups(i):
        match.append(i)

print(f"{len(match)} numbers match all three conditions!")
print(match)