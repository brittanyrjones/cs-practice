def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)

# Recursion
def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:] + s[0])
