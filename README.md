# Tracking-GUI界面

在PaddlePaddle中加入pyqt进行GUI页面研发，可使得整个训练过程可视化，并通过GUI界面进行调参，模型训练，视频输出等，通过多种类型的识别，简化整体训练难度。


主要包含两个步骤：

- 导入训练模型，修改模型名称
- 安装必要的依赖库

## 1. 导入预测模型

PaddleDetection在训练过程包括网络的前向和优化器相关参数，而在部署过程中，我们只需要前向参数，具体参考:[导出模型](https://github.com/PaddlePaddle/PaddleDetection/blob/develop/deploy/EXPORT_MODEL.md)

导入后目录下，包括`infer_cfg.yml`, `model.pdiparams`,  `model.pdiparams.info`, `model.pdmodel`四个文件。

## 2. 必要的依赖库安装

```
pyqt5
VideoFileClip
opencv-python
PySide2
matplotlib
```

在GUI界面选择后：


参数说明如下:

| 参数       | 是否必须 | 含义                                     |
| ---------- | -------- | ---------------------------------------- |
| 模型运行   | Option   | 点击后进行模型训练                       |
| 结果显示   | Option   | 在运行进度达到100%的时候进行结果视频显示 |
| 停止运行   | Option   | 停止整个视频输出                         |
| 取消轨迹   | Option   | 在一开始时取消轨迹                       |
| 阈值调试   | Option   | 预测得分的阈值，默认为0.5                |
| 输入FPS    | Option   | 视频的FPS                                |
| 检测用时   | Option   | 视频的检测时间                           |
| 人流量检测 | Option   | 每隔一段帧数内的人流量统计图表           |
| 时间长度   | Option   | 人流量时间统计长度                       |
| 开启出入口 | Option   | 导入视频后可自行选择是否开启出入口训练   |
| 导出文件   | Option   | 可视化结果保存的根目录，默认为output/    |


说明：

- 如果安装的PaddlePaddle不支持基于TensorRT进行预测，需要自行编译，详细可参考[预测库编译教程](https://paddleinference.paddlepaddle.org.cn/user_guides/source_compile.html)。