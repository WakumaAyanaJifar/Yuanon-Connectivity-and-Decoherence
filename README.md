# Yuanon Connectivity and Decoherence in the Mind–Thought Entanglement Theory

Code for the paper *"Yuanon Connectivity and Decoherence in the Mind–Thought Entanglement
Theory: Spectral Scaling Laws, a Quantum-Reference-Frame Reading and Tests in Band-Gap
Waveguides"* (H. Ning et al., submitted to *Entropy*).

It computes the exact complex poles of the MTE dispersion relation, simulates the full
two-field system on a lattice, runs the finite-reference delay model, and draws every
figure in the paper.

## Quick start

```bash
pip install -r requirements.txt
bash run_all.sh         # writes all figures to figs/ (about 2 minutes)
```

## Files

| File | What it does | Paper |
|---|---|---|
| `core.py` | Boundary kernel, exact complex poles, lattice simulation of the two-field system | Secs. 2-3 |
| `dde.py` | Finite-reference delay model and its comparison with the lattice | Sec. 3.4 |
| `checks.py` | General-*n* absorption formula; calibration of *C* from device data | Sec. 3.6, App. B |
| `style.py` | Shared plotting style | - |
| `fig1.py` | Figure 1 (concept) | Fig. 1 |
| `fig2.py` | Figure 2 (spectral structure) | Fig. 2 |
| `fig34.py` | Figures 3 and 4 (time domain, scaling laws) and Table 3 | Figs. 3-4 |
| `fig5.py` | Figure 5 (regime map) | Fig. 5 |
| `fig6.py` | Figure 6 (finite references); needs `dde.py` to have run first | Fig. 6 |
| `refs/` | Crossref verification and MDPI formatting of the reference list | References |

Units: *m* = 1 throughout. Lattice parameters: spacing *a* = 0.05, time step *dt* = 0.01/*m*,
velocity-Verlet integration.

## Citation

If you use this code, please cite the paper (citation details will be added on publication).

## License

MIT (see `LICENSE`).
