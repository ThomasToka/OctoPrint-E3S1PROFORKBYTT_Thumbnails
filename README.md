# OctoPrint E3S1PROFORKBYTT Thumbnails

OctoPrint plugin to read and expose E3S1PROFORKBYTT thumbnail/printdata formats in uploaded G-code files.

The wiki URL is:
https://github.com/ThomasToka/MarlinFirmware/wiki

The slicer postprocessing instructions are aligned with:
https://github.com/ThomasToka/MarlinFirmware/wiki/Gcode-preview

## Quick Notes

- Replace `YOURUSER` with your real Windows user name.
- Python-based scripts require Python 3.
- Since 2026-05-05, the Python scripts auto-install Pillow when missing.
- Where noted, add this block to your slicer machine/custom G-code:

```gcode
;AFTER_LAYER_CHANGE
;[layer_z]
```

## Postprocessing Scripts (MarlinFirmware)

All scripts are in:
https://github.com/ThomasToka/MarlinFirmware/tree/Firmware-Binaries

1. PrusaSlicer
	 - E3S1PROFORKBYTT_printdata_prusaslicer_v27_thumbnail.py
2. Cura 5.x
	 - E3S1PROFORKBYTT_printdata_cura_v5_thumbnail.py
3. Creality Slicer 4.8.x
	 - E3S1PROFORKBYTT_printdata_crealityslicer_thumbnail.py
4. Orca Slicer 1.8
	 - E3S1PROFORKBYTT_printdata_orcaslicer_v18_thumbnail.py
5. Orca Slicer 1.9
	 - E3S1PROFORKBYTT_printdata_orcaslicer_v19_thumbnail.py
6. Orca Slicer 2.x
	 - E3S1PROFORKBYTT_printdata_orcaslicer_v20_thumbnail.py
7. SuperSlicer
	 - E3S1PROFORKBYTT_printdata_superslicer_thumbnail.py
8. Creality Print 6.3
	 - E3S1PROFORKBYTT_printdata_creality_print_6_thumbnail.py
9. Creality Print 7.x
	 - E3S1PROFORKBYTT_printdata_creality_print_7_thumbnail.py
10. Bambu Studio 2.4.x
	 - E3S1PROFORKBYTT_printdata_bambustudio_thumbnail.py

## Slicer Setup Instructions

### PrusaSlicer

- Copy script to:
	- `C:\Users\YOURUSER\AppData\Roaming\PrusaSlicer\scripts`
- Script:
	- https://github.com/ThomasToka/MarlinFirmware/blob/Firmware-Binaries/E3S1PROFORKBYTT_printdata_prusaslicer_v27_thumbnail.py
- Configure postprocessing in Printer Settings -> General.
- Configure thumbnail/export options in Print Settings -> Output settings.
- Add this block in Printer Settings -> Custom G-code -> After layer change G-code:

```gcode
;AFTER_LAYER_CHANGE
;[layer_z]
```

- Example command (Windows):

```text
"C:\Users\YOURUSER\AppData\Local\Microsoft\WindowsApps\python3.exe" "C:\Users\YOURUSER\AppData\Roaming\PrusaSlicer\scripts\E3S1PROFORKBYTT_printdata_prusaslicer_v27_thumbnail.py"
```

### Cura 5.x

- Copy script to:
	- `C:\Users\YOURUSER\AppData\Roaming\cura\5.7\scripts`
- Script:
	- https://github.com/ThomasToka/MarlinFirmware/blob/Firmware-Binaries/E3S1PROFORKBYTT_printdata_cura_v5_thumbnail.py
- Add the script in Cura postprocessing.
- `;AFTER_LAYER_CHANGE` block is not needed for this Cura script.
- Example path entry:

```text
"C:\Users\YOURUSER\AppData\Roaming\cura\5.7\scripts\E3S1PROFORKBYTT_printdata_cura_v5_thumbnail.py"
```

### Creality Slicer 4.8.x

- Copy script to:
	- `C:\Program Files\Creality Slicer 4.8.2\plugins\PostProcessingPlugin\scripts`
- Script:
	- https://github.com/ThomasToka/MarlinFirmware/blob/Firmware-Binaries/E3S1PROFORKBYTT_printdata_crealityslicer_thumbnail.py
- Select the script in Creality Slicer postprocessing.
- Adjust filament density if needed.
- No extra M73 script is needed (built in).

### Orca Slicer (1.8 / 1.9 / 2.x)

- Copy script to:
	- `C:\Users\YOURUSER\AppData\Roaming\OrcaSlicer\user\default\process`
- Use the script that matches your Orca version:
	- 1.8: https://github.com/ThomasToka/MarlinFirmware/blob/Firmware-Binaries/E3S1PROFORKBYTT_printdata_orcaslicer_v18_thumbnail.py
	- 1.9: https://github.com/ThomasToka/MarlinFirmware/blob/Firmware-Binaries/E3S1PROFORKBYTT_printdata_orcaslicer_v19_thumbnail.py
	- 2.x: https://github.com/ThomasToka/MarlinFirmware/blob/Firmware-Binaries/E3S1PROFORKBYTT_printdata_orcaslicer_v20_thumbnail.py
- Set script in Printer Settings -> Basic information -> Advanced and in Preview -> Others.
- Add this block in Machine G-code -> Layer change G-code:

```gcode
;AFTER_LAYER_CHANGE
;[layer_z]
```

- Example command (Windows, Orca 1.9 shown):

```text
"C:\Users\YOURUSER\AppData\Local\Microsoft\WindowsApps\python3.exe" "C:\Users\YOURUSER\AppData\Roaming\OrcaSlicer\user\default\process\E3S1PROFORKBYTT_printdata_orcaslicer_v19_thumbnail.py"
```

### SuperSlicer

- Copy script to:
	- `C:\Users\YOURUSER\AppData\Roaming\SuperSlicer`
- Script:
	- https://github.com/ThomasToka/MarlinFirmware/blob/Firmware-Binaries/E3S1PROFORKBYTT_printdata_superslicer_thumbnail.py
- Configure:
	- Printer Settings -> General -> Firmware -> G-code flavor
	- Printer Settings -> General -> Thumbnail
	- Print Settings -> Output Options -> Post-processing scripts
- Example command (Windows):

```text
"C:\Users\YOURUSER\AppData\Local\Microsoft\WindowsApps\python3.exe" "C:\Users\YOURUSER\AppData\Roaming\SuperSlicer\E3S1PROFORKBYTT_printdata_superslicer_thumbnail.py"
```

### Creality Print 6.3

- Copy script to:
	- `C:\Users\YOURUSER\AppData\Roaming\Creality\Creality Print\6.0\user\default\process`
- Script:
	- https://github.com/ThomasToka/MarlinFirmware/blob/Firmware-Binaries/E3S1PROFORKBYTT_printdata_creality_print_6_thumbnail.py
- Add this block in Machine G-code -> Layer change G-code:

```gcode
;AFTER_LAYER_CHANGE
;[layer_z]
```

- Configure script under Global postprocessing.
- Example command (Windows):

```text
"C:\Users\YOURUSER\AppData\Local\Microsoft\WindowsApps\python3.exe" "C:\Users\YOURUSER\AppData\Roaming\Creality\Creality Print\6.0\user\default\process\E3S1PROFORKBYTT_printdata_creality_print_6_thumbnail.py";
```

### Creality Print 7.x

- Copy script to:
	- `C:\Users\YOURUSER\AppData\Roaming\Creality\Creality Print\7.0\user\default\process`
- Script:
	- https://github.com/ThomasToka/MarlinFirmware/blob/Firmware-Binaries/E3S1PROFORKBYTT_printdata_creality_print_7_thumbnail.py
- Add this block in Machine G-code -> Layer change G-code:

```gcode
;AFTER_LAYER_CHANGE
;[layer_z]
```

- Configure script under Global postprocessing.
- Example command (Windows):

```text
"C:\Users\YOURUSER\AppData\Local\Microsoft\WindowsApps\python3.exe" "C:\Users\YOURUSER\AppData\Roaming\Creality\Creality Print\7.0\user\default\process\E3S1PROFORKBYTT_printdata_creality_print_7_thumbnail.py";
```

### Bambu Studio 2.4.x

- Copy script to:
	- `C:\Users\YOURUSER\AppData\Roaming\BambuStudio\user\default\process`
- Script:
	- https://github.com/ThomasToka/MarlinFirmware/blob/Firmware-Binaries/E3S1PROFORKBYTT_printdata_bambustudio_thumbnail.py
- Add this block in Machine G-code -> Layer change G-code:

```gcode
;AFTER_LAYER_CHANGE
;[layer_z]
```

- Configure script under Global postprocessing.
- Example command (Windows):

```text
"C:\Users\YOURUSER\AppData\Local\Microsoft\WindowsApps\python3.exe" "C:\Users\YOURUSER\AppData\Roaming\BambuStudio\user\default\process\E3S1PROFORKBYTT_printdata_bambustudio_thumbnail.py";
```

Important note for Bambu Studio: the source thumbnail is 50x50 and gets scaled to 250x250, so preview quality is expected to be softer.

## OctoPrint Plugin Workflow

1. Install this plugin in OctoPrint.
2. Open plugin settings.
3. Run thumbnail scan on your file folders.
4. Thumbnails become available for supported print files.

## Reference Wiki Sections

- Main page: https://github.com/ThomasToka/MarlinFirmware/wiki/Gcode-preview
- PrusaSlicer: https://github.com/ThomasToka/MarlinFirmware/wiki/Gcode-preview#prusaslicer
- Cura 5.x: https://github.com/ThomasToka/MarlinFirmware/wiki/Gcode-preview#cura-5x
- Creality Slicer 4.8.x: https://github.com/ThomasToka/MarlinFirmware/wiki/Gcode-preview#creality-slicer-48x
- Orca Slicer: https://github.com/ThomasToka/MarlinFirmware/wiki/Gcode-preview#orca-slicer
- SuperSlicer: https://github.com/ThomasToka/MarlinFirmware/wiki/Gcode-preview#super-slicer
- Creality Print 6.3: https://github.com/ThomasToka/MarlinFirmware/wiki/Gcode-preview#creality-print-63
- Creality Print 7.x: https://github.com/ThomasToka/MarlinFirmware/wiki/Gcode-preview#creality-print-7x
- Bambu Studio 2.4: https://github.com/ThomasToka/MarlinFirmware/wiki/Gcode-preview#bambu-studio-24

## Special thanks and credits

This plugin has been mainly written by messedupRyan (https://github.com/messedupryan).
Without his skills i would not have been able to solve the remaining feature requests that fast as he introduced the needed techniques (events, handlers, services, etc). Many thanks Ryan!

Also a special thanks to jneilliii (https://github.com/jneilliii/OctoPrint-PrusaSlicerThumbnails) for his initial work on the Prusa Plugin that lead to the release of the first E3S1PROFORKBYTT Thumbnails Octoprint Plugin which was a fork of jneilliii`s plugin.
