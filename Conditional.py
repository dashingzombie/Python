score = input("Enter Score: ")
try :
    score=float(score)
except :
    print('Wrong type of input')
if score>1 :
    print('Enter score between 0.0 and 1.0')
elif score>=0.9 :
    print('A')
elif score>=0.8 :
    print('B')
elif score>=0.7 :
    print('C')
elif score>=0.6 :
    print('D')
elif score<0.6 :
    print('F')
