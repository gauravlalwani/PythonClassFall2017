subjectID = ['001', '003', '004', '006', '009', '012']
expCode = [0, 1, 0, 2, 3, 2]
expParadigm = ['congruent', 'incongruent', 'mixed', 'null']

print('ID    Paradigm')
for i,iSubj in enumerate(subjectID):
    print(iSubj + '   ', end='')
    print(expParadigm[expCode[i]])
