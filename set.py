#sets don't allow duplicates

colors = {'red', 'orange', 'yellow', 'green', 'blue', 'pink', 'purple', 'blue'}
print("The set removes the dups", colors)
print('red' in colors)
print('indigo' in colors)

vowelsAndY = set('AEIOUY')
print(vowelsAndY)
vowels = set('AEIOU')

print("And sometimes ", vowelsAndY - vowels)

consOnly = {x for x in 'patrick' if x not in 'aeiou'}
print(consOnly)