import math

startTime = "01:48:48"
startTimeSplit = startTime.split(":")
startTimeInSeconds = 0
startTimeInSeconds += int(startTimeSplit[0]) * 60 * 60
startTimeInSeconds += int(startTimeSplit[1]) * 60
startTimeInSeconds += int(startTimeSplit[2])

raw = """
00:00:02 1 Kim Samuel - With U (Chorus 2) (None)
00:00:41 2 Twice - Perfect World (Chorus 1) (None)
00:01:22 3 Twice - The Feels (Chorus 1) (None)
00:02:00 4 Pixy - Karma (Chorus 1) (None)
00:02:35 5 Ateez - Inception (Chorus 1) (None)
00:03:27 6 Stray Kids - Double Knot (Pre-Chorus 1) (None)
00:04:20 7 Monbin&Sanha - Who (Chorus 1) (None)
00:04:44 8 Itzy - Icy (Chorus 1) (None)
00:05:13 9 Kingdom - Dystopia (Chorus 1) (None)
00:06:02 10 Stray Kids - Domino (Chorus 1) (None)
00:06:43 11 TriBe - Rub-A-Dum (Pre-Chorus 1) (None)
00:07:35 12 Enhypen - Fever (Pre-Chorus 1, Chorus 1) (None)
00:08:24 13 Crayon Pop - Dancing Queen 2.0 (Chorus 1) (None)
00:09:12 14 BTS - Run BTS (Chorus 1) (None)
00:09:46 15 KARA - When I Move (Chorus 1) (None)
00:10:17 16 Red Velvet - Psycho (Chorus 1) (None)
00:10:55 17 Crush - Rush Hour (Chorus 1) (None)
00:11:35 18 Kard - Without you (Chorus 1) (None)
00:12:08 19 Blackpink - Pink Venom (Chorus 2) (None)
00:12:43 20 NCT - Zoo (Chorus 1) (None)
00:13:11 21 Woo!ah - Rollercoaster (Chorus 2) (None)
00:14:06 22 Le Sserafim - Fearless (Pre-Chorus 1, Chorus 1) (None)
00:14:57 23 aespa - Black Mamba (Chorus 1) (None)
00:15:38 24 Kep1er - Up (Chorus 1) (None)
00:16:23 25 Hyolin - Dally (Pre-Chorus 1) (None)
00:17:09 26 Everglow - First (Chorus 1) (None)
00:17:53 27 Ive - Kitsch (Chorus 1) (None)
00:18:27 28 Craxy - Poison Rose (Pre-Chorus 1) (None)
00:19:27 29 Hyuna - I'm not cool (Chorus 1) (None)
00:19:59 30 Enhypen - Future-Perfect (Chorus 1) (None)
00:20:54 31 Stray Kids - Case 143 (Chorus 1) (None)
00:21:28 32 8Turn - Tic Tac (Chorus 1) (None)
00:22:07 33 Blackpink - Kill This Love (Dancebreak) (None)
00:22:49 34 CLC - No (Chorus 1) (None)
00:23:36 35 BoysPlanet - En Garde (Chorus 1) (None)
00:24:16 36 Itzy - Loco (Pre-Chorus 1, Chorus 1) (None)
00:25:20 37 Billlie - Eunoia (Pre-Chorus 1) (None)
00:26:01 38 NCT - Universe (Chorus 1) (None)
00:26:36 39 Chung Ha - Gotta Go (Chorus 1) (None)
00:27:25 40 StayC - Teddybear (Chorus 1) (None)
00:28:09 41 WJSN - Boogie Up (Chorus 1) (None)
00:28:44 42 Girls Generation - Into the New World (Chorus 1) (None)
00:29:31 43 BoysPlanet - Supercharger (Dancebreak) (None)
00:30:16 44 Nmixx - Love me like this (Chorus 2) (None)
00:30:59 45 Artbeat - Aphrodite (Dancebreak) (None)
00:32:04 46 Seventeen - Hot (Chorus 1) (None)
00:32:53 47 Jisoo - Flower (Chorus 1) (None)
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
    