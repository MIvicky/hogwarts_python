length = len("Hello")
print(length)
length = len("Hello World")
print(length)

s = "Hello"
print(s.find("l"))
print(s.find("l",0,3))
print(s.find("k"))

s = "Hello Hello Hello"
print(s.replace("ll","LL"))
print(s.replace("l","L",4))

url = "https://www.ceshiren.com"
print(url.startswith("https://"))
print(url.startswith("https://", 0, 3))
print(url.startswith("https://", 5, 30))

url = "https://www.ceshiren.com"
print(url.endswith(".com"))
print(url.endswith(".com", 0, 20))
print(url.endswith(".com", 5, 30))

print("abc".isalpha())
print("ABC".isalpha())
print("ABCabc".isalpha())
print("123".isalpha())
print("a b".isalpha())
print("abc123".isalpha())
print("123abc".isalpha())
print("a@".isalpha())
print("".isalpha())

print("123".isdigit())
print("123abc".isdigit())
print("abc123".isdigit())
print("".isdigit())

print("ABC".isupper())
print("ABC123".isupper())
print("123ABC".isupper())
print("A!@#B".isupper())
print("abc".isupper())
print("abC".isupper())
print("abc123".isupper())
print("Abc!@#".isupper())
print("123".isupper())
print("".isupper())
print(" ".isupper())

print("abc".islower())
print("abc123".islower())
print("ABC".islower())
print("abC".islower())
print("Abc!@#".islower())
print("123".islower())
print("".islower())
print(" ".islower())

print("abc".upper())
print("ABC".upper())
print("abCd".upper())
print("abc123".upper())
print("abc123ABC".upper())

print("abc".lower())
print("ABC".lower())
print("abCd".lower())
print("abc123".lower())
print("abc123ABC".lower())

print("|" + "  hogworts  " + "|")
print("|" + "  hogworts  ".strip() + "|")
print("|" + "  hogworts".strip() + "|")
print("|" + "hogworts  ".strip() + "|")
print("|" + "  h o g w o r t s  ".strip() + "|")
print("|" + "bachogwortsabc".strip("cba") + "|")

print("a-b-c-d".split("-")) # ['a', 'b', 'c', 'd']
print("a-b-c-d".split("-", 2)) # ['a', 'b', 'c-d']
print("a--b-c-d".split("-")) # ['a', '', 'b', 'c', 'd']
print("a-+b-c-d".split("-+"))
print("a b\tc\nd\re".split()) # ['a', 'b', 'c', 'd', 'e']
print("a b c d e".split(" ", 3)) # ['a', 'b', 'c', 'd e']

print("Hello" + "World")
print("Hello" + "123")
# print("Hello" + 123)
# TypeError: can only concatenate str (not "int") to str

# join(iterable) 使用 string 连接可迭代对象中的所有元素，可迭代对象参数中的所有元素必须是字符串
print("".join(("a","b","c")))
print("-".join(("a","b","c")))
print("->".join(("a","b","c")))
print("->".join(["a","b","c"]))
print("->".join({"a","b","c"}))
print("->".join({"a":"A","b":"B","c":"C"})) # a->b->c

# 字符串对齐
print(f"The value is ljust: |{'abc':5}|")
print(f"The value is ljust: |{'abc':<5}|")
print(f"The value is rjust: |{'abc':>5}|")
# 数字对齐
print(f"The value is rjust: |{11:5}|")
print(f"The value is rjust: |{11:>5}|")
print(f"The value is ljust: |{11:<5}|")
# 小数保留
print(f"The value is rjust: |{3.1415926:5.2f}|")
