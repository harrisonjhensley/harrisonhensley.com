#!/bin/bash
# Auto-regenerate picks.html when CSV is saved
# Uses Python's built-in watchdog for file monitoring

cd "/Users/harrisonhensley/Personal Site"

echo "👀 Watching for changes to My Picks.csv..."
echo "Press Ctrl+C to stop"
echo ""

python3 << 'PYTHON'
import time
import subprocess
from pathlib import Path
from datetime import datetime

csv_file = Path("my-picks-data/My Picks.csv")
last_modified = csv_file.stat().st_mtime if csv_file.exists() else 0

print(f"Initial generation...")
subprocess.run(["python3", "generate-picks.py"])
print(f"✅ Ready! Watching for changes...\n")

try:
    while True:
        time.sleep(1)  # Check every second

        if csv_file.exists():
            current_modified = csv_file.stat().st_mtime

            if current_modified != last_modified:
                print(f"🔄 CSV updated - regenerating picks.html...")
                subprocess.run(["python3", "generate-picks.py"])
                print(f"✅ Done! {datetime.now().strftime('%H:%M:%S')}\n")
                last_modified = current_modified

except KeyboardInterrupt:
    print("\n\n👋 Stopped watching. Have a great day!")
PYTHON
