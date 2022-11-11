from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
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
