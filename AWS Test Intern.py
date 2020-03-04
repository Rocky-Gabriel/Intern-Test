T = int(input())

for i in range(T):
    count = 0
    Pattern = input()
    TextString = input()

    for j in range(len(Pattern)):
        for k in range(len(TextString)):
            if Pattern[j] == TextString[k]:
                count = count+1
                break
    if count == len(Pattern):
        print("YES")
    else:
        print("NO")
    
