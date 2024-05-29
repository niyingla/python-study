import cv2
import numpy as np
import requests
import uuid
import os


def _template_match(image_bg, image_fg):
    '''模板匹配'''
    res = cv2.matchTemplate(image_bg, image_fg, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    return top_left[0]


def _sobel_edge(image):
    image_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    abs_x = cv2.convertScaleAbs(image_x)
    image_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    abs_y = cv2.convertScaleAbs(image_y)
    dst = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    return np.asarray(dst, dtype=np.uint8)


def _edge(img):
    np_data = np.array(img)
    rr = np.where(np_data != 0)
    xmin = min(rr[1])
    ymin = min(rr[0])
    xmax = max(rr[1])
    ymax = max(rr[0])
    return xmin, ymin, xmax, ymax


def _read(path):
    # 读取图片
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # 高斯模糊
    image = cv2.GaussianBlur(image, (1, 1), 0)
    # Sobel算子
    return _sobel_edge(image)



def _get_slide_distance(image1, image2):
    '''获取滑块距离'''
    fg_image = _read(image1)
    bg_image = _read(image2)
    xmin, ymin, xmax, ymax = _edge(fg_image)
    fg_image = fg_image[ymin:ymax, :]
    bg_image = bg_image[ymin:ymax, :]
    return (int)(_template_match(bg_image, fg_image) * 0.616)


def get_distance(full_url, slider_url):
    '''获取滑块距离'''
    #下载图片
    full_image_path = _down_img(full_url)
    slider_image_path = _down_img(slider_url)
    #获取滑块距离
    distance = _get_slide_distance(full_image_path, slider_image_path)
    #删除图片
    os.remove(full_image_path)
    os.remove(slider_image_path)
    return distance


def _down_img(full_image_path_url):
    '''下载图片'''
    response = requests.get(full_image_path_url)
    image_path = str(uuid.uuid4())
    full_image_path = image_path + '.jpeg'
    with open(full_image_path, 'wb') as f:
        f.write(response.content)
        return full_image_path
