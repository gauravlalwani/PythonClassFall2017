def Handedness(hand):
    if hand=='left' or hand=='right':
        print('You are ' + hand + '-handed.')
    else:
        print('The input has to be left or right')

Handedness('right')
Handedness('left')
Handedness('neither')
