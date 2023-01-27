def example_function():
    print('this is an exmaple of python')
    return "this got returned"
result = example_function()
print(result)
#results none 

# lambda functions -- inline functions in python 

add_two_nums = lambda a, b: a + b 
#opens a code block, a+b

sum_of_nums = add_two_nums(3, 3) 
print(sum_of_nums)

# list comprehension

get_square = lambda num: num * num 
nums = list(range(1,11))

squares = [get_square(n) for n in nums]

#argumetns and params

def add(a,b):
    return a + b

print(add(4,2)) #python requiers that i fill up the parameters in this add method 
#for python functions we mus tpass in ethe eaxact number of positional arguments expected 


#how can we accept a varying number of arugments that allows multiple instances of adding

def add (*args):
    print(args)
print(add(1,2,3,4,5,6,7))


# this takes in a dev and thier skilsl and creates a dictionary with both 

def devs_skills(dev_name, *args):
    return {'dev_name': dev_name, 'skills': args}
print(devs_skills('lisa','html','css','react', 'graphql'))\


def dev_skills_2(**kwargs):
    print(kwargs)

# dev_skills_2(html=5, react=5, graph=3)

def create_dev_dictionary(dev_name, *args, **kwargs):
    return{
        'dev_name': dev_name,
        'projects': list(args),
        'skills': kwargs
    }

dev = create_dev_dictionary('ada', 'todo app', 'note taking app', HTML=5, CSS=5, REACT=5 )
print (dev)
