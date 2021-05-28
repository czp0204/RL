import math
import matplotlib.pyplot as plt
# created by CZP 2021.5.27
# 最大数据误差在10%以内 都怪round函数是nc  根据需要手动调试
# class SiAndGeTube:
''' 两种管的类  '''
# 通过ClassName.__doc__查看
ElectricityAndVoltage = [7.81, 0.02,
                         24.1, 0.04,
                         59.0, 0.06,
                         132., 0.08,
                         289., 0.100,
                         603., 0.120]
# 如果初始化的是一个0数组 那怎么输入一组数字并置换呢
Temp = 24.6  # 实验室的气温 p2
m = 6.  # 数据行数
count_x = 0.
count_x2 = 0.
count_y = 0.
count_xy = 0.
BoltzmannK = 0.
for i in range(0, 6):
    count_x += ElectricityAndVoltage[2*i+1]
    count_y += math.log(ElectricityAndVoltage[2*i])
    count_x2 += pow(ElectricityAndVoltage[2*i+1], 2)
    count_xy += ElectricityAndVoltage[2*i+1]*math.log(ElectricityAndVoltage[2*i])
    count_b = (m*count_xy-count_x*count_y)/(m*count_x2-count_x*count_x)
    BoltzmannK = 1.602 * math.pow(10, 4) / (count_b * (Temp + 273.15))

'''
Standard 关于玻尔兹曼E：

var p1 = _q[_testpaper.qmap.datafill2].answers;
var count_standard=Math.abs((p1-1.38)/1.38)*100;
_standard=Float.decimal(1,count_standard);
'''
p1 = round(BoltzmannK, 10)
print('BoltzmannK = ', p1)
BoltzmannE = abs((1.26-1.38)/1.38)*100
print('Boltzmann相对误差为 = ', BoltzmannE)
'''
Standard: 关于玻尔兹曼K 

var p1=_q[_map.table1].answers;
var p2=parseFloat(_q[_testpaper.qmap.datafill1].answers);
var m=p1.length/2;
var count_x=0;
var count_x2=0;
var count_y=0;
var count_xy=0;
for(var i=0;i<m;i++){
  count_x+=parseFloat(p1[2*i+1]);
  count_y+=Math.log(parseFloat(p1[2*i]));
  count_x2+=p1[2*i+1]*p1[2*i+1];
  count_xy+=p1[2*i+1]*Math.log(parseFloat(p1[2*i]));
}
var count_b=(m*count_xy-count_x*count_y)/(m*count_x2-count_x*count_x);
var count_standard=1.602*Math.pow(10,4)/(count_b*(p2+273.15));
_standard=Float.decimal(2,count_standard);

Rule：
<span style="display:block;float:left;"><b>评分规则：</b></span>
<span style="display:block;float:left;margin-bottom:8px;">                   
数据计算偏差在-0.1~0.1之间，有效数字全部保留正确（保留1位或者2位小数），得0.2分<br/>
数据偏差在-0.1~0.1之外，则得0分且显示“计算结果不正确”<br/>
数据有效数字不正确，则得0分显示“有效位数不正确”
</span>
'''

# I-U 特性图 ：算了还是用Excel吧 懒得学了
# x = [1, 2, 3, 4, 5, 6]
# y = [1, 2, 3, 4, 5, 6]
# plt.figure()
# plt.plot(x, y, color='red')

# 3.PN结正向电压与温度之间的关系（Si管）
'''
S 的禁带宽度 Standard
var p1=_q[_map.table3].answers;
var m=p1.length/3;
var count_x=0;
var count_x2=0;
var count_y=0;
var count_xy=0;
for(var i=0;i<m;i++){
  count_x+=parseFloat(p1[3*i+2]);
  count_y+=parseFloat(p1[3*i]);
  count_x2+=p1[3*i+2]*p1[3*i+2];
  count_xy+=p1[3*i+2]*p1[3*i];
}
var count_a=(count_y*count_x2-count_x*count_xy)/(m*count_x2-count_x*count_x);
_standard=Float.decimal(3,count_a);

禁带宽度 Rule:
<span style="display:block;float:left;"><b>评分规则：</b></span>
<span style="display:block;float:left;margin-bottom:8px;">                   
数据计算偏差在-0.01~0.01之间，有效数字全部保留正确，保留2位或者3位小数，得0.15分<br/>
数据偏差在-0.01~0.01之外，则得0分且显示“计算结果不正确”<br/>
数据有效数字不正确，则得0分显示“有效位数不正确”
</span>

相对误差：Standard：
var p1 = _q[_testpaper.qmap.datafill8].answers;
var count_standard=Math.abs((p1-1.21)/1.21)*100;
_standard=Float.effective(2,count_standard);
Rule：
<span style="display:block;float:left;"><b>评分规则：</b></span>
<span style="display:block;float:left;margin-bottom:8px;">                   
偏差在－10%～10%之内，且有效数字正确（保留1位或者2位有效数字）得0.1分<br/>
数据偏差在－10%～10%之外，则显示“计算结果不正确”，有效数字不正确则显示“有效位数不正确”
</span>
'''
Ts = 45.5  # 实验室当时温度
IF = 50  # 工作电流 单位是微A
UT = [0.515, 45.5, 318.7,
      0.502, 50.3, 323.5,
      0.494, 54.0, 327.2,
      0.483, 58.2, 331.4,
      0.476, 61.4, 334.6,
      0.469, 64.2, 337.4,
      0.459, 68.2, 341.4,
      0.450, 72.0, 345.2,
      0.441, 76.0, 349.2,
      0.431, 80.0, 353.2]  # 曲线测量数据记录表
length = 10
count_xx = 0
count_xx2 = 0
count_yy = 0
count_xyy = 0
Eg = 0  # 禁带宽度
# print(UT[2])
for i in range(0, 10):  # 根据列表的大小作调整
    count_xx += UT[3*i+2]
    count_yy += UT[3*i]
    count_xx2 += math.pow(UT[3*i+2], 2)
    count_xyy += UT[3*i+2]*UT[3*i]
    count_a = (count_yy*count_xx2-count_xx*count_xyy)/(length*count_xx2-count_xx*count_xx)
    Eg = count_a
print("禁带宽度是", round(Eg, 3))
E = round(abs((Eg-1.21)/1.21)*100, 3)
print("禁带宽度相对误差是", E, '%')








