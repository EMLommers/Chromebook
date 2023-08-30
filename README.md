# Chromebook
Chromebook hacks

# Remove / Replace Bitmaps ChromeOS
# Chromebook ELM / OAK / HANA / ELM

# Howto:
# flashrom -p host -r firmware.rom
# cbfstool firmware.rom extract -n vbgfx.bin -f vbgfx.bin -m arm64
# (extract vbgfx.bin from firmware file)
# this file in same directory
# python3 ./bitmap_mod.py
# cbfstool firmware.rom remove -n vbgfx.bin
# cbfstool firmware.rom add -n vbgfx.bin -f vbgfx.bin -m arm64
# flashrom -p host -w firmware.rom

# V0.20
# Should work on locale_xx.bin and font.bin as well (not yet tested)
