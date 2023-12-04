for i in range(1, 5):
    for j in range(1, 5):
        print(f"{i * j:4}", end="")
        if i * j == 9:
            break
    print()
