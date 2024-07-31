# 闭包与装饰器

# 函数的引用
# 闭包
def show():
    m = 100
    print("Show Run", m)

show() # Show Run 100
# 函数的引用
# 将一个函数名，赋值给另一个变量，赋值后，此变量就可以做为该函数的一个别名使用，可以调用函数。
# 注意: 在将一个函数名（函数引用）赋值给一个变量时，函数名后不能添加括号。
display = show
display() # Show Run 100

# print(m)
# NameError: name 'm' is not defined
# m是局部变量，在函数被调用时创建，在函数执行完成后销毁
# 如果我们想在函数执行完成后，在函数外部也能访问变量m（不通过return m的形式），就可以使用【闭包】

# 闭包 Closure 是指在一个嵌套的函数内部访问其外部函数中定义的变量或函数的能力。
# 换句话说，闭包是一个函数对象，它可以记住并访问它创建时的上下文环境中的变量。
# 环境变量是在外部函数中定义的变量或其他函数对象，它被内部函数引用并记住，即使外部函数执行完成后仍然存在。

# 闭包的特点包括：
# 内部函数可以访问外部函数中定义的变量和参数，即使外部函数已经执行完毕。
# 闭包可以在外部函数的作用域之外被调用和执行。
# 闭包可以访问并修改外部函数中的局部变量，使其具有持久性。

# 闭包的定义
# 外部函数
def out_func():
    out_n = 100
    # 内部函数
    def inner_func():
        # 引用外部函数的变量(引用环境变量)
        print("这是内部函数的输出，引用了外部函数的变量out_n，值为：", out_n)
    # 外部函数一定要返回内部函数的引用
    return inner_func

# 使用闭包
# 不能直接调用内部函数，会报错
# inner_func()
# NameError: name 'inner_func' is not defined
# 调用函数，out_func()调用后返回的是inner_func, 是内部函数的引用
in_func = out_func()
# 此时外部函数out_func已经执行完成，但由于局部变量out_n被内部函数使用了，所以在外部函数执行完成后局部变量out_n并没有被销毁
# print(out_n)
# NameError: name 'out_n' is not defined
# 但仍然不能在外部直接访问局部变量
# 但是可以通过内部函数来间接访问 out_n
# 通过内部函数的引用来调用内部函数
in_func()
# 这是内部函数的输出，引用了外部函数的变量out_n，值为： 100
# 上述闭包做到了：保护私有变量、延迟执行

in_func2 = out_func()
in_func2()
# 这是内部函数的输出，引用了外部函数的变量out_n，值为： 100

print(id(in_func)) # 4366341984
print(id(in_func2)) # 4366339744
print(in_func) # <function out_func.<locals>.inner_func at 0x104411760>
print(in_func2) # <function out_func.<locals>.inner_func at 0x104410ea0>
# in_func 和 in_func2虽然都调用了out_func返回了inner_func的引用，但是这是2个不同的独立的对象

