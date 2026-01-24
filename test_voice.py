# -*- coding: utf-8 -*-
from gtts import gTTS
import sys
import os
import re

# 1. 定義想說的話（台灣國語風格測試）
text = "你好，這裡是 BreezyVoice 專案，我們準備要開始寫程式囉！"

# 2. 轉換為語音檔案 (lang='zh-TW' 確保是台灣口音)
print("正在轉換語音...")
tts = gTTS(text=text, lang='zh-TW')
tts.save("hello.mp3")

# 3. 播放聲音 (在 WSL 裡播放聲音比較複雜，我們先確認檔案有產生)
if os.path.exists("hello.mp3"):
    print("成功！語音檔案 hello.mp3 已產生在資料夾中。")
else:
    print("失敗，找不到檔案。")

def tw_accent_converter(text):
    """
    簡單的台灣國語轉換器 (BreezyVoice 核心邏輯原型)
    """
    # 建立轉換規則字典
    rules = {
        "是": "速",
        "這": "這塊",
        "知道": "珠道",
        "什麼": "蝦咪",
        "就是": "就速",
        "我": "偶",
    }
    
    converted_text = text
    for key, value in rules.items():
        converted_text = converted_text.replace(key, value)
    return converted_text

# 原始文字
raw_text = "我跟你說，這件事情我真的不知道是什麼，就是這樣。"

# 轉換文字
tw_text = tw_accent_converter(raw_text)
print(f"原始文字: {raw_text}")
print(f"轉換後文字: {tw_text}")

# 產生語音
print("正在產生台灣國語風味語音...")
tts = gTTS(text=tw_text, lang='zh-TW')
tts.save("tw_style.mp3")
print("成功產生 tw_style.mp3！")

if __name__ == "__main__":
    # 如果執行時有帶參數，就用參數；沒有的話就用預設值
    input_text = sys.argv[1] if len(sys.argv) > 1 else "你好"
    tw_text = tw_accent_converter(input_text)
    
    print(f"轉換結果: {tw_text}")
    tts = gTTS(text=tw_text, lang='zh-TW')
    tts.save("custom.mp3")

def breezy_regex_engine(text):
    # 規則 1: 所有的「ㄕ」後面接一個母音時，把「ㄕ」換成「ㄙ」
    # \b 代表邊界，或是直接指定字元
    text = re.sub(r'是', '速', text)
    
    # 規則 2: 把所有「知道」換成「珠道」
    text = re.sub(r'知道', '珠道', text)
    
    # 規則 3: 模擬恩/昂不分 (簡單示範)
    # 把「正」經 變成 「真」經
    text = re.sub(r'正', '真', text)
    
    return text

test_str = "你是不知道，他這個人正經起來很奇怪。"
print(f"原本: {test_str}")
print(f"Regex 轉換: {breezy_regex_engine(test_str)}")

def breezy_simple_regex(text):
    # 規則 1：最基礎替換 (直接取代)
    # 把「我」換成「偶」
    text = re.sub(r'我', '偶', text)
    
    # 規則 2：多選一替換 (使用 | 符號)
    # 把「什麼」或「啥」都換成「蝦咪」
    # | 代表「或」(OR)
    text = re.sub(r'什麼|啥', '蝦咪', text)
    
    # 規則 3：捕捉結尾並加上語助詞
    # $ 代表「句子的結尾」
    # 我們在句尾加上一個溫馨的「齁」
    text = re.sub(r'[。！!]$', '齁', text)
    
    return text

# 測試看看
input_str = "我不知道你在說什麼！"
output_str = breezy_simple_regex(input_str)

print(f"原本：{input_str}")
print(f"轉後：{output_str}")

def generate_mp3_regex_engine(input_text):
    # 1. 執行 Regex 轉換
    converted_text = breezy_regex_engine(input_text)
    print(f"原始文字：{input_text}")
    print(f"轉換後文字：{converted_text}")

    # 2. 呼叫 gTTS 生成語音
    print("正在生成 MP3...")
    tts = gTTS(text=converted_text, lang='zh-TW')
    
    # 3. 儲存檔案
    filename = "breezy_output_engine.mp3"
    tts.save(filename)
    print(f"成功！檔案已儲存為: {filename}")

if __name__ == "__main__":
    # 測試一段有代表性的話
    my_text = "你是不知道，他這個人正經起來很奇怪。"
    generate_mp3_regex_engine(my_text)    

def generate_mp3_regex(input_text):
    # 1. 執行 Regex 轉換
    converted_text = breezy_simple_regex(input_text)
    print(f"原始文字：{input_text}")
    print(f"轉換後文字：{converted_text}")

    # 2. 呼叫 gTTS 生成語音
    print("正在生成 MP3...")
    tts = gTTS(text=converted_text, lang='zh-TW')
    
    # 3. 儲存檔案
    filename = "breezy_output.mp3"
    tts.save(filename)
    print(f"成功！檔案已儲存為: {filename}")

if __name__ == "__main__":
    # 測試一段有代表性的話
    my_text = "我不知道你在說什麼！"
    generate_mp3_regex(my_text)