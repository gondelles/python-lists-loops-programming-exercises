incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]

# Your code here
def full_names(usuario):

    full_name = usuario["name"] + " " + usuario["last_name"]

    return full_name

def data_transformer(incoming_ajax_data):

    full_name = list(map(full_names,incoming_ajax_data))

    return full_name

print(data_transformer(incoming_ajax_data))


