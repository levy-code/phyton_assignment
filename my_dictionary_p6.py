my_name = "Leslevy Arienza"
les_dictionary = {
    'Gender':           'Female',
    'Age':              29,
    'Hobby':            'Reading',
    'Marital Status':   'Single',
    'Occupation':       'Retail'
    }
print (f"My name is {my_name} and this is my dictionary!")

for key, value in les_dictionary.items():
    print(f"My {key} is {value}")

les_dictionary_add = {'Country': 'Philippines'}
les_dictionary.update(les_dictionary_add)
print(f"My new added dictionary: {les_dictionary}")

les_dictionary.pop('Marital Status')
print(f"My dictionary without Marital Status: {les_dictionary}")

les_dictionary['Age'] = 28
print(f"My dictionary with updated Age: {les_dictionary}")

les_dictionary.clear()
print(les_dictionary)
