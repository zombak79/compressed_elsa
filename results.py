import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from utils import *
from tables import *
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go
import html as pyhtml
import textwrap
import numpy as np

# insert css for recommendation rows
init_rows_rendering()

# prepare placeholder for table of contents
toc = TOC(st.sidebar.empty())

# read the data

# goodbooks
goodbooks_df=get_data("goodbooks")

goodbooks_factors_recall_20_df=get_data("goodbooks_factors_recall_20")
goodbooks_factors_recall_50_df=get_data("goodbooks_factors_recall_50")
goodbooks_factors_ndcg_100_df=get_data("goodbooks_factors_ndcg_100")

goodbooks_recall_20_lth_df=get_data("goodbooks_recall_20_lth")
goodbooks_recall_50_lth_df=get_data("goodbooks_recall_50_lth")
goodbooks_ndcg_100_lth_df=get_data("goodbooks_ndcg_100_lth")

# movielens
ml20m_df=get_data("ml20m")

ml20m_recall_20_lth_df=get_data("ml20m_recall_20_lth")
ml20m_recall_50_lth_df=get_data("ml20m_recall_50_lth")
ml20m_ndcg_100_lth_df=get_data("ml20m_ndcg_100_lth")

ml20m_factors_recall_20_df=get_data("ml20m_factors_recall_20")
ml20m_factors_recall_50_df=get_data("ml20m_factors_recall_50")
ml20m_factors_ndcg_100_df=get_data("ml20m_factors_ndcg_100")

# netflix prize
netflix_df=get_data("netflix")

netflix_factors_recall_20_df=get_data("netflix_factors_recall_20")
netflix_factors_recall_50_df=get_data("netflix_factors_recall_50")
netflix_factors_ndcg_100_df=get_data("netflix_factors_ndcg_100")

netflix_recall_20_lth_df=get_data("netflix_recall_20_lth")
netflix_recall_50_lth_df=get_data("netflix_recall_50_lth")
netflix_ndcg_100_lth_df=get_data("netflix_ndcg_100_lth")

st.markdown("""
# Results

Because of space limitations in the paper, this page provides the full experimental results for all datasets, all evaluation metrics, and all pruning strategies used in our study. These results include detailed Recall@20, Recall@50, and NDCG@100 scores, as well as ablations that did not fit into the manuscript.

To compare dense and sparse representations on equal footing, we report vector sizes in bytes (B) rather than in latent-factor counts. Dense ELSA models store one float32 value per latent dimension (4 bytes each), while sparse models store both the value and its index for every nonzero latent factor (2 × 4 bytes = 8 bytes per active dimension).

This means that:
- Dense models:
256, 128, 64, 32, 16 latent factors
→ 1024 B, 512 B, 256 B, 128 B, 64 B

- Sparse models:
128, 64, 32, 16, 8 nonzeros (nnz)
→ 1024 B, 512 B, 256 B, 128 B, 64 B

By normalizing both representations to the same byte budget, we can directly compare the accuracy of dense baselines (low-dimensional ELSA) with sparse methods, including Compressed ELSA.""")

# section with results for goodbooks
toc.append(st, "Results for GoodBooks-10k", "gb10k")
st.markdown("""
Below we present the full experimental results for the GoodBooks-10k dataset.
""")
toc.append(st, "Experimental results", "gb10k_exp", 1)
st.markdown("""
Across all storage budgets, Compressed ELSA achieves the strongest performance. 
Low-dimensional dense ELSA suffers substantial quality degradation at small vector sizes, 
and post-hoc sparse projection (ELSA + SAE) improves stability but remains below our method. 
Pruned EASE performs competitively while Compressed ELSA consistently delivers the best 
accuracy-size trade-off.
""")
st.markdown(gb_main , unsafe_allow_html=True)

toc.append(st, "Pruning strategies", "gb10k_prun", 1)
st.markdown("""
We compare several pruning schedules that gradually introduce sparsity during training. 
Step-wise pruning (the lottery-ticket style approach) performs noticeably worse than linear 
and exponential schedules, which update the mask every epoch and therefore avoid long periods 
of training with stale sparsity patterns. Restarting the model after each pruning step 
provides a small but consistent additional improvement.
""")
st.markdown(gb_pruning_strategy , unsafe_allow_html=True)
fig = plot_three_side_by_side(goodbooks_recall_20_lth_df, goodbooks_recall_50_lth_df, goodbooks_ndcg_100_lth_df, baselines=goodbooks_df[goodbooks_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list(), xcol="Vector size (bytes)")
st.plotly_chart(fig, use_container_width=True)

toc.append(st, "Initial embedding sizes", "gb10k_factors", 1)
st.markdown("""
We also evaluate different initial embedding dimensionalities. 
Here, “initial embedding size” refers to the dimensionality of the latent
space **before pruning**. During training, we start from a large dense
embedding (e.g., 8192, 6144, 4096, or 2048 factors) and gradually
apply a pruning schedule until reaching the same final byte budget. For
sparse embeddings, each active latent dimension requires 8 bytes 
(4 bytes for the value and 4 bytes for the index), so an embedding with 
8192 possible dimensions corresponds to a 64 kB budget 
(8192 × 8 bytes ≈ 64 kB). This setup allows us to study how the choice of
starting dimensionality influences the quality of the final sparse model
under identical memory constraints.

For the final evaluation we therefore use 4096 factors (32 kB initial size): 
on GoodBooks-10k the marginal benefit of larger starting sizes is minimal, 
while on MovieLens-20M and Netflix Prize higher initial dimensionalities 
consistently lead to worse performance. This makes 4096 factors the most 
effective and stable choice across all datasets.
""")
st.markdown(gb_factors , unsafe_allow_html=True)
fig = plot_three_side_by_side(goodbooks_factors_recall_20_df, goodbooks_factors_recall_50_df, goodbooks_factors_ndcg_100_df, baselines=goodbooks_df[goodbooks_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list(), legend_title_text="Initial Embedding Size", xcol="Vector size (bytes)")
st.plotly_chart(fig, use_container_width=True)

# section with results for movielens
toc.append(st, "Results for MovieLens-20M", "ml20m")
st.markdown("""
Below we present the full experimental results for the MovieLens-20M dataset.
""")
toc.append(st, "Experimental results", "ml20m_exp", 1)
st.markdown("""
On the MovieLens-20M dataset we observe similar trends as on GoodBooks-10k, 
but with smaller gaps between methods. Low-dimensional dense ELSA performs 
reasonably well at higher budgets but degrades more quickly under aggressive 
compression. Post-hoc sparse projection again lags behind training sparsity 
from scratch. Compressed ELSA remains consistently competitive across all 
byte budgets and achieves the best performance among compressed models.
""")
st.markdown(ml_main , unsafe_allow_html=True)
toc.append(st, "Pruning strategies", "ml20m_prun", 1)
st.markdown("""On MovieLens-20M the differences between pruning schedules are smaller, 
but the overall trend mirrors the GoodBooks-10k results. Exponential and 
linear schedules (both with and without restarting) perform the most 
consistently across all byte budgets. Step-wise pruning (lottery-ticket 
style) lags behind at lower budgets, and the constant-mask baseline shows 
the strongest degradation as sparsity increases.
""")
st.markdown(ml_pruning_strategy , unsafe_allow_html=True)

fig = plot_three_side_by_side(ml20m_recall_20_lth_df, ml20m_recall_50_lth_df, ml20m_ndcg_100_lth_df, baselines=ml20m_df[ml20m_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list(), xcol="Vector size (bytes)")
st.plotly_chart(fig, use_container_width=True) 

toc.append(st, "Initial embedding sizes", "ml20m_factors", 1)
st.markdown("""
On MovieLens-20M, increasing the initial embedding size helps only up to a
point. Moving from 2048 to 4096 factors consistently improves the final
sparse model, but larger initial sizes (6144 and 8192 factors) do not yield
additional gains and even slightly degrade performance. This suggests that
MovieLens-20M benefits from moderate overparameterization during early
training, but very large initial embeddings offer no advantage and may make
optimization harder.
""")
st.markdown(ml_factors, unsafe_allow_html=True)
fig = plot_three_side_by_side(ml20m_factors_recall_20_df, ml20m_factors_recall_50_df, ml20m_factors_ndcg_100_df, baselines=ml20m_df[ml20m_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list(), legend_title_text="Initial Embedding Size", xcol="Vector size (bytes)")
st.plotly_chart(fig, use_container_width=True)

# section with results for netflix
toc.append(st, "Results for Netflix prize", "netflix")
st.markdown("""
Below we present the full experimental results for the Netflix dataset.
""")
toc.append(st, "Experimental results", "netflix_exp", 1)
st.markdown("""
On the Netflix dataset we observe the same overall pattern as on
GoodBooks-10k and MovieLens-20M, but the separation between methods is
even clearer. Low-dimensional dense ELSA degrades rapidly under stronger
compression, while post-hoc sparse projection performs the worst (except the smaller budget). 
Pruned EASE remains competitive at larger sizes but drops off at
smaller ones. Compressed ELSA is the only method that matches
the full dense ELSA baseline. The relative gaps between models are larger on Netflix than on
MovieLens, suggesting that sparsity-aware training has an even stronger
effect on Netflix dataset.
""")
st.markdown(netflix_main, unsafe_allow_html=True)

toc.append(st, "Pruning strategies", "netflix_prun", 1)
st.markdown("""
On the Netflix dataset the behavior of the pruning schedules largely mirrors
what we observed on MovieLens-20M, but the differences between methods are
even smaller. Exponential and linear schedules continue to perform the most
robustly across all compression levels, yet the gap to the step-wise
(lottery-ticket-style) methods narrows substantially. At very small vector
sizes (high sparsity), the curves nearly overlap, indicating that Netflix is
less sensitive to the exact pruning schedule than the other datasets. Overall,
frequent mask updates still offer a slight advantage, but the effect is
weaker than on GoodBooks-10k and MovieLens-20M.
""")
st.markdown(netflix_pruning_startegy, unsafe_allow_html=True)
fig = plot_three_side_by_side(netflix_recall_20_lth_df, netflix_recall_50_lth_df, netflix_ndcg_100_lth_df, baselines=netflix_df[netflix_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list(), xcol="Vector size (bytes)")
st.plotly_chart(fig, use_container_width=True) 

toc.append(st, "Initial embedding sizes", "netflix_factors", 1)
st.markdown("""
The effect of the initial embedding size on Netflix follows a pattern very
similar to MovieLens-20M. Increasing the starting dimensionality from 2048
to 4096 factors improves the final sparse model, but the performance drops
for 6144 and 8192 factors. This indicates that Netflix, like MovieLens, benefits 
from a moderately overparameterized starting space, while much larger initial
embeddings do not provide additional advantages.
""")
st.markdown(netflix_factors, unsafe_allow_html=True)
fig = plot_three_side_by_side(netflix_factors_recall_20_df,netflix_factors_recall_50_df, netflix_factors_ndcg_100_df, baselines=netflix_df[netflix_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list(), legend_title_text="Initial Embedding Size", xcol="Vector size (bytes)")
st.plotly_chart(fig, use_container_width=True)

# section on interpretability
toc.append(st, "Interpretability", "interpretability")

st.markdown("""
We evaluate interpretability on the GoodBooks-10k dataset, where rich item
metadata enables meaningful semantic segment construction.

To interpret the sparse latent space, we group items according to their
most dominant latent factor. Each item activates one latent dimension
more strongly than the others (including its sign), and all items that
share the same dominant factor form an initial group.
""")

toc.append(st, "Naming segments", "naming", 1)
st.markdown("""
For each such group, we generate a short semantic descriptor using item
metadata (title, author, year, and description).

We used `gpt-4.1-nano-2025-04-14` model via standard OpenAI API with `temperature` parameter set to 0.

Prompt for naming the most significant latents:
```
You are given a list of books, each with title, author, year, and description.

1. Identify the most common concept that links all the books (an author, genre, theme, 
   or hybrid such as romantic sci-fi).
2. Convert that concept into a segment name suitable for a recommendation system.

The segment name must be title-case, concise (2-3 words), and sound natural — like a content 
category (e.g., Romantic Comedies, Cyberpunk Thrillers, Classic Mysteries).

Output: Only the final segment name, nothing else.

Books:
```

""")

toc.append(st, "Merging segments", "merging", 1)

st.markdown("""
First, we compute embeddings for segments with the `thenlper/gte-large` sentence transformer model, available 
at [HugginFace](https://huggingface.co/thenlper/gte-large). Then, we iteratively merged segments with similarity score>=0.95 
with the following prompt:
```
You are given several segment names that describe similar types of content.
Merge them into one unified segment name that sounds natural and general enough to cover all of them.

The final name must be:
• Title-case (each main word capitalized)
• 2-3 words maximum
• Natural and human-friendly (like a content category)

Output: Only the final merged segment name.

Example Input: ["Supernatural Romance", "Supernatural Series", "Supernatural Urban Fantasy",
 "Supernatural Fiction", "Supernatural Romance", "Paranormal Romance",
 "Supernatural Fantasy", "Supernatural Suspense"]

Example Output

Supernatural Romance

Segments:
```

Each segment is then mapped back to the latent space via the set of
latent dimensions that characterize its items, allowing us to construct a
sparse segment-latent matrix. Because this matrix is compatible with the
ELSA scoring function, we can compute relevance scores for segments in
exactly the same way as for individual items, enabling unified recommendation
of both items and interpretable semantic segments from the same user
representation.
""")

toc.append(st, "Explore discovered segments", "explore", 1)

st.markdown("""
Here, you can explore the resulting segments for the GoodBooks-10k dataset. First, select a segment from the final list.
""")

items = get_items("gb10")
its=[
    {
    "id": str(row.book_id),
    "image": row.image_url,
    "title": row.original_title,
    "authors": row.authors,
    "description": row.mistral_7b[:225]+"...",
} for i,row in items.iterrows()
]


segments = load_gb_segments()
segs = {}
for k in segments.keys():
    segs[k]=[
        {
            "id": str(row.book_id),
            "image": row.image_url,
            "title": row.original_title,
            "authors": row.authors,
            "description": row.mistral_7b[:225]+"...",
        } for i,row in segments[k]["precomputed_segment_items"].iterrows()
    ]

# Build a global dict for lookup when opening the modal
ALL = {it["id"]: it for seg in segs.values() for it in seg}

seg=st.selectbox("Select segment", options=list(segs.keys()))

st.markdown("""
Now, explore the original segments that was merged into the final segment selected above.
""")

sdf=pd.DataFrame(zip(segments[seg]["similar"], segments[seg]["descriptions"]))
sdf.columns=["latent", "name"]

st.dataframe(
    sdf, 
    width="content",
    row_height=25, 
    column_config={
        "latent": st.column_config.Column("Significant Latent"),
        "name": st.column_config.Column("Name", width="large")
    }
)

st.markdown("""
Finally, see items assigned by the selected segment.
""")

for idx, (seg_title, items) in enumerate(segs.items(), start=1):
    if seg_title==seg:
        render_row(seg_title, items, row_id=f"rail_{idx}")


# render table of content
toc()