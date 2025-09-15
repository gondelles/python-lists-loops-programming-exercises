all_names = ["Romario", "Boby", "Roosevelt", "Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

# Your code here
def resulting_names(name):
    return name[0] == "R"

final_list = list(filter(resulting_names, all_names))

print(final_list)




