from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os
from pytube import YouTube
import random
import math
from pydub import AudioSegment
from datetime import datetime

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

@app.get("/")
def read_root():
    return {"Data": "Hello World"}

@app.get("/createPlaylist/{dancer_ids}")
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
    sequence.Start, sequence.End, sequence.Desription
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

        if file_name not in raw_folder_content:
            print(f"{file_name} is missing! Downloading... ")

            yt = YouTube(song["URL"])
            audio_stream = yt.streams.get_audio_only()
            audio_stream.download("raw/", file_name)
        else:
            print(f"{file_name} is already downloaded and is skipped.")

    timestamps = []

    export = AudioSegment.empty()

    print("Creating Export...")
    for song in song_list:

        file_name = song["Artist"] + " - " + song["Title"] + ".mp4"

        song_snippet = AudioSegment.from_file("raw/" + file_name)[(song["Start"] - 10) * 1000:(song["End"] + 2) * 1000].fade_in(2000).fade_out(2000)

        export += song_snippet

    export_file_name = "".join([str(datetime.now().strftime("%Y-%m-%d_%H_%M_%S"))]) + ".mp3"

    print("Exporting...")
    export.export("export/" + export_file_name , format="mp3")

    return song_list

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

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
