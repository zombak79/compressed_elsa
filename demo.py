import streamlit as st
from utils import *

MIN_RECOMMS = 3
MAX_RECOMMS = 20
DEFAULT_RECOMMS = 10

MIN_SEGMENTS = 1
MAX_SEGMENTS = 10
DEFAULT_SEGMENTS = 5

# load all data, cached inside the utils module
goodbooks_df=get_data("goodbooks")
items = get_items("gb10")
segments = load_gb_segments()
A = get_A()
B = get_B(segments)
items_idx = load_idx()
X_test = get_test_users()

# insert css for recommendation rows
init_rows_rendering()

# prepare placeholder for table of contents in the sidebar
toc = TOC(st.sidebar.empty())

# start the document
toc.append(st, "Live Demo", "demo")

st.markdown("This demo illustrates how Compressed ELSA activates sparse latent factors for a user and how these activations correspond to interpretable segments and recommended items. Use the controls on the left to switch users and toggle analysis options; the visualization updates instantly.")

items = items.set_index(items.book_id.astype(str))

# init recommender
rec = CompressedSparseElsaRecommender(A, items, items_idx, B, segments)

with st.sidebar:
    # pick a user from the list
    user_index = st.selectbox(
        label="Select a user from the test set", 
        options=np.arange(X_test.shape[0]), 
        index=1011
    )
    user = X_test[user_index]

    # checkbox to show latent space analysis
    show_analysis = st.checkbox("Show latent space analysis", value=True)

    only_active = st.checkbox("Show only latents for matching segments", value=True, disabled=not show_analysis)
    sort_latents = st.checkbox("Sort latents by matching segments", value=True, disabled=not only_active)

    # checkbox to show/hide user history
    show_user_history = st.checkbox("Show user history", value=False)

    # checkbox to show scores
    show_scores = st.checkbox("Show scores", value=False)

    # checkbox to show ids
    show_ids = st.checkbox("Show item ids", value=False)

    # select k for recomms
    k = st.select_slider("Select number of recommendations per row", options=range(MIN_RECOMMS,MAX_RECOMMS+1), value = DEFAULT_RECOMMS)

    num_segments = st.select_slider("Select number of recommended segments", options=range(MIN_SEGMENTS,MAX_SEGMENTS+1), value = DEFAULT_SEGMENTS)

# Standard recommendations by the Compressed Sparse ELSA model
recommended_items=rec.recommend_items(user, k=k)
# Get recommended segments
recommended_segments = rec.recommend_segments(user, k=num_segments)

if show_analysis:
    fig=rec.explore_user_segments(
        user, 
        list(recommended_segments.keys()), 
        user_index, 
        scores=list(recommended_segments.values()) if show_scores else None, 
        only_active=only_active,
        sort_latents=sort_latents,
    )
    st.plotly_chart(fig, use_container_width=True)

if show_user_history:
    # Show all items interacted by the user
    render_row(
        f"Interactions of the user {user_index}", 
        transform_items_for_row(
            rec.get_user_history(
                user,
            ),
            show_ids=show_ids,
            show_scores=show_scores,
        ), 
        row_id=f"rail_{0}"
    )

render_row(
    "Recommended for you", 
    transform_items_for_row(
        recommended_items,
        show_scores=show_scores,
        show_ids=show_ids,
    ), 
    row_id=f"rail_{0}"
)

# Render each segment and make personalized order inside the segment
i = 0
for recommended_segment, score in recommended_segments.items():
    i+=1

    render_row(
        f"{recommended_segment} ({score:.2f})" if show_scores else f"{recommended_segment}", 
        transform_items_for_row(
            rec.recommend_items(
                user,
                segment=recommended_segment,
                k=k,
            ),
            show_scores=show_scores,
            show_ids=show_ids,
        ), 
        row_id=f"rail_{0}",
    )

# render table of content
# toc()

