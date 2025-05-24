import tkinter as tk
from tkinter import ttk
import xml.etree.ElementTree as ET
import xml.dom.minidom
import os

# Define your system data as a list of dictionaries
systems = [
    {"fullname": "3DO Interactive Multiplayer", "name": "3do", "manufacturer": "Panasonic", "hardwareType": "Console", "releaseYear": "1993", "systemsortname": ""},
    {"fullname": "Acorn Archimedes", "name": "archimedes", "manufacturer": "Acorn", "hardwareType": "Computer", "releaseYear": "1987", "systemsortname": ""},
    {"fullname": "Acorn Computers BBC Micro", "name": "bbcmicro", "manufacturer": "Acorn Computers", "hardwareType": "Computer", "releaseYear": "1981", "systemsortname": ""},
    {"fullname": "Acorn Electron", "name": "electron", "manufacturer": "Acorn", "hardwareType": "Computer", "releaseYear": "1983", "systemsortname": ""},
    {"fullname": "Adobe Flash", "name": "flash", "manufacturer": "Adobe", "hardwareType": "Engine", "releaseYear": "1996", "systemsortname": ""},
    {"fullname": "AdvanceMAME", "name": "mame-advmame", "manufacturer": "AdvanceMAME", "hardwareType": "Emulator", "releaseYear": "1998", "systemsortname": ""},
    {"fullname": "Adventure Game Studio Game Engine", "name": "ags", "manufacturer": "Chris Jones", "hardwareType": "Engine", "releaseYear": "1997", "systemsortname": ""},
    {"fullname": "Amstrad CPC", "name": "amstradcpc", "manufacturer": "Amstrad", "hardwareType": "Computer", "releaseYear": "1984", "systemsortname": ""},
    {"fullname": "Amstrad GX4000", "name": "gx4000", "manufacturer": "Amstrad", "hardwareType": "Console", "releaseYear": "1990", "systemsortname": ""},
    {"fullname": "Android Apps", "name": "androidapps", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000", "systemsortname": ""},
    {"fullname": "Android Games", "name": "androidgames", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000", "systemsortname": ""},
    {"fullname": "Apple II", "name": "apple2", "manufacturer": "Apple", "hardwareType": "Computer", "releaseYear": "1977", "systemsortname": ""},
    {"fullname": "Apple IIGS", "name": "apple2gs", "manufacturer": "Apple", "hardwareType": "Computer", "releaseYear": "1986", "systemsortname": ""},
    {"fullname": "Apple Macintosh", "name": "macintosh", "manufacturer": "Apple", "hardwareType": "Computer", "releaseYear": "1984", "systemsortname": ""},
    {"fullname": "Arcade", "name": "arcade", "manufacturer": "Arcade", "hardwareType": "Arcade", "releaseYear": "0000", "systemsortname": ""},
    {"fullname": "Arduboy Miniature Game System", "name": "arduboy", "manufacturer": "Kevin Bates", "hardwareType": "Portable", "releaseYear": "2015", "systemsortname": ""},
    {"fullname": "Atari 2600", "name": "atari2600", "manufacturer": "Atari", "hardwareType": "Console", "releaseYear": "1977", "systemsortname": ""},
    {"fullname": "Atari 5200", "name": "atari5200", "manufacturer": "Atari", "hardwareType": "Console", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "Atari 7800 ProSystem", "name": "atari7800", "manufacturer": "Atari", "hardwareType": "Console", "releaseYear": "1986", "systemsortname": ""},
    {"fullname": "Atari 800", "name": "atari800", "manufacturer": "Atari", "hardwareType": "Computer", "releaseYear": "1979", "systemsortname": ""},
    {"fullname": "Atari Jaguar", "name": "atarijaguar", "manufacturer": "Atari", "hardwareType": "Console", "releaseYear": "1993", "systemsortname": ""},
    {"fullname": "Atari Jaguar CD", "name": "atarijaguarcd", "manufacturer": "Atari", "hardwareType": "Console", "releaseYear": "1995", "systemsortname": ""},
    {"fullname": "Atari Lynx", "name": "atarilynx", "manufacturer": "Atari", "hardwareType": "Portable", "releaseYear": "1989", "systemsortname": ""},
    {"fullname": "Atari ST", "name": "atarist", "manufacturer": "Atari", "hardwareType": "Computer", "releaseYear": "1985", "systemsortname": ""},
    {"fullname": "Atari XE", "name": "atarixe", "manufacturer": "Atari", "hardwareType": "Computer", "releaseYear": "1987", "systemsortname": ""},
    {"fullname": "Bally Astrocade", "name": "astrocade", "manufacturer": "Bally", "hardwareType": "Console", "releaseYear": "1977", "systemsortname": ""},
    {"fullname": "Bandai SuFami Turbo", "name": "sufami", "manufacturer": "Bandai", "hardwareType": "Peripheral", "releaseYear": "1996", "systemsortname": ""},
    {"fullname": "Bandai WonderSwan", "name": "wonderswan", "manufacturer": "Bandai", "hardwareType": "Portable", "releaseYear": "1999", "systemsortname": ""},
    {"fullname": "Bandai WonderSwan Color", "name": "wonderswancolor", "manufacturer": "Bandai", "hardwareType": "Portable", "releaseYear": "2000", "systemsortname": ""},
    {"fullname": "Capcom Play System", "name": "cps", "manufacturer": "Capcom", "hardwareType": "Arcade", "releaseYear": "1988", "systemsortname": ""},
    {"fullname": "Capcom Play System I", "name": "cps1", "manufacturer": "Capcom", "hardwareType": "Arcade", "releaseYear": "1988", "systemsortname": ""},
    {"fullname": "Capcom Play System II", "name": "cps2", "manufacturer": "Capcom", "hardwareType": "Arcade", "releaseYear": "1993", "systemsortname": ""},
    {"fullname": "Capcom Play System III", "name": "cps3", "manufacturer": "Capcom", "hardwareType": "Arcade", "releaseYear": "1996", "systemsortname": ""},
    {"fullname": "Casio PV-1000", "name": "pv1000", "manufacturer": "Casio", "hardwareType": "Console", "releaseYear": "1983", "systemsortname": ""},
    {"fullname": "ChaiLove Game Engine", "name": "chailove", "manufacturer": "ChaiLove Team", "hardwareType": "Engine", "releaseYear": "2017", "systemsortname": ""},
    {"fullname": "Coleco Adam", "name": "adam", "manufacturer": "Coleco", "hardwareType": "Computer", "releaseYear": "1983", "systemsortname": ""},
    {"fullname": "Coleco ColecoVision", "name": "colecovision", "manufacturer": "Coleco", "hardwareType": "Console", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "Commodore 64", "name": "c64", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "Commodore Amiga", "name": "amiga", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1985", "systemsortname": ""},
    {"fullname": "Commodore Amiga 1200", "name": "amiga1200", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1985", "systemsortname": ""},
    {"fullname": "Commodore Amiga 600", "name": "amiga600", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1985", "systemsortname": ""},
    {"fullname": "Commodore Amiga CD32", "name": "amigacd32", "manufacturer": "Commodore", "hardwareType": "Console", "releaseYear": "1993", "systemsortname": ""},
    {"fullname": "Commodore CDTV", "name": "cdtv", "manufacturer": "Commodore", "hardwareType": "Console", "releaseYear": "1991", "systemsortname": ""},
    {"fullname": "Commodore Plus/4", "name": "plus4", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1984", "systemsortname": ""},
    {"fullname": "Commodore VIC-20", "name": "vic20", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1980", "systemsortname": ""},
    {"fullname": "Console Arcade Games", "name": "consolearcade", "manufacturer": "Various", "hardwareType": "Arcade", "releaseYear": "0000", "systemsortname": ""},
    {"fullname": "Creatronic Mega Duck", "name": "megaduck", "manufacturer": "Creatronic", "hardwareType": "Portable", "releaseYear": "1993", "systemsortname": ""},
    {"fullname": "Daphne Arcade LaserDisc Emulator", "name": "daphne", "manufacturer": "Matt Ownby", "hardwareType": "Arcade", "releaseYear": "2007", "systemsortname": ""},
    {"fullname": "Desktop Applications", "name": "desktop", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000", "systemsortname": ""},
    {"fullname": "Doom", "name": "doom", "manufacturer": "id Software", "hardwareType": "Engine", "releaseYear": "1993", "systemsortname": ""},
    {"fullname": "DOS (PC)", "name": "dos", "manufacturer": "Microsoft", "hardwareType": "OS", "releaseYear": "1981", "systemsortname": ""},
    {"fullname": "Dragon Data Dragon 32", "name": "dragon32", "manufacturer": "Dragon Data, Ltd.", "hardwareType": "Computer", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "EasyRPG Game Engine", "name": "easyrpg", "manufacturer": "EasyRPG Team", "hardwareType": "Engine", "releaseYear": "2007", "systemsortname": ""},
    {"fullname": "Emerson Arcadia 2001", "name": "arcadia", "manufacturer": "Emerson", "hardwareType": "Console", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "Emulators", "name": "emulators", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000", "systemsortname": ""},
    {"fullname": "Epic Games Store", "name": "epic", "manufacturer": "Epic", "hardwareType": "Collection", "releaseYear": "2018", "systemsortname": ""},
    {"fullname": "Fairchild Channel F", "name": "channelf", "manufacturer": "Fairchild", "hardwareType": "Console", "releaseYear": "1976", "systemsortname": ""},
    {"fullname": "FinalBurn Alpha", "name": "fba", "manufacturer": "Arcade", "hardwareType": "Arcade", "releaseYear": "2000", "systemsortname": ""},
    {"fullname": "FinalBurn Neo", "name": "fbneo", "manufacturer": "Arcade", "hardwareType": "Arcade", "releaseYear": "2002", "systemsortname": ""},
    {"fullname": "FM-7", "name": "fm7", "manufacturer": "Fujitsu", "hardwareType": "Computer", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "Fujitsu FM Towns", "name": "fmtowns", "manufacturer": "Fujitsu", "hardwareType": "Console", "releaseYear": "1993", "systemsortname": ""},
    {"fullname": "Future Pinball", "name": "fpinball", "manufacturer": "Christopher Leathley", "hardwareType": "Engine", "releaseYear": "2005", "systemsortname": ""},
    {"fullname": "Gamate", "name": "gamate", "manufacturer": "Bit Corporation", "hardwareType": "Portable", "releaseYear": "1990", "systemsortname": ""},
    {"fullname": "Game Master", "name": "gmaster", "manufacturer": "Hartung", "hardwareType": "Portable", "releaseYear": "1990", "systemsortname": ""},
    {"fullname": "Google Android", "name": "android", "manufacturer": "Google", "hardwareType": "OS", "releaseYear": "2008", "systemsortname": ""},
    {"fullname": "IBM PC", "name": "pc", "manufacturer": "IBM", "hardwareType": "Computer", "releaseYear": "1981", "systemsortname": ""},
    {"fullname": "Infocom Z-machine", "name": "zmachine", "manufacturer": "Infocom", "hardwareType": "Engine", "releaseYear": "1979", "systemsortname": ""},
    {"fullname": "Java 2 Micro Edition (J2ME)", "name": "j2me", "manufacturer": "Oracle", "hardwareType": "OS", "releaseYear": "1998", "systemsortname": ""},
    {"fullname": "Kodi Home Theatre Software", "name": "kodi", "manufacturer": "XBMC Foundation", "hardwareType": "Collection", "releaseYear": "2007", "systemsortname": ""},
    {"fullname": "LaserDisc Games", "name": "laserdisc", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000", "systemsortname": ""},
    {"fullname": "LCD Handheld Games", "name": "lcdgames", "manufacturer": "Various", "hardwareType": "Portable", "releaseYear": "0000", "systemsortname": ""},
    {"fullname": "LowRes NX", "name": "lowresnx", "manufacturer": "Timo Kloss", "hardwareType": "Engine", "releaseYear": "2017", "systemsortname": ""},
    {"fullname": "Lutris Open Gaming Platform", "name": "lutris", "manufacturer": "Mathieu Comandon", "hardwareType": "Collection", "releaseYear": "2010", "systemsortname": ""},
    {"fullname": "Lutro Game Engine", "name": "lutro", "manufacturer": "libretro", "hardwareType": "Engine", "releaseYear": "2015", "systemsortname": ""},
    {"fullname": "M.U.G.E.N Game Engine", "name": "mugen", "manufacturer": "Elecbyte", "hardwareType": "Engine", "releaseYear": "1999", "systemsortname": ""},
    {"fullname": "Magnavox Odyssey2", "name": "odyssey2", "manufacturer": "Magnavox", "hardwareType": "Console", "releaseYear": "1978", "systemsortname": ""},
    {"fullname": "Mattel Electronics Intellivision", "name": "intellivision", "manufacturer": "Mattel", "hardwareType": "Console", "releaseYear": "1979", "systemsortname": ""},
    {"fullname": "MGT SAM Coupé", "name": "samcoupe", "manufacturer": "MGT", "hardwareType": "Computer", "releaseYear": "1989", "systemsortname": ""},
    {"fullname": "Microsoft Windows", "name": "windows", "manufacturer": "Microsoft", "hardwareType": "OS", "releaseYear": "1985", "systemsortname": ""},
    {"fullname": "Microsoft Xbox", "name": "xbox", "manufacturer": "Microsoft", "hardwareType": "Console", "releaseYear": "2001", "systemsortname": ""},
    {"fullname": "Microsoft Xbox 360", "name": "xbox360", "manufacturer": "Microsoft", "hardwareType": "Console", "releaseYear": "2005", "systemsortname": ""},
    {"fullname": "Microsoft Xbox One", "name": "xboxone", "manufacturer": "Microsoft", "hardwareType": "Console", "releaseYear": "2013", "systemsortname": ""},
    {"fullname": "MSX", "name": "msx", "manufacturer": "Microsoft", "hardwareType": "Computer", "releaseYear": "1983", "systemsortname": ""},
    {"fullname": "MSX Turbo R", "name": "msxturbor", "manufacturer": "Microsoft", "hardwareType": "Computer", "releaseYear": "1991", "systemsortname": ""},
    {"fullname": "MSX1", "name": "msx1", "manufacturer": "Microsoft", "hardwareType": "Computer", "releaseYear": "1983", "systemsortname": ""},
    {"fullname": "MSX2", "name": "msx2", "manufacturer": "Microsoft", "hardwareType": "Computer", "releaseYear": "1985", "systemsortname": ""},
    {"fullname": "Multi Emulator Super System", "name": "mess", "manufacturer": "MESS Team", "hardwareType": "Emulator", "releaseYear": "1998", "systemsortname": ""},
    {"fullname": "Multiple Arcade Machine Emulator", "name": "mame", "manufacturer": "MAME Team", "hardwareType": "Emulator", "releaseYear": "1997", "systemsortname": ""},
    {"fullname": "Naomi 2", "name": "naomi2", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "2000", "systemsortname": ""},
    {"fullname": "NEC PC Engine", "name": "pcengine", "manufacturer": "NEC", "hardwareType": "Console", "releaseYear": "1987", "systemsortname": ""},
    {"fullname": "NEC PC Engine CD", "name": "pcenginecd", "manufacturer": "NEC", "hardwareType": "Peripheral", "releaseYear": "1988", "systemsortname": ""},
    {"fullname": "NEC PC-8800 Series", "name": "pc88", "manufacturer": "NEC", "hardwareType": "Computer", "releaseYear": "1981", "systemsortname": ""},
    {"fullname": "NEC PC-9800 Series", "name": "pc98", "manufacturer": "NEC", "hardwareType": "Computer", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "NEC PC-FX", "name": "pcfx", "manufacturer": "NEC", "hardwareType": "Console", "releaseYear": "1994", "systemsortname": ""},
    {"fullname": "NEC SuperGrafx", "name": "supergrafx", "manufacturer": "NEC", "hardwareType": "Console", "releaseYear": "1989", "systemsortname": ""},
    {"fullname": "NEC TurboGrafx-16", "name": "tg16", "manufacturer": "NEC", "hardwareType": "Console", "releaseYear": "1989", "systemsortname": ""},
    {"fullname": "NEC TurboGrafx-CD", "name": "tg-cd", "manufacturer": "NEC", "hardwareType": "Peripheral", "releaseYear": "1989", "systemsortname": ""},
    {"fullname": "N-Gage", "name": "ngage", "manufacturer": "Nokia", "hardwareType": "Portable", "releaseYear": "2003", "systemsortname": ""},
    {"fullname": "Nintendo 3DS", "name": "n3ds", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "2011", "systemsortname": ""},
    {"fullname": "Nintendo 64", "name": "n64", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1996", "systemsortname": ""},
    {"fullname": "Nintendo 64DD", "name": "n64dd", "manufacturer": "Nintendo", "hardwareType": "Peripheral", "releaseYear": "1999", "systemsortname": ""},
    {"fullname": "Nintendo DS", "name": "nds", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "2004", "systemsortname": ""},
    {"fullname": "Nintendo Entertainment System", "name": "nes", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1985", "systemsortname": ""},
    {"fullname": "Nintendo Famicom Disk System", "name": "fds", "manufacturer": "Nintendo", "hardwareType": "Peripheral", "releaseYear": "1986", "systemsortname": ""},
    {"fullname": "Nintendo Family Computer", "name": "famicom", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1983", "systemsortname": ""},
    {"fullname": "Nintendo Game and Watch", "name": "gameandwatch", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "1980", "systemsortname": ""},
    {"fullname": "Nintendo Game Boy", "name": "gb", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "1989", "systemsortname": ""},
    {"fullname": "Nintendo Game Boy Advance", "name": "gba", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "2001", "systemsortname": ""},
    {"fullname": "Nintendo Game Boy Color", "name": "gbc", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "1998", "systemsortname": ""},
    {"fullname": "Nintendo GameCube", "name": "gc", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "2001", "systemsortname": ""},
    {"fullname": "Nintendo Pokémon Mini", "name": "pokemini", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "2001", "systemsortname": ""},
    {"fullname": "Nintendo Satellaview", "name": "satellaview", "manufacturer": "Nintendo", "hardwareType": "Peripheral", "releaseYear": "1995", "systemsortname": ""},
    {"fullname": "Nintendo SFC (Super Famicom)", "name": "sfc", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1990", "systemsortname": ""},
    {"fullname": "Nintendo SNES (Super Nintendo)", "name": "snes", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1992", "systemsortname": ""},
    {"fullname": "Nintendo SNES (Super Nintendo) [North America]", "name": "snesna", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1991", "systemsortname": ""},
    {"fullname": "Nintendo Super Game Boy", "name": "sgb", "manufacturer": "Nintendo", "hardwareType": "Peripheral", "releaseYear": "1994", "systemsortname": ""},
    {"fullname": "Nintendo Switch", "name": "switch", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "2017", "systemsortname": ""},
    {"fullname": "Nintendo Virtual Boy", "name": "virtualboy", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "1995", "systemsortname": ""},
    {"fullname": "Nintendo Wii", "name": "wii", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "2006", "systemsortname": ""},
    {"fullname": "Nintendo Wii U", "name": "wiiu", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "2012", "systemsortname": ""},
    {"fullname": "OpenBOR Game Engine", "name": "openbor", "manufacturer": "Senile Team", "hardwareType": "Engine", "releaseYear": "2003", "systemsortname": ""},
    {"fullname": "Othello Multivision", "name": "multivision", "manufacturer": "Tsukuda Original", "hardwareType": "Console", "releaseYear": "1983", "systemsortname": ""},
    {"fullname": "Palm OS", "name": "palm", "manufacturer": "Palm", "hardwareType": "OS", "releaseYear": "1997", "systemsortname": ""},
    {"fullname": "PC Arcade Games", "name": "pcarcade", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000", "systemsortname": ""},
    {"fullname": "Philips CD-i", "name": "cdimono1", "manufacturer": "Philips", "hardwareType": "Console", "releaseYear": "1991", "systemsortname": ""},
    {"fullname": "Philips Videopac G7000", "name": "videopac", "manufacturer": "Philips", "hardwareType": "Console", "releaseYear": "1978", "systemsortname": ""},
    {"fullname": "PICO-8 Fantasy Console", "name": "pico8", "manufacturer": "Lexaloffle", "hardwareType": "Engine", "releaseYear": "2015", "systemsortname": ""},
    {"fullname": "Ports", "name": "ports", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000", "systemsortname": ""},
    {"fullname": "Quake", "name": "quake", "manufacturer": "id Software", "hardwareType": "Engine", "releaseYear": "1996", "systemsortname": ""},
    {"fullname": "Sammy Corporation Atomiswave", "name": "atomiswave", "manufacturer": "Sammy", "hardwareType": "Arcade", "releaseYear": "2003", "systemsortname": ""},
    {"fullname": "ScummVM Game Engine", "name": "scummvm", "manufacturer": "ScummVM", "hardwareType": "Engine", "releaseYear": "2001", "systemsortname": ""},
    {"fullname": "Sega CD", "name": "segacd", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1992", "systemsortname": ""},
    {"fullname": "Sega Dreamcast", "name": "dreamcast", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1998", "systemsortname": ""},
    {"fullname": "Sega Game Gear", "name": "gamegear", "manufacturer": "Sega", "hardwareType": "Portable", "releaseYear": "1990", "systemsortname": ""},
    {"fullname": "Sega Genesis", "name": "genesis", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1989", "systemsortname": ""},
    {"fullname": "Sega Genesis 32X [North America]", "name": "sega32xna", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1994", "systemsortname": ""},
    {"fullname": "Sega Mark III", "name": "mark3", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1985", "systemsortname": ""},
    {"fullname": "Sega Master System", "name": "mastersystem", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1986", "systemsortname": ""},
    {"fullname": "Sega Mega Drive", "name": "megadrive", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1990", "systemsortname": ""},
    {"fullname": "Sega Mega Drive [Japan]", "name": "megadrivejp", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1988", "systemsortname": ""},
    {"fullname": "Sega Mega Drive 32X", "name": "sega32x", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1994", "systemsortname": ""},
    {"fullname": "Sega Mega-CD", "name": "megacd", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1993", "systemsortname": ""},
    {"fullname": "Sega Mega-CD [Japan]", "name": "megacdjp", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1991", "systemsortname": ""},
    {"fullname": "Sega Model 2", "name": "model2", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "1993", "systemsortname": ""},
    {"fullname": "Sega Model 3", "name": "model3", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "1996", "systemsortname": ""},
    {"fullname": "Sega NAOMI", "name": "naomi", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "1998", "systemsortname": ""},
    {"fullname": "Sega NAOMI GD-ROM", "name": "naomigd", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "1998", "systemsortname": ""},
    {"fullname": "Sega Saturn", "name": "saturn", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1995", "systemsortname": ""},
    {"fullname": "Sega Saturn [Japan]", "name": "saturnjp", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1994", "systemsortname": ""},
    {"fullname": "Sega SG-1000", "name": "sg-1000", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1983", "systemsortname": ""},
    {"fullname": "Sega Super 32X [Japan]", "name": "sega32xjp", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1994", "systemsortname": ""},
    {"fullname": "Sharp X1", "name": "x1", "manufacturer": "Sharp", "hardwareType": "Computer", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "Sharp X68000", "name": "x68000", "manufacturer": "Sharp", "hardwareType": "Computer", "releaseYear": "1987", "systemsortname": ""},
    {"fullname": "Sinclair ZX Spectrum", "name": "zxspectrum", "manufacturer": "Sinclair", "hardwareType": "Computer", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "Sinclair ZX Spectrum Next", "name": "zxnext", "manufacturer": "Sinclair", "hardwareType": "Computer", "releaseYear": "2017", "systemsortname": ""},
    {"fullname": "Sinclair ZX81", "name": "zx81", "manufacturer": "Sinclair", "hardwareType": "Computer", "releaseYear": "1981", "systemsortname": ""},
    {"fullname": "Smith Engineering Vectrex", "name": "vectrex", "manufacturer": "Smith Engineering", "hardwareType": "Console", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "SNK Neo Geo", "name": "neogeo", "manufacturer": "SNK", "hardwareType": "Console", "releaseYear": "1990", "systemsortname": ""},
    {"fullname": "SNK Neo Geo CD", "name": "neogeocd", "manufacturer": "SNK", "hardwareType": "Console", "releaseYear": "1994", "systemsortname": ""},
    {"fullname": "SNK Neo Geo CD [Japan]", "name": "neogeocdjp", "manufacturer": "SNK", "hardwareType": "Console", "releaseYear": "1994", "systemsortname": ""},
    {"fullname": "SNK Neo Geo Pocket", "name": "ngp", "manufacturer": "SNK", "hardwareType": "Portable", "releaseYear": "1998", "systemsortname": ""},
    {"fullname": "SNK Neo Geo Pocket Color", "name": "ngpc", "manufacturer": "SNK", "hardwareType": "Portable", "releaseYear": "1999", "systemsortname": ""},
    {"fullname": "Solarus Game Engine", "name": "solarus", "manufacturer": "Christopho", "hardwareType": "Engine", "releaseYear": "2021", "systemsortname": ""},
    {"fullname": "Sony PlayStation", "name": "psx", "manufacturer": "Sony", "hardwareType": "Console", "releaseYear": "1994", "systemsortname": ""},
    {"fullname": "Sony PlayStation 2", "name": "ps2", "manufacturer": "Sony", "hardwareType": "Console", "releaseYear": "2000", "systemsortname": ""},
    {"fullname": "Sony PlayStation 3", "name": "ps3", "manufacturer": "Sony", "hardwareType": "Console", "releaseYear": "2006", "systemsortname": ""},
    {"fullname": "Sony PlayStation 4", "name": "ps4", "manufacturer": "Sony", "hardwareType": "Console", "releaseYear": "2013", "systemsortname": ""},
    {"fullname": "Sony PlayStation Portable", "name": "psp", "manufacturer": "Sony", "hardwareType": "Portable", "releaseYear": "2004", "systemsortname": ""},
    {"fullname": "Sony PlayStation Vita", "name": "psvita", "manufacturer": "Sony", "hardwareType": "Portable", "releaseYear": "2011", "systemsortname": ""},
    {"fullname": "Spectravideo", "name": "spectravideo", "manufacturer": "Spectravideo", "hardwareType": "Console", "releaseYear": "1983", "systemsortname": ""},
    {"fullname": "ST-V", "name": "stv", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "1994", "systemsortname": ""},
    {"fullname": "Super A'can", "name": "supracan", "manufacturer": "Funtech", "hardwareType": "Console", "releaseYear": "1995", "systemsortname": ""},
    {"fullname": "Super Cassette Vision", "name": "scv", "manufacturer": "Epoch Co.", "hardwareType": "Console", "releaseYear": "1984", "systemsortname": ""},
    {"fullname": "Symbian", "name": "symbian", "manufacturer": "Symbian Ltd.", "hardwareType": "OS", "releaseYear": "1997", "systemsortname": ""},
    {"fullname": "Taito Type X", "name": "type-x", "manufacturer": "Taito", "hardwareType": "Arcade", "releaseYear": "2004", "systemsortname": ""},
    {"fullname": "Tandy Color Computer", "name": "coco", "manufacturer": "Tandy", "hardwareType": "Computer", "releaseYear": "1984", "systemsortname": ""},
    {"fullname": "Tandy TRS-80", "name": "trs-80", "manufacturer": "Tandy", "hardwareType": "Computer", "releaseYear": "1984", "systemsortname": ""},
    {"fullname": "Tangerine Computer Systems Oric", "name": "oric", "manufacturer": "Tangerine Computer Systems", "hardwareType": "Computer", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "Tano Dragon", "name": "tanodragon", "manufacturer": "Tano", "hardwareType": "Computer", "releaseYear": "1984", "systemsortname": ""},
    {"fullname": "Texas Instruments TI-99", "name": "ti99", "manufacturer": "Texas Instruments", "hardwareType": "Computer", "releaseYear": "1981", "systemsortname": ""},
    {"fullname": "Thomson MO/TO Series", "name": "moto", "manufacturer": "Thomson SA", "hardwareType": "Computer", "releaseYear": "1984", "systemsortname": ""},
    {"fullname": "Thomson TO8", "name": "to8", "manufacturer": "Thomson", "hardwareType": "Computer", "releaseYear": "1986", "systemsortname": ""},
    {"fullname": "TIC-80 Game Engine", "name": "tic80", "manufacturer": "Vadim Grigoruk", "hardwareType": "Engine", "releaseYear": "2017", "systemsortname": ""},
    {"fullname": "Tiger Electronics Game.com", "name": "gamecom", "manufacturer": "Tiger", "hardwareType": "Portable", "releaseYear": "1997", "systemsortname": ""},
    {"fullname": "Triforce Arcade System", "name": "triforce", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "2002", "systemsortname": ""},
    {"fullname": "Uzebox Open Source Console", "name": "uzebox", "manufacturer": "Belogic Software", "hardwareType": "Console", "releaseYear": "2008", "systemsortname": ""},
    {"fullname": "Valve Steam", "name": "steam", "manufacturer": "Valve", "hardwareType": "Collection", "releaseYear": "2003", "systemsortname": ""},
    {"fullname": "Vircon32", "name": "vircon32", "manufacturer": "Carra", "hardwareType": "Engine", "releaseYear": "2021", "systemsortname": ""},
    {"fullname": "Visual Pinball", "name": "vpinball", "manufacturer": "Visual Pinball Team", "hardwareType": "Engine", "releaseYear": "2000", "systemsortname": ""},
    {"fullname": "VTech CreatiVision", "name": "crvision", "manufacturer": "VTech", "hardwareType": "Console", "releaseYear": "1982", "systemsortname": ""},
    {"fullname": "VTech V.Smile", "name": "vsmile", "manufacturer": "VTech", "hardwareType": "Console", "releaseYear": "2004", "systemsortname": ""},
    {"fullname": "WASM-4 Fantasy Console", "name": "wasm4", "manufacturer": "Bruno Garcia", "hardwareType": "Engine", "releaseYear": "2022", "systemsortname": ""},
    {"fullname": "Watara Supervision", "name": "supervision", "manufacturer": "Watara", "hardwareType": "Portable", "releaseYear": "1992", "systemsortname": ""},
    {"fullname": "Windows 3.X", "name": "windows3x", "manufacturer": "Microsoft", "hardwareType": "OS", "releaseYear": "1992", "systemsortname": ""},
	{"fullname": "Windows 9X", "name": "windows9x", "manufacturer": "Microsoft", "hardwareType": "OS", "releaseYear": "1998", "systemsortname": ""},
]

systems_columns = ("fullname", "name", "manufacturer", "hardwareType", "releaseYear", "systemsortname")

# Add empty row for new input
systems.append({col: "" for col in systems_columns})

# Custom collections now only have a name
custom_collections = [
    {"name": ""}
]

root = tk.Tk()
root.title("XMB xml Generator")
root.geometry("1000x700")

# Checkbox variables
auto_all_var = tk.BooleanVar()
auto_fav_var = tk.BooleanVar()
auto_last_var = tk.BooleanVar()
group_custom_var = tk.BooleanVar()

# Folder and file for saving/loading last inputs
SAVE_FOLDER = "theme-customizations"
SAVE_FILE = os.path.join(SAVE_FOLDER, "last_inputs.xml")

# Create notebook (tabs)
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True)

# -------- Input Tab --------
input_frame = ttk.Frame(notebook)
notebook.add(input_frame, text="Input")

checkbox_frame = ttk.Frame(input_frame)
checkbox_frame.pack(fill=tk.X, padx=10, pady=5)

tk.Checkbutton(checkbox_frame, text="Auto - All Games", variable=auto_all_var).pack(side=tk.LEFT, padx=5)
tk.Checkbutton(checkbox_frame, text="Auto - Favorites", variable=auto_fav_var).pack(side=tk.LEFT, padx=5)
tk.Checkbutton(checkbox_frame, text="Auto - Last Played", variable=auto_last_var).pack(side=tk.LEFT, padx=5)
tk.Checkbutton(checkbox_frame, text="Group Custom Collections", variable=group_custom_var).pack(side=tk.LEFT, padx=5)

# Systems Treeview
systems_columns = ("fullname", "name", "manufacturer", "hardwareType", "releaseYear", "systemsortname")
tree_systems = ttk.Treeview(input_frame, columns=systems_columns, show="headings", height=15)
for col in systems_columns:
    tree_systems.heading(col, text=col, command=lambda c=col: sort_treeview_column(tree_systems, c))
    tree_systems.column(col, width=140 if col != "systemsortname" else 200)
tree_systems.pack(fill=tk.X, padx=10, pady=5)

def sort_treeview_column(tree, col, descending=False):
    data = []
    blank_row = None

    for child in tree.get_children():
        row_vals = tree.item(child)["values"]
        if all(v == "" for v in row_vals):  # Identify blank row
            blank_row = row_vals
        else:
            val = tree.set(child, col)
            data.append((val.lower() if isinstance(val, str) else val, row_vals))

    # Sort by selected column, then by fullname
    col_index = tree["columns"].index(col)
    fullname_index = tree["columns"].index("fullname")

    sorted_data = sorted(
        data,
        key=lambda x: (
            x[0],
            x[1][fullname_index].lower() if isinstance(x[1][fullname_index], str) else x[1][fullname_index]
        ),
        reverse=descending
    )

    # Reinsert sorted rows
    children = tree.get_children()
    for i, (_, row_vals) in enumerate(sorted_data):
        tree.item(children[i], values=row_vals)

    # Place blank row last
    if blank_row is not None:
        tree.item(children[-1], values=blank_row)

    # Toggle sort order on next click
    tree.heading(col, command=lambda: sort_treeview_column(tree, col, not descending))

def load_systems():
    tree_systems.delete(*tree_systems.get_children())
    for idx, row in enumerate(systems):
        tree_systems.insert("", "end", iid=str(idx), values=tuple(row[col] for col in systems_columns))

load_systems()

# Custom Collections Header
custom_header = ttk.Label(input_frame, text="Custom Collections", font=("Segoe UI", 12, "bold"))
custom_header.pack(padx=10, pady=(15, 0), anchor="w")

# Custom Collections Treeview
custom_columns = ("name",)
tree_custom = ttk.Treeview(input_frame, columns=custom_columns, show="headings", height=5)
for col in custom_columns:
    tree_custom.heading(col, text=col)
    tree_custom.column(col, width=400)
tree_custom.pack(fill=tk.X, padx=10, pady=10)

def load_custom_collections():
    tree_custom.delete(*tree_custom.get_children())
    for idx, row in enumerate(custom_collections):
        tree_custom.insert("", "end", iid=str(idx), values=(row["name"],))

load_custom_collections()

def start_edit(tree, item_id, column_index):
    bbox = tree.bbox(item_id, f"#{column_index+1}")
    if not bbox:
        return
    x, y, width, height = bbox
    abs_x = tree.winfo_rootx() - root.winfo_rootx() + x
    abs_y = tree.winfo_rooty() - root.winfo_rooty() + y

    value = tree.set(item_id, column=tree["columns"][column_index])
    entry = tk.Entry(root)
    entry.place(x=abs_x, y=abs_y, width=width, height=height)
    entry.insert(0, value)
    entry.focus()

    def save_edit(event=None):
        new_val = entry.get()
        tree.set(item_id, column=tree["columns"][column_index], value=new_val)
        entry.destroy()
        if tree == tree_systems:
            idx = int(item_id)
            systems[idx][tree["columns"][column_index]] = new_val

            # If editing the last row and user entered something non-empty, add new empty row
            if idx == len(systems) - 1 and any(systems[idx][col].strip() for col in systems_columns):
                systems.append({col: "" for col in systems_columns})
                load_systems()
        elif tree == tree_custom:
            custom_collections[int(item_id)]["name"] = new_val
            last_idx = len(custom_collections) - 1
            if int(item_id) == last_idx and custom_collections[last_idx]["name"].strip():
                custom_collections.append({"name": ""})
                load_custom_collections()
        update_output_tab()

    entry.bind("<Return>", save_edit)
    entry.bind("<FocusOut>", save_edit)

def on_double_click_systems(event):
    item_id = tree_systems.identify_row(event.y)
    column = tree_systems.identify_column(event.x)
    if item_id and column:
        col_index = int(column[1:]) - 1
        start_edit(tree_systems, item_id, col_index)

tree_systems.bind("<Double-1>", on_double_click_systems)

def on_double_click_custom(event):
    item_id = tree_custom.identify_row(event.y)
    column = tree_custom.identify_column(event.x)
    if item_id:
        col_index = int(column[1:]) - 1
        start_edit(tree_custom, item_id, col_index)

tree_custom.bind("<Double-1>", on_double_click_custom)

# -------- Output Tab --------
output_frame = ttk.Frame(notebook)
notebook.add(output_frame, text="Output")

checkbox_frame_out = ttk.Frame(output_frame)
checkbox_frame_out.pack(fill=tk.X, padx=10, pady=5)

tk.Checkbutton(checkbox_frame_out, text="Auto - All Games", variable=auto_all_var).pack(side=tk.LEFT, padx=5)
tk.Checkbutton(checkbox_frame_out, text="Auto - Favorites", variable=auto_fav_var).pack(side=tk.LEFT, padx=5)
tk.Checkbutton(checkbox_frame_out, text="Auto - Last Played", variable=auto_last_var).pack(side=tk.LEFT, padx=5)
tk.Checkbutton(checkbox_frame_out, text="Group Custom Collections", variable=group_custom_var).pack(side=tk.LEFT, padx=5)

output_columns = ("name", "systemsortname")
tree_output = ttk.Treeview(output_frame, columns=output_columns, show="headings")
for col in output_columns:
    tree_output.heading(col, text=col)
    tree_output.column(col, width=200)
tree_output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

def update_output_tab():
    tree_output.delete(*tree_output.get_children())

    # Add systems with valid systemsortname
    filtered_systems = sorted(
        [s for s in systems if s["systemsortname"].strip()],
        key=lambda x: x["systemsortname"].lower()
    )
    for s in filtered_systems:
        tree_output.insert("", "end", values=(s["name"], s["systemsortname"]))

    # Custom collections - sorted by name
    filtered_custom = sorted([c for c in custom_collections if c["name"].strip()], key=lambda c: c["name"].lower())
    if group_custom_var.get():
        tree_output.insert("", "end", values=("custom-collections", "custom-collection"))
    else:
        for c in filtered_custom:
            tree_output.insert("", "end", values=(c["name"], f"custom-{c['name']}"))

    # Auto entries
    if auto_all_var.get():
        tree_output.insert("", "end", values=("auto-allgames", "auto-collection"))
    if auto_fav_var.get():
        tree_output.insert("", "end", values=("auto-favorites", "auto-collection"))
    if auto_last_var.get():
        tree_output.insert("", "end", values=("auto-lastplayed", "auto-collection"))

def export_to_xml():
    folder_name = SAVE_FOLDER
    carousel_folder = os.path.join(folder_name, "gamelist-carousel")
    os.makedirs(folder_name, exist_ok=True)
    os.makedirs(carousel_folder, exist_ok=True)

    root_elem = ET.Element("systemList")

    output_names = []

    # Add systems with valid systemsortname
    filtered_systems = sorted(
        [s for s in systems if s["systemsortname"].strip()],
        key=lambda x: x["systemsortname"].lower()
    )
    for s in filtered_systems:
        output_names.append(s["name"])

    # Custom collections sorted by name
    filtered_custom = sorted([c for c in custom_collections if c["name"].strip()], key=lambda c: c["name"].lower())
    if group_custom_var.get():
        output_names.append("custom-collections")
    else:
        for c in filtered_custom:
            output_names.append(c["name"])

    # Auto entries
    if auto_all_var.get():
        output_names.append("auto-allgames")
    if auto_fav_var.get():
        output_names.append("auto-favorites")
    if auto_last_var.get():
        output_names.append("auto-lastplayed")

    # Build root XML excluding auto and custom collections as before
    for name in output_names:
        if name == "custom-collections":
            continue
        if name in ("auto-allgames", "auto-favorites", "auto-lastplayed"):
            continue
        if any(c["name"] == name for c in custom_collections):
            continue

        sortname = ""
        for s in systems:
            if s["name"] == name:
                sortname = s["systemsortname"]
                break

        if not sortname:
            sortname = ""

        if sortname.isdigit():
            sortname = sortname.zfill(len(sortname))

        system_elem = ET.SubElement(root_elem, "system")
        ET.SubElement(system_elem, "name").text = name
        ET.SubElement(system_elem, "systemsortname").text = sortname

    rough_string = ET.tostring(root_elem, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="    ")

    file_path = os.path.join(folder_name, "es_systems_sorting.xml")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

    n = len(output_names)

    def get_wrapped(idx):
        return output_names[idx % n]

    for i, current_name in enumerate(output_names):
        theme = ET.Element("theme")
        variables = ET.SubElement(theme, "variables")

        ET.SubElement(variables, "systemMinus2").text = get_wrapped(i - 2)
        ET.SubElement(variables, "systemMinus1").text = get_wrapped(i - 1)
        ET.SubElement(variables, "systemPlus1").text = get_wrapped(i + 1)
        ET.SubElement(variables, "systemPlus2").text = get_wrapped(i + 2)
        ET.SubElement(variables, "systemPlus3").text = get_wrapped(i + 3)
        ET.SubElement(variables, "systemPlus4").text = get_wrapped(i + 4)
        ET.SubElement(variables, "systemPlus5").text = get_wrapped(i + 5)
        ET.SubElement(variables, "systemPlus6").text = get_wrapped(i + 6)
        ET.SubElement(variables, "systemPlus7").text = get_wrapped(i + 7)

        rough_xml = ET.tostring(theme, 'utf-8')
        pretty_xml = xml.dom.minidom.parseString(rough_xml).toprettyxml(indent="    ")

        out_file = os.path.join(carousel_folder, f"{current_name}.xml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(pretty_xml)

    print(f"Export complete! Main XML: {file_path} and carousel XMLs in {carousel_folder}")

# Save/load last inputs (systems' systemsortname and custom collections' names)

def save_last_inputs():
    os.makedirs(SAVE_FOLDER, exist_ok=True)
    root_elem = ET.Element("lastInputs")

    systems_elem = ET.SubElement(root_elem, "systems")
    for s in systems:
        s_elem = ET.SubElement(systems_elem, "system")
        ET.SubElement(s_elem, "fullname").text = s.get("fullname", "")
        ET.SubElement(s_elem, "name").text = s["name"]
        ET.SubElement(s_elem, "manufacturer").text = s.get("manufacturer", "")
        ET.SubElement(s_elem, "hardwareType").text = s.get("hardwareType", "")
        ET.SubElement(s_elem, "releaseYear").text = s.get("releaseYear", "")
        ET.SubElement(s_elem, "systemsortname").text = s["systemsortname"]

    custom_elem = ET.SubElement(root_elem, "customCollections")
    for c in custom_collections:
        ET.SubElement(custom_elem, "collection").text = c["name"]

    ET.SubElement(root_elem, "autoAll").text = str(auto_all_var.get())
    ET.SubElement(root_elem, "autoFav").text = str(auto_fav_var.get())
    ET.SubElement(root_elem, "autoLast").text = str(auto_last_var.get())
    ET.SubElement(root_elem, "groupCustom").text = str(group_custom_var.get())

    rough_string = ET.tostring(root_elem, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="    ")

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

def load_last_inputs():
    if not os.path.exists(SAVE_FILE):
        return
    try:
        tree = ET.parse(SAVE_FILE)
        root_elem = tree.getroot()

        # Load systems - replace entire list
        systems_elem = root_elem.find("systems")
        if systems_elem is not None:
            systems.clear()
            for s_elem in systems_elem.findall("system"):
                systems.append({
                    "fullname": s_elem.findtext("fullname", default=""),
                    "name": s_elem.findtext("name", default=""),
                    "manufacturer": s_elem.findtext("manufacturer", default=""),
                    "hardwareType": s_elem.findtext("hardwareType", default=""),
                    "releaseYear": s_elem.findtext("releaseYear", default=""),
                    "systemsortname": s_elem.findtext("systemsortname", default=""),
                })
            # Always add empty row at end for new input
            if not systems or any(systems[-1][col].strip() for col in systems_columns):
                systems.append({col: "" for col in systems_columns})

        # Load custom collections
        custom_elem = root_elem.find("customCollections")
        if custom_elem is not None:
            custom_collections.clear()
            for c_elem in custom_elem.findall("collection"):
                name = c_elem.text or ""
                custom_collections.append({"name": name})
            # Ensure there is always one empty row at the end
            if not custom_collections or custom_collections[-1]["name"].strip():
                custom_collections.append({"name": ""})

        # Load checkboxes
        auto_all_var.set(root_elem.findtext("autoAll") == "True")
        auto_fav_var.set(root_elem.findtext("autoFav") == "True")
        auto_last_var.set(root_elem.findtext("autoLast") == "True")
        group_custom_var.set(root_elem.findtext("groupCustom") == "True")

    except Exception as e:
        print("Error loading last inputs:", e)

def on_closing():
    save_last_inputs()
    root.destroy()

# Bind checkbox changes to update output tab
def bind_checkbox_updates():
    for var in (auto_all_var, auto_fav_var, auto_last_var, group_custom_var):
        var.trace_add("write", lambda *args: update_output_tab())

bind_checkbox_updates()

load_last_inputs()
load_systems()
load_custom_collections()
update_output_tab()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Export button
export_button = ttk.Button(output_frame, text="Export XML", command=export_to_xml)
export_button.pack(pady=5)

root.mainloop()
