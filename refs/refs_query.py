import json, urllib.request, urllib.parse, time, re, sys
Q = {
'ning_cpst2015':'Cyber-physical-social-thinking space based science and technology framework for the Internet of Things Ning Liu',
'ning_cybermatics':'Cybermatics: Cyber-physical-social-thinking hyperspace based science and technology Ning',
'ning_gc2018':'General Cyberspace: Cyberspace and Cyber-Enabled Spaces Ning',
'zhang_iob2022':'Internet of Brain, Thought, Thinking, and Creation Zhang Yin Ning',
'ning_cyberology':'Cyberology: Cyber-Physical-Social-Thinking Spaces-Based Discipline and Interdiscipline Hierarchy for Metaverse',
'dhelim_cyberentity':'Cyberentity and its consistency in the cyber-physical-social-thinking hyperspace Dhelim',
'aharonov1967':'Charge Superselection Rule Aharonov Susskind 1967',
'bartlett2007':'Reference frames, superselection rules, and quantum information Bartlett Rudolph Spekkens',
'giacomini2019':'Quantum mechanics and the covariance of physical laws in quantum reference frames Giacomini Castro-Ruiz Brukner',
'vanrietvelde2020':'A change of perspective: switching quantum reference frames via a perspective-neutral framework Vanrietvelde',
'hamette2020':'Quantum reference frames for general symmetry groups de la Hamette Galley',
'aliahmad2022':'Quantum Relativity of Subsystems Ali Ahmad Galley Hohn Lock Smith',
'castroruiz2025':'Relative subsystems and quantum reference frame transformations Castro-Ruiz Oreshkov',
'devuyst2026':'On the relation between perspective-neutral, algebraic, and effective quantum reference frames De Vuyst Hoehn Tsobanjan',
'poulin2007':'Dynamics of a quantum reference frame Poulin Yard',
'loveridge2018':'Symmetry, Reference Frames, and Relational Quantities in Quantum Mechanics Loveridge Miyadera Busch',
'castroruiz2020':'Quantum clocks and the temporal localisability of events in the presence of gravitating quantum systems',
'gambini2004':'Realistic Clocks, Universal Decoherence, and the Black Hole Information Paradox Gambini Porto Pullin',
'pikovski2015':'Universal decoherence due to gravitational time dilation Pikovski Zych Costa Brukner',
'zurek2003':'Decoherence, einselection, and the quantum origins of the classical Zurek',
'schlosshauer2019':'Quantum decoherence Schlosshauer Physics Reports 2019',
'lindblad1976':'On the generators of quantum dynamical semigroups Lindblad',
'gks1976':'Completely positive dynamical semigroups of N-level systems Gorini Kossakowski Sudarshan',
'caldeira1983':'Path integral approach to quantum Brownian motion Caldeira Leggett',
'leggett1987':'Dynamics of the dissipative two-state system Leggett Chakravarty Dorsey Fisher Garg Zwerger',
'devega2017':'Dynamics of non-Markovian open quantum systems de Vega Alonso',
'john1990':'Quantum electrodynamics near a photonic band gap: Photon bound states and dressed atoms John Wang',
'john1994':'Spontaneous emission near the edge of a photonic band gap John Quang',
'kofman1994':'Spontaneous and Induced Atomic Decay in Photonic Band Structures Kofman Kurizki Sherman',
'lambropoulos2000':'Fundamental quantum optics in structured reservoirs Lambropoulos Nikolopoulos Nielsen Bay',
'gonzaleztudela2017':'Markovian and non-Markovian dynamics of quantum emitters coupled to two-dimensional structured reservoirs Gonzalez-Tudela Cirac',
'liu2017':'Quantum electrodynamics near a photonic bandgap Liu Houck',
'sundaresan2019':'Interacting Qubit-Photon Bound States with Superconducting Circuits Sundaresan Lundgren Zhu Gorshkov Houck',
'mirhosseini2018':'Superconducting metamaterials for waveguide quantum electrodynamics Mirhosseini Kim Painter',
'kim2021':'Quantum Electrodynamics in a Topological Waveguide Kim Zhang Ferreira Painter',
'krinner2018':'Spontaneous emission of matter waves from a tunable open quantum system Krinner Stewart Pazmino Kwon Schneble',
'goban2014':'Atom-light interactions in photonic crystals Goban Hung Yu Kimble',
'hood2016':'Atom-atom interactions around the band edge of a photonic crystal waveguide Hood Goban Asenjo-Garcia',
'douglas2015':'Quantum many-body models with cold atoms coupled to photonic crystals Douglas Habibian Hung Gorshkov Kimble Chang',
'calajo2016':'Atom-field dressed states in slow-light waveguide QED Calajo Ciccarello Chang Rabl',
'roy2017':'Colloquium: Strongly interacting photons in one-dimensional continuum Roy Wilson Firstenberg',
'sheremet2023':'Waveguide quantum electrodynamics: Collective radiance and photon-photon correlations Sheremet Petrov Iorsh Poshakinskiy Poddubny',
'gu2017':'Microwave photonics with superconducting quantum circuits Gu Kockum Miranowicz Liu Nori',
'lodahl2015':'Interfacing single photons and single quantum dots with photonic nanostructures Lodahl Mahmoodian Stobbe',
'dorner2002':'Laser-driven atoms in half-cavities Dorner Zoller',
'tufarelli2013':'Dynamics of spontaneous emission in a single-end photonic waveguide Tufarelli Ciccarello Kim',
'koch2007':'Charge-insensitive qubit design derived from the Cooper pair box Koch',
'krantz2019':'A quantum engineer\'s guide to superconducting qubits Krantz Kjaergaard Yan Orlando Gustavsson Oliver',
'blais2021':'Circuit quantum electrodynamics Blais Grimsmo Girvin Wallraff Reviews of Modern Physics',
'yan2018':'Tunable Coupling Scheme for Implementing High-Fidelity Two-Qubit Gates Yan',
'klimov2018':'Fluctuations of Energy-Relaxation Times in Superconducting Qubits Klimov',
'burnett2019':'Decoherence benchmarking of superconducting qubits Burnett',
'shalibo2010':'Lifetime and Coherence of Two-Level Defects in a Josephson Junction Shalibo',
'dvali2000':'4D gravity on a brane in 5D Minkowski space Dvali Gabadadze Porrati',
'randall1999':'An Alternative to Compactification Randall Sundrum',
'maldacena1999':'The Large N Limit of Superconformal Field Theories and Supergravity Maldacena',
'vanraamsdonk2010':'Building up spacetime with quantum entanglement Van Raamsdonk',
'ryu2006':'Holographic Derivation of Entanglement Entropy from the anti-de Sitter Space/Conformal Field Theory Correspondence Ryu Takayanagi',
'tegmark2000':'Importance of quantum decoherence in brain processes Tegmark',
'hameroff2014':'Consciousness in the universe: A review of the Orch OR theory Hameroff Penrose',
'fisher2015':'Quantum cognition: The possibility of processing with nuclear spins in the brain Fisher',
'pothos2013':'Can quantum probability provide a new direction for cognitive modeling? Pothos Busemeyer',
'seth2022':'Theories of consciousness Seth Bayne Nature Reviews Neuroscience',
'verlet1967':'Computer Experiments on Classical Fluids. I. Thermodynamical Properties of Lennard-Jones Molecules Verlet',
'ford1965':'Statistical Mechanics of Assemblies of Coupled Oscillators Ford Kac Mazur',
}
out={}
for k,q in Q.items():
    url='https://api.crossref.org/works?'+urllib.parse.urlencode({'query.bibliographic':q,'rows':3,'select':'DOI,title,author,container-title,short-container-title,issued,volume,page,article-number,type'})
    for attempt in range(3):
        try:
            d=json.load(urllib.request.urlopen(url,timeout=30)); break
        except Exception as e:
            time.sleep(2); d=None
    items=d['message']['items'] if d else []
    out[k]=items
    t=items[0]['title'][0] if items and items[0].get('title') else '??'
    print(k,'|',t[:90],'|',items[0].get('DOI') if items else '',flush=True)
    time.sleep(0.3)
json.dump(out,open('crossref_raw.json','w'))
