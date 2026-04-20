import streamlit as st
from utils import TOC

# prepare placeholder for table of contents
toc = TOC(st.sidebar.empty())

st.markdown ("""## Efficient Learning of Sparse Representations from Interactions

This mini-page accompanies our [paper](https://dl.acm.org/doi/abs/10.1145/3774904.3792914) and provides all experiments, ablations, and visualizations that 
could not fit into the manuscript. The source code is at https://github.com/zombak79/compressed_elsa. The source 
code for this site is in the branch "demo".
""")

st.markdown("""### Abstract""")

st.markdown("""
Recommender systems rely on embeddings learned from interactions that capture meaningful 
behavioral patterns. In practice, however, the retrieval stage faces a persistent tension: dense 
embeddings are expressive but expensive to store and serve at scale, while compact representations risk 
losing essential signal. This tradeoff makes it difficult to build retrieval models that are both fast 
and accurate.

Our approach takes inspiration from recent work on sparse embedding compression. Instead of compressing 
dense vectors after training, we train high-dimensional sparse embeddings directly, preserving expressive 
capacity while keeping memory and latency low. Applied to the production-grade ELSA autoencoder, this 
strategy yields up to 10× smaller embeddings with no accuracy loss, and up to 100× compression with 
only a 2.5% drop.

A further benefit emerges from the sparsity itself: the active dimensions form a natural inverted-index 
structure that groups items into coherent semantic segments aligned with the model’s latent space. This 
makes it possible to expose interpretable segments and support segment-level recommendations (such 
as 2D homepage layouts) directly within the retrieval layer.""")

st.markdown("""### Navigation""")  
st.markdown("""
This page is organised as follows:

- In <a href="results" target="_self">Results</a>, you'll find extended tables, pruning-schedule ablations, 
embedding-size comparisons, and additional metrics.
- In <a href="demo" target="_self">Live Demo</a>, you can interact with the latent space: select a user, 
inspect their sparse activations, explore discovered segments, and see how recommendations change in real time.
""", unsafe_allow_html=True)

st.markdown("""### Citation""")  
st.markdown("""```bibtex
@inproceedings{10.1145/3774904.3792914,
    author = {Van\\v{c}ura, Vojt\\v{e}ch and Spi\\v{s}\\'{a}k, Martin and Alves, Rodrigo and Pe\\v{s}ka, Ladislav},
    title = {Efficient Learning of Sparse Representations from Interactions},
    year = {2026},
    isbn = {9798400723070},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3774904.3792914},
    doi = {10.1145/3774904.3792914},
    abstract = {Behavioral patterns captured in embeddings learned from interaction data are pivotal across various stages of production recommender systems. However, in the initial retrieval stage, practitioners face an inherent tradeoff between embedding expressiveness and the scalability and latency of serving components, resulting in the need for representations that are both compact and expressive. To address this challenge, we propose a training strategy for learning high-dimensional sparse embedding layers in place of conventional dense ones, balancing efficiency, representational expressiveness, and interpretability. To demonstrate our approach, we modified the production-grade collaborative filtering autoencoder ELSA, achieving up to 10\\texttimes{} reduction in embedding size with no loss of recommendation accuracy, and up to 100\\texttimes{} reduction with only a 2.5\\% loss. Moreover, the active embedding dimensions reveal an interpretable inverted-index structure that segments items in a way directly aligned with the model's latent space, thereby enabling integration of segment-level recommendation functionality (e.g., 2D homepage layouts) within the candidate retrieval model itself. Source codes, additional results, as well as a live demo are available at https://github.com/zombak79/compressed_elsa.},
    booktitle = {Proceedings of the ACM Web Conference 2026},
    pages = {8577–8580},
    numpages = {4},
    keywords = {collaborative filtering, linear autoencoder, sparse representation},
    location = {United Arab Emirates},
    series = {WWW '26}
}
```""")  

st.markdown("""### Acknowledgments""")
st.markdown("""
Book cover images are provided by the Open Library Covers API. © Open Library. https://openlibrary.org
""")
toc()
