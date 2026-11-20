import json, re, html
meta=json.load(open('crossref_meta.json'))
ABBR={'Physical Review':'Phys. Rev.','Physical Review Letters':'Phys. Rev. Lett.','Physical Review A':'Phys. Rev. A','Physical Review E':'Phys. Rev. E',
'Physical Review X':'Phys. Rev. X','Physical Review Applied':'Phys. Rev. Appl.','Reviews of Modern Physics':'Rev. Mod. Phys.','Nature Physics':'Nat. Phys.',
'Nature Communications':'Nat. Commun.','Nature Photonics':'Nat. Photonics','Nature':'Nature','Communications Physics':'Commun. Phys.','Quantum':'Quantum',
'New Journal of Physics':'New J. Phys.','Foundations of Physics':'Found. Phys.','Physics Reports':'Phys. Rep.','Communications in Mathematical Physics':'Commun. Math. Phys.',
'Journal of Mathematical Physics':'J. Math. Phys.','Physica A: Statistical Mechanics and its Applications':'Phys. A','Journal of Modern Optics':'J. Mod. Opt.',
'Reports on Progress in Physics':'Rep. Prog. Phys.','Proceedings of the National Academy of Sciences':'Proc. Natl. Acad. Sci. USA','Applied Physics Reviews':'Appl. Phys. Rev.',
'npj Quantum Information':'npj Quantum Inf.','Physics Letters B':'Phys. Lett. B','International Journal of Theoretical Physics':'Int. J. Theor. Phys.',
'General Relativity and Gravitation':'Gen. Relativ. Gravit.','Physics of Life Reviews':'Phys. Life Rev.','Annals of Physics':'Ann. Phys.','Behavioral and Brain Sciences':'Behav. Brain Sci.',
'Nature Reviews Neuroscience':'Nat. Rev. Neurosci.','Science China Information Sciences':'Sci. China Inf. Sci.','Future Generation Computer Systems':'Future Gener. Comput. Syst.',
'IEEE Internet of Things Journal':'IEEE Internet Things J.','Chinese Journal of Electronics':'Chin. J. Electron.','Computers &amp; Electrical Engineering':'Comput. Electr. Eng.',
'Computers & Electrical Engineering':'Comput. Electr. Eng.'}
MANUAL={
'ning_mte':r"Ning, H. General Mind--Thought Entanglement Theory (MTE): A Classical Field-Theoretic Model---With a Note on the Concept and Mathematical Definition of the Conscious Yuanon. PhilArchive, manuscript. Available online: \url{https://philarchive.org/rec/NINGME} (accessed on 20 November 2026).",
'ning_fourfactor':r"Ning, H. From Bit to Consciousness: A Four-Factor Framework for Unified Information Theory Based on Biton, Gene, Meme, and Yuanon. PhilArchive, manuscript. Available online: \url{https://philarchive.org/rec/NINFBT} (accessed on 20 November 2026).",
'ning_cyberism':r"Ning, H. Cyberism: The Theory for Relationships between Human and Cyberspace. {\em Chin. J. Eng.} {\bf 2025}, {\em 47}, 1240--1256. \url{https://doi.org/10.13374/j.issn2095-9389.2025.05.27.001}.",
'luppi2026':r"Luppi, P.; Kabel, V.; Giacomini, F.; Smirne, A. Reduced Quantum-Reference-Frame Channels for Open Quantum Systems. {\em arXiv} {\bf 2026}, arXiv:2607.05578.",
'behera2025':r"Behera, S.R.; Sen, K.; Sinha Roy, A.; Ray, S.; Singh, A.; Rau, A.R.P.; Sinha, U. Temporal Steering of Entanglement Decay with Single-Shot Control. {\em arXiv} {\bf 2025}, arXiv:2505.16623.",
'breuer2002':r"Breuer, H.-P.; Petruccione, F. {\em The Theory of Open Quantum Systems}; Oxford University Press: Oxford, UK, 2002.",
'weiss2012':r"Weiss, U. {\em Quantum Dissipative Systems}, 4th ed.; World Scientific: Singapore, 2012.",
}
def initials(given):
    parts=re.split(r'[\s]+',given.strip()); out=''
    for p in parts:
        sub=p.split('-'); out+='-'.join(s[0]+'.' for s in sub if s)
    return out
AUTH_FIX={
'vanrietvelde2020':'Vanrietvelde, A.; H\\"{o}hn, P.A.; Giacomini, F.; Castro-Ruiz, E.',
'caldeira1983':'Caldeira, A.O.; Leggett, A.J.',
'kofman1994':'Kofman, A.G.; Kurizki, G.; Sherman, B.',
'fisher2015':'Fisher, M.P.A.',
'zhang_iob2022':'Zhang, Z.; Yin, R.; Ning, H.',
'dhelim_cyberentity':'Dhelim, S.; Ning, H.; Cui, S.; Ma, J.; Huang, R.; Wang, K.I.-K.',
'devuyst2026':'De Vuyst, J.; H\\"{o}hn, P.A.; Tsobanjan, A.',
'aliahmad2022':'Ali Ahmad, S.; Galley, T.D.; H\\"{o}hn, P.A.; Lock, M.P.E.; Smith, A.R.H.',
}
def fmt(k,m):
    au=m.get('author',[])
    names=[]
    for a in au:
        if 'family' in a: names.append(a['family']+', '+initials(a.get('given','')) if a.get('given') else a['family'])
        elif 'name' in a: names.append(a['name'])
    if len(names)>10: names=names[:10]+['et al']
    auth='; '.join(names)
    if k in AUTH_FIX: auth=AUTH_FIX[k]
    title=html.unescape(re.sub(r'<[^>]+>','',m['title'][0])); title=re.sub(r'\s+',' ',title).strip()
    if title.startswith('Colloquium:'): pass
    ct=(m.get('container-title') or [''])[0]; ct=html.unescape(ct)
    j=ABBR.get(ct, ABBR.get(ct.replace('&','&amp;'), ct))
    yr=(m.get('published-print') or m.get('published-online') or m.get('issued'))['date-parts'][0][0]
    vol=m.get('volume',''); pg=m.get('page') or m.get('article-number') or ''
    a_=pg.split('-')
    if len(a_)==2 and a_[0]==a_[1]: pg=a_[0]
    pg=pg.replace('-','--')
    doi=m['DOI']
    tex_title=title.replace('&','\\&').replace('%','\\%')
    TFIX={'hameroff2014':"Consciousness in the universe: A review of the `Orch OR' theory",'roy2017':'Colloquium: Strongly interacting photons in one-dimensional continuum','gks1976':'Completely positive dynamical semigroups of $N$-level systems'}
    if k in TFIX: tex_title=TFIX[k]
    tex_title=re.sub(r'"([^"]*)"',r"``\1''",tex_title)
    sep='' if auth.endswith('.') else '.'
    tsep='' if tex_title.endswith('?') else '.'
    s=f"{auth}{sep} {tex_title}{tsep} {{\\em {j}}} {{\\bf {yr}}}"
    if vol: s+=f", {{\\em {vol}}}"
    if pg: s+=f", {pg}"
    s+=f". \\url{{https://doi.org/{doi}}}."
    return s
src=open('body.tex').read()+open('appendix.tex').read()
order=[]
for grp in re.findall(r'\\cite\{([^}]*)\}',src):
    for k in grp.split(','):
        k=k.strip()
        if k not in order: order.append(k)
items=[]; missing=[]
for k in order:
    if k in MANUAL: items.append((k,MANUAL[k]))
    elif k in meta and meta[k]: items.append((k,fmt(k,meta[k])))
    else: missing.append(k)
bib="\\begin{adjustwidth}{-\\extralength}{0cm}\n\\reftitle{References}\n\\begin{thebibliography}{999}\n"+"\n".join(f"\\bibitem{{{k}}}\n{t}" for k,t in items)+"\n\\end{thebibliography}\n\\end{adjustwidth}\n"
open('bib.tex','w').write(bib)
unused=[k for k in list(meta)+list(MANUAL) if k not in order]
print('cited:',len(order),'missing:',missing,'unused:',unused)
