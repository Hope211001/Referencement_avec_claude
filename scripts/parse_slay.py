import re
import sys

with open('C:/Users/Admin/AppData/Local/Temp/slayradio_home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

title = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
print('TITLE:', title.group(1).strip() if title else 'NOT FOUND')

# Meta description (two patterns)
desc = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)', html, re.IGNORECASE)
if not desc:
    desc = re.search(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']description', html, re.IGNORECASE)
print('META DESC:', desc.group(1)[:160] if desc else 'NOT FOUND')

canon = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', html, re.IGNORECASE)
print('CANONICAL:', canon.group(1) if canon else 'NOT FOUND')

lang = re.search(r'<html[^>]+lang=["\']([^"\']+)', html, re.IGNORECASE)
print('LANG:', lang.group(1) if lang else 'NOT FOUND')

robots = re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)', html, re.IGNORECASE)
print('ROBOTS META:', robots.group(1) if robots else 'NOT FOUND')

json_lds = re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.IGNORECASE | re.DOTALL)
print(f'JSON-LD BLOCKS: {len(json_lds)}')
for i, jld in enumerate(json_lds):
    print(f'  Block {i+1}:', jld[:300].strip())

hreflangs = re.findall(r'<link[^>]+hreflang=["\']([^"\']+)', html, re.IGNORECASE)
print('HREFLANG:', hreflangs if hreflangs else 'NOT FOUND')

images = re.findall(r'<img[^>]*>', html, re.IGNORECASE)
print(f'TOTAL IMAGES: {len(images)}')
missing_alt = [img for img in images if 'alt=' not in img.lower()]
print(f'IMAGES WITHOUT ALT: {len(missing_alt)}')
lazy = [img for img in images if 'loading=' in img.lower()]
print(f'IMAGES WITH LOADING ATTR: {len(lazy)}')

viewport = re.search(r'<meta[^>]+name=["\']viewport["\'][^>]+content=["\']([^"\']+)', html, re.IGNORECASE)
print('VIEWPORT:', viewport.group(1) if viewport else 'NOT FOUND')

charset = re.search(r'<meta[^>]+charset=["\']([^"\']+)', html, re.IGNORECASE)
print('CHARSET:', charset.group(1) if charset else 'NOT FOUND')

print(f'HTML SIZE: {len(html)} bytes ({len(html)/1024:.1f} KB)')
