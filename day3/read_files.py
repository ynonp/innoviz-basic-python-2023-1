with open('demo.txt', 'r', encoding='utf8') as f:
    with open('demo_without_indexes', 'w', encoding='utf8') as fout:
        for line in f:
            words = line.split()
            line_without_first_word = ' '.join(words[1:])
            fout.write(line_without_first_word)
            fout.write("\n")

