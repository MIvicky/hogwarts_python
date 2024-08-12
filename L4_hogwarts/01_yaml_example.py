import yaml

# YAML 模块使用 safe_load() 方法读取 yaml 文件，在读取文件之前，和普通文件一样，需要先将文件打开
# 读取 YAML 文件, 以前面复杂结果数据为例
with open("data.yaml", "r") as file:
    data = yaml.safe_load(file)

# 处理读取到的数据
print(data)
print(data['cool_list'])
print(data['hard_list'][2]['test'])

# YAML 模块使用 safe_dump() 方法向 yaml 文件中写入数据，在写入文件之前，也需要先将文件打开
# 要写入的数据
data2 = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': {
        'key4': 'value4'
    }
}

# 写入 YAML 文件
with open("data.yaml", "a") as file:
    yaml.safe_dump(data2, file)
    # key1: value1
    # key2: value2
    # key3:
    #   key4: value4