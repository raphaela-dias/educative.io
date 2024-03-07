def check_balance(brackets, open_brackets, close_brackets):

    if brackets[0] == ']' or brackets[-1] == '[':
        return False
    else:
        for i in range(1, (len(brackets)) - 1):
            if brackets[i] == '[':
                open_brackets += 1
            else:
                close_brackets += 1

        if open_brackets == close_brackets:
            return True
        else:
            return False

open_brackets = 0
close_brackets = 0
bracket_string = '[[[[][]]]'

print(check_balance(bracket_string, open_brackets, close_brackets))