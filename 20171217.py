i = 2
while(i < 100):
    j = 2
    while(j <= i):
        if(not(i%j)):
            if(i == j):
                print(i,"是素数")
            #else:
                #print(i, "不是素数")
            break
        else:
            j = j + 1
    i = i + 1
#if后面可以不用加括号
#break不管判断是否为真都结束循环，跳出整个循环
#continue是跳出本次循环

for letter in "python":
    if letter == 'h':
        break
    else:
        print(letter)

for letter in "python":
    if letter == 'h':
        continue
    else:
        print(letter)