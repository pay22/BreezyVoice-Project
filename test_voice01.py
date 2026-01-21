# -*- coding: utf-8 -*-
# BreezyVoice Project Spec 
import asyncio
import edge_tts

async def amain():
    # 測試台灣女聲曉臻
    TEXT = "嗨！你好喔，我是你的 Breezy 助手。現在測試聲音正常嗎？"
    VOICE = "zh-TW-HsiaoChenNeural"
    OUTPUT_FILE = "test_output.mp3"
    
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"成功啦！請到資料夾打開 {OUTPUT_FILE} 聽聽看。")

if __name__ == "__main__":
    asyncio.run(amain())