the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
new_list = list(map(lambda x: 'woko' if x == 0 else 'wiki', the_bools))

print(new_list)