import math

startTime = "01:15:55"
startTimeSplit = startTime.split(":")
startTimeInSeconds = 0
startTimeInSeconds += int(startTimeSplit[0]) * 60 * 60
startTimeInSeconds += int(startTimeSplit[1]) * 60
startTimeInSeconds += int(startTimeSplit[2])

raw = """
00:00:03 1 Brave Girls - Chi Mat Ba Ram (Chorus 1) (None)
00:01:03 2 Seventeen - Fear (Chorus 2) (None)
00:01:44 3 Itzy - Icy (Chorus 1) (None)
00:02:13 4 Blackpink - Kill this Love (Chorus 1) (None)
00:02:46 5 Trendz - Vagabond (Pre-Chorus 1) (None)
00:03:46 6 Golden Child - One (Lucid Dream) (Chorus 1) (None)
00:04:40 7 Jessi - Zoom (Chorus 1) (None)
00:05:11 8 Kiss of Life - Sugarcoat (Chorus 1) (None)
00:05:55 9 Stray Kids - S-Class (Chorus 1) (None)
00:06:39 10 Ateez - Wave (Chorus 1) (None)
00:07:13 11 BTS - Idol (Chorus 1) (None)
00:08:07 12 TAN - Louder (Chorus 1) (None)
00:09:05 13 Kingdom - Long Live The King (Chorus 1) (None)
00:09:50 14 Red Velvet - Russian Roulette (Dancebreak) (None)
00:11:03 15 Pixy - Bewitched (Chorus 1) (None)
00:12:01 16 KARA - Mamma Mia (Chorus 1) (None)
00:12:47 17 Kang Soyeon - Loca Loca (Pre-Chorus 1) (None)
00:13:33 18 Purplekiss - Ponzona (Dancebreak) (None)
00:14:18 19 EXID - I love you (Chorus 1) (None)
00:15:17 20 The Boyz - Roar (Chorus 1) (None)
00:16:02 21 Enhypen - One and Only (Chorus 1) (None)
00:16:30 22 NCT - Sticker (Pre-Chorus 1) (None)
00:17:13 23 TXT - No Rules (Chorus 1) (None)
00:18:01 24 fromis_9 - Attitude (Chorus 1) (None)
00:18:50 25 NewJeans - OMG (Pre-Chorus 1) (None)
00:19:37 26 Taemin - Criminal (Pre-Chorus 1) (None)
00:20:31 27 Shinee - Lucifer (Chorus 1 (Beginning)) (None)
00:21:30 28 Triple S - Rising (Chorus 1) (None)
00:22:30 29 Twice - TT (Pre-Chorus 1, Chorus 1) (None)
00:23:24 30 A.C.E - Undercover (Pre-Chorus 1) (None)
00:24:26 31 Girls Planet - Shoot (Chorus 1) (None)
00:25:26 32 Twice - The Feels (Chorus 1) (None)
"""

rawSplit = raw.split("\n")[1:-1]
for x in rawSplit:
    playlistTimeStampInSeconds = 0
    newTimeStampHour = 0
    newTimeStampMinute = 0

    # Remove unnecassary Suffix
    noSuffix = x.rsplit(" (", 2)[0]
    noSuffixSplit = noSuffix.split(" ", 2)

    playlistTimeStampSplit = noSuffixSplit[0].split(":")
    playlistTimeStampInSeconds += int(playlistTimeStampSplit[0]) * 60 * 60
    playlistTimeStampInSeconds += int(playlistTimeStampSplit[1]) * 60
    playlistTimeStampInSeconds += int(playlistTimeStampSplit[2])

    newTimeStampInSeconds = startTimeInSeconds + playlistTimeStampInSeconds

    newTimeStampHour =  math.floor(newTimeStampInSeconds / 3600)
    newTimeStampInSeconds = newTimeStampInSeconds % 3600
    newTimeStampHourString = str(newTimeStampHour).zfill(2)

    newTimeStampMinute =  math.floor(newTimeStampInSeconds / 60)
    newTimeStampInSeconds = newTimeStampInSeconds % 60
    newTimeStampMinuteString = str(newTimeStampMinute).zfill(2)

    newTimeStampSecondString =str(newTimeStampInSeconds).zfill(2)

    newTimeStampString = ":".join([newTimeStampHourString, newTimeStampMinuteString, newTimeStampSecondString])

    print(newTimeStampString + " " + noSuffixSplit[2])
    