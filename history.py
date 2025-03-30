import json
from urllib.parse import urlparse
from collections import defaultdict
from datetime import datetime

# Load history data from your JSON file
with open("data.json", "r", encoding="utf-8") as f:
    history = json.load(f)

# Group history by domain
grouped = defaultdict(list)
for entry in history:
    domain = urlparse(entry["url"]).netloc
    grouped[domain].append(entry)

# Generate HTML
html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Firefox History Viewer</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background-color: #f3f3f3; color: #333; margin: 0; padding: 20px; }
        h1 { font-size: 24px; margin-bottom: 10px; }
        .folder { margin-bottom: 20px; background: white; border-radius: 8px; box-shadow: 0 0 5px rgba(0,0,0,0.1); }
        .folder-name { padding: 12px 20px; background: #e1e1e1; font-weight: bold; border-top-left-radius: 8px; border-top-right-radius: 8px; }
        ul { list-style: none; margin: 0; padding: 0 20px 20px; }
        li { margin: 8px 0; }
        a { color: #0066cc; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .timestamp { font-size: 0.9em; color: #888; margin-left: 10px; }
    </style>
</head>
<body>
    <h1>Firefox Search History</h1>
'''

for domain, items in grouped.items():
    html += f'<div class="folder"><div class="folder-name">{domain}</div><ul>'
    for entry in items:
        time_str = datetime.fromtimestamp(entry["lastVisitTime"] / 1000).strftime('%Y-%m-%d %H:%M:%S')
        html += f'<li><a href="{entry["url"]}" target="_blank">{entry["title"]}</a><span class="timestamp">({time_str})</span></li>'
    html += '</ul></div>'

html += '''
</body>
</html>
'''

# Save to HTML file
with open("firefox_history.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML file generated as 'firefox_history.html'")
