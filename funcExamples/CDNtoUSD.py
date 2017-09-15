def CDNtoUSD(amountCDN, exchRate=0.78):
    amountUSD = amountCDN * exchRate
    return amountUSD

print(CDNtoUSD(125))
print(CDNtoUSD(125,0.80))
