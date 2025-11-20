# My Picks Auto-Update

## Quick Start

To automatically regenerate picks.html when you save the CSV:

```bash
cd "/Users/harrisonhensley/Personal Site"
./watch-picks.sh
```

Leave this running in a terminal. Every time you save `My Picks.csv`, it will automatically:
1. Regenerate `picks.html` with new content
2. Show picks marked with `Featured = TRUE` in the Featured Picks section
3. Update filter categories based on Medium types

Press `Ctrl+C` to stop watching.

## Manual Update

If you prefer to update manually:

```bash
cd "/Users/harrisonhensley/Personal Site"
python3 generate-picks.py
```

## How It Works

- **CSV File**: `my-picks-data/My Picks.csv` - Edit this to add/remove picks
- **Generator**: `generate-picks.py` - Python script that builds the HTML
- **Output**: `picks.html` - Your My Picks page
- **Auto-watcher**: `watch-picks.sh` - Monitors CSV and auto-regenerates

## CSV Format

```
Title,Medium,Why I loved it,Link/Where to Find,Featured
Book Title,Book,Your thoughts here,https://amazon.com/...,TRUE
Video Title,YouTube,Your thoughts here,https://youtube.com/...,
```

- **Featured**: Set to `TRUE` to display in the Featured Picks section (mark exactly 3 picks as featured)
- **Supported Mediums**: Book, YouTube, Music, Film, TV, Podcast, Product, Article, or anything else you want!
