# 相机参数设置

感光元件使用时必须要用其对应模块 *sensor*

## 首先是参数设置

使用之前一些基本的信息是要被知晓的

### 实例

```python
import sensor

# init device
sensor.reset()

# 输出属性设置
sensor.set_pixformat(sensor.RGB565)  # 设置为彩色
sensor.set_framesize(sensor.QVGA)  # 设置图像的大小
sensor.skip_frames()  # 跳过n张照片，在更改设置后，跳过一些帧，等待感光元件变稳定
```

* 以上代码暂时还为经过测试, 暂时省略用法标注

### 详解

#### 色位深度设置

<details>
<summary>sensor.set_pixformat() 设置像素模式。</summary>

sensor.GRAYSCALE: 灰度，每个像素8bit。

sensor.RGB565: 彩色，每个像素16bit。

</details>

#### 图像大小设置

<details>
<summary>sensor.set_framesize() 设置图像的大小</summary>

sensor.QQCIF: 88x72

sensor.QCIF: 176x144

sensor.CIF: 352x288

sensor.QQSIF: 88x60

sensor.QSIF: 176x120

sensor.SIF: 352x240

sensor.QQQQVGA: 40x30

sensor.QQQVGA: 80x60

sensor.QQVGA: 160x120

sensor.QVGA: 320x240

sensor.VGA: 640x480

sensor.HQQQVGA: 80x40

sensor.HQQVGA: 160x80

sensor.HQVGA: 240x160

sensor.B64X32: 64x32 (用于帧差异 image.find_displacement())

sensor.B64X64: 64x64 用于帧差异 image.find_displacement())

sensor.B128X64: 128x64 (用于帧差异 image.find_displacement())

sensor.B128X128: 128x128 (用于帧差异 image.find_displacement())

sensor.LCD: 128x160 (用于LCD扩展板)

sensor.QQVGA2: 128x160 (用于LCD扩展板)

sensor.WVGA: 720x480 (用于 MT9V034)

sensor.WVGA2:752x480 (用于 MT9V034)

sensor.SVGA: 800x600 (仅用于 OV5640 感光元件)

sensor.XGA: 1024x768 (仅用于 OV5640 感光元件)

sensor.SXGA: 1280x1024 (仅用于 OV5640 感光元件)

sensor.UXGA: 1600x1200 (仅用于 OV5640 感光元件)

sensor.HD: 1280x720 (仅用于 OV5640 感光元件)

sensor.FHD: 1920x1080 (仅用于 OV5640 感光元件)

sensor.QHD: 2560x1440 (仅用于 OV5640 感光元件)

sensor.QXGA: 2048x1536 (仅用于 OV5640 感光元件)

sensor.WQXGA: 2560x1600 (仅用于 OV5640 感光元件)

sensor.WQXGA2: 2592x1944 (仅用于 OV5640 感光元件)

</details>

#### 跳过一些帧

* sensor.skip_frames(n=10)

    跳过n张照片，在更改设置后，跳过一些帧，等待感光元件变稳定。

#### 摄像参数设置

* sensor.set_auto_gain()

    自动增益开启（True）或者关闭（False）。在使用颜色追踪时，需要关闭自动增益。

* sensor.set_auto_whitebal()

    自动白平衡开启（True）或者关闭（False）。在使用颜色追踪时，需要关闭自动白平衡。

* sensor.set_auto_exposure(enable[\, exposure_us])

    enable 打开（True）或关闭（False）自动曝光。默认打开。
    如果 enable 为False， 则可以用 exposure_us 设置一个固定的曝光时间（以微秒为单位）。

#### 设置窗口ROI

ROI行话缩写, Range Of Interesting

图像处理中的术语“感兴趣区”。就是在要处理的图像中提取出的要处理的区域。

* sensor.set_windowing(roi)

    其中roi对象是一个4元素数组(x, y, w, h)

#### 设置反转

* sensor.set_hmirror(bool)

    水平镜像

* sensor.set_vflip(bool)

    垂直翻转

## 测试图像

```python
sensor.snapshot()
```

直接以当前设置进行单张拍摄, 该方法将返回一个image对象
