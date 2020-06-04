words = ["one", "two", "three", "four"]

for w in words:
    print(w, len(w), "static")


for w in words.copy():
    print(w, len(w), "static")


for i in range(21):
    print(i)

for i in range(300,310):
    print(i)

sentence = ["Go", "fuck", "yourself", "you", "fucking", "child"]

for i in range(len(sentence)):
    print(i, sentence[i])

print(sum(range(5)))

a = list(range(101,105))

print(a)

