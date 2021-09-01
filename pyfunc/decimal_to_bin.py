###################################
#Python Algorithm Made By Imalaia3#
###################################
#Please Give Credit If You Want (For Some Reason) To Use This
#github.com/imalaia3



def to_binary(decimal):
    binary_out = ''
    zeroed = False
    left = decimal
    #--Start Of Calculation Block--
    
    while zeroed == False:
        if left % 2 == 1:
            left = left // 2
            binary_out = binary_out + "1"
            if left == 0:
                zeroed = True
        else:
            left = left // 2
            binary_out = binary_out + "0"
            if left == 0:
                zeroed = True


    #--Start Of Calculation Block--
    return int(binary_out[::-1])







print(to_binary(int(10)))
