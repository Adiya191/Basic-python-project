#this is basic program to study table of different number by Aditya Yadav

import random

numbers = list(range(12,20))
no_of_time_asking = 14 
current_number_table = random.choice(numbers)

while no_of_time_asking > 0:
    if numbers == []:
        break
    current_number = random.choice(numbers)
    current_number_index = numbers.index(current_number)
    numbers_0_9 = list(range(1,11))
    no_of_time_asking_2 = 10

    while no_of_time_asking_2 > 0:
        current_number_2 = random.choice(numbers_0_9)
        current_number_2_index = numbers_0_9.index(current_number_2)
        answer_ = input(f"{current_number}*{current_number_2}: ")
        if current_number * current_number_2 == int(answer_):
            print(f"😀,Your Answer is Correct {answer_}")
        else:
            print(f"😪,Your Answer is wrong,Actual Answer is  {current_number*current_number_2}")
        numbers_0_9.pop(current_number_2_index)
        no_of_time_asking_2 = no_of_time_asking_2 - 1
    numbers.pop(current_number_index)
    no_of_time_asking = no_of_time_asking - 1