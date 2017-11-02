def CaesarCipher(inText, shift=5):
    # alphabets as a string
    alphaOrig = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # converting the input text to upper case
    inTextU = inText.upper()
    # initializing the output text
    outText = ''
    # loop over each character in the input text
    for iChar in inTextU:
        if iChar.isalpha():
            newIndex = (alphaOrig.index(iChar) + shift) % 26
            outText += alphaOrig[newIndex]
        else:
            outText += iChar
    # returning the encrypted text
    return outText

text1 = 'And you Brutus'
print(CaesarCipher(text1))

