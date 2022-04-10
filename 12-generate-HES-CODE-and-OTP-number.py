# HES is an application that Turkey uses while fighting the COVID-19 pandemic. 
#The HES code is a personal code that indicates whether you are COVID positive or in contact with the patient.

import random
hesCodesSet = set()

def hes_code():
        
    while True:
        a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','R','S','O','V','T','Y','Z','Q','W']
        n = ['1','2','3','4','5','6','7','8','9']
        
        r1 = random.sample(a,3)
        r1.append(' ')
        r1.append('-')
        r1.append(' ')
     
        r2 = random.sample(n,3)
        r2.append(' ')
        r2.append('-')
        r2.append(' ')

        r3 = random.sample(a, 3)
        r3.append(' ')
        r3.append('-')
        r3.append(' ')
    
        r4 = random.sample(n, 3)
        
        sumList = r1 + r2 + r3 + r4
        hesCode = ''.join(sumList)
        
        if hesCode not in hesCodesSet:
            
            hesCodesSet.add(hesCode)
            print(hesCodesSet)
            return hesCode
        pass
    

#gives a random number and checks inputed number. If those are compatible process is successful. 
def checkNumber():
    import random 
    a = 0
    while a<3:
        try:
            check_number = random.randrange(1000, 1000000)
            print('Check Number: {}'.format(check_number))
            number_input = int(input("Please enter the given check number: "))
            if check_number == number_input:
                print("Successful.")
                break
            else:
                a += 1
                if a <= 2:
                    print("Please try again.")
                else:
                    print("It's blocked because you entered it wrong 3 times.")
        except ValueError:
            print('Enter just a number.')