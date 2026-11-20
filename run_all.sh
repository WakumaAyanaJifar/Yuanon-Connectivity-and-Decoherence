#!/usr/bin/env bash
# Reproduce every figure and numerical result in the paper.
set -e
cd "$(dirname "$0")"
mkdir -p figs
echo "[1/6] checks (general-n formula, device calibration)"; python3 checks.py
echo "[2/6] delay model vs lattice (Sec. 3.4)";              python3 dde.py
echo "[3/6] Figure 1";                                       python3 fig1.py
echo "[4/6] Figure 2";                                       python3 fig2.py
echo "[5/6] Figures 3 and 4 (lattice simulations)";          python3 fig34.py
echo "[6/6] Figures 5 and 6";                                python3 fig5.py; python3 fig6.py
echo "Done. Figures are in figs/"
