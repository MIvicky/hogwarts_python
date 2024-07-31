# 【练习】计数器函数

# 知识点
# 闭包与装饰器

# 作业要求
# 编写一个Python程序，实现一个计数器函数，该函数能够记录特定函数的调用次数。
# 你需要使用闭包和装饰器来实现这个功能。

def counter_func_call(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"函数 '{func.__name__}' 已被调用 {count} 次")

        return func(*args, **kwargs)
    return inner

@counter_func_call
def test_func_add(a, b):
    return a + b

print(test_func_add(1, 2))
# 在第一次被调用时，add函数的引用作为参数传递给counter函数，执行counter函数，初始化count的值为0，返回inner函数的引用
# Python解释器会将inner函数的引用赋值给被装饰的add函数，执行add函数，实际执行的是inner函数
# 所以在同一次代码执行中，第一次调用add函数后，add函数已经被装饰成了inner函数
# 后续再调用add函数，其实就是直接调用inner函数。所以，不会再初始化count的值为0了。
print(test_func_add(3, 4))
print(test_func_add(5, 6))
# 函数 'test_func_add' 已被调用 1 次
# 3
# 函数 'test_func_add' 已被调用 2 次
# 7
# 函数 'test_func_add' 已被调用 3 次
# 11