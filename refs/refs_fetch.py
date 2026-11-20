import json, urllib.request, time
raw=json.load(open('crossref_raw.json'))
doi={k:(v[0]['DOI'] if v else None) for k,v in raw.items()}
doi.update({'ning_cyberology':'10.1109/JIOT.2022.3217821','hameroff2014':'10.1016/j.plrev.2013.08.002',
            'ford1965':'10.1063/1.1704304','maldacena1999':'10.1023/A:1026654312961',
            'ning_cyberism':'10.13374/j.issn2095-9389.2025.05.27.001'})
meta={}
for k,d in doi.items():
    for a in range(3):
        try:
            m=json.load(urllib.request.urlopen('https://api.crossref.org/works/'+d,timeout=30))['message']; break
        except Exception as e: m=None; time.sleep(2)
    meta[k]=m
    if m:
        yr=(m.get('published-print') or m.get('published-online') or m.get('issued'))['date-parts'][0][0]
        print(k,'|',m['title'][0][:70],'|',(m.get('short-container-title') or m.get('container-title') or [''])[0],yr,m.get('volume'),m.get('page') or m.get('article-number'),flush=True)
    else: print(k,'FAILED',d)
    time.sleep(0.2)
json.dump(meta,open('crossref_meta.json','w'))
