def add_and_subtract(num_one,num_two,num_three):

    def sum_numbers():

        return num_one + num_two

    def subtract():
        return sum_numbers() - number_three
    return subtract()


number_one = int(input())
number_two = int(input())
number_three = int(input())


function = add_and_subtract(number_one,number_two,number_three)
print(function)

