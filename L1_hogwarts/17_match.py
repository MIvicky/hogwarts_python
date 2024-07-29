http_code = int(input("请输入一个HTTP状态码："))

match http_code:
    case 100 | 101:
        print("临时响应")
    case 200 | 201 | 203 | 204 | 205:
        print("请求成功")
    case 301 | 304 | 307:
        print("重定向")
    case 404 | 401 | 403 | 405:
        print("页面找不到")
    case 500 | 502 | 503:
        print("服务器内部错误")
    # 匹配值为变量，用来匹配任意值，如 _，但是在一个匹配语句中，只能出现一个独立的匹配变量
    case _:
        print("无效的状态码")

# point is an (x, y) tuple
x = int(input("x: "))
y = int(input("y: "))
point = (x, y)
match point:
    case (0, 0):
        print("坐标在原点上")
    case (0, y):
        print(f"坐标在Y轴上")
    case (x, 0):
        print(f"坐标在X轴上")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("没有这个坐标点")