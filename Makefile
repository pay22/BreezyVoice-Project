# 定義變數
VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

# 建立環境與安裝套件
setup:
	python3 -m venv $(VENV)
	$(PIP) install gTTS pygame

# 執行測試
test:
	$(PYTHON) test_voice.py

# 讓你可以在終端機輸入 make say MSG="內容" 來測試
say:
	$(PYTHON) test_voice.py "$(MSG)"

# 執行批次處理
batch:
	$(PYTHON) test_voice.py --batch tasks.txt	