in_list = list(map(int, input().split()))

left = 1
right = len(in_list)

def swap(left, right):
    for i in range(left, right):
        if in_list[i-1] > in_list[i]:
            in_list[i-1], in_list[i] = in_list[i], in_list[i-1]

while True:
    if left == right:
        break
    swap(left, right)
    right -= 1

print(*in_list)