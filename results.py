import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from utils import *
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

goodbooks_recall_20_df=get_data("goodbooks_recall_20")
goodbooks_recall_50_df=get_data("goodbooks_recall_50")
goodbooks_ndcg_100_df=get_data("goodbooks_ndcg_100")

goodbooks_recall_20_elsa_df=get_data("goodbooks_recall_20_elsa")
goodbooks_recall_50_elsa_df=get_data("goodbooks_recall_50_elsa")
goodbooks_ndcg_100_elsa_df=get_data("goodbooks_ndcg_100_elsa")

goodbooks_factors_recall_20_df=get_data("goodbooks_factors_recall_20")
goodbooks_factors_recall_50_df=get_data("goodbooks_factors_recall_50")
goodbooks_factors_ndcg_100_df=get_data("goodbooks_factors_ndcg_100")

goodbooks_recall_20_lth_df=get_data("goodbooks_recall_20_lth")
goodbooks_recall_50_lth_df=get_data("goodbooks_recall_50_lth")
goodbooks_ndcg_100_lth_df=get_data("goodbooks_ndcg_100_lth")

# movielens
ml20m_df=get_data("ml20m")
ml20m_recall_20_df=get_data("ml20m_recall_20")
ml20m_recall_50_df=get_data("ml20m_recall_50")
ml20m_ndcg_100_df=get_data("ml20m_ndcg_100")

ml20m_recall_20_elsa_df=get_data("ml20m_recall_20_elsa")
ml20m_recall_50_elsa_df=get_data("ml20m_recall_50_elsa")
ml20m_ndcg_100_elsa_df=get_data("ml20m_ndcg_100_elsa")

ml20m_recall_20_lth_df=get_data("ml20m_recall_20_lth")
ml20m_recall_50_lth_df=get_data("ml20m_recall_50_lth")
ml20m_ndcg_100_lth_df=get_data("ml20m_ndcg_100_lth")


# netflix prize
netflix_df=get_data("netflix")

netflix_recall_20_df=get_data("netflix_recall_20")
netflix_recall_50_df=get_data("netflix_recall_50")
netflix_ndcg_100_df=get_data("netflix_ndcg_100")

netflix_recall_20_elsa_df=get_data("netflix_recall_20_elsa")
netflix_recall_50_elsa_df=get_data("netflix_recall_50_elsa")
netflix_ndcg_100_elsa_df=get_data("netflix_ndcg_100_elsa")

netflix_recall_20_lth_df=get_data("netflix_recall_20_lth")
netflix_recall_50_lth_df=get_data("netflix_recall_50_lth")
netflix_ndcg_100_lth_df=get_data("netflix_ndcg_100_lth")

number_format=st.column_config.NumberColumn(format="%.3f", width="small")
column_config = {
    "recall@20":number_format,
    "recall@50":number_format,
    "ndcg@100":number_format
}
# section with results for goodbooks
toc.append(st, "Results for GoodBooks-10k", "gb10k")

st.dataframe(goodbooks_df.reset_index(drop=True).style.apply(highlight_cells, axis=None), width="content", row_height=25, height=int(3+25)*len(goodbooks_df), column_config=column_config)

fig = plot_three_side_by_side(goodbooks_recall_20_df, goodbooks_recall_50_df, goodbooks_ndcg_100_df, baselines=goodbooks_df[goodbooks_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list(), baselines_2=goodbooks_df[goodbooks_df.method=="ease"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list())
st.plotly_chart(fig, use_container_width=True)

fig = plot_three_side_by_side(goodbooks_recall_20_elsa_df, goodbooks_recall_50_elsa_df, goodbooks_ndcg_100_elsa_df, baselines=goodbooks_df[goodbooks_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list(), legend_title_text="Factors", xcol="compression_rate")
st.plotly_chart(fig, use_container_width=True)

fig = plot_three_side_by_side(goodbooks_factors_recall_20_df, goodbooks_factors_recall_50_df, goodbooks_factors_ndcg_100_df, baselines=goodbooks_df[goodbooks_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list(), legend_title_text="Factors")
st.plotly_chart(fig, use_container_width=True)

fig = plot_three_side_by_side(goodbooks_recall_20_lth_df, goodbooks_recall_50_lth_df, goodbooks_ndcg_100_lth_df, baselines=goodbooks_df[goodbooks_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list())
st.plotly_chart(fig, use_container_width=True)


# section with results for movielens
toc.append(st, "Results for MovieLens-20M", "ml20m")

st.dataframe(ml20m_df.reset_index(drop=True).style.apply(highlight_cells, axis=None), width="content", row_height=25, height=int(3+25)*len(ml20m_df),column_config=column_config)
fig = plot_three_side_by_side(ml20m_recall_20_df, ml20m_recall_50_df, ml20m_ndcg_100_df, baselines=ml20m_df[ml20m_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list())
st.plotly_chart(fig, use_container_width=True)

fig = plot_three_side_by_side(ml20m_recall_20_elsa_df, ml20m_recall_50_elsa_df, ml20m_ndcg_100_elsa_df, baselines=ml20m_df[ml20m_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list(), legend_title_text="Factors", xcol="compression_rate")
st.plotly_chart(fig, use_container_width=True)

fig = plot_three_side_by_side(ml20m_recall_20_lth_df, ml20m_recall_50_lth_df, ml20m_ndcg_100_lth_df, baselines=ml20m_df[ml20m_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list())
st.plotly_chart(fig, use_container_width=True) 


# section with results for goodbooks
toc.append(st, "Results for Netflix prize", "netflix")

st.dataframe(netflix_df.reset_index(drop=True).style.apply(highlight_cells, axis=None), width="content", row_height=25, height=int(3+25)*len(netflix_df),column_config=column_config)
fig = plot_three_side_by_side(netflix_recall_20_df, netflix_recall_50_df, netflix_ndcg_100_df, baselines=netflix_df[netflix_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list())
st.plotly_chart(fig, use_container_width=True)

fig = plot_three_side_by_side(netflix_recall_20_elsa_df, netflix_recall_50_elsa_df, netflix_ndcg_100_elsa_df, baselines=netflix_df[netflix_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list(), legend_title_text="Factors", xcol="compression_rate")
st.plotly_chart(fig, use_container_width=True)

fig = plot_three_side_by_side(netflix_recall_20_lth_df, netflix_recall_50_lth_df, netflix_ndcg_100_lth_df, baselines=netflix_df[netflix_df.method=="baseline"][["recall@20",	"recall@50",	"ndcg@100"]].iloc[0].to_list())
st.plotly_chart(fig, use_container_width=True) 

# section on interpretability
toc.append(st, "Interpretability", "interpretability")

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

for idx, (seg_title, items) in enumerate(segs.items(), start=1):
    if seg_title==seg:
        render_row(seg_title, items, row_id=f"rail_{idx}")


# render table of content
toc()