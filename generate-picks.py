#!/usr/bin/env python3
"""
Generate Library HTML from CSV file
"""

import csv
from collections import OrderedDict
from urllib.parse import urlparse

def get_domain_name(url):
    """Extract a clean domain name from a URL"""
    if not url:
        return ""
    try:
        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path
        # Remove www. prefix
        if domain.startswith('www.'):
            domain = domain[4:]
        # Capitalize first letter
        return domain.split('.')[0].capitalize() + '.com' if domain else url
    except:
        return url

# Read the CSV file
picks = []
mediums = set()

with open('my-picks-data/My Picks.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        picks.append(row)
        mediums.add(row['Medium'].lower())

# Sort mediums alphabetically
mediums = sorted(mediums)

# Generate Featured Picks HTML (filter by Featured column = TRUE)
featured_picks = [pick for pick in picks if pick.get('Featured', '').strip().upper() == 'TRUE']
recent_picks_html = ""
for pick in featured_picks:
    link = pick.get('Link/Where to Find', '').strip()
    title = pick['Title']

    if link:
        title_html = f'<a href="{link}" target="_blank">{title}</a>'
    else:
        title_html = title

    # Add link section if there's a link
    link_section = ""
    if link:
        domain = get_domain_name(link)
        link_section = f'<p class="pick-link"><strong>Link:</strong> <a href="{link}" target="_blank">{domain}</a></p>'

    recent_picks_html += f'''                <!-- Pick -->
                <div class="pick-card">
                    <span class="pick-medium">{pick['Medium']}</span>
                    <h3>{title_html}</h3>
                    <p class="pick-description">{pick['Why I loved it']}</p>
                    {link_section}
                </div>

'''

# Generate filter buttons
filter_buttons_html = '                    <button class="filter-btn active" data-filter="all">All</button>\n'
for medium in mediums:
    # Capitalize first letter of each word
    display_name = medium.title() + 's' if not medium.endswith('s') else medium.title()
    filter_buttons_html += f'                    <button class="filter-btn" data-filter="{medium}">{display_name}</button>\n'

# Generate All Picks table rows
all_picks_html = ""
for pick in picks:
    link = pick.get('Link/Where to Find', '').strip()
    title = pick['Title']
    medium_lower = pick['Medium'].lower()

    if link:
        title_html = f'<a href="{link}" target="_blank">{title}</a>'
    else:
        title_html = title

    # Add link section if there's a link
    link_section = ""
    if link:
        domain = get_domain_name(link)
        link_section = f'<p class="row-link"><strong>Link:</strong> <a href="{link}" target="_blank">{domain}</a></p>'

    all_picks_html += f'''                <!-- Row -->
                <div class="table-row" data-medium="{medium_lower}">
                    <div class="row-title">
                        <span class="medium-badge">{pick['Medium']}</span>
                        <h4>{title_html}</h4>
                    </div>
                    <p class="row-description">{pick['Why I loved it']}</p>
                    {link_section}
                </div>

'''

# Read the template or create the full HTML
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Library - Harrison Hensley</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Montserrat:wght@600;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="picks.css">
</head>
<body>
    <nav class="main-nav">
        <div class="nav-content">
            <a href="index.html" class="nav-home">Harrison Hensley</a>
            <div class="nav-links">
                <a href="blog.html">Insight Over Index</a>
                <a href="projects.html">Projects</a>
                <a href="picks.html">Library</a>
                <a href="about.html">About Me</a>
            </div>
        </div>
    </nav>

    <main class="page-content">
        <!-- Header -->
        <section class="page-header">
            <h1>Library</h1>
            <p class="page-description">The inputs that are shaping my outputs. Books, films, tools, podcasts, creators, and rabbit holes worth sharing.</p>
        </section>

        <!-- Featured Picks -->
        <section class="recent-picks">
            <h2>Featured Picks</h2>
            <div class="recent-grid">
{recent_picks_html}            </div>
        </section>

        <!-- Full Database -->
        <section class="picks-database">
            <div class="database-header">
                <h2>All Picks</h2>
                <div class="filter-bar">
{filter_buttons_html}                </div>
            </div>

            <div class="picks-table">
{all_picks_html}            </div>
        </section>
    </main>

    <footer>
        <p>Bringing Midwest Spirit to AI-Native CPG Insights</p>
    </footer>

    <script src="picks.js"></script>
</body>
</html>
'''

# Write the HTML file
with open('picks.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✓ picks.html generated successfully!")
print(f"  - {len(picks)} picks imported")
print(f"  - {len(mediums)} categories: {', '.join(mediums)}")
