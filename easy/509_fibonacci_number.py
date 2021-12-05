# recursive solution
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    return memo[n]


# non-recursive solution
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         pre_one = -1
#         pre_two = 1
#         result = 0
#         for i in range(n + 1):
#             result = pre_one + pre_two
#             pre_one = pre_two
#             pre_two = result
#         return result


if __name__ == '__main__':
    n = 50
    print(fib(n))
