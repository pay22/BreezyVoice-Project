import whisper
import os

def run_advanced_whisper(audio_path):
    if not os.path.exists(audio_path):
        print("找不到檔案！")
        return

    # 1. 載入模型 (強制 CPU)
    model = whisper.load_model("base", device="cpu")

    # 2. 執行辨識 + 即時翻譯 (task="translate" 會將任何語言轉為英文)
    print(f"正在處理中，請稍候...")
    
    # 這裡我們跑兩次，一次正常辨識，一次翻譯
    result_zh = model.transcribe(audio_path, fp16=False)
    result_en = model.transcribe(audio_path, fp16=False, task="translate")

    # 3. 輸出到檔案 (result.txt)
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write("--- 中文辨識內容 ---\n")
        f.write(result_zh["text"] + "\n\n")
        f.write("--- 英文翻譯內容 ---\n")
        f.write(result_en["text"] + "\n")
    print("✅ 已將文字存入 result.txt")

    # 4. 製作字幕檔格式 (SRT)
    with open("result.srt", "w", encoding="utf-8") as srt:
        for i, segment in enumerate(result_zh["segments"]):
            start = format_time(segment["start"])
            end = format_time(segment["end"])
            text = segment["text"]
            srt.write(f"{i + 1}\n{start} --> {end}\n{text}\n\n")
    print("✅ 已將字幕存入 result.srt")

def format_time(seconds):
    """將秒數轉為 SRT 字幕時間格式 00:00:00,000"""
    td = float(seconds)
    hours = int(td // 3600)
    minutes = int((td % 3600) // 60)
    secs = int(td % 60)
    millis = int((td % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

if __name__ == "__main__":
    run_advanced_whisper("test_audio.mp3")