list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
sorted_list = []

def sort_odd_even(list):

    even = []
    odd = []
    
    for n in list:
        if n % 2 != 0:
            odd.append(n)
        else:
            even.append(n)
            
    sorted_list = odd
    sorted_list.extend(even)   
    
    return sorted_list
        




print(sort_odd_even(list_of_numbers))

