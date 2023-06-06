import math

startTime = "01:52:06"
startTimeSplit = startTime.split(":")
startTimeInSeconds = 0
startTimeInSeconds += int(startTimeSplit[0]) * 60 * 60
startTimeInSeconds += int(startTimeSplit[1]) * 60
startTimeInSeconds += int(startTimeSplit[2])

raw = """
00:00:03 1 mave - pandora (Chorus 1) (None)
00:00:49 2 enhypen - giventaken (Chorus 1) (Red)
00:01:39 3 bts - on (Chorus 1) (None)
00:02:10 4 superm - 100 (Chorus 1) (None)
00:02:40 5 monstax - alligator (Pre-Chorus 1) (None)
00:03:26 6 billlie - gingamingayo (Pre-Chorus 1) (None)
00:04:06 7 twice - gohard (Chorus 1) (None)
00:04:37 8 aespa - spicy (Chorus 1) (None)
00:05:23 9 tribe - doomdoomta (Chorus 1) (None)
00:06:05 10 itzy - wannabe (Pre-Chorus 1, Chorus 1) (None)
00:06:59 11 dreamcatcher - youandi (Chorus 1) (None)
00:07:45 12 newjeans - attention (Chorus 1) (None)
00:08:18 13 twice - icantstopme (Chorus 1) (None)
00:09:10 14 lesserafim - impurities (Chorus 1) (None)
00:09:45 15 4minute - crazy (Chorus 1) (None)
00:10:22 16 fromis9 - fun (Chorus 2) (None)
00:11:08 17 lisa - lalisa (Chorus 1) (None)
00:11:45 18 pixy - wings (Pre-Chorus 1) (None)
00:13:04 19 jyp - fever (Chorus 1) (None)
00:13:38 20 blackpink - pinkvenom (Chorus 1) (None)
00:14:18 21 mamamoo - illella (Chorus 1) (None)
00:15:03 22 straykids - boxer (Chorus 1) (None)
00:15:55 23 kep1er - backtothecity (Chorus 1) (None)
00:16:31 24 imfact - thelight (Pre-Chorus 1) (None)
00:17:19 25 9muses - hurtlocker (Chorus 1) (None)
00:17:48 26 boysplanet - engarde (Chorus 1) (None)
00:18:30 27 gidle - tomboy (Pre-Chorus 1, Chorus 1) (None)
00:19:16 28 alexa - bomb (Pre-Chorus 1) (None)
00:20:08 29 redvelvet - naughty (Pre-Chorus 1) (None)
00:20:55 30 ateez - guerilla (Chorus 1) (Red)
00:21:45 31 txt - sugarrushride (Chorus 1) (Blue)
00:22:31 32 twice - harehare (Chorus 1) (None)
00:23:01 33 oneus - nodiggity (Pre-Chorus 1) (None)
00:24:03 34 bss - fighting (Chorus 1) (None)
00:24:43 35 loona - ptt (Pre-Chorus 1) (None)
00:25:27 36 straykids - cantstop (Chorus 3) (None)
00:26:26 37 ive - lovedive (Pre-Chorus 1, Chorus 1) (None)
00:27:25 38 kard - redmoon (Chorus 1) (None)
00:28:20 39 dreamnote - lemonade (Chorus 1) (None)
00:29:11 40 bts - idol (Chorus 1) (Blue)
00:29:54 41 seventeen - sonogong (Chorus 1) (None)
00:30:34 42 mcnd - mood (Chorus 1) (None)
00:31:11 43 kep1er - giddy (Pre-Chorus 1) (None)
00:31:54 44 cravity - cloud9 (Chorus 1) (None)
00:32:40 45 straykids - backdoor (Chorus 1) (None)
00:33:13 46 exo - loveshot (Chorus 1) (None)
00:34:03 47 dkz - uhheung (Dancebreak) (None)
00:34:47 48 xg - leftright (Chorus 1) (None)
00:35:27 49 psy - thatthat (Pre-Chorus 1, Chorus 1) (None)
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
    