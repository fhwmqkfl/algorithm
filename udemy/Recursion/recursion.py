# the process of opening each new box is the same

#each time we open the box, we make the problem smaller

 
# def open_gift_box():
#     if ball:
#         return ball
#     open_gift_box() 

def funcThree():
    print('Three')

def funcTwo():
    funcThree()
    print('Two')

def funcOne():
    funcTwo()
    print('One')

funcOne()