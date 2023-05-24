# ### Exercise 1

# - Create a list named `students` containing some student names (strings).
# - Print out the second student's name.
# - Print out the last student's name.

students = ['Carlos', 'Steven', 'Martinez', 'John']

print(students[1])
print(students[-1])

# ### Exercise 2

# - Create a tuple named `foods` containing the same number of foods (strings) as there are names in the `students` list.
# - Use a `for` loop to print out the string "[*food goes here*] is a good food".

foods = ('Hamburger', 'Wings', 'Gallopinto', 'Seafood')

for food in foods:
    print(f'{food} is a good food')

# ### Exercise 3

# - Using a `for` loop, print just the last two food strings from `foods`.

#     > Hint:  Use the slice operator to select the last two foods
#     >

for food in foods[-2:]:
    print(food)

# ### Exercise 4

# - Create a dictionary named `home_town` containing the keys of `city`, `state` and `population`.
# - Print a string with this format: `"I was born in *city*, *state* - population of *population*"`

home_town = {
    'city': 'Masaya',
    'state': 'Masaya',
    'population': '183,874'
}

print(
    f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')

# ### Exercise 5

# - Iterate over the *key: value* pairs in `home_town` and print a string for each item, for example:

# ```python
# "city = Arcadia"
# "state = California"
# "population = 58000"
# ```

for key, value in home_town.items():
    print(f'{key} = {value}')


# ### Exercise 6

# - Create an empty list named `cohort`.
# - Using a `for` loop to iterate over the `students` list.

#     > Hint: Use the enumerate function to provide both the index & student
#     >
# - Within the `for` loop, add a dictionary to the `cohort` list that combines the student's name and the food in the `foods` list at the same index. Each dictionary will have this shape:

#     ```
#     {
#       'student': 'Tina',
#       'fav_food': 'Cheeseburger'
#     }

#     ```

# - Iterate over the `cohort` list, printing out each item (it's not necessary to format the dictionaries).

cohort = []
for food, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[food]
    })
for item in cohort:
    print(item)

# ### Exercise 7

# - Using the list of `students` and a list comprehension, assign to a variable named `awesome_students` a new list containing strings similar to this:<br>`["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]`
# - Iterate over the `awesome_students` list, printing out each string.

awesome_students = [f"{student} is awesome!" for student in students]

for student in awesome_students:
    print(student)


# ### Exercise 8

# - Use a `for` loop to iterate over a list comprehension that filters the `foods` tuple to only include food strings that contains the letter `a`.
# - Within the `for` loop, print each food string.

foods_with_a = [food for food in foods if 'a' in food]

for food in foods_with_a:
    print(food)