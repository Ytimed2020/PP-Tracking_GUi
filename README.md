# PP-Tracking GUI界面测试版

本项目是基于飞桨开源的实时跟踪系统[PP-Tracking](https://github.com/PaddlePaddle/PaddleDetection/blob/develop/deploy/pptracking/README.md)开发的可视化界面

在PaddlePaddle中加入pyqt进行GUI页面研发，可使得整个训练过程可视化，并通过GUI界面进行调参，模型预测，视频输出等，通过多种类型的识别，简化整体预测流程。

![image-20211122180124835](https://z3.ax1x.com/2021/11/22/IzBXjg.png)

GUI界面基于PyQT和PP-Tracking python部署代码开发；当前覆盖单镜头的全部功能，如行人跟踪，车辆跟踪，流量统计等

推荐使用Windows环境

主要包含两个步骤：

- 导入训练模型，修改模型名称
- 安装必要的依赖库
- 启动前端界面

## 1. 下载预测模型

PP-Tracking 提供了覆盖多种场景的预测模型，用户可以根据自己的实际使用场景在[链接](https://github.com/PaddlePaddle/PaddleDetection/blob/develop/deploy/pptracking/README.md#%E4%BA%8C%E7%AE%97%E6%B3%95%E4%BB%8B%E7%BB%8D)中直接下载表格最后一列的预测部署模型

如果您想自己训练得到更符合您场景需求的模型，可以参考[快速开始文档](https://github.com/PaddlePaddle/PaddleDetection/blob/develop/configs/mot/fairmot/README_cn.md#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)训练并导出预测模型

模型导出放在`./output_inference`目录下


## 2. 必要的依赖库安装

```
pyqt5
moviepy
opencv-python
PySide2
matplotlib
scipy
cython_bbox
paddlepaddle
```

**注：**

1. Windows环境下，需要手动下载安装[cython_bbox](https://pypi.org/project/pip/)，然后将setup.py中的找到steup.py, 修改`extra_compile_args=[’-Wno-cpp’]`，替换为`extra_compile_args = {'gcc': ['/Qstd=c99']}`, 然后运行`python setup.py build_ext install`

## 3. 启动前端界面

执行`python main.py`启动前端界面


参数说明如下:

| 参数       | 是否必须 | 含义                                     |
| ---------- | -------- | ---------------------------------------- |
| 模型运行   | Option   | 点击后进行模型训练                       |
| 结果显示   | Option   | 在运行状态为检测完成的时候进行结果视频显示 |
| 停止运行   | Option   | 停止整个视频输出                         |
| 取消轨迹   | Option   | 在一开始时取消轨迹                       |
| 阈值调试   | Option   | 预测得分的阈值，默认为0.5                |
| 输入FPS    | Option   | 输入视频的FPS                                |
| 检测用时   | Option   | 视频的检测时间                           |
| 人流量检测 | Option   | 每隔一段帧数内的人流量统计图表           |
| 时间长度   | Option   | 人流量时间统计长度                       |
| 开启出入口 | Option   | 导入视频后可自行选择是否开启出入口训练   |
| 导出文件   | Option   | 可视化结果保存的根目录，默认为output/    |


说明：

- 如果安装的PaddlePaddle不支持基于TensorRT进行预测，需要自行编译，详细可参考[预测库编译教程](https://paddleinference.paddlepaddle.org.cn/user_guides/source_compile.html)。
- 建议使用windows环境进行运行
