import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

# Sample data
system_data = [
    {"fullname": "3DO Interactive Multiplayer", "name": "3do", "manufacturer": "Panasonic", "hardwareType": "Console", "releaseYear": "1993"},
    {"fullname": "Acorn Archimedes", "name": "archimedes", "manufacturer": "Acorn", "hardwareType": "Computer", "releaseYear": "1987"},
    {"fullname": "Acorn Computers BBC Micro", "name": "bbcmicro", "manufacturer": "Acorn Computers", "hardwareType": "Computer", "releaseYear": "1981"},
    {"fullname": "Acorn Electron", "name": "electron", "manufacturer": "Acorn", "hardwareType": "Computer", "releaseYear": "1983"},
    {"fullname": "Adobe Flash", "name": "flash", "manufacturer": "Adobe", "hardwareType": "Engine", "releaseYear": "1996"},
    {"fullname": "AdvanceMAME", "name": "mame-advmame", "manufacturer": "AdvanceMAME", "hardwareType": "Emulator", "releaseYear": "1998"},
    {"fullname": "Adventure Game Studio Game Engine", "name": "ags", "manufacturer": "Chris Jones", "hardwareType": "Engine", "releaseYear": "1997"},
    {"fullname": "Amstrad CPC", "name": "amstradcpc", "manufacturer": "Amstrad", "hardwareType": "Computer", "releaseYear": "1984"},
    {"fullname": "Amstrad GX4000", "name": "gx4000", "manufacturer": "Amstrad", "hardwareType": "Console", "releaseYear": "1990"},
    {"fullname": "Android Apps", "name": "androidapps", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000"},
    {"fullname": "Android Games", "name": "androidgames", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000"},
    {"fullname": "Apple II", "name": "apple2", "manufacturer": "Apple", "hardwareType": "Computer", "releaseYear": "1977"},
    {"fullname": "Apple IIGS", "name": "apple2gs", "manufacturer": "Apple", "hardwareType": "Computer", "releaseYear": "1986"},
    {"fullname": "Apple Macintosh", "name": "macintosh", "manufacturer": "Apple", "hardwareType": "Computer", "releaseYear": "1984"},
    {"fullname": "Arcade", "name": "arcade", "manufacturer": "Arcade", "hardwareType": "Arcade", "releaseYear": "0000"},
    {"fullname": "Arduboy Miniature Game System", "name": "arduboy", "manufacturer": "Kevin Bates", "hardwareType": "Portable", "releaseYear": "2015"},
    {"fullname": "Atari 2600", "name": "atari2600", "manufacturer": "Atari", "hardwareType": "Console", "releaseYear": "1977"},
    {"fullname": "Atari 5200", "name": "atari5200", "manufacturer": "Atari", "hardwareType": "Console", "releaseYear": "1982"},
    {"fullname": "Atari 7800 ProSystem", "name": "atari7800", "manufacturer": "Atari", "hardwareType": "Console", "releaseYear": "1986"},
    {"fullname": "Atari 800", "name": "atari800", "manufacturer": "Atari", "hardwareType": "Computer", "releaseYear": "1979"},
    {"fullname": "Atari Jaguar", "name": "atarijaguar", "manufacturer": "Atari", "hardwareType": "Console", "releaseYear": "1993"},
    {"fullname": "Atari Jaguar CD", "name": "atarijaguarcd", "manufacturer": "Atari", "hardwareType": "Console", "releaseYear": "1995"},
    {"fullname": "Atari Lynx", "name": "atarilynx", "manufacturer": "Atari", "hardwareType": "Portable", "releaseYear": "1989"},
    {"fullname": "Atari ST", "name": "atarist", "manufacturer": "Atari", "hardwareType": "Computer", "releaseYear": "1985"},
    {"fullname": "Atari XE", "name": "atarixe", "manufacturer": "Atari", "hardwareType": "Computer", "releaseYear": "1987"},
    {"fullname": "Bally Astrocade", "name": "astrocade", "manufacturer": "Bally", "hardwareType": "Console", "releaseYear": "1977"},
    {"fullname": "Bandai SuFami Turbo", "name": "sufami", "manufacturer": "Bandai", "hardwareType": "Peripheral", "releaseYear": "1996"},
    {"fullname": "Bandai WonderSwan", "name": "wonderswan", "manufacturer": "Bandai", "hardwareType": "Portable", "releaseYear": "1999"},
    {"fullname": "Bandai WonderSwan Color", "name": "wonderswancolor", "manufacturer": "Bandai", "hardwareType": "Portable", "releaseYear": "2000"},
    {"fullname": "Capcom Play System", "name": "cps", "manufacturer": "Capcom", "hardwareType": "Arcade", "releaseYear": "1988"},
    {"fullname": "Capcom Play System I", "name": "cps1", "manufacturer": "Capcom", "hardwareType": "Arcade", "releaseYear": "1988"},
    {"fullname": "Capcom Play System II", "name": "cps2", "manufacturer": "Capcom", "hardwareType": "Arcade", "releaseYear": "1993"},
    {"fullname": "Capcom Play System III", "name": "cps3", "manufacturer": "Capcom", "hardwareType": "Arcade", "releaseYear": "1996"},
    {"fullname": "Casio PV-1000", "name": "pv1000", "manufacturer": "Casio", "hardwareType": "Console", "releaseYear": "1983"},
    {"fullname": "ChaiLove Game Engine", "name": "chailove", "manufacturer": "ChaiLove Team", "hardwareType": "Engine", "releaseYear": "2017"},
    {"fullname": "Coleco Adam", "name": "adam", "manufacturer": "Coleco", "hardwareType": "Computer", "releaseYear": "1983"},
    {"fullname": "Coleco ColecoVision", "name": "colecovision", "manufacturer": "Coleco", "hardwareType": "Console", "releaseYear": "1982"},
    {"fullname": "Commodore 64", "name": "c64", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1982"},
    {"fullname": "Commodore Amiga", "name": "amiga", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1985"},
    {"fullname": "Commodore Amiga 1200", "name": "amiga1200", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1985"},
    {"fullname": "Commodore Amiga 600", "name": "amiga600", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1985"},
    {"fullname": "Commodore Amiga CD32", "name": "amigacd32", "manufacturer": "Commodore", "hardwareType": "Console", "releaseYear": "1993"},
    {"fullname": "Commodore CDTV", "name": "cdtv", "manufacturer": "Commodore", "hardwareType": "Console", "releaseYear": "1991"},
    {"fullname": "Commodore Plus/4", "name": "plus4", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1984"},
    {"fullname": "Commodore VIC-20", "name": "vic20", "manufacturer": "Commodore", "hardwareType": "Computer", "releaseYear": "1980"},
    {"fullname": "Console Arcade Games", "name": "consolearcade", "manufacturer": "Various", "hardwareType": "Arcade", "releaseYear": "0000"},
    {"fullname": "Creatronic Mega Duck", "name": "megaduck", "manufacturer": "Creatronic", "hardwareType": "Portable", "releaseYear": "1993"},
    {"fullname": "Daphne Arcade LaserDisc Emulator", "name": "daphne", "manufacturer": "Matt Ownby", "hardwareType": "Arcade", "releaseYear": "2007"},
    {"fullname": "Desktop Applications", "name": "desktop", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000"},
    {"fullname": "Doom", "name": "doom", "manufacturer": "id Software", "hardwareType": "Engine", "releaseYear": "1993"},
    {"fullname": "DOS (PC)", "name": "dos", "manufacturer": "Microsoft", "hardwareType": "OS", "releaseYear": "1981"},
    {"fullname": "Dragon Data Dragon 32", "name": "dragon32", "manufacturer": "Dragon Data, Ltd.", "hardwareType": "Computer", "releaseYear": "1982"},
    {"fullname": "EasyRPG Game Engine", "name": "easyrpg", "manufacturer": "EasyRPG Team", "hardwareType": "Engine", "releaseYear": "2007"},
    {"fullname": "Emerson Arcadia 2001", "name": "arcadia", "manufacturer": "Emerson", "hardwareType": "Console", "releaseYear": "1982"},
    {"fullname": "Emulators", "name": "emulators", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000"},
    {"fullname": "Epic Games Store", "name": "epic", "manufacturer": "Epic", "hardwareType": "Collection", "releaseYear": "2018"},
    {"fullname": "Fairchild Channel F", "name": "channelf", "manufacturer": "Fairchild", "hardwareType": "Console", "releaseYear": "1976"},
    {"fullname": "FinalBurn Alpha", "name": "fba", "manufacturer": "Arcade", "hardwareType": "Arcade", "releaseYear": "2000"},
    {"fullname": "FinalBurn Neo", "name": "fbneo", "manufacturer": "Arcade", "hardwareType": "Arcade", "releaseYear": "2002"},
    {"fullname": "FM-7", "name": "fm7", "manufacturer": "Fujitsu", "hardwareType": "Computer", "releaseYear": "1982"},
    {"fullname": "Fujitsu FM Towns", "name": "fmtowns", "manufacturer": "Fujitsu", "hardwareType": "Console", "releaseYear": "1993"},
    {"fullname": "Future Pinball", "name": "fpinball", "manufacturer": "Christopher Leathley", "hardwareType": "Engine", "releaseYear": "2005"},
    {"fullname": "Gamate", "name": "gamate", "manufacturer": "Bit Corporation", "hardwareType": "Portable", "releaseYear": "1990"},
    {"fullname": "Game Master", "name": "gmaster", "manufacturer": "Hartung", "hardwareType": "Portable", "releaseYear": "1990"},
    {"fullname": "Google Android", "name": "android", "manufacturer": "Google", "hardwareType": "OS", "releaseYear": "2008"},
    {"fullname": "IBM PC", "name": "pc", "manufacturer": "IBM", "hardwareType": "Computer", "releaseYear": "1981"},
    {"fullname": "Infocom Z-machine", "name": "zmachine", "manufacturer": "Infocom", "hardwareType": "Engine", "releaseYear": "1979"},
    {"fullname": "Java 2 Micro Edition (J2ME)", "name": "j2me", "manufacturer": "Oracle", "hardwareType": "OS", "releaseYear": "1998"},
    {"fullname": "Kodi Home Theatre Software", "name": "kodi", "manufacturer": "XBMC Foundation", "hardwareType": "Collection", "releaseYear": "2007"},
    {"fullname": "LaserDisc Games", "name": "laserdisc", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000"},
    {"fullname": "LCD Handheld Games", "name": "lcdgames", "manufacturer": "Various", "hardwareType": "Portable", "releaseYear": "0000"},
    {"fullname": "LowRes NX", "name": "lowresnx", "manufacturer": "Timo Kloss", "hardwareType": "Engine", "releaseYear": "2017"},
    {"fullname": "Lutris Open Gaming Platform", "name": "lutris", "manufacturer": "Mathieu Comandon", "hardwareType": "Collection", "releaseYear": "2010"},
    {"fullname": "Lutro Game Engine", "name": "lutro", "manufacturer": "libretro", "hardwareType": "Engine", "releaseYear": "2015"},
    {"fullname": "M.U.G.E.N Game Engine", "name": "mugen", "manufacturer": "Elecbyte", "hardwareType": "Engine", "releaseYear": "1999"},
    {"fullname": "Magnavox Odyssey2", "name": "odyssey2", "manufacturer": "Magnavox", "hardwareType": "Console", "releaseYear": "1978"},
    {"fullname": "Mattel Electronics Intellivision", "name": "intellivision", "manufacturer": "Mattel", "hardwareType": "Console", "releaseYear": "1979"},
    {"fullname": "MGT SAM Coupé", "name": "samcoupe", "manufacturer": "MGT", "hardwareType": "Computer", "releaseYear": "1989"},
    {"fullname": "Microsoft Windows", "name": "windows", "manufacturer": "Microsoft", "hardwareType": "OS", "releaseYear": "1985"},
    {"fullname": "Microsoft Xbox", "name": "xbox", "manufacturer": "Microsoft", "hardwareType": "Console", "releaseYear": "2001"},
    {"fullname": "Microsoft Xbox 360", "name": "xbox360", "manufacturer": "Microsoft", "hardwareType": "Console", "releaseYear": "2005"},
    {"fullname": "Microsoft Xbox One", "name": "xboxone", "manufacturer": "Microsoft", "hardwareType": "Console", "releaseYear": "2013"},
    {"fullname": "MSX", "name": "msx", "manufacturer": "Microsoft", "hardwareType": "Computer", "releaseYear": "1983"},
    {"fullname": "MSX Turbo R", "name": "msxturbor", "manufacturer": "Microsoft", "hardwareType": "Computer", "releaseYear": "1991"},
    {"fullname": "MSX1", "name": "msx1", "manufacturer": "Microsoft", "hardwareType": "Computer", "releaseYear": "1983"},
    {"fullname": "MSX2", "name": "msx2", "manufacturer": "Microsoft", "hardwareType": "Computer", "releaseYear": "1985"},
    {"fullname": "Multi Emulator Super System", "name": "mess", "manufacturer": "MESS Team", "hardwareType": "Emulator", "releaseYear": "1998"},
    {"fullname": "Multiple Arcade Machine Emulator", "name": "mame", "manufacturer": "MAME Team", "hardwareType": "Emulator", "releaseYear": "1997"},
    {"fullname": "Naomi 2", "name": "naomi2", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "2000"},
    {"fullname": "NEC PC Engine", "name": "pcengine", "manufacturer": "NEC", "hardwareType": "Console", "releaseYear": "1987"},
    {"fullname": "NEC PC Engine CD", "name": "pcenginecd", "manufacturer": "NEC", "hardwareType": "Peripheral", "releaseYear": "1988"},
    {"fullname": "NEC PC-8800 Series", "name": "pc88", "manufacturer": "NEC", "hardwareType": "Computer", "releaseYear": "1981"},
    {"fullname": "NEC PC-9800 Series", "name": "pc98", "manufacturer": "NEC", "hardwareType": "Computer", "releaseYear": "1982"},
    {"fullname": "NEC PC-FX", "name": "pcfx", "manufacturer": "NEC", "hardwareType": "Console", "releaseYear": "1994"},
    {"fullname": "NEC SuperGrafx", "name": "supergrafx", "manufacturer": "NEC", "hardwareType": "Console", "releaseYear": "1989"},
    {"fullname": "NEC TurboGrafx-16", "name": "tg16", "manufacturer": "NEC", "hardwareType": "Console", "releaseYear": "1989"},
    {"fullname": "NEC TurboGrafx-CD", "name": "tg-cd", "manufacturer": "NEC", "hardwareType": "Peripheral", "releaseYear": "1989"},
    {"fullname": "N-Gage", "name": "ngage", "manufacturer": "Nokia", "hardwareType": "Portable", "releaseYear": "2003"},
    {"fullname": "Nintendo 3DS", "name": "n3ds", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "2011"},
    {"fullname": "Nintendo 64", "name": "n64", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1996"},
    {"fullname": "Nintendo 64DD", "name": "n64dd", "manufacturer": "Nintendo", "hardwareType": "Peripheral", "releaseYear": "1999"},
    {"fullname": "Nintendo DS", "name": "nds", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "2004"},
    {"fullname": "Nintendo Entertainment System", "name": "nes", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1985"},
    {"fullname": "Nintendo Famicom Disk System", "name": "fds", "manufacturer": "Nintendo", "hardwareType": "Peripheral", "releaseYear": "1986"},
    {"fullname": "Nintendo Family Computer", "name": "famicom", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1983"},
    {"fullname": "Nintendo Game and Watch", "name": "gameandwatch", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "1980"},
    {"fullname": "Nintendo Game Boy", "name": "gb", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "1989"},
    {"fullname": "Nintendo Game Boy Advance", "name": "gba", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "2001"},
    {"fullname": "Nintendo Game Boy Color", "name": "gbc", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "1998"},
    {"fullname": "Nintendo GameCube", "name": "gc", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "2001"},
    {"fullname": "Nintendo Pokémon Mini", "name": "pokemini", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "2001"},
    {"fullname": "Nintendo Satellaview", "name": "satellaview", "manufacturer": "Nintendo", "hardwareType": "Peripheral", "releaseYear": "1995"},
    {"fullname": "Nintendo SFC (Super Famicom)", "name": "sfc", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1990"},
    {"fullname": "Nintendo SNES (Super Nintendo)", "name": "snes", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1992"},
    {"fullname": "Nintendo SNES (Super Nintendo) [North America]", "name": "snesna", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "1991"},
    {"fullname": "Nintendo Super Game Boy", "name": "sgb", "manufacturer": "Nintendo", "hardwareType": "Peripheral", "releaseYear": "1994"},
    {"fullname": "Nintendo Switch", "name": "switch", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "2017"},
    {"fullname": "Nintendo Virtual Boy", "name": "virtualboy", "manufacturer": "Nintendo", "hardwareType": "Portable", "releaseYear": "1995"},
    {"fullname": "Nintendo Wii", "name": "wii", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "2006"},
    {"fullname": "Nintendo Wii U", "name": "wiiu", "manufacturer": "Nintendo", "hardwareType": "Console", "releaseYear": "2012"},
    {"fullname": "OpenBOR Game Engine", "name": "openbor", "manufacturer": "Senile Team", "hardwareType": "Engine", "releaseYear": "2003"},
    {"fullname": "Othello Multivision", "name": "multivision", "manufacturer": "Tsukuda Original", "hardwareType": "Console", "releaseYear": "1983"},
    {"fullname": "Palm OS", "name": "palm", "manufacturer": "Palm", "hardwareType": "OS", "releaseYear": "1997"},
    {"fullname": "PC Arcade Games", "name": "pcarcade", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000"},
    {"fullname": "Philips CD-i", "name": "cdimono1", "manufacturer": "Philips", "hardwareType": "Console", "releaseYear": "1991"},
    {"fullname": "Philips Videopac G7000", "name": "videopac", "manufacturer": "Philips", "hardwareType": "Console", "releaseYear": "1978"},
    {"fullname": "PICO-8 Fantasy Console", "name": "pico8", "manufacturer": "Lexaloffle", "hardwareType": "Engine", "releaseYear": "2015"},
    {"fullname": "Ports", "name": "ports", "manufacturer": "Various", "hardwareType": "Collection", "releaseYear": "0000"},
    {"fullname": "Quake", "name": "quake", "manufacturer": "id Software", "hardwareType": "Engine", "releaseYear": "1996"},
    {"fullname": "Sammy Corporation Atomiswave", "name": "atomiswave", "manufacturer": "Sammy", "hardwareType": "Arcade", "releaseYear": "2003"},
    {"fullname": "ScummVM Game Engine", "name": "scummvm", "manufacturer": "ScummVM", "hardwareType": "Engine", "releaseYear": "2001"},
    {"fullname": "Sega CD", "name": "segacd", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1992"},
    {"fullname": "Sega Dreamcast", "name": "dreamcast", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1998"},
    {"fullname": "Sega Game Gear", "name": "gamegear", "manufacturer": "Sega", "hardwareType": "Portable", "releaseYear": "1990"},
    {"fullname": "Sega Genesis", "name": "genesis", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1989"},
    {"fullname": "Sega Genesis 32X [North America]", "name": "sega32xna", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1994"},
    {"fullname": "Sega Mark III", "name": "mark3", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1985"},
    {"fullname": "Sega Master System", "name": "mastersystem", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1986"},
    {"fullname": "Sega Mega Drive", "name": "megadrive", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1990"},
    {"fullname": "Sega Mega Drive [Japan]", "name": "megadrivejp", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1988"},
    {"fullname": "Sega Mega Drive 32X", "name": "sega32x", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1994"},
    {"fullname": "Sega Mega-CD", "name": "megacd", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1993"},
    {"fullname": "Sega Mega-CD [Japan]", "name": "megacdjp", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1991"},
    {"fullname": "Sega Model 2", "name": "model2", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "1993"},
    {"fullname": "Sega Model 3", "name": "model3", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "1996"},
    {"fullname": "Sega NAOMI", "name": "naomi", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "1998"},
    {"fullname": "Sega NAOMI GD-ROM", "name": "naomigd", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "1998"},
    {"fullname": "Sega Saturn", "name": "saturn", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1995"},
    {"fullname": "Sega Saturn [Japan]", "name": "saturnjp", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1994"},
    {"fullname": "Sega SG-1000", "name": "sg-1000", "manufacturer": "Sega", "hardwareType": "Console", "releaseYear": "1983"},
    {"fullname": "Sega Super 32X [Japan]", "name": "sega32xjp", "manufacturer": "Sega", "hardwareType": "Peripheral", "releaseYear": "1994"},
    {"fullname": "Sharp X1", "name": "x1", "manufacturer": "Sharp", "hardwareType": "Computer", "releaseYear": "1982"},
    {"fullname": "Sharp X68000", "name": "x68000", "manufacturer": "Sharp", "hardwareType": "Computer", "releaseYear": "1987"},
    {"fullname": "Sinclair ZX Spectrum", "name": "zxspectrum", "manufacturer": "Sinclair", "hardwareType": "Computer", "releaseYear": "1982"},
    {"fullname": "Sinclair ZX Spectrum Next", "name": "zxnext", "manufacturer": "Sinclair", "hardwareType": "Computer", "releaseYear": "2017"},
    {"fullname": "Sinclair ZX81", "name": "zx81", "manufacturer": "Sinclair", "hardwareType": "Computer", "releaseYear": "1981"},
    {"fullname": "Smith Engineering Vectrex", "name": "vectrex", "manufacturer": "Smith Engineering", "hardwareType": "Console", "releaseYear": "1982"},
    {"fullname": "SNK Neo Geo", "name": "neogeo", "manufacturer": "SNK", "hardwareType": "Console", "releaseYear": "1990"},
    {"fullname": "SNK Neo Geo CD", "name": "neogeocd", "manufacturer": "SNK", "hardwareType": "Console", "releaseYear": "1994"},
    {"fullname": "SNK Neo Geo CD [Japan]", "name": "neogeocdjp", "manufacturer": "SNK", "hardwareType": "Console", "releaseYear": "1994"},
    {"fullname": "SNK Neo Geo Pocket", "name": "ngp", "manufacturer": "SNK", "hardwareType": "Portable", "releaseYear": "1998"},
    {"fullname": "SNK Neo Geo Pocket Color", "name": "ngpc", "manufacturer": "SNK", "hardwareType": "Portable", "releaseYear": "1999"},
    {"fullname": "Solarus Game Engine", "name": "solarus", "manufacturer": "Christopho", "hardwareType": "Engine", "releaseYear": "2021"},
    {"fullname": "Sony PlayStation", "name": "psx", "manufacturer": "Sony", "hardwareType": "Console", "releaseYear": "1994"},
    {"fullname": "Sony PlayStation 2", "name": "ps2", "manufacturer": "Sony", "hardwareType": "Console", "releaseYear": "2000"},
    {"fullname": "Sony PlayStation 3", "name": "ps3", "manufacturer": "Sony", "hardwareType": "Console", "releaseYear": "2006"},
    {"fullname": "Sony PlayStation 4", "name": "ps4", "manufacturer": "Sony", "hardwareType": "Console", "releaseYear": "2013"},
    {"fullname": "Sony PlayStation Portable", "name": "psp", "manufacturer": "Sony", "hardwareType": "Portable", "releaseYear": "2004"},
    {"fullname": "Sony PlayStation Vita", "name": "psvita", "manufacturer": "Sony", "hardwareType": "Portable", "releaseYear": "2011"},
    {"fullname": "Spectravideo", "name": "spectravideo", "manufacturer": "Spectravideo", "hardwareType": "Console", "releaseYear": "1983"},
    {"fullname": "ST-V", "name": "stv", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "1994"},
    {"fullname": "Super A'can", "name": "supracan", "manufacturer": "Funtech", "hardwareType": "Console", "releaseYear": "1995"},
    {"fullname": "Super Cassette Vision", "name": "scv", "manufacturer": "Epoch Co.", "hardwareType": "Console", "releaseYear": "1984"},
    {"fullname": "Symbian", "name": "symbian", "manufacturer": "Symbian Ltd.", "hardwareType": "OS", "releaseYear": "1997"},
    {"fullname": "Taito Type X", "name": "type-x", "manufacturer": "Taito", "hardwareType": "Arcade", "releaseYear": "2004"},
    {"fullname": "Tandy Color Computer", "name": "coco", "manufacturer": "Tandy", "hardwareType": "Computer", "releaseYear": "1984"},
    {"fullname": "Tandy TRS-80", "name": "trs-80", "manufacturer": "Tandy", "hardwareType": "Computer", "releaseYear": "1984"},
    {"fullname": "Tangerine Computer Systems Oric", "name": "oric", "manufacturer": "Tangerine Computer Systems", "hardwareType": "Computer", "releaseYear": "1982"},
    {"fullname": "Tano Dragon", "name": "tanodragon", "manufacturer": "Tano", "hardwareType": "Computer", "releaseYear": "1984"},
    {"fullname": "Texas Instruments TI-99", "name": "ti99", "manufacturer": "Texas Instruments", "hardwareType": "Computer", "releaseYear": "1981"},
    {"fullname": "Thomson MO/TO Series", "name": "moto", "manufacturer": "Thomson SA", "hardwareType": "Computer", "releaseYear": "1984"},
    {"fullname": "Thomson TO8", "name": "to8", "manufacturer": "Thomson", "hardwareType": "Computer", "releaseYear": "1986"},
    {"fullname": "TIC-80 Game Engine", "name": "tic80", "manufacturer": "Vadim Grigoruk", "hardwareType": "Engine", "releaseYear": "2017"},
    {"fullname": "Tiger Electronics Game.com", "name": "gamecom", "manufacturer": "Tiger", "hardwareType": "Portable", "releaseYear": "1997"},
    {"fullname": "Triforce Arcade System", "name": "triforce", "manufacturer": "Sega", "hardwareType": "Arcade", "releaseYear": "2002"},
    {"fullname": "Uzebox Open Source Console", "name": "uzebox", "manufacturer": "Belogic Software", "hardwareType": "Console", "releaseYear": "2008"},
    {"fullname": "Valve Steam", "name": "steam", "manufacturer": "Valve", "hardwareType": "Collection", "releaseYear": "2003"},
    {"fullname": "Vircon32", "name": "vircon32", "manufacturer": "Carra", "hardwareType": "Engine", "releaseYear": "2021"},
    {"fullname": "Visual Pinball", "name": "vpinball", "manufacturer": "Visual Pinball Team", "hardwareType": "Engine", "releaseYear": "2000"},
    {"fullname": "VTech CreatiVision", "name": "crvision", "manufacturer": "VTech", "hardwareType": "Console", "releaseYear": "1982"},
    {"fullname": "VTech V.Smile", "name": "vsmile", "manufacturer": "VTech", "hardwareType": "Console", "releaseYear": "2004"},
    {"fullname": "WASM-4 Fantasy Console", "name": "wasm4", "manufacturer": "Bruno Garcia", "hardwareType": "Engine", "releaseYear": "2022"},
    {"fullname": "Watara Supervision", "name": "supervision", "manufacturer": "Watara", "hardwareType": "Portable", "releaseYear": "1992"},
    {"fullname": "Windows 3.X", "name": "windows3x", "manufacturer": "Microsoft", "hardwareType": "OS", "releaseYear": "1992"},
    {"fullname": "Windows 9X", "name": "windows9x", "manufacturer": "Microsoft", "hardwareType": "OS", "releaseYear": "1998"},
]

class SystemTransferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("XMB XML Generator")
        self.root.geometry("1700x800")  # Increased height slightly to accommodate Export button

        self.original_left_data = system_data.copy()
        self.left_data = self.original_left_data.copy()
        self.right_data = []
        self.custom_systems = []
        self.custom_collections = []

        self.columns = ("fullname", "name", "manufacturer", "hardwareType", "releaseYear")
        self.sort_orders = {"fullname": False}

        self.left_data.sort(key=lambda x: x["fullname"], reverse=False)

        self.var_allgames = tk.BooleanVar()
        self.var_favorites = tk.BooleanVar()
        self.var_lastplayed = tk.BooleanVar()
        self.var_groupcustom = tk.BooleanVar()

        self.setup_ui()
        self.dragging_index = None

    def setup_ui(self):
        style = ttk.Style()
        style.configure("GrayText.Treeview", foreground="gray")
        style.map("GrayText.Treeview", foreground=[("selected", "white")])

        top_frame = tk.Frame(self.root)
        top_frame.grid(row=0, column=0, columnspan=4, sticky="w", padx=10, pady=(10,0))

        self.left_tree = ttk.Treeview(self.root, columns=self.columns, show="headings", height=15)
        self.left_tree.grid(row=1, column=0, padx=(10, 0), pady=10, sticky="nsew")

        for col in self.columns:
            self.left_tree.heading(col, text=col, command=lambda c=col: self.sort_left_table(c))
            self.left_tree.column(col, width=200)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=1, column=1, padx=10, pady=(140, 0), sticky="n")

        self.to_right_btn = tk.Button(button_frame, text="→", width=5, command=self.move_to_right)
        self.to_right_btn.pack(pady=5)

        self.to_left_btn = tk.Button(button_frame, text="←", width=5, command=self.move_to_left)
        self.to_left_btn.pack(pady=5)

        right_frame = tk.Frame(self.root)
        right_frame.grid(row=1, column=2, columnspan=2, padx=(0, 10), pady=10, sticky="nsew")

        right_frame.grid_rowconfigure(6, weight=1)
        right_frame.grid_rowconfigure(9, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)

        systems_label = tk.Label(right_frame, text="Systems", font=("TkDefaultFont", 10, "bold"))
        systems_label.grid(row=1, column=0, sticky="w")

        add_system_frame = tk.Frame(right_frame)
        add_system_frame.grid(row=2, column=0, sticky="w", pady=(0,10))

        add_system_label = tk.Label(add_system_frame, text="Add custom system:")
        add_system_label.pack(side="left")

        self.add_system_entry = tk.Entry(add_system_frame)
        self.add_system_entry.pack(side="left", padx=(5,5))
        self.add_system_entry.bind("<Return>", self.add_custom_system)

        add_system_btn = tk.Button(add_system_frame, text="Add", command=self.add_custom_system)
        add_system_btn.pack(side="left")

        self.right_tree = ttk.Treeview(right_frame, columns=("name", "systemsortname"), show="headings", height=10)
        self.right_tree.grid(row=3, column=0, sticky="nsew")
        self.right_tree.tag_configure("gray", foreground="gray")

        self.right_tree.heading("name", text="name")
        self.right_tree.heading("systemsortname", text="systemsortname")
        self.right_tree.column("name", width=200)
        self.right_tree.column("systemsortname", width=200)

        reorder_frame = tk.Frame(right_frame)
        reorder_frame.grid(row=3, column=1, padx=(5,10), sticky="ns")

        self.up_btn = tk.Button(reorder_frame, text="▲", width=3, command=self.move_up)
        self.up_btn.pack(pady=(80,10))

        self.down_btn = tk.Button(reorder_frame, text="▼", width=3, command=self.move_down)
        self.down_btn.pack()

        custom_collections_label = tk.Label(right_frame, text="Custom Collections", font=("TkDefaultFont", 10, "bold"))
        custom_collections_label.grid(row=4, column=0, sticky="w", pady=(10, 0))

        add_custom_collection_frame = tk.Frame(right_frame)
        add_custom_collection_frame.grid(row=5, column=0, sticky="w", pady=(0, 10))

        add_custom_collection_label = tk.Label(add_custom_collection_frame, text="Add custom collection:")
        add_custom_collection_label.pack(side="left")

        self.add_custom_collection_entry = tk.Entry(add_custom_collection_frame)
        self.add_custom_collection_entry.pack(side="left", padx=(5, 5))
        self.add_custom_collection_entry.bind("<Return>", self.add_custom_collection)

        add_custom_collection_btn = tk.Button(add_custom_collection_frame, text="Add", command=self.add_custom_collection)
        add_custom_collection_btn.pack(side="left")
        
        cb_groupcustom = tk.Checkbutton(add_custom_collection_frame, text="Group Custom Collections", variable=self.var_groupcustom, command=self.refresh_tables)
        cb_groupcustom.pack(side="left", padx=10)

        self.custom_collections_tree = ttk.Treeview(right_frame, columns=("name", "systemsortname"), show="headings", height=7)
        self.custom_collections_tree.grid(row=6, column=0, sticky="nsew")

        self.custom_collections_tree.heading("name", text="name")
        self.custom_collections_tree.heading("systemsortname", text="systemsortname")
        self.custom_collections_tree.column("name", width=200)
        self.custom_collections_tree.column("systemsortname", width=200)

        self.custom_collections_tree.bind("<Delete>", self.delete_custom_collection)
        self.custom_collections_tree.bind("<Double-1>", self.on_custom_collection_double_click)

        auto_label_frame = tk.Frame(right_frame)
        auto_label_frame.grid(row=7, column=0, columnspan=2, sticky="w", pady=(10, 0))

        auto_label = tk.Label(auto_label_frame, text="Auto Collections", font=("TkDefaultFont", 10, "bold"))
        auto_label.pack(side="left", padx=(0, 10))

        cb_allgames = tk.Checkbutton(auto_label_frame, text="All Games", variable=self.var_allgames, command=self.refresh_tables)
        cb_allgames.pack(side="left", padx=5)

        cb_favorites = tk.Checkbutton(auto_label_frame, text="Favorites", variable=self.var_favorites, command=self.refresh_tables)
        cb_favorites.pack(side="left", padx=5)

        cb_lastplayed = tk.Checkbutton(auto_label_frame, text="Last Played", variable=self.var_lastplayed, command=self.refresh_tables)
        cb_lastplayed.pack(side="left", padx=5)

        self.auto_tree = ttk.Treeview(right_frame, columns=("name", "systemsortname"), show="headings", height=5)
        self.auto_tree.grid(row=9, column=0, sticky="nsew")

        self.auto_tree.heading("name", text="name")
        self.auto_tree.heading("systemsortname", text="systemsortname")
        self.auto_tree.column("name", width=200)
        self.auto_tree.column("systemsortname", width=200)

        self.right_tree.bind("<ButtonPress-1>", self.on_right_tree_press)
        self.right_tree.bind("<B1-Motion>", self.on_right_tree_motion)
        self.right_tree.bind("<ButtonRelease-1>", self.on_right_tree_release)

        self.left_tree.bind("<Double-1>", self.on_left_double_click)
        self.right_tree.bind("<Double-1>", self.on_right_double_click)
        self.right_tree.bind("<Delete>", lambda e: self.move_to_left())

        self.auto_tree.bind("<Delete>", self.delete_auto_collection)
        self.auto_tree.bind("<Double-1>", self.delete_auto_collection)

        self.refresh_tables()
        
        from tkinter import filedialog  # Add this at the top if not already imported

        export_frame = tk.Frame(self.root)
        export_frame.grid(row=2, column=0, columnspan=4, pady=(5, 15))

        # New button: Import es_log.txt
        import_log_btn = tk.Button(export_frame, text="Import es_log.txt", font=("TkDefaultFont", 10, "bold"), command=self.import_es_log)
        import_log_btn.pack(side="left", padx=(0, 20))  # Add padding to separate from Export

        # Existing Export XML button
        export_btn = tk.Button(export_frame, text="Export XML", font=("TkDefaultFont", 10, "bold"), command=self.export_xml)
        export_btn.pack(side="left")
        
    def import_es_log(self):
        filepath = filedialog.askopenfilename(
            title="Select es_log.txt file",
            filetypes=[("Log files", "*.txt"), ("All files", "*.*")]
        )
        if not filepath:
            return  # User cancelled
        print(f"Selected es_log.txt path: {filepath}")
        
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()

        found_system_names = []
        found_custom_systems = []
        found_custom_collections = []

        for line in lines:
            if 'ViewController::preload(): Populating gamelist for system "' in line:
                start = line.find('"') + 1
                end = line.find('"', start)
                name = line[start:end].strip()

                if name == "collections":
                    self.var_groupcustom.set(True)
                elif name == "all":
                    self.var_allgames.set(True)
                elif name == "favorites":
                    self.var_favorites.set(True)
                elif name == "recent":
                    self.var_lastplayed.set(True)
                else:
                    if name not in found_system_names and name not in found_custom_systems:
                        match = next((s for s in self.original_left_data if s["name"] == name), None)
                        if match:
                            found_system_names.append(name)
                        else:
                            found_custom_systems.append(name)

            elif 'ViewController::preload(): Populating gamelist for custom collection "' in line:
                start = line.find('"') + 1
                end = line.find('"', start)
                name = line[start:end].strip()
                if name not in found_custom_collections:
                    found_custom_collections.append(name)

        # Add matched known systems in log order
        for name in found_system_names:
            if not any(s["name"] == name for s in self.right_data):
                match = next((s for s in self.original_left_data if s["name"] == name), None)
                if match:
                    self.right_data.append(match)

        # Add custom systems in log order
        for name in found_custom_systems:
            if not any(s["name"] == name for s in self.right_data) and not any(s["name"] == name for s in self.custom_systems):
                new_sys = {"fullname": name, "name": name, "manufacturer": "", "hardwareType": "", "releaseYear": ""}
                self.custom_systems.append(new_sys)
                self.right_data.append(new_sys)

        # Add custom collections in log order
        for name in found_custom_collections:
            if not any(c["name"] == name for c in self.custom_collections):
                self.custom_collections.append({"name": name, "systemsortname": name})

        self.refresh_tables()
    
    def export_xml(self):
        os.makedirs("theme-customizations", exist_ok=True)
        os.makedirs("theme-customizations/gamelist-carousel", exist_ok=True)
        filepath = os.path.join("theme-customizations", "es_systems_sorting.xml")

        # === Main systemList XML ===
        root = ET.Element("systemList")
        for idx, system in enumerate(self.right_data):
            system_el = ET.SubElement(root, "system")
            name_el = ET.SubElement(system_el, "name")
            name_el.text = system["name"]
            sort_el = ET.SubElement(system_el, "systemsortname")
            sort_el.text = f"{idx + 1:03d}"

        rough_string = ET.tostring(root, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="    ")

        with open(filepath, "w", encoding="utf-8") as f:
            lines = [line for line in pretty_xml.splitlines() if line.strip()]
            f.write("\n".join(lines))

        # === Prepare combined lists for carousel XMLs ===
        systems = self.right_data

        if self.var_groupcustom.get():
            custom_cols = [{"name": "custom-collections", "systemsortname": "custom-collections"}]
        else:
            custom_cols = self.custom_collections

        auto_cols = []
        if self.var_allgames.get():
            auto_cols.append({"name": "auto-allgames", "systemsortname": "auto-allgames"})
        if self.var_favorites.get():
            auto_cols.append({"name": "auto-favorites", "systemsortname": "auto-favorites"})
        if self.var_lastplayed.get():
            auto_cols.append({"name": "auto-lastplayed", "systemsortname": "auto-lastplayed"})

        combined = systems + custom_cols + auto_cols

        def circular_index(idx):
            return idx % len(combined)

        # Create carousel XMLs, one per item in combined
        for idx, item in enumerate(combined):
            theme_root = ET.Element("theme")
            variables = ET.SubElement(theme_root, "variables")

            # Surrounding systems: up to 7 before and 7 after (indexes -7 to +7, skip 0)
            # You can adjust range(-7, 8) if you want fewer surrounding entries
            for offset in range(-2, 8):
                if offset == 0:
                    continue
                pos_idx = circular_index(idx + offset)
                pos_item = combined[pos_idx]
                tag_name = f"systemPlus{offset}" if offset > 0 else f"systemMinus{-offset}"

                var_el = ET.SubElement(variables, tag_name)
                # Direct text with system/collection name (no nested tags)
                var_el.text = pos_item["name"]

            # Write to file named <name>.xml
            filename = f"{item['name']}.xml"
            carousel_path = os.path.join("theme-customizations", "gamelist-carousel", filename)

            rough_xml = ET.tostring(theme_root, 'utf-8')
            reparsed_xml = minidom.parseString(rough_xml)
            pretty_xml = reparsed_xml.toprettyxml(indent="    ")

            with open(carousel_path, "w", encoding="utf-8") as f:
                lines = [line for line in pretty_xml.splitlines() if line.strip()]
                f.write("\n".join(lines))

    def add_custom_system(self, event=None):
        name = self.add_system_entry.get().strip()
        if not name:
            return
        if any(d["name"] == name for d in self.right_data) or any(d["name"] == name for d in self.custom_systems):
            self.add_system_entry.delete(0, tk.END)
            return
        new_sys = {"fullname": name, "name": name, "manufacturer": "", "hardwareType": "", "releaseYear": ""}
        self.custom_systems.append(new_sys)
        self.right_data.append(new_sys)
        self.add_system_entry.delete(0, tk.END)
        self.refresh_tables()

    def add_custom_collection(self, event=None):
        name = self.add_custom_collection_entry.get().strip()
        if not name:
            return
        if any(d["name"] == name for d in self.custom_collections):
            self.add_custom_collection_entry.delete(0, tk.END)
            return
        new_col = {"name": name, "systemsortname": name}
        self.custom_collections.append(new_col)
        self.add_custom_collection_entry.delete(0, tk.END)
        self.refresh_tables()

    def delete_custom_collection(self, event=None):
        selected = self.custom_collections_tree.selection()
        for sel in selected:
            vals = self.custom_collections_tree.item(sel, "values")
            name = vals[0]
            self.custom_collections = [d for d in self.custom_collections if d["name"] != name]
        self.refresh_tables()

    def on_custom_collection_double_click(self, event):
        selected = self.custom_collections_tree.selection()
        if not selected:
            return
        for sel in selected:
            vals = self.custom_collections_tree.item(sel, "values")
            name = vals[0]
            self.custom_collections = [c for c in self.custom_collections if c["name"] != name]
        self.refresh_tables()

    def delete_auto_collection(self, event=None):
        selected = self.auto_tree.selection()
        for sel in selected:
            vals = self.auto_tree.item(sel, "values")
            name = vals[0]
            if name == "auto-allgames":
                self.var_allgames.set(False)
            elif name == "auto-favorites":
                self.var_favorites.set(False)
            elif name == "auto-lastplayed":
                self.var_lastplayed.set(False)
        self.refresh_tables()

    def refresh_tables(self):
        right_names = {d["name"] for d in self.right_data}
        self.left_data = [d for d in self.original_left_data if d["name"] not in right_names]
        if self.sort_orders:
            column, reverse = next(iter(self.sort_orders.items()))
            self.left_data.sort(key=lambda x: x[column], reverse=reverse)

        for col in self.columns:
            heading_text = col
            if col in self.sort_orders:
                heading_text += " ▲" if not self.sort_orders[col] else " ▼"
            self.left_tree.heading(col, text=heading_text, command=lambda c=col: self.sort_left_table(c))

        for row in self.left_tree.get_children():
            self.left_tree.delete(row)
        for item in self.left_data:
            self.left_tree.insert("", "end", values=(item["fullname"], item["name"], item["manufacturer"], item["hardwareType"], item["releaseYear"]))

        for row in self.right_tree.get_children():
            self.right_tree.delete(row)
        for idx, item in enumerate(self.right_data):
            systemsortname = f"{idx + 1:03d}"
            tag = "gray" if item in self.custom_systems else ""
            self.right_tree.insert("", "end", values=(item["name"], systemsortname), tags=(tag,))

        # === MODIFIED PART FOR custom_collections_tree ===
        for row in self.custom_collections_tree.get_children():
            self.custom_collections_tree.delete(row)

        if self.var_groupcustom.get():
            # Show only one grouped custom collection entry
            self.custom_collections_tree.insert("", "end", values=("custom-collections", "custom-collections"))
        else:
            # Show all custom collections as before
            for col in self.custom_collections:
                self.custom_collections_tree.insert("", "end", values=(col["name"], col["systemsortname"]))

        for row in self.auto_tree.get_children():
            self.auto_tree.delete(row)

        if self.var_allgames.get():
            self.auto_tree.insert("", "end", values=("auto-allgames", "auto-allgames"))
        if self.var_favorites.get():
            self.auto_tree.insert("", "end", values=("auto-favorites", "auto-favorites"))
        if self.var_lastplayed.get():
            self.auto_tree.insert("", "end", values=("auto-lastplayed", "auto-lastplayed"))

    def sort_left_table(self, column):
        current = self.sort_orders.get(column, False)
        self.sort_orders = {column: not current}
        self.refresh_tables()

    def move_to_right(self):
        selected = self.left_tree.selection()
        for sel in selected:
            vals = self.left_tree.item(sel, "values")
            name = vals[1]
            item = next((d for d in self.left_data if d["name"] == name), None)
            if item:
                self.right_data.append(item)
        self.refresh_tables()

    def move_to_left(self):
        selected = self.right_tree.selection()
        for sel in selected:
            vals = self.right_tree.item(sel, "values")
            name = vals[0]
            self.right_data = [d for d in self.right_data if d["name"] != name]
            self.custom_systems = [d for d in self.custom_systems if d["name"] != name]
        self.refresh_tables()

    def on_left_double_click(self, event):
        self.move_to_right()

    def on_right_double_click(self, event):
        self.move_to_left()

    def move_up(self):
        selected = self.right_tree.selection()
        if not selected:
            return
        idx = self.right_tree.index(selected[0])
        if idx > 0:
            self.right_data[idx], self.right_data[idx-1] = self.right_data[idx-1], self.right_data[idx]
            self.refresh_tables()
            self.right_tree.selection_set(self.right_tree.get_children()[idx-1])

    def move_down(self):
        selected = self.right_tree.selection()
        if not selected:
            return
        idx = self.right_tree.index(selected[0])
        if idx < len(self.right_data) - 1:
            self.right_data[idx], self.right_data[idx+1] = self.right_data[idx+1], self.right_data[idx]
            self.refresh_tables()
            self.right_tree.selection_set(self.right_tree.get_children()[idx+1])

    def on_right_tree_press(self, event):
        item = self.right_tree.identify_row(event.y)
        if item:
            self.dragging_index = self.right_tree.index(item)
        else:
            self.dragging_index = None

    def on_right_tree_motion(self, event):
        pass

    def on_right_tree_release(self, event):
        if self.dragging_index is None:
            return
        item = self.right_tree.identify_row(event.y)
        if item:
            new_index = self.right_tree.index(item)
            if new_index != self.dragging_index:
                data = self.right_data.pop(self.dragging_index)
                self.right_data.insert(new_index, data)
                self.refresh_tables()
                self.right_tree.selection_set(self.right_tree.get_children()[new_index])
        self.dragging_index = None


if __name__ == "__main__":
    root = tk.Tk()
    app = SystemTransferApp(root)
    root.mainloop()
