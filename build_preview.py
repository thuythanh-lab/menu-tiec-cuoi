from pathlib import Path
r=Path(__file__).parent
(r/'Shared.html').write_text('<script>\n'+(r/'Core.gs').read_text()+'\n</script>')
s=(r/'Index.html').read_text().replace('<?!= bootJson ?>','{"preview":true}')
for name in ['Styles','Shared','Client']:s=s.replace("<?!= include_('"+name+"'); ?>",(r/(name+'.html')).read_text())
(r/'preview.html').write_text(s)
(r/'index.html').write_text(s)
(r/'dist').mkdir(exist_ok=True)
(r/'dist/index.html').write_text(s)
