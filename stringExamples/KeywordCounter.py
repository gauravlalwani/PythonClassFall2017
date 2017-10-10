abstract = '''In this paper, we propose several measures of nodal
qualities which capture different aspects of their activities and
influence in online social networks. Using these measures we analyze
the prevalence of the generalized friendship paradox over Twitter
and we report high levels of prevalence (up to over 90% of nodes).
We contend that this prevalence of the friendship paradox and its
generalized version arise because of the hierarchical nature of the
connections in the network.
'''

def RemovePunct(text):
    newText = text.replace(',','').replace('.','').replace('(','').replace(')','')
    return newText

def KeywordCounter(text,keyword):
    listWords = RemovePunct(text).lower().split()
    countKeyword = 0
    for iWord in listWords:
        if iWord == keyword.lower():
            countKeyword += 1
    return countKeyword


print(KeywordCounter(abstract, 'prevalence'))
