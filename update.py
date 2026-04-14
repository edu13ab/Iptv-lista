import requests

urls = [
    
    "https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8",
    "https://pastebin.com/raw/YVBjE9ii",
    "https://pastebin.com/raw/kJuhKyDw",
    "https://www.m3u.cl/lista/ES.m3u"

    "https://www.m3u.cl/lista/ES.m3u",
    "https://iptv-org.github.io/iptv/languages/spa.m3u",
    "https://www.tdtchannels.com/lists/tv.m3u8"
]

contenido_final = "#EXTM3U\n"

for url in urls:
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            lineas = r.text.splitlines()
            for linea in lineas:
                if linea.startswith("#EXTINF") or linea.startswith("http"):
                    contenido_final += linea + "\n"
    except:
        pass

with open("lista.m3u", "w", encoding="utf-8") as f:
    f.write(contenido_final)
