# ask the user to input the amount
sampleQty = int(input('How much sea water to be transported? '))

# calculating the number of necessary containers
# 20L containers
container20 = sampleQty // 20
leftover = sampleQty % 20
# 10L containers
container10 = leftover // 10
leftover = leftover % 10
# 5L containers
container5 = leftover // 5
leftover = leftover % 5
# 1L containers
container1 = leftover


# printing out the result
print('To trasport ' + str(sampleQty) + 'L of sea water, you need:')
print(str(container20) + ' x 20L containers')
print(str(container10) + ' x 10L containers')
print(str(container5) + ' x 5L containers')
print(str(container1) + ' x 1L containers')
