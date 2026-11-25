from pathlib import Path
r=Path(__file__).parent
s=(r/'Index.html').read_text()
for marker,name in [('STYLES','Styles.html'),('CORE','core.js'),('CLIENT','Client.html')]:
    content=(r/name).read_text()
    if marker=='CORE': content='<script>\n'+content+'\n</script>'
    s=s.replace('<!-- '+marker+' -->',content)
(r/'index.html').write_text(s)
(r/'dist').mkdir(exist_ok=True)
(r/'dist/index.html').write_text(s)
