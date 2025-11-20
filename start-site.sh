#!/bin/bash
# Start local web server for Personal Site

cd "/Users/harrisonhensley/Personal Site"

echo "🌐 Starting web server..."
echo "📍 Open your browser to: http://localhost:8000"
echo "Press Ctrl+C to stop"
echo ""

python3 -m http.server 8000
