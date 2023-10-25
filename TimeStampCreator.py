import math

startTime = "01:34:15"
startTimeSplit = startTime.split(":")
startTimeInSeconds = 0
startTimeInSeconds += int(startTimeSplit[0]) * 60 * 60
startTimeInSeconds += int(startTimeSplit[1]) * 60
startTimeInSeconds += int(startTimeSplit[2])

raw = """
00:00:03 1 GFRIEND - Rough (Pre-Chorus 1) (None)
00:00:49 2 Monsta X - Alligator (Chorus 1) (None)
00:01:39 3 Block B - Nillili Mambo (Chorus 1) (None)
00:02:30 4 IzOne - La vie en rose (Pre-Chorus 1, Chorus 1) (None)
00:03:16 5 Stray kids - Domino (Chorus 1) (None)
00:03:59 6 Jhope ft. Becky G - Chicken noodle soup (Chorus 1) (None)
00:04:35 7 Red Velvet - Ice Cream Cake (Chorus 1) (None)
00:05:17 8 The Boyz - Maverick (Chorus 1) (None)
00:06:16 9 RIIZE - Siren (Chorus 1) (None)
00:06:51 10 Jun Seventeen - Psycho (Chorus 1) (None)
00:07:27 11 tripleS - Girls’ Capitalism (Chorus 1) (None)
00:08:15 12 NCT U - The 7th Sense (Pre-Chorus 1) (None)
00:09:06 13 BIBI - Law (Beginning) (None)
00:09:56 14 Itzy - Wannabe (Pre-Chorus 1, Chorus 1) (None)
00:10:50 15 Bts - Silver Spoon (Pre-Chorus 1) (None)
00:11:51 16 Enhypen - Bite Me (Chorus 1) (None)
00:12:25 17 Le Sserafim - Blue Flame (Chorus 1) (None)
00:13:19 18 TAN - DU DU DU (Pre-Chorus 2) (None)
00:14:18 19 XIKERS - XIKEY (Chorus 1) (None)
00:14:53 20 Exo - Growl (Chorus 1) (None)
00:15:31 21 ToppDogg - TOPDOG (Chorus 1) (None)
00:16:14 22 VIXX - Voodoo Doll (Pre-Chorus 1) (None)
00:16:49 23 Twice - Go Hard (Chorus 1) (None)
00:17:28 24 Lee Chaeyeon - Knock (Dancebreak) (None)
00:18:15 25 Momoland - Bboom Bboom (Pre-Chorus 1, Chorus 1) (None)
00:19:07 26 MissA - Only you (Chorus 1) (None)
00:20:01 27 Hwasa - I love my body (Chorus 1) (None)
00:20:30 28 Girls generation - The boys (Chorus 1) (None)
00:21:04 29 Psy - New face (Pre-Chorus 1) (None)
00:21:46 30 2NE1 - Come back home (Chorus 1) (None)
00:22:55 31 Seventeen - Very nice (Chorus 1) (None)
00:23:32 32 Atbo - Monochrome (Pre-Chorus 1) (None)
00:24:43 33 Twice - Like Ooh Ahh (Dancebreak) (None)
00:25:19 34 Dreamcatcher - Bon Voyage (Chorus 1) (None)
00:26:01 35 Arin & Soobin - Dolphin (Chorus 1) (None)
00:26:38 36 ACE - Goblin (Pre-Chorus 1) (None)
00:27:34 37 Ateez - Bouncy (Chorus 1) (None)
00:28:20 38 Hyuna - Bubble pop! (Chorus 1) (None)
00:29:16 39 Bts - Save me (Chorus 1) (None)
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
    