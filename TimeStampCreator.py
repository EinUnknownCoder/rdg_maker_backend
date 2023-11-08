import math

startTime = "00:00:-34"
startTimeSplit = startTime.split(":")
startTimeInSeconds = 0
startTimeInSeconds += int(startTimeSplit[0]) * 60 * 60
startTimeInSeconds += int(startTimeSplit[1]) * 60
startTimeInSeconds += int(startTimeSplit[2])

raw = """
00:33:06 NCT - Kick it
00:33:43 Sf9 - puzzle
00:34:33 nmixx - dice
00:35:48 Kang Daniel - Paranoia
00:36:36 Gfriend - Apple
00:37:24 Loona - Paint the town
00:38:13 Pristin - Black widow
00:38:54 purple kiss - Zombie
00:39:47 Stray Kids - Venom
00:41:21 Vcha - Y.O Universe
00:42:04 Dreamcatcher - Maison
00:42:37 P1Harmony - Reset
00:43:17 Yena - Whicked love
00:43:57 Hyuna & Dawn - Ping Pong
00:44:39 Chung Ha - Play
00:45:25 Winner - Really Really
00:45:55 Enhypen - Bite me
00:46:50 Pentagon - Feelin Like
00:47:28 ATEEZ - Halazia
00:48:12 Taemin - Advice
00:49:02 BTS - Black Swan
00:49:54 Ateez - Halazia
00:50:45 Blackpink - Kill this love
00:51:53 Aespa - Dreams Come True
00:52:33 Jessi - Cold blooded
00:53:18 XG - New Dance
00:54:08 Troublemaker - Troublemaker
00:55:00 TXT - Chasing that feeling
00:55:39 Jun - Psycho
00:56:21 Pixy - Addicted
00:57:12 Monsta X - Fantasia
00:58:04 Kingdom - Black Crown
00:58:45 IVE - Baddie
00:59:49 Red Velvet - Naughty
01:00:36 Stray Kids - Case 143
01:01:18 Kai - Rover
01:01:59 Pentagon - Dr. BeBe
01:02:41 WayV - Phantom
01:03:26 Enhypen - Future Perfect (Pass the Mic)
01:04:19 Red Velvet - Monster
01:05:07 Wonder girls - Be my Baby
01:05:48 Jennie - You&Me
01:06:24 Bts - On
01:07:55 Le’v - A.I.BAE
01:08:33 Everglow - Dun Dun
01:09:26 AoA - Miniskirt
01:10:16 P1Harmony - Back Down
01:10:55 ATEEZ - Wonderland
01:11:42 Hyuna - I'm not cool
01:12:15 Triple S LOVElution - Girls Capitalism
01:13:02 Dia - Mr. Potter
01:13:43 Sunmi - Tail
01:14:31 Pink Fantasy - Tales of the Unusual
01:15:05 Gidle - Queencard
01:15:50 Blackpink - As if it's your last
01:16:50 Itzy - Ringo
01:17:28 Stayc - Bubble
01:18:14 Nature - Girls
01:19:09 PURPLE KISS - Ponzona
01:20:02 Pixy - Wings
01:21:01 Seventeen - Cheers
01:22:20 Xikers - Koong
01:23:05 Twice - Cry for Me
01:23:47 Dynamic duo - Smoke
01:24:22 Boysplanet - Here I am
01:25:26 AESPA - Better things
01:26:03 Momoland - I'm so Hot
01:26:46 TXT, Annita - Back for more
01:27:24 Stray Kids - Super Bowl
01:28:11 Jihyo -twice - Killing me Good
01:28:53 Red velvet - Psycho
01:29:36 Kep1er - We fresh
01:30:24 NewJeans - Super Shy
01:31:09 EXO - The Eve
01:32:12 PRISTIN V - Get It
01:32:55 Pixy - Bewitched
01:33:52 Twice - The Feels
01:34:30 Pentagon - Humph!
01:35:15 Itzy - Icy
01:35:45 Oneus - Baila Conmigo
01:36:29 The Boyz - No Air
01:37:25 Enhypen - Criminal love
01:38:25 Moonbin & Sanha - Madness
01:39:03 Kard - Icky
01:39:52 Dreamcatcher - Scream
01:40:43 Yooa - Bon Voyage
01:41:47 WJSN - Last Sequence
01:42:37 P1Harmony - Scared
01:43:13 Gidle - Lion
01:44:03 KISS OF LIFE (Natty) - Sugarcoat
01:44:49 Blackpink - Kill this Love
01:45:21 Hwasa - I love my body
01:45:52 JBJ - Fantasy
01:46:38 ATEEZ - The Black Cat Nero
01:47:27 Straykids - Maniac
01:48:11 XG - Puppet Show
01:48:53 EXO - Monster
01:49:35 baekhyun - candy
01:50:19 Riize - Siren
01:50:52 Purple Kiss - Nerdy
01:51:36 Vixx - On and On
01:52:24 TXT - Frost
01:53:09 Enhypen - Drunk Dazed
01:54:06 Mamamoo - Hip
01:54:46 Shinee - Lucifer
01:55:44 Nct 127 - Fact check
01:56:27 aespa - Illusion
01:57:23 Stray Kids - Gods Menu
01:58:02 Chungha - Stay Tonight
01:58:59 BTS - Fake Love
02:00:13 Jessi - Zoom
02:00:45 Red Velvet - Peek-A-Boo
02:01:35 Jungkook - 3D (feat. Jack Harlow)
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
    