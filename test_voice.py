# -*- coding: utf-8 -*-
from gtts import gTTS
import sys
import os

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