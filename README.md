# Compressed ELSA: Efficient Sparse Representations for Large-Scale Recommendation
Official repository for the paper "Efficient Sparse Representations for Large-Scale Recommendation", submitted to the **THE ACM WEB CONFERENCE 2026 (WWW 2026)** - *Short Paper Track*.

## Overview
**Compressed ELSA** is a sparse, scalable variant of the [ELSA](https://github.com/recombee/ELSA) collaborative-filtering autoencoder. It learns **high-dimensional sparse item embeddings directly during training**, significantly reducing model size and speeding up retrieval while preserving recommendation quality.

**This enables:**  
- **10×–100× smaller** smaller embeddings with minimal accuracy loss, competitive with strong baselines on several datasets  
- **Faster inference** via sparse matrix–vector operations 
- **Interpretable latent spaces**, where dimensions naturally correspond to item segments

## [Live Demo](https://compressed-elsa-demo.streamlit.app/)
Our interactive demo showcases additional experiments, ablations, and visualizations that did not fit into the manuscript.

You can also explore:
- Segment-level recommendation  
- Interpretability of the learned sparse latent factors  

The source code for the demo lives in the [demo branch](https://github.com/zombak79/compressed_elsa/tree/demo).

## Repository Layout
```
run.py                Main entry point (training / evaluation controller)
recommenders/
    baselines.py        Baseline recommender models for comparison
    elsa_models.py      ELSA variants (dense, hybrid, compressed-sparse)
experiments/          Experiment runner scripts and configs
results/              Metrics, logs, checkpoints, run artifacts
_datasets/            Download / load / parse / preprocess utilities + data
```

## Environment Setup
```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# or manual:
pip install numpy scipy torch keras scikit-learn recpack tqdm pandas implicit
```
## Example Usage (Training)
From repository root, run, e.g.,
```bash
python experiments/experiment_compressed_elsa.py --dataset ml20m --factors 4096 --batch_size 1024 --max_output 20000 --decay_strategy Exponential --vals "0 1024 512 256 128 64 32 16" --lth True
```
Check individual experiments for available arguments.

## Citation
(To be added once the camera-ready version is finalized.)

## License
This repository is licensed under CC BY-NC 4.0.
See the [LICENSE](LICENSE) file for details.