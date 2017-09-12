amountSpent = float(input('Enter the amount spent '))
if amountSpent<50:
    shippingFee = 12.00
elif amountSpent<100:
    shippingFee = 8.00
elif amountSpent<150:
    shippingFee = 5.00
else:
    shippingFee = 0

print('The shipping fee for this purchase is $' + str(shippingFee))
