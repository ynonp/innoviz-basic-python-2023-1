# Pattern 1 - Write text to file

f = open('demo.txt', 'w', encoding='utf8')
for i in range(10):
    f.write(f"{i} Hello World 🎈️🎈️🎈\n️")
f.close()

with open('demo.txt', 'w', encoding='utf8') as f:
    for i in range(10):
        f.write(f"{i} Hello World 🎈️🎈️🎈\n️")
