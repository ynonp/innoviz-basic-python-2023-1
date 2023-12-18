import collections

text = """
In Africa, pythons are native to the tropics south of the Sahara, but not in the extreme south-western tip of southern Africa (Western Cape) or in Madagascar. In Asia, they occur from Bangladesh, Nepal, India, Pakistan, and Sri Lanka, including the Nicobar Islands, through Myanmar, east to Indochina, southern China, Hong Kong and Hainan, as well as in the Malayan region of Indonesia and the Philippines.[1]
Invasive
Some suggest that P. bivittatus and P. sebae have the potential to be problematic invasive species in South Florida.[26] In early 2016, after a culling operation yielded 106 pythons, Everglades National Park officials suggested that "thousands" may live within the park, and that the species has been breeding there for some years. More recent data suggest that these pythons would not withstand winter climates north of Florida, contradicting previous research suggesting a more significant geographic potential range.[27]
Python skin is used to make clothing, such as vests, belts, boots and shoes, or fashion accessories such as handbags. It may also be stretched and formed as the sound board of some string musical instruments, such as the erhu spike-fiddle, sanxian and the sanshin lutes.[28][29] With a high demand of snake skin in the current fashion industry, countries in Africa and Southern Asia partake in the legal and illegal selling of python skin. Providing an extremely low pay for the hunters with an extremely high selling product for the consumers, there is an enormous gap between the beginning and end of the snake skin trade.[30]
"""

words = text.split()
print(words)
counter = {}

for word in words:
    counter[word] = counter.get(word, 0) + 1

counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

default_counter = collections.defaultdict(int)
for word in words:
    default_counter[word] += 1

counter_counter = collections.Counter(words)
print(counter_counter)


print(counter)
print(default_counter)

d = {
    "some": 12,
    "that": 8
}

d["that"] += 1

# Hint: with a dictionary
d["that"] = d.get("that", 0) + 1

# or with default dict
d = collections.defaultdict(int)
d["that"] += 1


print(counter_counter.most_common(3))





