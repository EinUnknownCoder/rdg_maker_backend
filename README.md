# rdg_maker_backend

[.venv Setup](https://code.visualstudio.com/docs/python/environments)

[FFMPEG Download](https://ffmpeg.org/download.html)
ffmpeg.exe & ffprobe.exe needed

uvicorn main:app --reload

TTS by https://voicemaker.in/

Changes:
Added
r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)'
at pytube/cipher.py -> get_throttling_function_name