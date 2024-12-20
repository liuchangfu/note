# PyQt6核心功能介绍

1、QtCore 模块是非 GUI 的核心库，这个模块用来处理时间、文件、目录、各种类型的数据、流（stream）、URLs，mime 类型、线程和进程等。

2、QtGui 专注于图形界面元素，提供了诸如窗口系统集成、事件处理、2D图形，基本图像、字体、文本的类。

3、QtWidgets 提供常用的GUI组件，用于创建各种风格的UI界面。

4、QtDBus 提供了使用 D-Bus 处理 IPC 通讯的类。

5、QtNetwork 提供了网络集成工具，这些工具使网络编程变得更容易，可移植性也更好，方便了 TCP/IP 和 UDP 服务端和客户端编程。

## 一、QtWidgets

`QWidget` 模块提供了一些常用的 GUI 组件。

- QMainWindow：用于创建主窗体。

- QLabel：用于显示文本或图片。

- QPushButton：用于创建按钮。

- QCheckBox：用于创建复选框。

- QRadioButton：用于创建单选按钮。

- QComboBox：用于创建下拉框。

- QLineEdit：用于创建单行文本框。

- QTextEdit：用于创建多行文本框。

- QSlider：用于创建滑动条。

- QProgressBar：用于创建进度条。

- QSpinBox：用于创建数字输入框。

- QCalendarWidget：用于创建日历组件。

- QTabWidget：用于创建选项卡组件。

- QDockWidget：用于创建可停靠的面板组件。

- QSplitter：用于创建可拖动分割器。

- QScrollArea：用于创建可滚动区域。

## 二、QtGui

提供了一些用于创建图形用户界面的类和函数。在QtGui模块中，包含了许多用于处理 GUI 元素的类

- QApplication：用于管理应用程序的主要控制流程。

- QWidget：用于创建窗口或其他用户界面元素的基类。

- QLabel：用于显示文本或图片。

- QPushButton：用于创建按钮。

- QCheckBox：用于创建复选框。

- QRadioButton：用于创建单选按钮。

- QLineEdit：用于创建单行文本框。

- QTextEdit：用于创建多行文本框。

- QComboBox：用于创建下拉框。

- QSlider：用于创建滑动条。

- QProgressBar：用于创建进度条。

- QFileDialog：用于打开和保存文件对话框等。

## 三、QtCore

QtCore 是 PyQt 中的另一个重要模块，提供了一些用于处理核心功能的类和函数。QtCore 模块包含了许多与应用程序开发密切相关的类，其中一些常用的类包括：

- QObject：所有 Qt 对象的基类，支持信号和槽机制。

- QTimer：用于定时器操作，可以实现定时执行某个函数或操作。

- QStringList：用于处理字符串列表。

- QThread：用于创建线程。

- QVariant：用于处理不同数据类型的值。

- QDateTime：用于处理日期和时间信息。

- QSettings：用于应用程序设置的类。

- QTimerEvent：定时器事件类，继承自 QEvent，用于处理定时器事件。

- QEventLoop：用于事件处理和事件循环的类。

- QCoreApplication：用于管理应用程序的主要控制流程。

- QtCore 模块包含了许多用于处理数据、事件、线程等核心功能的类，是 PyQt6 应用程序的基础。通过 QtCore 模块，开发者可以实现事件处理、数据存储、线程管理等功能。
