# Chromebook<br>
Chromebook hacks<br>

Remove / Replace Bitmaps ChromeOS<br>
Chromebook ELM / OAK / HANA / ELM<br>
<br>
<b size=15># Backup your current firmware first:</b><br>
flashrom -p host -r backup.bin<br>
<br>
<b size=15># Howto:</b><br>
 cp backup.bin 235.bin # backup.bin is your backup of your firmware<br>
 cbfstool 235.bin extract -n vbgfx.bin -f vbgfx.bin -m arm64<br>
 cbfstool 235.bin extract -n font.bin -f font.bin -m arm64<br>
 cbfstool 235.bin extract -n locale_en.bin -f  locale.bin -m arm64<br>
python3 ./bitmap_mod.py<br>
cbfstool 235.bin remove -n vbgfx.bin<br>
cbfstool 235.bin remove -n font.bin<br>
cbfstool 235.bin remove -n locale_en.bin<br>
cbfstool 235.bin add -n vbgfx.bin -f vbgfx.bin -c lzma -t raw<br>
cbfstool 235.bin add -n locale_en.bin -f locale_en.bin -c lzma -t raw<br>
cbfstool 235.bin add -n font.bin -f font.bin -c lzma -t raw<br>
flashrom -p host -w 235.bin<br>
exit<br>


Will not remove background yet, but images it does...<br>
ChromeOS is not using Background.bmp in dev mode, it is just a programmed background, not an image.<br>
Try to find workaround. <br>
