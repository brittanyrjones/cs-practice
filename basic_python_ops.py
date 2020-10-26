

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#USE HELPER FUNCS
# CLARIFY Q

#SORT DICT BY VALUE
print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])})
#OUTPUT {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}


# SORT DICT BY KEY
print({key:x[key] for key in sorted(x.keys())})
#OUTPUT {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}

# Python code to convert string to list character-wise
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
# Driver code
str1="ABCD"
print(Convert(str1))
#Output: ['A','B','C','D']


bb = 100002
res = [int(b) for b in str(bb)]
print(res)
#OUTPUT [1, 0, 0, 0, 0, 2]


ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}
ex_dict.keys()
# ["a","b","c"]
ex_dict.values()
# ["anteater", "bumblebee", "cheetah"]
ex_dict.items()
# [("a","anteater"),("b","bumblebee"),("c","cheetah")]
# with default
{"name": "Victor"}.get("nickname", "nickname is not a key")
# returns "nickname is not a key"

# DO SOMETHING A CERTAIN AMOUNT OF TIMES
for i in range(3):
  print(i)
# Print "WARNING" 3 times:
for i in range(3):
  print("WARNING")


str = 'yellow'
str[1]     # => 'e'
str[-1]    # => 'w'
str[4:6]   # => 'ow'
str[:4]    # => 'yell'
str[-3:]   # => 'low'

owners_names = ['Jenny', 'Sam', 'Alexis']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter']
owners_dogs = zip(owners_names, dogs_names)
print(list(owners_dogs))
# Result: [('Jenny', 'Elphonse'), ('Sam', 'Dr.Doggy DDS'), ('Alexis', 'Carter')]



items = [1, 2, 3, 4, 5, 6]
# All items from index `0` to `3`
print(items[:4])
# All items from index `2` to the last item, inclusive
print(items[2:])

#NESTED
groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]
# This outer loop will iterate over each list in the groups list
for group in groups:
  # This inner loop will go through each name in each list
  for name in group:
    print(name)


"""
Is the input already sorted?
Is the input reverse sorted?
Is the input only one element? If so, is that considered “sorted” (if returning a bool)?
Is the input such that all the of elements are of equal value?
Is an “empty” version of the input (NULL, nil, or whitespace) considered sorted or not (especially important if you’re returning a bool)?
Is the input of different types (e.g., numbers and strings) that would be difficult to sort against each other? If so and you’re only sorting one of the types, should the other types be eliminated or saved? If saved, how should they be placed (before or after the sorted type) and should the other types be sorted against themselves?
If you plan on doing a split when doing the sorting algorithm (a common technique) is the input even or odd?

Input & Output
WHat is coming in, what do we want to return?

Numbers
Zero (0)
NULL or nil
Negative Numbers
Floats or Doubles (clarifies if Ints only?)
Min/Max Int

Strings
Empty string
NULL or nil (and Optionals, depending on language)
Spaces (multiple words or sentences, or single/multiple whitespaces alone)
Punctuation
Upper, lowercase, or mixed (e.g., “stRiNg”)
Strings of numbers (e.g., “12”) Should these be changed to Int, Float, or Double?
Different Languages (Diacritics? Unicode compliant? ASCII?)
Emoji 👍 (especially if question is presented as a text field input by a user)
Long String
