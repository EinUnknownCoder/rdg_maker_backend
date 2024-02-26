import math

startTime = "01:34:19"
startTimeSplit = startTime.split(":")
startTimeInSeconds = 0
startTimeInSeconds += int(startTimeSplit[0]) * 60 * 60
startTimeInSeconds += int(startTimeSplit[1]) * 60
startTimeInSeconds += int(startTimeSplit[2])

raw = """
00:00:03 1 Bts - Airplane pt.2 (Chorus 1) (None)
00:01:01 2 Baekhyun - Bambi (Chorus 1) (None)
00:01:50 3 Stray Kids - All in (Chorus 2) (None)
00:02:22 4 oneus - bbusyeo (Chorus 1) (None)
00:02:59 5 Orange caramell - My copycat (Chorus 2) (None)
00:03:46 6 Itzy - Cherry (Chorus 1) (None)
00:04:19 7 Seventeen - Super (Pre-Chorus 1) (None)
00:05:17 8 WayV - Poppin’ Love (Chorus 1) (None)
00:06:00 9 snsd - genie (Chorus 1) (None)
00:06:48 10 Twice - Yes or Yes (Chorus 1) (None)
00:07:34 11 Yuju - DALALA (Chorus 1) (None)
00:08:23 12 J Hope - Hope World (Chorus 1) (None)
00:08:57 13 Jungkook - 3D (Chorus 1) (None)
00:09:41 14 EXO - Lucky One (Chorus 1) (None)
00:10:29 15 Red Velvet - Psycho (Chorus 1) (None)
00:11:08 16 Dreamcatcher - Chase me (Chorus 1) (None)
00:11:48 17 Momoland - I'm so Hot (Chorus 1) (None)
00:12:31 18 Twice - Likey (Chorus 1) (None)
00:13:17 19 NCT Dream - BOOM (Pre-Chorus 1) (None)
00:14:06 20 Stray Kids - The view (Chorus 3) (None)
00:15:01 21 (G)-IDLE - Super Lady (Chorus 1) (None)
00:15:32 22 Hwasa - Chili (Chorus 1) (None)
00:16:08 23 Everglow - Dun Dun (Pre-Chorus 1, Chorus 1) (None)
00:17:02 24 Pentagon - Humph (Chorus 1) (None)
00:17:51 25 lightsum - vivace (Chorus 1) (None)
00:18:40 26 Itzy - Ringo (Chorus 1) (None)
00:19:26 27 Ateez - Fireworks (I'm the one) (Chorus 1) (None)
00:20:11 28 RIIZE - Siren (Chorus 2) (None)
00:20:48 29 Apink - Dumhdurum (Chorus 1) (None)
00:21:41 30 THE BOYZ - WATCH IT (Chorus 1) (None)
00:22:17 31 Blackpink - Pretty Savage (Pre-Chorus 1) (None)
00:22:54 32 Vcha - Ready for the world (Chorus 1) (None)
00:23:34 33 Stray Kids - Easy (Chorus 1) (None)
00:24:18 34 New Jeans - Hype Boy (Chorus 1) (None)
00:25:15 35 Kep1er - Back to the City (Chorus 1) (None)
00:25:52 36 KNK - Knock (Chorus 1) (None)
00:26:31 37 Enhypen - Still Monster (Chorus 1) (None)
00:27:13 38 NMIXX - Soñar (Breaker) (Chorus 1) (None)
00:27:45 39 Taemin - Guilty (Pre-Chorus 1) (None)
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
    