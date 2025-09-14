import requests

# 读取 sources.txt
with open("sources.txt", "r") as f:
    sources = [line.strip() for line in f if line.strip() and not line.startswith("#")]

merged = "#EXTM3U\n"

for url in sources:
    try:
        print(f"Fetching {url} ...")
        r = requests.get(url, timeout=10)
        if r.status_code == 200 and "#EXTM3U" in r.text:
            merged += r.text.strip() + "\n"
        else:
            print(f"Skipped invalid source: {url}")
    except Exception as e:
        print(f"Failed {url}: {e}")

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(merged)

print("✅ Done. playlist.m3u generated.")
