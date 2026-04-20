# Compressed ELSA: Efficient Sparse Representations for Large-Scale Recommendation
Official repository for the paper "[Efficient Sparse Representations for Large-Scale Recommendation](https://dl.acm.org/doi/abs/10.1145/3774904.3792914)", accepted to the **THE ACM WEB CONFERENCE 2026 (WWW 2026)** - *Short Paper Track*.

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

```
@inproceedings{10.1145/3774904.3792914,
    author = {Van\v{c}ura, Vojt\v{e}ch and Spi\v{s}\'{a}k, Martin and Alves, Rodrigo and Pe\v{s}ka, Ladislav},
    title = {Efficient Learning of Sparse Representations from Interactions},
    year = {2026},
    isbn = {9798400723070},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3774904.3792914},
    doi = {10.1145/3774904.3792914},
    abstract = {Behavioral patterns captured in embeddings learned from interaction data are pivotal across various stages of production recommender systems. However, in the initial retrieval stage, practitioners face an inherent tradeoff between embedding expressiveness and the scalability and latency of serving components, resulting in the need for representations that are both compact and expressive. To address this challenge, we propose a training strategy for learning high-dimensional sparse embedding layers in place of conventional dense ones, balancing efficiency, representational expressiveness, and interpretability. To demonstrate our approach, we modified the production-grade collaborative filtering autoencoder ELSA, achieving up to 10	exttimes{} reduction in embedding size with no loss of recommendation accuracy, and up to 100	exttimes{} reduction with only a 2.5\% loss. Moreover, the active embedding dimensions reveal an interpretable inverted-index structure that segments items in a way directly aligned with the model's latent space, thereby enabling integration of segment-level recommendation functionality (e.g., 2D homepage layouts) within the candidate retrieval model itself. Source codes, additional results, as well as a live demo are available at https://github.com/zombak79/compressed_elsa.},
    booktitle = {Proceedings of the ACM Web Conference 2026},
    pages = {8577–8580},
    numpages = {4},
    keywords = {collaborative filtering, linear autoencoder, sparse representation},
    location = {United Arab Emirates},
    series = {WWW '26}
}
```

## License
This repository is licensed under CC BY-NC 4.0.
See the [LICENSE](LICENSE) file for details.
