"""
Input file input.txt
Questions-
1. How many of the lines are files?
2. How many of the lines are directories?
3. Given a user, how many files they have?
4. Given a user, how many directories they have?
5. How many different users are in the file?
"""
from collections import Counter
num_files = 0
num_directories = 0
files_by_user = Counter()

with open('input.txt', 'r', encoding='utf8') as f:
    for line in f:
        # Q1 - startswith
        if line.startswith('-'):
            num_files += 1

        if line.startswith('d'):
            num_directories += 1

        if line.endswith('a\n'):
            print("line ends with a")

        if 'total' in line:
            print('line has the word "total"')


        words = line.split()
        if line.startswith('-'):
            username = words[2]
            files_by_user[username] += 1

        print(line, end='')

print(f"input.txt had {num_files} files")
print(files_by_user)