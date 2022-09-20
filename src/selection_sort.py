in_list = list(map(int, input().split()))

left = 0
right = len(in_list)

while True:
    if left == right:
        break

    # 入力の最大サイズを100万と仮定する。(実際にはgenrand.pyは100が最大だけど)
    min = 1000000
    tmp = 0

    for i in range(left, right):
        if in_list[i] < min:
            tmp = i
            min = in_list[i]

    in_list.insert(left, in_list.pop(tmp))
    left += 1

print(*in_list)