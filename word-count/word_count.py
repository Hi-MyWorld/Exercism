def count_words(sentence: str) -> dict[str, int]:
    """
    A function to count the number of each word in a text.

    input: str
    output: dict[str, int]
    """

    # Define punctuation characters to replace with spaces.
    characters = '.!@#$%^&*(),";:_-/[]{}<>|?'

    # Replace punctuation characters with spaces.
    for element in sentence:
        if element in characters:
            sentence = sentence.replace(element, " ")

    sentence_length = len(sentence)

    # Handle apostrophes: preserve those within words and replace
    # leading, trailing, or standalone apostrophes with spaces.
    for element in range(sentence_length):
        if sentence[element] == "'":
            if (element == 0) or (element == sentence_length - 1):
                sentence = sentence[:element] + " " + sentence[element + 1 :]
                continue

            if (sentence[element - 1] in " '") or (sentence[element + 1] in " '"):
                sentence = sentence[:element] + " " + sentence[element + 1 :]

    words_list = sentence.lower().split()
    words_list.sort()  # Sort the words alphabetically.

    words_list = [
        word.strip() for word in words_list
    ]  # Remove leading and trailing whitespace from each word.

    # Count the occurrences of each word using a dictionary.
    # words_count_dict = {x: words_list.count(x) for x in words_list}

    # Alternatively, count word occurrences in a single pass through the list.
    dictionary_count = {}
    for word in words_list:
        if word in dictionary_count:
            dictionary_count[word] = dictionary_count[word] + 1
        else:
            dictionary_count.update({word: 1})

    return dictionary_count
