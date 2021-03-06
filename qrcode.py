# -*- coding = utf-8 -*-
# @Time : 2021/6/14 0:24
# @Author : toast
# @File : demo.py
# @Software : PyCharm

from MyQR import myqr

myqr.run(
    words='https://baidu.com',  # 二维码内容
    version=20,  # 二维码大小
    level='H',  # 纠错等级（L，M，Q，H 四个等级，左到右依次升高，默认为H）
    picture='E:\\图片\\cat.jpg',  # 图片位置
    colorized=True,  # True为彩色，False为黑白（默认）
    contrast=1.0,   # 图片对比度
    brightness=1.0,   # 图片亮度
    save_name='QR_code.png',  # 输出文件名（默认"qrcode.png"）
    save_dir=r'E:\\桌面',  # 储存位置（默认为当前目录）
)
