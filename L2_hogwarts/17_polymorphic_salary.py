# 【练习】员工薪资

# 知识点
# 实例方法、实例属性、类属性
# 构造方法、封装、继承、多态

# 作业要求
# 设计一个简单员工系统，包括不同类型的员工（如全职员工和兼职员工）。每个员工有不同的薪资计算方法

class Employee:
    def __init__(self, hours, hourly_rate):
        self.hours = hours
        self.hourly_rate = hourly_rate

    def salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, hours, hourly_rate):
        super().__init__(hours, hourly_rate)

    def salary(self):
        return f"全职员工的工资为: {self.hours * self.hourly_rate}"

class PartTimeEmployee(Employee):
    def __init__(self, hours, hourly_rate):
        super().__init__(hours, hourly_rate)

    def salary(self):
        return f"兼职员工的工资为: {self.hours * self.hourly_rate}"

def cal_salary(worker_type):
    if isinstance(worker_type, Employee):
        return worker_type.salary()

full_time_worker = FullTimeEmployee(240, 200)
print(cal_salary(full_time_worker))
# 全职员工的工资为: 48000

part_time_worker = PartTimeEmployee(70, 25)
print(cal_salary(part_time_worker))
# 兼职员工的工资为: 1750