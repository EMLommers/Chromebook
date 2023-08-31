# Chromebook<br>
Chromebook hacks<br>

Remove / Replace Bitmaps ChromeOS<br>
Chromebook ELM / OAK / HANA / ELM<br>

<b size=15># Howto:</b><br>
flashrom -p host -r firmware.rom<br>
cbfstool firmware.rom extract -n vbgfx.bin -f vbgfx.bin -m arm64<br>
# (extract vbgfx.bin from firmware file)<br>
# this file in same directory
python3 ./bitmap_mod.py<br>
cbfstool firmware.rom remove -n vbgfx.bin<br>
cbfstool firmware.rom add -n vbgfx.bin -f vbgfx.bin -c lzma -t raw
flashrom -p host -w firmware.rom<br>

V0.20<br>
Should work on locale_xx.bin and font.bin as well (not yet tested)<br>

Will not remove background yet, but images it does...
