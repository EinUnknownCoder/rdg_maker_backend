import math

startTime = "01:32:19"
startTimeSplit = startTime.split(":")
startTimeInSeconds = 0
startTimeInSeconds += int(startTimeSplit[0]) * 60 * 60
startTimeInSeconds += int(startTimeSplit[1]) * 60
startTimeInSeconds += int(startTimeSplit[2])

raw = """
00:05:03 7 The Boyz - DDD (Dancebreak) (None)
00:06:02 8 Ciipher - I like you (Chorus 2) (None)
00:06:37 9 Fifty Fifty - Cupid (Pre-Chorus 1) (None)
00:07:13 10 TNX - Love or Die (Chorus 1) (None)
00:07:48 11 Twice - The Feels (Chorus 1) (None)
00:08:26 12 WJSN - Secret (Chorus 1) (None)
00:09:19 13 Ateez - Horizon (Chorus 1) (None)
00:09:46 14 Stray Kids - S-Class (Pre-Chorus 1) (None)
00:10:31 15 Twice - Set Me Free (Pre-Chorus 1) (None)
00:11:22 16 JYP - Groove Back (Chorus 2) (None)
00:12:11 17 EXID - I love you (Chorus 1) (None)
00:13:08 18 NCT - Perfume (Chorus 1) (None)
00:13:38 19 Iz*One - Panorama (Pre-Chorus 1) (None)
00:14:24 20 Itzy - Loco (Pre-Chorus 2, Dancebreak, Chorus 3) (None)
00:15:58 21 Nature - Limbo (Chorus 1) (None)
00:16:34 22 Seventeen - Rock with You (Pre-Chorus 1) (None)
00:17:16 23 KDA - The Baddest (Chorus 1) (None)
00:18:00 24 New Jeans - OMG (Chorus 1) (None)
00:18:57 25 Enhypen - Go Big or Go Home (Chorus 1) (None)
00:19:40 26 Pink Fantasy - Iriwa (Chorus 1) (None)
00:20:14 27 Blackpink - Kill this Love (Chorus 1) (None)
00:20:46 28 StayC - Poppy (Chorus 1) (None)
00:21:31 29 TXT - New Rules (Chorus 1) (None)
00:22:18 30 Pixy - Bewitched (Pre-Chorus 1) (None)
00:23:11 31 Kingdom - Long Live The King (Chorus 1) (None)
00:23:55 32 Ive - Kitsch (Chorus 1) (None)
00:24:25 33 Tribe - Would You Run (Pre-Chorus 1) (None)
00:25:16 34 ChungHa - Sparkling (Chorus 1) (None)
00:26:01 35 Craxy - Poison Rose (Pre-Chorus 1) (None)
00:26:45 36 Itzy - Icy (Chorus 1) (None)
00:27:14 37 aespa - Illusion (Pre-Chorus 1, Chorus 1) (None)
00:28:09 38 Oh My Girl - Nonstop (Chorus 1) (None)
00:28:57 39 LeSserafim - Unforgiven (Pre-Chorus 1) (None)
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
    