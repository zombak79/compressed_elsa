import streamlit as st
from utils import TOC

# prepare placeholder for table of contents
toc = TOC(st.sidebar.empty())

st.markdown ("""## Efficient Learning of Sparse Representations from Interactions

This mini-page accompanies our paper [link TBA] and provides all experiments, ablations, and visualizations that 
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
st.markdown("""TBA""")  

st.markdown("""### Acknowledgments""")
st.markdown("""
Book cover images are provided by the Open Library Covers API. © Open Library. https://openlibrary.org
""")
toc()
