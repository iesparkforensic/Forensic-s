# Site Opener

Opens a list of websites in your default browser, one every 10 seconds.

Requires Python 3 (no extra packages).

## Usage

1. Put your sites in `sites.txt`, one per line (`https://` is optional).
2. Run:

```bash
python site_opener.py sites.txt
```

Options:

```bash
python site_opener.py sites.txt -i 5            # 5-second interval instead of 10
python site_opener.py sites.txt --new-window    # new window per site instead of a tab
python site_opener.py example.com github.com    # pass URLs directly
```

Press `Ctrl+C` to stop early.
