# Set are unordered, unique, mutable(elements should be hasable)
# Set cannot be indexed or sliced
# Includes hasable objects
# Boundary --- {.......}
# Creation of empty set --- 1st Method
s ={1, 1.3, (1, 2, 3), "hi"}
print(s)        # {'hi', 1, (1, 2, 3), 1.3}
#  Creating of empty set ---2nd Method
s1 = set('hi')
print(s1)       # {'i', 'h'}
#  Length of set
print(len(s))

# Hasable objects are objects implements magic method and hash method can be called
# only immutable objects have hash values, hash can be used to check mutable and immutable
# All immutable objects are hasable, but all hasable objects are not immutable
