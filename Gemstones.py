def gemStones(arr):
    gems = {}
    setArr = list(set(arr))
    smallest = setArr[0]
    for i in range(1,len(setArr)):
        if len(setArr[i]) < len(smallest):
            smallest = setArr[i]
    setArr.remove(smallest)
    print(smallest,setArr)
    cnt = 0
    flag = False
    for ele in smallest:
        for string in setArr:
            if ele in string:
                flag = True
            else:
                flag = False
                break
        # print(ele,flag)
        if (flag == True) and (ele not in gems):
            gems[ele] = True
            cnt+=1
    # print(gems)
    return cnt


print(gemStones(["vtrjvgbj",
"mkmjyaeav",
"sibzdmsk"]))
