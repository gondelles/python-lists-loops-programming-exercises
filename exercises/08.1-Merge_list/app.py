chunk_one = ['Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell']
chunk_two = ['Lucas', 'Jake', 'Scott', 'Amy', 'Molly', 'Hannah', 'Lucas']


def merge_list(list1, list2):
    # Your code here
    new_list = []
    for n in chunk_one:
        new_list.append(n)
    for n in chunk_two:
        new_list.append(n)
    return new_list

print(merge_list(chunk_one, chunk_two))
