def check_sum(num_list):

    for first_number in num_list:
        for second_number in num_list:
            result = first_number + second_number
            if result == 0:
                return True
    return False            
            

num_list = [10, -14, 26, 5, -3, 13, -5]
print(check_sum(num_list))