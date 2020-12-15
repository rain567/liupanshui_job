"""
三个隶属度函数，用来计算污渍的隶属度
1.表示SD；2.表示MD；3.表示LD
以洗衣机洗涤时间为例，令污泥stain和油脂oil为输入变量，洗涤时间time为输出。
假设污泥、油脂、洗涤时间的论域分别为[0,100]、[0,100]、[0,60]。步骤如下：
"""
"""
步骤1.引用相关模块并设置各个变量范围：
"""
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt

x_stain_range=np.arange(0, 100, 2, np.float32)
y_oil_range=np.arange(0, 100, 1, np.float32)
z_time_range=np.arange(0, 60, 1, np.float32)

"""
步骤2.定义输入输出模糊集和其隶属度函数（使用三角函数），同时定义输出解模糊规则。模糊集如下：
污泥（少）=S，污泥（中）=M，污泥（多）=L
油脂（少）=S，油脂（中）=M，油脂（多）=L
洗涤时间（很短）=VS，洗涤时间（短）=S，洗涤时间（中）=M，洗涤时间（长）=L，洗涤时间（很短）=VL
"""
# 创建模糊控制变量

x_stain=ctrl.Antecedent(x_stain_range, 'stain')
y_oil=ctrl.Antecedent(y_oil_range, 'oil')
z_time=ctrl.Consequent(z_time_range, 'time')

# 定义模糊隶属度函数

x_stain['S']=fuzz.trimf(x_stain_range, [0, 0, 50])
x_stain['M']=fuzz.trimf(x_stain_range, [0, 50, 100])
x_stain['L']=fuzz.trimf(x_stain_range, [50, 100, 100])

y_oil['S']=fuzz.trimf(y_oil_range, [0, 0, 50])
y_oil['M']=fuzz.trimf(y_oil_range, [0, 50, 100])
y_oil['L']=fuzz.trimf(y_oil_range, [50, 100, 100])

z_time['VS']=fuzz.trimf(z_time_range, [0, 0, 10])
z_time['S']=fuzz.trimf(z_time_range, [0, 10, 25])
z_time['M']=fuzz.trimf(z_time_range, [10, 25, 40])
z_time['L']=fuzz.trimf(z_time_range, [25, 40, 60])
z_time['VL']=fuzz.trimf(z_time_range, [40, 60, 60])

# #可视化这些输入输出和隶属函数
# x_stain.automf()
# y_oil.automf()#三种程度
# x_stain.view()
# y_oil.view()
# plt.show()
# 设定输出powder的解模糊方法——质心解模糊方式
z_time.defuzzify_method='centroid'

"""
步骤3.建立模糊控制规则，并初始化控制系统和运行环境。规则如下表所示：
"""

# 输出为VS的规则
rule = ctrl.Rule(antecedent=(x_stain['S'] & y_oil['S']),
                 consequent=z_time['VS'], label='VS')

# 输出为S的规则
rule1 = ctrl.Rule(antecedent=(x_stain['M'] & y_oil['S']),
                  consequent=z_time['S'], label='S')

# 输出为M的规则
rule2 = ctrl.Rule(antecedent=((x_stain['S'] & y_oil['M']) |
                              (x_stain['M'] & y_oil['M']) |
                              (x_stain['L'] & y_oil['M'])),
                  consequent=z_time['M'], label='M')

# 输出为L的规则
rule3 = ctrl.Rule(antecedent=((x_stain['S'] & y_oil['L']) |
                              (x_stain['M'] & y_oil['L']) |
                              (x_stain['L'] & y_oil['M'])),
                  consequent=z_time['L'], label='L')

# 输出为VL的规则
rule4 = ctrl.Rule(antecedent=((x_stain['L'] & y_oil['L']) |
                              (x_stain['M'] & y_oil['L'])),
                  consequent=z_time['VL'], label='VL')

# 系统和运行环境初始化
system = ctrl.ControlSystem(rules=[rule, rule1, rule2, rule3, rule4])
sim_time = ctrl.ControlSystemSimulation(system)
"""
步骤4.系统建立完成后，通过输入变量值来查看系统的输出
令输入污泥，油脂的值。
"""
sim_time.input['stain'] = int(input("请输入污泥的值：0-100"))
sim_time.input['oil'] = int(input("请输入油脂的值：0-100"))
sim_time.compute()   # 运行系统
output_time = sim_time.output['time']
z_time.view(sim_time)
plt.show()
# 打印输出结果
print(output_time)