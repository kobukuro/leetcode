def solution(chars):
    start = 0
    end = len(chars) - 1
    while start < end:
        chars[start], chars[end] = chars[end], chars[start]  # change values
        start += 1
        end -= 1
    return chars


if __name__ == '__main__':
    input_list = ["h", "e", "l", "l", "o"]
    print(solution(input_list))
