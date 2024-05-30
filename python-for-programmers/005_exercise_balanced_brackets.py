def check_balance(brackets):

    half_index = int(len(brackets)/2)

    first_half_string = brackets[:half_index]

    second_half_string = brackets[half_index:]

    second_half_string = list(second_half_string)

    reversed_list = []

    for i in range(len(second_half_string) - 1, -1, -1):
        reversed_list.append(second_half_string[i])

    second_half_string_reversed = ''.join(reversed_list)

    second_half_string_reversed = second_half_string_reversed.replace('[', '_')

    second_half_string_reversed = second_half_string_reversed.replace(']', '[')

    second_half_string_reversed = second_half_string_reversed.replace('_', ']')

    print(first_half_string)
    print(second_half_string_reversed)

    if first_half_string == second_half_string_reversed:
        return True
    else:
        return False

bracket_string = '[[[][]]][[]]'

print(check_balance(bracket_string))
