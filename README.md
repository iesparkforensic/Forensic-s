# Site Opener

Opens a list of websites in your default browser, one every 10 seconds.

## Setup

Put your sites in `sites.txt`, one per line (`https://` is optional, lines starting with `#` are ignored).
Keep `sites.txt` in the same folder as the opener file.

## Windows

Double-click `open_sites.bat`. Close the black window to stop early.

For a different interval, open Command Prompt in the folder and run `open_sites.bat 5` (5 seconds).

## Mac

Double-click `open_sites.command`. The first time, macOS may block it because it isn't from the App Store:
right-click the file, choose **Open**, then **Open** again. Press `Ctrl+C` in the Terminal window to stop early.

If double-clicking does nothing, open Terminal in the folder and run `chmod +x open_sites.command` once.
For a different interval, run `./open_sites.command 5`.

## Python (optional, any system)

If you have Python 3 installed:

```bash
python site_opener.py sites.txt                 # 10-second interval
python site_opener.py sites.txt -i 5            # 5-second interval
python site_opener.py sites.txt --new-window    # new window per site instead of a tab
```
