title = input()
n = int(input())
words = [input() for _ in range(n)]

for w in words:
    temp_title = list(title) # cast string to list
    indices = [0]

    for char in w:
        if char in temp_title[indices[-1]: ]: # moving only forward
            current_index = temp_title[indices[-1]:].index(char)
            temp_title[current_index + indices[-1]] = "_" # count from last "-" forward
            indices.append(current_index + indices[-1])

    if len(indices[1:]) == len(w):
        title = []
        for char in temp_title:
            if char != "_":
                title.append(char)
        print("".join(title))
    else:
        print("No such title found!")
