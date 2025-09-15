my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds():
    var1 = 0

    for n in my_list:
        if n % 2 != 0:
            var1 += n
    return var1

print(sum_odds())