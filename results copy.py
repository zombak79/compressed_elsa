import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from utils import TOC
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go
import html as pyhtml


RESTORE_JS = """
<script>
(function() {
  try {
    // Restore vertical page scroll
    const y = sessionStorage.getItem('page_scroll_y');
    if (y !== null) window.scrollTo(0, parseInt(y, 10));

    // Restore each carousel's horizontal scroll by id
    const raw = sessionStorage.getItem('carousel_scroll');
    if (raw) {
      const map = JSON.parse(raw);
      Object.entries(map).forEach(([id, x]) => {
        const el = document.getElementById(id);
        if (el) el.scrollLeft = x;
      });
    }
  } catch(e) { /* ignore */ }
})();
</script>
"""
components.html(RESTORE_JS, height=0)

@st.cache_data
def get_data(dataset: str):
    return pd.read_feather(f"data/{dataset}_df.feather")

@st.cache_data
def get_items(dataset: str):
    return pd.read_feather(f"data/{dataset}_items.feather")

def highlight_cells(x):
    df_styled = x.copy()
    # Default: no style
    df_styled = pd.DataFrame('', index=x.index, columns=x.columns, dtype=object)
    
    # Highlight specific cells (by condition or coordinates)
    for i in range(len(df_styled)):
        j = (i-1)//3
        if j%2 == 0:
            df_styled.iloc[i, :] += 'background-color: #f0f8ff;'
        else:
            df_styled.iloc[i, :] += 'background-color: white;'

        if (i)%3 == 1:
            for c in x.columns:
                if x[c].dtype=="float":
                    sub_series = df_styled[c].iloc[i:i+3]
                    sub_series.iloc[sub_series.argmax()]+= 'font-weight: bold;'
    return df_styled

def plot_three_side_by_side(df1, df2, df3, titles=("Recall@20","Recall@50","NDCG@100")):
    # Collect method names (all columns except 'nnz')
    # normalize once
    (df1, df2, df3), cat_str = normalize_x_as_reversed_categories(
        df1, df2, df3
    )
    def methods(df): return [c for c in df.columns if c not in ["nnz", "nnz_cat"]]
    all_methods = list(dict.fromkeys(methods(df1) + methods(df2) + methods(df3)))  # stable order

    # Consistent colors across all panels
    palette = px.colors.qualitative.Set2 + px.colors.qualitative.D3
    color_map = {m: palette[i % len(palette)] for i, m in enumerate(all_methods)}

    fig = sp.make_subplots(rows=1, cols=3, subplot_titles=titles)

    for i, df in enumerate([df1, df2, df3], start=1):
        for m in all_methods:
            if m not in df.columns:
                continue  # method not present in this DF
            fig.add_trace(
                go.Scatter(
                    x=df["nnz_cat"], y=df[m],
                    mode="lines+markers",
                    name=m if i == 1 else m,     # name is required for legendgroup
                    showlegend=(i == 1),         # ONLY show legend in the first subplot
                    legendgroup=m,               # link traces across subplots
                    line=dict(color=color_map[m]),
                    marker=dict(color=color_map[m]),
                    hovertemplate = f"nnz=%{{x}}<br>%{{y:.4f}}<extra>{m}</extra>"
                ),
                row=1, col=i
            )
        #fig.update_xaxes(autorange="reversed", tickvals=[128, 64, 32, 16, 8], title_text="nnz", row=1, col=i)
        fig.update_yaxes(title_text="Score", row=1, col=i)
        fig.update_xaxes(type="category", categoryorder="array",
                     categoryarray=cat_str, tickangle=0, title_text="nnz",
                     row=1, col=i)

    fig.update_layout(
        height=420, width=1200,
        legend_title_text="Method",
        title_text="",
        margin=dict(l=40, r=20, t=60, b=40)
    )
    return fig

def normalize_x_as_reversed_categories(*dfs, xcol="nnz"):
    # collect all x values across dfs, make one global reversed order
    cats = sorted(
        {int(v) for df in dfs for v in df[xcol].unique()},
        reverse=True
    )
    cat_str = [str(v) for v in cats]

    out = []
    for df in dfs:
        df = df.copy()
        df["nnz_cat"] = pd.Categorical(
            df[xcol].astype(int).astype(str),
            categories=cat_str,
            ordered=True
        )
        out.append(df)
    return out, cat_str


# prepare placeholder for table of contents
toc = TOC(st.sidebar.empty())

# read the data
goodbooks_df=get_data("goodbooks")
goodbooks_recall_20_df=get_data("goodbooks_recall_20")
goodbooks_recall_50_df=get_data("goodbooks_recall_50")
goodbooks_ndcg_100_df=get_data("goodbooks_ndcg_100")

ml20m_df=get_data("ml20m")
ml20m_recall_20_df=get_data("ml20m_recall_20")
ml20m_recall_50_df=get_data("ml20m_recall_50")
ml20m_ndcg_100_df=get_data("ml20m_ndcg_100")


# section with results for goodbooks
toc.append(st, "Results for GoodBooks-10k", "gb10k")

st.dataframe(goodbooks_df.reset_index(drop=True).style.apply(highlight_cells, axis=None), row_height=25, height=int(3+25)*len(goodbooks_df))
fig = plot_three_side_by_side(goodbooks_recall_20_df, goodbooks_recall_50_df, goodbooks_ndcg_100_df)
st.plotly_chart(fig, use_container_width=True)


# section with results for movielens
toc.append(st, "Results for MovieLens-20M", "ml20m")

st.dataframe(ml20m_df.reset_index(drop=True).style.apply(highlight_cells, axis=None), row_height=25, height=int(3+25)*len(goodbooks_df))
fig = plot_three_side_by_side(ml20m_recall_20_df, ml20m_recall_50_df, ml20m_ndcg_100_df)
st.plotly_chart(fig, use_container_width=True)


# section on interpretability
toc.append(st, "Interpretability", "interpretability")

items = get_items("gb10")
row=items.iloc[0][["original_title","authors","image_url","qwen2_7b_raw"]]
item = {
    "image": row.image_url,
    "title": row.original_title,
    "authors": row.authors,
    "description": row.qwen2_7b_raw,
}

its=[
    {
    "id": row.book_id,
    "image": row.image_url,
    "title": row.original_title,
    "authors": row.authors,
    "description": row.qwen2_7b_raw,
} for i,row in items.iterrows()
]

CARD_HTML = f"""
<style>
.card {{
  width: 220px; border-radius: 12px;
  background: #ffffff10; box-shadow: 0 2px 6px rgba(0,0,0,0.15);
  overflow: hidden; font-family: sans-serif;
}}
.card img {{
  width: 100%; height: 124px; object-fit: cover;
  border-top-left-radius: 12px; border-top-right-radius: 12px;
}}
.card-body {{ padding: 8px 10px 10px 10px; color: #333; }}
.card-title {{
  margin: 4px 0 2px 0; font-weight: 600; font-size: 0.95rem;
  overflow: hidden; white-space: nowrap; text-overflow: ellipsis;
}}
.card-sub {{ font-size: 0.8rem; color: #666; }}
.card-meta {{ font-size: 0.6rem; color: #888; margin-top: 4px; }}
.card a {{ color: inherit; text-decoration: none; }}
</style>

<div class="card">

    <img src="{item['image']}" alt="{item['title']}">
    <div class="card-body">
      <div class="card-title" title="{item['title']}">{item['title']}</div>
      <div class="card-sub">{item['authors']}</div>
      <div class="card-meta">{item['description']}</div>
    </div>

</div>
"""

components.html(CARD_HTML, height=240)


# ---------- dialog ----------
@st.dialog("Details", width="large")
def show_detail(it):
    st.image(it["image"], use_container_width=True)
    st.markdown(f"### {it['title']}")
    st.caption(it["authors"])
    st.write(it["description"])

    def _close():
        # Clear the ?open=... param and rerun
        try:
            st.query_params.clear()
        except Exception:
            st.experimental_set_query_params()
        st.rerun()

    st.button("Close", on_click=_close)


# ---------- html row renderer (horizontal scroll with arrows) ----------
def render_row(title, items, row_id: str):
    cards = []
    for it in items:
        t = pyhtml.escape(it["title"])
        a = pyhtml.escape(it["authors"])
        # IMPORTANT: link to ?open=<id> to trigger the dialog
        cards.append(f"""
        <a class="card" href="javascript:void(0)" onclick="openDetail('{row_id}','{it['id']}')" title="{t}">
          <img src="{it['image']}" alt="{t}">
          <div class="card-body">
            <div class="card-title">{t}</div>
            <div class="card-sub">{a}</div>
          </div>
        </a>
        """)

    block = f"""
    <style>
    .row-wrap {{ margin: 8px 0 22px 0; }}
    .row-title {{ font-weight: 700; font-size: 1.1rem; margin: 4px 0 8px 0; }}
    .carousel-wrap {{ position: relative; }}
    .carousel {{
        display: flex; gap: 14px; overflow-x: auto; overflow-y: hidden;
        scroll-snap-type: x mandatory; padding: 4px 36px; scroll-behavior: smooth;
    }}
    .card {{
        flex: 0 0 auto; width: 220px; scroll-snap-align: start;
        border-radius: 12px; background: #fff; color: #222;
        box-shadow: 0 2px 8px rgba(0,0,0,0.12); text-decoration: none;
    }}
    .card img {{ width: 100%; height: 124px; object-fit: cover;
        border-top-left-radius: 12px; border-top-right-radius: 12px; }}
    .card-body {{ padding: 8px 10px 10px 10px; }}
    .card-title {{ font-weight: 600; font-size: .95rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
    .card-sub {{ font-size: .8rem; color: #666; }}

    .arrow {{
        position: absolute; top: 50%; transform: translateY(-50%);
        width: 28px; height: 28px; border-radius: 50%; border: 0;
        background: #fff; box-shadow: 0 2px 8px rgba(0,0,0,.2);
        display:flex; align-items:center; justify-content:center; cursor:pointer;
        user-select:none;
    }}
    .left {{ left: 4px; }} .right {{ right: 4px; }}
    </style>

    <div class="row-wrap">
      <div class="row-title">{pyhtml.escape(title)}</div>
      <div class="carousel-wrap">
        <button class="arrow left"  onclick="document.getElementById('{row_id}').scrollBy({{left:-600,behavior:'smooth'}})">&#8249;</button>
        <div class="carousel" id="{row_id}">
          {''.join(cards)}
        </div>
        <button class="arrow right" onclick="document.getElementById('{row_id}').scrollBy({{left:600,behavior:'smooth'}})">&#8250;</button>
      </div>
    </div>
    <script>
      // Save positions and open detail via parent query param
      function openDetail(rowId, itemId) {{
        try {{
          // Save vertical page scroll (in the parent document)
          sessionStorage.setItem('page_scroll_y', window.parent.scrollY.toString());

          // Save horizontal scroll for all carousels present
          const carousels = window.document.querySelectorAll('.carousel[id]');
          const map = {{}};
          carousels.forEach(el => map[el.id] = el.scrollLeft);
          sessionStorage.setItem('carousel_scroll', JSON.stringify(map));

          // Update parent URL without losing history state
          const url = new URL(window.parent.location.href);
          url.searchParams.set('open', itemId);
          window.parent.location.href = url.toString();  // navigate (triggers rerun)
        }} catch (e) {{
          // Fallback: simple navigation
          window.parent.location.search = '?open=' + encodeURIComponent(itemId);
        }}
      }}
    </script>
    """
    # Taller height so arrows + row fit comfortably
    components.html(block, height=260, scrolling=False)

st.markdown("## 🎬 Netflix-style rows + native Streamlit modal")

# render a couple of rows
render_row("Because you liked Sci-Fi", its[:10], "0")

# ---------- open dialog if query param is present ----------
# Works with both new and old Streamlit APIs
try:
    params = st.query_params
    open_id = params.get("open")
except Exception:
    params = st.experimental_get_query_params()
    open_id = params.get("open", [None])
    open_id = open_id[0] if isinstance(open_id, list) else open_id

st.write(open_id)

if open_id:
    # find the item by id and show modal
    by_id = {str(it["id"]):it for it in its}
    it = by_id.get(open_id)
    if it:
        st.write("detail")
        show_detail(it)
print(open_id)
# render table of content
toc()