# 装饰器

# 装饰器是 Python 提供的一种语法糖，装饰器使用 @ 符号加上装饰器名称
# 用于修改其他函数的行为，并且在不修改原始函数定义和调用的情况下添加额外的功能。

# 装饰器提供了一种简洁而优雅的方式来扩展和修改函数或类的功能。它本质上就是一个闭包函数。

# 装饰器的功能特点:
# 不修改已有函数的源代码
# 不修改已有函数的调用方式
# 给已有函数增加额外的功能

# 装饰器的使用
# 由于装饰器本质上就是一个闭包函数，所以在使用自定义装饰器之前，需要先定义一个用来作为装饰器的闭包。
# 而闭包的外部函数名，就作为装饰器名使用。
import time

# 定义装饰器：接收一个函数作为参数
def count_time(func):
    def inner():
        start_time = time.time()
        # 闭包：内部函数使用外部函数的参数
        func()
        stop_time = time.time()
        print(f"函数执行时间为：{stop_time - start_time} 秒")
    return inner

# 使用装饰器
# 把show这个函数作为参数传递给count_time函数，然后执行count_time函数，并把返回的inner函数引用赋值给被装饰的函数，然后执行被装饰函数
@count_time
def show():
    for i in range(3):
        print(f"第 {i+1} 次输出")
        time.sleep(1)

# 上面代码中，使用闭包实现了一个统计函数执行时间的功能。
# 在 show 函数上，使用闭包函数作为装饰器，统计 show 的运行时间。
# 通过代码可以看出，在使用 count_time 函数做为装饰器时，即没有改变show函数的内部定义，也没有改变 show 函数的调用方式，
# 但却为 show 函数额外扩展了统计运行时间的功能，这就是装饰器的作用。

if __name__ == '__main__':
    show()
# 第 1 次输出
# 第 2 次输出
# 第 3 次输出
# 函数执行时间为：3.011897087097168 秒

# 装饰器的本质：函数的使用
# 上述装饰器的效果相当于把 show 函数作为参数传递给count_time函数，然后执行count_time函数，并把返回的inner函数引用赋值给被装饰的函数，然后执行被装饰函数
show = count_time(show)
show()
# 第 1 次输出
# 第 2 次输出
# 第 3 次输出
# 函数执行时间为：3.0087931156158447 秒

# 装饰器提供了一种简洁而优雅的方式 -- 语法糖 来扩展和修改函数或类的功能。其本质就是函数的使用。
# 语法糖：在计算机科学中，语法糖（Syntactic sugar）是指一种语法上的扩展，
# 它并不改变编程语言的功能，只是提供了更便捷、更易读的写法，使得代码更加简洁和可理解。
# 常见的语法糖: 推导式、装饰器、切片、上下文管理器

# Python 解释器在遇到装饰器时，会将被装饰函数的引用做为参数传递给闭包的外函数，
# 外函数执行后，返回内函数的引用，此时，再将内函数的引用赋值给被装饰的函数。

# 当 Python 解释器执行完装饰过程后，被装饰函数的函数名就不在保存原函数的引用，而是保存的闭包函数 inner 的引用。
# 而当执行被装饰函数时，实际执行的是闭包函数 inner ，由 inner 间接调用被装饰函数，完成整个调用过程。

print("==============================")

# 通用装饰器
# 理论上，一个装饰器可以装饰任何函数，但实际前面定义的 count_time 却只能装饰特定的无参无返回值的函数。
# 如果需要装饰器可以装饰任何函数，那么就需要解决被装饰函数的参数及返回值的问题。
# 可以通过可变参数和在内函数中返回被装饰函数执行结果的形式解决此问题。
# 做为装饰器名的外函数，使用参数接收被装饰函数的引用
def decorator(func):
    # 内函数的可变参数用来接收被装饰函数使用的参数
    def inner(*args, **kwargs):
        # 装饰器功能代码
        # 调用被装饰函数，并将接收的参数传递给被装饰函数，保存被装饰函数执行结果
        result = func(*args, **kwargs)
        # 返回被装饰函数执行结果
        return result
    # 返回内函数引用
    return inner

# 带参数的装饰器
# 除了普通装饰器使用方式外，在使用装饰器时，还需要向装饰器传递一些参数，
# 比如测试框架 pytest 实现数据驱动时，可以将测试数据以装饰器参数形式传入，
# 此时，前面定义的做为装饰器的闭包形式就不能满足需求了。

# 可以在通用装饰器外，再定义一层函数，用来接收装饰器的参数。
def decorator_args(vars, datas):
    def decorator(func):
        def inner(*args, **kwargs):
            # 这里给func传参是解包操作
            return func(*args, **kwargs)
        return inner
    return decorator

data = [(1,2,3),(4,5,6),(7,8,9)]
# 装饰器传参
@decorator_args("a, b, c", data)
def show2(a, b, c):
    print(a, b, c)

show2(1, 2, 3)
# 1 2 3

# 装饰器传参原理: 装饰器传参的本质就是链式语法的多次函数调用
# @decorator_args("a,b,c", data) 解析:
# 1、先执行 decorator_args("a,b,c", data) 部分
# 2、得到结果 decorator 与 @ 结合变成装饰器形式 @decorator
# 3、通过结果 @decorator 装饰器正常装饰被装饰函数

# 使用装饰器传参，实现数据驱动过程
# 此过程只用来讲解装饰器形式如何实现数据驱动过程，并没有完整实现。

# 接收装饰器参数的函数
# 参数一：以字符串形式接收被装饰函数的参数列表，需要与被装饰函数参数名保持一致，例："a,b,c"
# 参数二：以[(),(),()] 形式传入驱动数据。
def decorator_args(vars, datas):
    def decorator(func):
        # 将字符串参数分割备用
        v_keys = vars.split(",")
        # 定义保存 [{},{},{}] 形式的数据
        new_datas = []
        # 遍历数据，取出一组元素数据
        for item in datas:
            # 定义一个新字典，用来保存 变量名与传入数据组成的字典
            d_item = {}
            # 使用 zip 函数，同时遍历两个元组，变量名做为key, 元素数据做为value
            for k, v in zip(v_keys, item):
                # 将 变量名和值对应保存到字典中
                d_item[k] = v
            # 将组合好的字典追加到新数据中备用
            new_datas.append(d_item)
        def inner(*args, **kwargs):
            # 这里给func传参是解包操作
            return func(*args, **kwargs)
        # 遍历新数据，取出元素字典
        for item in new_datas:
            # 将字典中的数据解包传给内函数
            # 字典中的数据：{"a":1, "b":2, "c":3}
            # 解包 **item: a=1, b=2, c=3
            inner(**item)
        return inner
    return decorator

# 数据驱动的测试数据
data = [(1,2,3),(4,5,6),(7,8,9)]

# 装饰器传参
@decorator_args("a,b,c", data)
def show3(a,b,c):
    print(a,b,c)
# 无需手动调用show3()，因为在装饰器函数中，调用了inner()函数
# 1 2 3
# 4 5 6
# 7 8 9