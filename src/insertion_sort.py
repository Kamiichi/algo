in_list = list(map(int, input().split()))

tmp = 0
left, right = 1, len(in_list)

for i in range(left, right):
    if in_list[i-1] > in_list[i]:
        tmp = in_list[i]
        k = i
        while k > 0:
            if in_list[k-1] > tmp:
                in_list[k] = in_list[k-1]
                in_list[k-1] = tmp
            k -= 1
    # print(i, "回目のソート：", *in_list)

print(*in_list)