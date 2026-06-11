import urllib.request
import json
import os
import sys

USERNAME = os.getenv("GITHUB_ACTOR", "ekaznyra")
TOKEN = os.getenv("GITHUB_TOKEN", "")

def fetch_events():
    url = f"https://api.github.com/users/{USERNAME}/events/public"
    req = urllib.request.Request(url)
    if TOKEN:
        req.add_header("Authorization", f"token {TOKEN}")
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        print(f"Error fetching events: {e}")
        return []

def get_recent_commits(events, limit=3):
    commits = []
    for event in events:
        if event['type'] == 'PushEvent':
            repo_name = event['repo']['name']
            for commit in event['payload'].get('commits', []):
                msg = commit['message'].split('\n')[0]
                commits.append(f"[{repo_name}] {msg}")
                if len(commits) >= limit:
                    return commits
    if not commits:
        commits = ["[*] Initialized defense systems...", "[*] Scanning for anomalies...", "[*] No recent anomalies detected."]
    return commits

def generate_svg(commits):
    svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="800" height="200">
  <style>
    .terminal {{
      font-family: "Courier New", Consolas, monospace;
      font-size: 14px;
      fill: #caa84d;
    }}
    .prompt {{ fill: #5c574c; }}
    .cursor {{
      animation: blink 1s step-end infinite;
    }}
    @keyframes blink {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
    .line {{
      opacity: 0;
      animation: appear 0.1s forwards;
    }}
    .l1 {{ animation-delay: 0.5s; }}
    .l2 {{ animation-delay: 1.5s; }}
    .l3 {{ animation-delay: 2.5s; }}
    .l4 {{ animation-delay: 3.5s; }}
    @keyframes appear {{ to {{ opacity: 1; }} }}
    .scanline {{
      width: 100%;
      height: 100px;
      fill: url(#scanGradient);
      animation: scan 4s linear infinite;
    }}
    @keyframes scan {{ 0% {{ transform: translateY(-100px); }} 100% {{ transform: translateY(200px); }} }}
  </style>
  <defs>
    <linearGradient id="scanGradient" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#caa84d" stop-opacity="0" />
      <stop offset="100%" stop-color="#caa84d" stop-opacity="0.05" />
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="800" height="200" fill="#0a0a0c" rx="10"/>
  <!-- Top bar -->
  <rect width="800" height="30" fill="#14110a" rx="10" />
  <!-- Controls -->
  <circle cx="20" cy="15" r="6" fill="#ff5f56"/>
  <circle cx="40" cy="15" r="6" fill="#ffbd2e"/>
  <circle cx="60" cy="15" r="6" fill="#27c93f"/>
  <text x="400" y="20" fill="#caa84d" opacity="0.6" font-family="monospace" font-size="12" text-anchor="middle">root@sec-mainframe:~</text>

  <rect class="scanline" />

  <g class="terminal">
    <text x="20" y="60" class="line l1"><tspan class="prompt">root@sec-mainframe:~$</tspan> tail -n 3 /var/log/syslog</text>
    <text x="20" y="90" class="line l2">[SYS] {commits[0] if len(commits) > 0 else ""}</text>
    <text x="20" y="115" class="line l3">[SYS] {commits[1] if len(commits) > 1 else ""}</text>
    <text x="20" y="140" class="line l4">[SYS] {commits[2] if len(commits) > 2 else ""}</text>
    <text x="20" y="170" class="line l4"><tspan class="prompt">root@sec-mainframe:~$</tspan> <tspan class="cursor">_</tspan></text>
  </g>
</svg>"""
    return svg_template

if __name__ == "__main__":
    events = fetch_events()
    commits = get_recent_commits(events, limit=3)
    # clean up commit strings to avoid breaking XML
    commits = [c.replace("<", "&lt;").replace(">", "&gt;").replace("&", "&amp;") for c in commits]
    svg_content = generate_svg(commits)
    
    os.makedirs("assets", exist_ok=True)
    with open("assets/terminal.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("assets/terminal.svg generated successfully.")
