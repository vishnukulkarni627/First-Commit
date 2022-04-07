word = "Python"
print(word[0:6:1])
print(word[::1])
print(word[::-1])
print(word[-1:-7:-1])
# print(word[42])
# word[0] = 'p'

square = [1, 4, 9, 16, 25]
print(square[0])
print(square[-1])
print(square[-3:])
square=(square + [36, 49, 64, 81, 100])
print(square)
cube = [1, 8, 27, 65]
cube[3]= 64
print(cube)
cube.append(125)
print(cube)
cube.append({7: 7 ** 3})
print(cube)
cube.append('cube')
print(cube)
cube.extend([1, 2])
print(cube)
cube.extend('hello')
print(cube)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

print(pairs)
