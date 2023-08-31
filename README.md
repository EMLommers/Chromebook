# Chromebook<br>
Chromebook hacks<br>

Remove / Replace Bitmaps ChromeOS<br>
Chromebook ELM / OAK / HANA / ELM<br>

<b size=15># Howto:</b><br>
 cp backup.bin 235.bin # backup.bin is your backup of your firmware
 cbfstool 235.bin extract -n vbgfx.bin -f vbgfx.bin -m arm64
 cbfstool 235.bin extract -n font.bin -f font.bin -m arm64
 cbfstool 235.bin extract -n locale_en.bin -f  locale.bin -m arm64
python3 ./bitmap_mod.py
cbfstool 235.bin remove -n vbgfx.bin
cbfstool 235.bin remove -n font.bin
cbfstool 235.bin remove -n locale_en.bin
cbfstool 235.bin add -n vbgfx.bin -f vbgfx.bin -c lzma -t raw
cbfstool 235.bin add -n locale_en.bin -f locale_en.bin -c lzma -t raw
cbfstool 235.bin add -n font.bin -f font.bin -c lzma -t raw
flashrom -p host -w 235.bin
exit


Will not remove background yet, but images it does...
ChromeOS is not using Background.bmp in dev mode, it is just a programmed background, not an image.
Try to find workaround. 
