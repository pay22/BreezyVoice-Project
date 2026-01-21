# BreezyVoice 台灣國語設計框架

這是一個專門將生硬文字轉化為在地「台灣國語」語氣，並合成親切語音的實驗專案。

## 專案開發進度
- [x] 環境架設 (Python, venv, edge-tts)
- [ ] 撰寫文案轉譯器 (Translator.py)
- [ ] 建立在地化詞庫 (Dictionary.json)
- [ ] 整合語音合成 (Synthesizer.py)

## 設計規範 (Spec)
1. **語氣：** 結尾需含「喔、啦、吼」等助詞。
2. **用詞：** 必須將「信息」改為「訊息」、「質量」改為「品質」。
3. **發音：** 去除兒化音，弱化捲舌音。

## 如何執行
1. 啟動環境：`venv\Scripts\activate`
2. 執行測試：`python test_voice.py`