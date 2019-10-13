

def convertToSentence(passedList):

    sentence = ""

    for i in range(len(passedList)):

        if i == len(passedList) - 1:
            sentence += "and " + str(passedList[i])
        else:
            sentence += str(passedList[i]) + ", "

    return sentence


print(convertToSentence(['spam','eggs','bacon', 'orange juice']))