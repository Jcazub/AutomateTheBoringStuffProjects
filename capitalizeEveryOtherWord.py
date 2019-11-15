def capitalizeEveryOtherWordStringFormat(word):
    if len(word) < 2:
        return word

    newWord = ""

    for characterIndex in range(len(word)):
        if characterIndex % 2 == 0:
            newWord += word[characterIndex].upper()
        else:
            newWord += word[characterIndex]
    return newWord


def capitalizeEveryOtherWordJoinFormat(word):
    if len(word) < 2:
        return word

    wordList = list(word)

    for characterIndex in range(len(wordList)):
        if characterIndex % 2 == 0:
            wordList[characterIndex] = wordList[characterIndex].upper()

    return ''.join(wordList)


word = "Supercalifragilisticespialidocious!"

print(capitalizeEveryOtherWordJoinFormat(word))