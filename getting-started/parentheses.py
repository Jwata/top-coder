def count_ways(string):
    ans = 1
    cnt = 0

    for i in range(len(string)):
        char = string[i]

        if char == '(':
            cnt += 1

        if char == ')':
            ans *= cnt
            cnt -= 1

    print('input {}, ans {}'.format(string, ans))

count_ways('()()()')
count_ways('()(()())')
count_ways('((()))')
