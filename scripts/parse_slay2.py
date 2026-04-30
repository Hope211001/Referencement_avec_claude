import re
import json

with open('C:/Users/Admin/AppData/Local/Temp/slayradio_home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Extract full JSON-LD
json_lds = re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.IGNORECASE | re.DOTALL)
for i, jld in enumerate(json_lds):
    print(f'=== JSON-LD Block {i+1} ===')
    try:
        parsed = json.loads(jld.strip())
        print(json.dumps(parsed, indent=2, ensure_ascii=False))
    except Exception as e:
        print('RAW:', jld[:500])
        print('ERROR:', e)

# Hreflang tags full
hreflang_tags = re.findall(r'<link[^>]+hreflang[^>]+>', html, re.IGNORECASE)
print('\n=== HREFLANG TAGS ===')
for t in hreflang_tags:
    print(t)

# Meta description full
desc_tags = re.findall(r'<meta[^>]+description[^>]+>', html, re.IGNORECASE)
print('\n=== META DESC TAGS ===')
for t in desc_tags:
    print(t)

# Title length
title = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
if title:
    t = title.group(1).strip()
    print(f'\n=== TITLE ({len(t)} chars) ===')
    print(t)

# Image tags
images = re.findall(r'<img[^>]+>', html, re.IGNORECASE)
print(f'\n=== IMAGES ({len(images)} total) ===')
for img in images:
    src_m = re.search(r'src=["\']([^"\']+)', img)
    alt_m = re.search(r'alt=["\']([^"\']*)', img)
    width_m = re.search(r'width=["\']([^"\']+)', img)
    height_m = re.search(r'height=["\']([^"\']+)', img)
    loading_m = re.search(r'loading=["\']([^"\']+)', img)
    src = src_m.group(1) if src_m else 'NO SRC'
    alt = alt_m.group(1) if alt_m else 'NO ALT'
    w = width_m.group(1) if width_m else '?'
    h = height_m.group(1) if height_m else '?'
    loading = loading_m.group(1) if loading_m else 'not set'
    print(f'  src={src[:60]} | alt="{alt[:40]}" | {w}x{h} | loading={loading}')
