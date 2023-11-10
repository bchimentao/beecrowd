# 2594 - Eachianos II

for n in range(int(input())):

    # Input string
    input_string = input()

    #input word
    input_word = input()

    # Step 1: Split the string into words and also keep track of their starting indices
    words = input_string.split()
    word_indices = {}

    current_index = 0

    for word in words:
        if word in word_indices:
            word_indices[word].append(current_index)
        else:
            word_indices[word] = [current_index]
        current_index += len(word) + 1  # Add 1 for the space

    if input_word in word_indices.keys():
        if len(word_indices[input_word]) > 1:
            for i in range(len(word_indices[input_word]) - 1):
                print(word_indices[input_word][i], end=' ')
            print(word_indices[input_word][len(word_indices[input_word]) - 1])
        else:
            print(word_indices[input_word][0])            
    else:
        print(-1)