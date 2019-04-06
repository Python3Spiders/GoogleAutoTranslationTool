# -*- coding: utf-8 -*-
# author:           inspurer(月小水长)
# pc_type           lenovo
# create_time:      2019/4/6 15:44
# file_name:        translator.py
# github            https://github.com/inspurer
# qq邮箱            2391527690@qq.com
# 微信公众号         月小水长(ID: inspurer)

import requests
from HandleJs import Py4Js

import win32clipboard as w
import win32con
import time
def getText():#读取剪切板
    # 打开剪贴板
    w.OpenClipboard()
    # 读取剪贴板的内容
    d = w.GetClipboardData(win32con.CF_TEXT)
    # 关闭剪贴板
    w.CloseClipboard()
    try:
        return d.decode('utf-8')
    except:
        return d.decode('gbk')
def setText(aString):#写入剪切板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardText(aString)
    w.CloseClipboard()

def translate(tk, content):
    if len(content) > 4891:
        print("翻译的长度超过限制！！！")
        return

    param = {'tk': tk, 'q': content}

    result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en
        &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
        &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param)

    data = result.json()
    # print(data)
    print(data[0][0][0])
    print(data[0][1][2])
    return data[0][0][0]




def main():
    js = Py4Js()
    ls = ''
    while(True):
        # 如果剪贴板正在被占用
        try:
            cs = getText()
        except:
            time.sleep(1)
            cs = getText()
        print('cs',cs)
        if cs and cs != ls:
            print('准备翻译')
            content = getText()
            tk = js.getTk(content)
            res = translate(tk, content)
            setText(res)
            time.sleep(1)
            ls = res

if __name__ == "__main__":
    main()

# i am a girl
# i am a boy