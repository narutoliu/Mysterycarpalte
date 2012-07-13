#mysterycarplate.py

car_dic={}
car_dic['A']=1
car_dic['B']=2
car_dic['C']=3
car_dic['D']=4
car_dic['E']=5
car_dic['F']=6
car_dic['G']=7
car_dic['H']=8
car_dic['I']=9
car_dic['J']=10
car_dic['K']=11
car_dic['L']=12
car_dic['M']=13
car_dic['N']=14
car_dic['O']=15
car_dic['P']=16
car_dic['Q']=17
car_dic['R']=18
car_dic['S']=19
car_dic['T']=20
car_dic['U']=21
car_dic['V']=22
car_dic['W']=23
car_dic['X']=24
car_dic['Y']=25
car_dic['Z']=26

multiply=[14,2,12,2,11,1]
checksum=[]

def num_checker(a):
    list(a)
    
    if a[2].isdigit():
        num=2
        checksum.append(multiply[0]*car_dic[a[0]])
        checksum.append(multiply[1]*car_dic[a[1]])
        for i in a:
            
            if i.isdigit():
                i=int(i)
                checksum.append(multiply[num]*i)
                num=num+1
                
            
            
    else:
        num=2
        checksum.append(multiply[0]*car_dic[a[1]])
        checksum.append(multiply[1]*car_dic[a[2]])
    
        for i in a:
            if i.isdigit():
                i=int(i)
                checksum.append(multiply[num]*i)
                num=num+1
    checksum_checker=0
    for i in checksum:
        checksum_checker=checksum_checker+i
    checksum_checker=checksum_checker%19
    
    for k,v in car_dic.items():
        if k==a[-1]:
            if v==checksum_checker:
                return True
    return False

        
        
                
    
        
        
print (num_checker('SBA1234G'))







