import math

startTime = "01:16:34"
startTimeSplit = startTime.split(":")
startTimeInSeconds = 0
startTimeInSeconds += int(startTimeSplit[0]) * 60 * 60
startTimeInSeconds += int(startTimeSplit[1]) * 60
startTimeInSeconds += int(startTimeSplit[2])

raw = """
00:00:03 1 Le Sserafim - Eve, Psyche and the Bluebeards Wife (Chorus 1) (None)
00:00:55 2 SuperJunior - Lo Siento (Chorus 2) (None)
00:01:50 3 Kard - Dumb Litty (Pre-Chorus 1) (None)
00:02:31 4 Kingdom - Ascension (Pre-Chorus 1) (None)
00:03:14 5 Blackpink - Ddu-Du Ddu-du (Chorus 1) (None)
00:03:45 6 Craxy - Nugudom (Pre-Chorus 1) (None)
00:04:46 7 Ateez - Wave (Chorus 1) (None)
00:05:20 8 Nmixx - Young, Dumb, Stupid (Chorus 1) (None)
00:05:57 9 CL - Spicy (Pre-Chorus 1) (None)
00:06:38 10 Fromis_9 - Rewind (Chorus 1) (None)
00:07:23 11 Nature - Girls (Chorus 1) (None)
00:08:19 12 New Jeans - Attention (Chorus 1) (None)
00:08:53 13 Itzy - Wannabe (Pre-Chorus 1, Chorus 1) (None)
00:09:47 14 Jimin - Set Me Free pt. 2 (Chorus 1) (None)
00:10:33 15 aespa - Spicy (Chorus 1) (None)
00:11:17 16 Seventeen - Super (Pre-Chorus 1) (None)
00:12:07 17 Girls Generation - The Boys (Chorus 1) (None)
00:12:32 18 Athena - Snap (Chorus 2) (None)
00:13:29 19 Tribe - Rub a Dum (Chorus 1) (None)
00:14:14 20 Twice - Jelly Jelly (Chorus 1) (None)
00:14:54 21 (G)-Idle - Nxde (Chorus 1) (None)
00:15:38 22 Everglow - Adios (Chorus 1) (None)
00:16:28 23 Treasure - I love you (Pre-Chorus 1) (None)
00:17:06 24 Boys Planet - Supercharger (Pre-Chorus 1) (None)
00:17:40 25 TXT - Farewell, Neverland (Chorus 2) (None)
00:18:38 26 Enhypen - Blessed-Cursed (Chorus 1) (None)
00:19:22 27 Oneus - Lit (Chorus 1) (None)
00:20:14 28 Momoland - Bboom Bboom (Pre-Chorus 1, Chorus 1) (None)
00:21:05 29 Oh My Girl - Nonstop (Chorus 1) (None)
00:21:44 30 BTS - Boy with Love (Pre-Chorus 1) (None)
00:22:39 31 Stray Kids - S-Class (Dancbreak) (None)
00:23:12 32 Twice - Fancy (Pre-Chorus 1, Chorus 1) (None)
00:23:52 33 Ive - Love Dive (Pre-Chorus 1, Chorus 1) (None)
00:24:51 34 Enhypen - Bite Me (Pre-Chorus 1) (None)
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
    