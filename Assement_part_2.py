'''str1 = input("Please Enter your Own String : ")
li=[]
li[:0]=str1
print(li)
result=[]
for i in range(len(li)):
    result.append(ord(li[i]))
    result = list(set(result))
print(result)
final=sum(result)
print("The sum of the your string '{}'is: {}".format(str1,final))'''

'''N = int(input())
for num in range(1,N+1):
    if(num>1 and num<100000):
        for i in range(2,num):
            if(num%i ==0):
                break
        else:
            print(num,end=' ')'''

'''#n=int(input())
#k =int(input())
a = list(map(str,input().split(' ')))
print(a)'''

item = list(map(str,input().split(' ')))
menu ={'oniondosa': 90,
       'plaindosa':40,
       'ravadosa':75,
       'idli':10,
       'vada':5,
       'poori':30,
       'chapathi':30,
       'pongal':35,
       'tea':25,
       'coffee':35,
       'meals':75}
for i in range(len(item)):
    if i%2==0:
        item[i].lower==menu
        break
    else:
        print("Sorry, Only recipes on the menu!")
'''for i in range(len(item)):
    if i%2!=0:
        total = int(item[i])*int(menu.values())
        print(total)'''






