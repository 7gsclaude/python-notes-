
person = {
    'name': 'claude',
    'occupation': 'engineer',
    'location': 'chicago'
}

# print(type(person))

# (print(person['name']))

# phrase = f'myname is {person["name"]}'
# print(phrase)

# print(person.get('fave_color', "blue" ))
# blue is a strict value to find the color as. 
# this will return none, python saying that it doesnt exist. 
# we can set values to items using square brkacket notation 

# user_input = input('pleasde in put a char')
# if user_input in 'aeiouy':
#     print()

# we can use an operater to check whether an item exists ina  dictionary

# if 'fav_color' in person:
#     print(person ['fav_color'])
# else:
#     color = input ('please enter your fave color: ')
#     person ['fav_color'] = color 
#     print(person)

#deleting items from a dictionary with del operator 
# del person ['location']

# print(person)

# def delete_item(item, person_object):
#     del person_object[item]
#     print(f'{item} has been removed from {person_object}')

# delete_item('location', person)

#iterating over items 

# looping over all items and grabbing the keys
 
# for key in person:
#     print(key)
#     another version of this is 
#     print (person[key])

    # apprently this is bad practice ???? ^^^

# dictionaries have a mechism built in in the form of a method 
# .items  
# converts dictionaries into objects that can be iterated over better  
# dictionary view object. diesnged to make a dictionary easier to iterate 
# print(person.items())

# for key, value in person.items():
#     print(key, value)


# where_my_things_are = {
#     "ps5" : "my room",
#     "reeftank": "entry"
# }

# for thing, location in where_my_things_are.items():
#     print(f"my {thing} is kept in {location}")

#pyhton lists

colors = ['red', 'green', 'blue']

# #access items
# print(colors[-1])

# # assigning items to a list
# colors[1] = 'seafoam green'

# #adding an item to a list 
# colors.append('purple')

# #print(colors)
# print(dir(colors))

# other_colors = ['orange', 'black']

# colors.extend(other_colors)
# # extend uses add behind the scenes 

# print(colors+['orange', 'grey'])

# colors.insert(1, 'yellow')

# # delete or remove items from a list 

# colors.pop(-2)
# # this is assignable to a variable

# colors.remove("blue")
# #needs you to actually write it out and there could be typos fromthat

# del colors[1]

# colors.clear() 
# # will nuke the list 

# print (colors)


# phrase_list = []

# ## iterating a list
# for color in colors: 
#     phrase = f'{color} is a cool color'
#     phrase_list.append(phrase)
# print(phrase_list)


# print (enumerate(colors))
# # this shows a specifc number that chagnes everttime inside of my ocmputer, does something similart to dictionary.items
# # enumerate allows fro the acces of index position 

# for index, color in enumerate(colors):
#     # print(f'{color} is located at position {index}')

    # this allows access to an index item in a list 

# nums = [1,2,3,4,5,6,7,8,9,10]


# # list comprehension 
# squares = [n * n for n in nums]
# # 

# even_squares = [n * n for n in nums if (n*n) % 2 == 0]
# # this is saying if it produces an even number then it will return 

# print(squares)


#TUple example 
# colors = ('red','green', 'blue' )

# # print(type(colors))

# phrases_tuple = ('hello world',)
# # print(type(phrases_tuple))

# # commas create the tuple 

# print(dir(phrases_tuple))

# print(colors[-1]) 
# print(colors.index('green')) #kinda works like index of 

# #tuple unpacking
# a,b,c = colors

# #can reaassing these variabels now
# a = 'something else entirely'

# print(a,b,c)



#slice operator in python 
#useable for every sequence type 

print('hellowrold'[:5])
# this will slice up to but not including 5

nums = list(range(0,101)) [1::2]
nums = list(range(0,101))[1:25:2]

#adding a step sequence / adding addtional colon  it will step over the evens 

print(colors[1:])
# strings cannot be mutated
