my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

# Your code here
sum_total = 0
number_of_items = len(my_list)

for n in my_list:
    sum_total += n

avg = sum_total / number_of_items
print(avg)