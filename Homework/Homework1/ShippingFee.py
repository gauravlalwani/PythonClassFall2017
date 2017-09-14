# some pre-defined parameters
qtyJar = 6  # the quantity in each jar

# ask the user to input necessary information
qtyOrder = int(input('How many jars? '))
deliverZIP = int(input('Destination ZIP code? '))

# Calculating the base shipping fee first
wgtOrder = qtyOrder * qtyJar  # order in terms of oz
if wgtOrder<=24:
    baseFee = 5.00
elif wgtOrder<=48:
    baseFee = 7.50
elif wgtOrder<=72:
    baseFee = 9.00
else:
    baseFee = 10.00

# next, calculating surcharge
if deliverZIP>=99501 and deliverZIP<=99950:  # Alaska
    surcharge = 6.00
elif deliverZIP>=96701 and deliverZIP<=96898:  # Hawaii
    surcharge = 0.20 * wgtOrder
else:
    surcharge = 0.00

# Finally, priting out the total
totalFee = baseFee + surcharge
print('The total shipping fee is ' + str(totalFee))


