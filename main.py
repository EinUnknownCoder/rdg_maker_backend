from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os
from pytube import YouTube
import random
from pydub import AudioSegment
from datetime import datetime
import time
from pydantic import BaseModel
from openpyxl import load_workbook

class Dancer(BaseModel):
    name: str

class ExcelPlaylist(BaseModel):
    countdown: bool
    countdownCrossfade: bool
    intro: bool
    outro: bool
    preTime: int
    postTime: int
    fadeInTime: int
    fadeOutTime: int
    countdownVoice: str
    coverImage: str


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

@app.get("/")
def read_root():
    return {"Data": "Hello World"}

@app.post("/createExcelPlaylist")
def create_item(playlist: ExcelPlaylist):

    wb = load_workbook(filename="songlist.xlsx", data_only=True)
    sheet = wb["Songlist"]
    
    monsta_x_love = {
        "URL": "https://youtu.be/wssbMRrXRD8",
        "Title": "LOVE",
        "Artist": "MONSTA X",
        "Start": 84,
        "End": 91,
        "Description": "Custom: Intro",
        "Dancer": "None"
    }

    bts_run = {
        "URL": "https://youtu.be/2WBwJD6hldA",
        "Title": "RUN",
        "Artist": "BTS",
        "Start": 228,
        "End": 233,
        "Description": "Custom: Outro",
        "Dancer": "None"
    }

    song_list = []

    for x in range(2, sheet.max_row + 1):
        startTime = sheet.cell(x, 10).value
        if(sheet.cell(x, 10).value < playlist.preTime):
            startTime = playlist.preTime
        song_list.append({
            "URL": sheet.cell(x, 1).value,
            "Artist": sheet.cell(x, 2).value,
            "Title": sheet.cell(x, 3).value,
            "Description": sheet.cell(x, 4).value,
            "Dancer": sheet.cell(x, 5).value,
            "Start": startTime,
            "End": sheet.cell(x, 11).value
        })

    wb.close()

    random.shuffle(song_list)

    if(playlist.intro):
        song_list.insert(0, monsta_x_love)

    if(playlist.outro):
        song_list.append(bts_run)

    # Download mp4 files from YouTube
    raw_folder_content = os.listdir("raw")
    for song in song_list:
        file_name = song["Artist"] + " - " + song["Title"] + ".mp4"
        file_name = file_name.casefold()

        if file_name not in raw_folder_content:
            print(f"{file_name} is missing! Downloading... ")

            yt = YouTube(song["URL"])
            audio_stream = yt.streams.get_audio_only()
            audio_stream.download("raw/", file_name)
        
    print("Download missing songs complete!")

    if (playlist.countdown and not playlist.intro):
        chapters = [["00:00:00", 
            0, 
            "RDG Start",
            "",
            ""]]
    else:
        chapters = []

    song_counter = 0
    countdown = AudioSegment.from_file(f"templates/countdown/{playlist.countdownVoice}.mp3")
    export = AudioSegment.empty()

    print("Creating Export...")
    for song in song_list:

        if (playlist.countdown and not (song["Description"] == "Custom: Intro" or song["Description"] == "Custom: Outro")):
            export += countdown

        # Chapters
        song_counter += 1
        timestamp = time.strftime('%H:%M:%S', time.gmtime(int(export.duration_seconds)))
        chapters.append([
            timestamp, 
            song_counter, 
            " - ".join([song["Artist"], song["Title"]]),
            f"({song['Description']})",
            f"({song['Dancer']})"
            ])

        # Audio
        file_name = song["Artist"] + " - " + song["Title"] + ".mp4"
        file_name = file_name.casefold()
        song_snippet = AudioSegment.from_file("raw/" + file_name)[(song["Start"] - playlist.preTime) * 1000:(song["End"] + playlist.postTime) * 1000].fade_in(1000 * playlist.fadeInTime).fade_out(1000 * playlist.fadeOutTime)
        song_snippet_normalized = match_target_amplitude(song_snippet, -10.0)
        if playlist.countdown and playlist.countdownCrossfade and not (song["Description"] == "Custom: Intro" or song["Description"] == "Custom: Outro"):
            export = export.append(song_snippet_normalized, crossfade=1000)
        else:
            export += song_snippet_normalized

    export_file_name = "".join([str(datetime.now().strftime("%Y-%m-%d_%H_%M_%S"))]) + ".mp3"

    print("Exporting...")
    export.export("export/" + export_file_name , format="mp3")

    chapter_summary_comment = ""
    chapter_summary_YouTube = ""

    for chapter in chapters:
        chapter_summary_comment += f"{chapter[0]} {chapter[1]} {chapter[2]} {chapter[3]} {chapter[4]}newLine"
        chapter_summary_YouTube += f"{chapter[0]} {chapter[1]} {chapter[2]} {chapter[3]} {chapter[4]}\n"

    os.system(f"""ffmpeg.exe -loop 1 -framerate 1 -i templates/image/{playlist.coverImage}.jpg -i export/{export_file_name} -map 0:v -map 1:a -r 10 -vf \"scale='iw-mod(iw,2)\':\'ih-mod(ih,2)\',format=yuv420p\" -movflags +faststart -shortest -fflags +shortest -max_interleave_delta 100M -metadata comment=\"{chapter_summary_comment}\" export/{export_file_name}.mp4""")

    return chapter_summary_YouTube

@app.get("/showExcel")
def read_root():
    wb = load_workbook(filename="songlist.xlsx", data_only=True)
    sheet = wb["Songlist"]

    answer = []

    for x in range(2, sheet.max_row + 1):
        answer.append({
            "URL": sheet.cell(x, 1).value,
            "Artist": sheet.cell(x, 2).value,
            "Title": sheet.cell(x, 3).value,
            "Description": sheet.cell(x, 4).value,
            "Dancer": sheet.cell(x, 5).value,
            "Start": sheet.cell(x, 10).value,
            "End": sheet.cell(x, 11).value
        })
    
    wb.close()

    return answer

@app.post("/dancer/")
def create_item(dancer: Dancer):
    con = sqlite3.connect("songlist.db")
    cur = con.cursor()

    # res = cur.execute(f"""
    # INSERT INTO
    # DancerNew (Name)
    # VALUES ('{dancer.name}')
    # """)

    # res = cur.execute(f"""
    # CREATE TABLE DancerNew (
    #     DancerID INTEGER PRIMARY KEY,
    #     Name TEXT NOT NULL
    # )
    # """)

    # res = cur.execute(f"""
    # DROP TABLE DancerNew
    # """)

    # data = res.fetchall()
    con.close()
    return dancer

@app.get("/createVAOPlaylist/{dancer_ids}")
def read_item(dancer_ids):
    dancer_array = dancer_ids.split(",")
    condition_array = []
    for x in dancer_array:
        condition_array.append(f"dancer.DancerID={x}")
    condition_string =  " OR ".join(condition_array)

    con = sqlite3.connect("songlist.db")
    cur = con.cursor()
    res = cur.execute(f"""
    SELECT 
    song.URL, song.Title, song.Artist,
    sequence.Start, sequence.End, sequence.Description
    FROM sequence
    INNER JOIN song ON sequence.SongID=song.SongID
    INNER JOIN mastery ON sequence.SequenceID=mastery.SequenceID
    INNER JOIN dancer ON mastery.DancerID=dancer.DancerID
    WHERE {condition_string}
    """)
    data = res.fetchall()
    con.close()

    monsta_x_love = {
        "URL": "https://youtu.be/wssbMRrXRD8",
        "Title": "LOVE",
        "Artist": "MONSTA X",
        "Start": 84,
        "End": 91,
        "Description": "Custom: Intro"
    }

    bts_run = {
        "URL": "https://youtu.be/2WBwJD6hldA",
        "Title": "RUN",
        "Artist": "BTS",
        "Start": 228,
        "End": 233,
        "Description": "Custom: Outro" 
    }

    song_list = []

    for entry in data:
        song_list.append({
            "URL": entry[0],
            "Title": entry[1],
            "Artist": entry[2],
            "Start": entry[3],
            "End": entry[4],
            "Description": entry[5]
        })

    # Shuffle Playlist and reduce the length to 97 songs
    random.shuffle(song_list)
    song_list = song_list[:97]
    song_list.append(bts_run)
    song_list.insert(0, monsta_x_love)

    # Download mp4 files from YouTube
    raw_folder_content = os.listdir("raw")
    for song in song_list:
        file_name = song["Artist"] + " - " + song["Title"] + ".mp4"
        file_name = file_name.casefold()

        if file_name not in raw_folder_content:
            print(f"{file_name} is missing! Downloading... ")

            yt = YouTube(song["URL"])
            audio_stream = yt.streams.get_audio_only()
            audio_stream.download("raw/", file_name)
        else:
            print(f"{file_name} is already downloaded.")

    chapters = []
    song_counter = 0
    export = AudioSegment.empty()

    print("Creating Export...")
    for song in song_list:

        # Chapters
        song_counter += 1
        timestamp = time.strftime('%H:%M:%S', time.gmtime(int(export.duration_seconds)))
        chapters.append([
            timestamp, 
            song_counter, 
            " - ".join([song["Artist"], song["Title"]]),
            f"({song['Description']})"
            ])

        # Audio
        file_name = song["Artist"] + " - " + song["Title"] + ".mp4"
        file_name = file_name.casefold()
        song_snippet = AudioSegment.from_file("raw/" + file_name)[(song["Start"] - 10) * 1000:(song["End"] + 2) * 1000].fade_in(2000).fade_out(2000)
        export += song_snippet

    export_file_name = "".join([str(datetime.now().strftime("%Y-%m-%d_%H_%M_%S"))]) + ".mp3"

    print("Exporting...")
    export.export("export/" + export_file_name , format="mp3")

    chapter_summary_comment = ""
    chapter_summary_YouTube = ""

    for chapter in chapters:
        chapter_summary_comment += f"{chapter[0]} {chapter[1]} {chapter[2]} {chapter[3]}newLine"
        chapter_summary_YouTube += f"{chapter[0]} {chapter[1]} {chapter[2]} {chapter[3]}\n"

    os.system(f"""ffmpeg.exe -loop 1 -framerate 1 -i image.jpg -i export/{export_file_name} -map 0:v -map 1:a -r 10 -vf \"scale='iw-mod(iw,2)\':\'ih-mod(ih,2)\',format=yuv420p\" -movflags +faststart -shortest -fflags +shortest -max_interleave_delta 100M -metadata comment=\"{chapter_summary_comment}\" export/{export_file_name}.mp4""")

    return {"Data": chapter_summary_YouTube}

@app.get("/showPreview/{dancer_ids}")
def read_item(dancer_ids):
    dancer_array = dancer_ids.split(",")
    condition_array = []
    for x in dancer_array:
        condition_array.append(f"dancer.DancerID={x}")
    condition_string =  " OR ".join(condition_array)

    con = sqlite3.connect("songlist.db")
    cur = con.cursor()
    res = cur.execute(f"""
    SELECT 
    song.URL, song.Title, song.Artist, 
    sequence.Description, sequence.Start, sequence.End, sequence.LastTimeInRDG, sequence.comment, 
    dancer.Name,
    mastery.MasteryID
    FROM sequence
    INNER JOIN song ON sequence.SongID=song.SongID
    INNER JOIN mastery ON sequence.SequenceID=mastery.SequenceID
    INNER JOIN dancer ON mastery.DancerID=dancer.DancerID
    WHERE {condition_string}
    """)
    data = res.fetchall()
    con.close()

    answer = []
    for entry in data:
        answer.append(
            {
                "Title": entry[1],
                "Artist": entry[2],
                "Description": entry[3],
                "Dancer": entry[8],
                "MasteryID": entry[9],
            }
        )
    return answer

@app.get("/mastery")
def read_root():
    con = sqlite3.connect("songlist.db")
    cur = con.cursor()
    res = cur.execute("""
    SELECT 
    mastery.*,
    sequence.Description,
    song.Artist, song.Title,
    dancer.Name
    FROM mastery
    INNER JOIN sequence ON sequence.SequenceID=mastery.SequenceID
    INNER JOIN song ON sequence.SongID=song.SongID
    INNER JOIN dancer ON dancer.DancerID=mastery.DancerID
    """)
    data = res.fetchall()
    con.close()

    answer = []
    for entry in data:
        answer.append(
            {
                "ID": entry[0],
                "SequenceID": entry[1],
                "DancerID": entry[2],
                "Description": entry[3],
                "Artist": entry[4],
                "Title": entry[5],
                "Name": entry[6],
            }
        )
    return answer

@app.get("/sequence")
def read_root():
    con = sqlite3.connect("songlist.db")
    cur = con.cursor()
    res = cur.execute("""
    SELECT 
    sequence.*,
    song.Artist, song.Title
    FROM sequence
    INNER JOIN song ON sequence.SongID=song.SongID
    """)
    data = res.fetchall()
    con.close()

    answer = []
    for entry in data:
        answer.append(
            {
                "ID": entry[0],
                "SongID": entry[1],
                "Start": entry[2],
                "End": entry[3],
                "Description": entry[4],
                "Comment": entry[5],
                "LastTimeInRDG": entry[6],
                "Artist": entry[7],
                "Title": entry[8],
            }
        )
    return answer

@app.get("/song")
def read_root():
    con = sqlite3.connect("songlist.db")
    cur = con.cursor()
    res = cur.execute("""
    SELECT 
    *
    FROM song
    """)
    data = res.fetchall()
    con.close()

    answer = []
    for entry in data:
        answer.append(
            {
                "ID": entry[0],
                "URL": entry[1],
                "Artist": entry[2],
                "Title": entry[3],
                "Comment": entry[4],
            }
        )
    return answer

@app.get("/dancer")
def read_root():
    con = sqlite3.connect("songlist.db")
    cur = con.cursor()
    res = cur.execute("""
    SELECT 
    *
    FROM dancer
    """)
    data = res.fetchall()
    con.close()

    answer = []
    for entry in data:
        answer.append(
            {
                "ID": entry[0],
                "Name": entry[1],
            }
        )
    return answer

@app.get("/all")
def read_root():
    con = sqlite3.connect("songlist.db")
    cur = con.cursor()
    res = cur.execute("""
    SELECT 
    song.URL, song.Title, song.Artist, 
    sequence.Description, sequence.Start, sequence.End, sequence.LastTimeInRDG, sequence.comment, 
    dancer.Name
    FROM sequence
    INNER JOIN song ON sequence.SongID=song.SongID
    INNER JOIN mastery ON sequence.SequenceID=mastery.SequenceID
    INNER JOIN dancer ON mastery.DancerID=dancer.DancerID
    """)
    data = res.fetchall()
    con.close()

    answer = []
    for entry in data:
        answer.append(
            {
                "URL": entry[0],
                "Title": entry[1],
                "Artist": entry[2],
                "Description": entry[3],
                "Start": entry[4],
                "End": entry[5],
                "LastTimeInRDG": entry[6],
                "Comment": entry[7],
                "Dancer": entry[8],
            }
        )
    return answer
