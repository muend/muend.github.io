"""Check generated bilingual pages, local destinations and current-profile invariants."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import sys
from projects import PROJECTS

ROOT=Path(__file__).resolve().parents[1]
class Document(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.ids=[];self.h1=0;self.lang=None;self.alternates={};self.text=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang')
        if tag=='h1':self.h1+=1
        if 'id' in a:self.ids.append(a['id'])
        if tag=='link' and a.get('rel')=='alternate':self.alternates[a.get('hreflang')]=a.get('href')
        for key in ('href','src','poster'):
            if a.get(key):self.links.append(a[key])
    def handle_data(self,value):self.text.append(value)

pages=sorted([*ROOT.glob('*.html'),*ROOT.glob('projects/*.html'),*ROOT.glob('tr/*.html'),*ROOT.glob('tr/projects/*.html')])
errors=[]
expected=2*(len(PROJECTS)+3)
if len(pages)!=expected:errors.append(f'{len(pages)} pages, expected {expected}')
for page in pages:
    relative=page.relative_to(ROOT).as_posix();doc=Document();doc.feed(page.read_text(encoding='utf-8'))
    if doc.h1!=1:errors.append(f'{relative}: h1 count {doc.h1}')
    if len(doc.ids)!=len(set(doc.ids)):errors.append(f'{relative}: duplicate IDs')
    if doc.lang!=('tr' if relative.startswith('tr/') else 'en'):errors.append(f'{relative}: wrong language')
    if not all(x in doc.alternates for x in ('en','tr','x-default')):errors.append(f'{relative}: language alternate missing')
    for href in doc.links:
        u=urlsplit(href)
        if u.scheme or u.netloc or not u.path:continue
        target=ROOT/u.path.lstrip('/') if u.path.startswith('/') else page.parent/unquote(u.path)
        if not target.exists():errors.append(f'{relative}: missing {href}')
    text=' '.join(doc.text)
    for obsolete in ('August – October 2026','Ağustos – Ekim 2026','Aug – Oct 2026','Ağu – Eki 2026','full-time from July 2027','Temmuz 2027\'den itibaren','ArcGIS Pro 3.1–3.3'):
        if obsolete in text:errors.append(f'{relative}: obsolete {obsolete}')
    if any('smithery.ai' in x for x in doc.links):errors.append(f'{relative}: removed Smithery link')
    if relative.endswith('projects/neuron-to-gpt.html') and '124,439,808' not in text and '124.439.808' not in text:errors.append(f'{relative}: 124M evidence missing')
    if relative.endswith('projects/geoai-skills.html') and not all(x in text for x in ('Awesome Claude Code','Awesome Geospatial','92')):errors.append(f'{relative}: current skills evidence missing')
    if relative.endswith('projects/placetwin.html') and '1,712' not in text and '1.712' not in text:errors.append(f'{relative}: current inventory missing')
    if relative.endswith('projects/arcgis-mcp-bridge.html') and not all(x in text for x in ('TDQS','3.5/5' if doc.lang=='en' else '3,5/5')):errors.append(f'{relative}: Glama score missing')
print(f'Checked {len(pages)} bilingual pages and {len(PROJECTS)} project pairs: {len(errors)} errors')
for error in errors:print(error)
sys.exit(bool(errors))
