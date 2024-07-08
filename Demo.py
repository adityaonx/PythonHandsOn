s = "hello"
sum = 0
for i in range(len(s)-1):
        a= ord(s[i])
        b= ord(s[i+1])
        print("i:", i ,"ascii:" ,b)
        sub = abs(a-b)
        sum = sum + sub
# print(sum)