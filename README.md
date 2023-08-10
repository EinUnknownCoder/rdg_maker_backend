# rdg_maker_backend

[.venv Setup](https://code.visualstudio.com/docs/python/environments)

[FFMPEG Download](https://ffmpeg.org/download.html)
ffmpeg.exe & ffprobe.exe needed

uvicorn main:app --reload

TTS by https://voicemaker.in/ (Salli)

Changes:

## 2023 08 10
### pytube.exceptions.AgeRestrictedError: XdBz3aVxHnc is age restricted, and can't be accessed without logging in.

For pytube 15.0.0 I had the AgeRestrictedError in streams contents even using the use_oauth option.

I fixed the problem only changing ANDROID_MUSIC with ANDROID as "client" at line 223 of innertube.py:

>def __init__(self, client='ANDROID_MUSIC', use_oauth=False, allow_cache=True):

>def __init__(self, client='ANDROID', use_oauth=False, allow_cache=True):

### pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W
As juanchosaravia suggested on https://github.com/pytube/pytube/issues/1199, in order to solve the problem, you should go in the cipher.py file and replace the line 30, which is:

>var_regex = re.compile(r"^\w+\W")

With that line:

>var_regex = re.compile(r"^\$*\w+\W")

After that, it worked again.

~~Added~~
~~r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)'~~
~~at pytube/cipher.py -> get_throttling_function_name~~