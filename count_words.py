def split(text, delimiter=" "):
    """
    Splits a text string into substrings at each occurrence of the specified delimiter.

    Parameters:
    - text (str): The string to be split.
    - delimiter (str): The character or string to use as the delimiter. Defaults to a single space (" ").

    Returns:
    - result (list): A list containing the substrings resulting from the split operation.
    """
    result = []
    start = 0
    end = len(text) - 1
    for i, char in enumerate(text):
        if char==delimiter:
            result.append(text[start:i])
            start = i + 1
        if i == end:
            result.append(text[start:i+1])
    return result

def count(text, word):
    """
    Counts the frequency of occurence of the specified word in the text string.

    Parameters:
    - text (str): The string where the occurence is to be counted.
    - word (str): The string whose occurence is to be counted.

    Returns:
    - count (int): The integer representing the number of occurence  of the word in the text string.
    """
    words = split(text)
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count

def freq(text):
    """
    Counts the frequency of occurence of each word in the text string.

    Parameters:
    - text (str): The text string where the occurence is to be counted.

    Returns:
    - counts (dict): The dictonary with key as the word and value as the frequency of occurence of that word.
    """
    counts = {}
    words = split(text)
    for word in words:
        counts[word] = count(text, word)
    return counts

print(freq("this is is is a a a text this"))