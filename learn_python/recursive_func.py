
def recursive_func(n):
    # 递归函数
    if n == 1:
        return 1
    return n * recursive_func(n-1)

if __name__ == '__main__':
    print(recursive_func(1))
    print(recursive_func(5))