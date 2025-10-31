import streamlit as st
from utils import *

MIN_RECOMMS = 3
MAX_RECOMMS = 20
DEFAULT_RECOMMS = 10

MIN_SEGMENTS = 1
MAX_SEGMENTS = 10
DEFAULT_SEGMENTS = 3

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
items = items.set_index(items.book_id.astype(str))

# init recommender
rec = CompressedSparseElsaRecommender(A, items, items_idx, B, segments)

with st.sidebar:
    # pick a user from the list
    user_index = st.selectbox(
        label="Select user", 
        options=np.arange(X_test.shape[0]), 
        index=1488
    )
    user = X_test[user_index]

    # checkbox to show/hide user history
    show_user_history = st.checkbox("Show user history", value=True)

    # select k for recomms
    k = st.select_slider("Select number of recommendations per row", options=range(MIN_RECOMMS,MAX_RECOMMS+1), value = DEFAULT_RECOMMS)

    num_segments = st.select_slider("Select number of recommended segments", options=range(MIN_SEGMENTS,MAX_SEGMENTS+1), value = DEFAULT_SEGMENTS)

if show_user_history:
    # Show all items interacted by the user
    render_row(
        f"Interactions of the user {user_index}", 
        transform_items_for_row(
            rec.get_user_history(
                user,
            )
        ), 
        row_id=f"rail_{0}"
    )

# Standard recommendations by the Compressed Sparse ELSA model
recommended_items=rec.recommend_items(user, k=k)
render_row(
    "Recommended for you", 
    transform_items_for_row(
        recommended_items,
    ), 
    row_id=f"rail_{0}"
)
# print(set(recommended_items.book_id.to_list()))
# Get recommended segments
recommended_segments = rec.recommend_segments(user, k=num_segments)

# Render each segment and make personalized order inside the segment
i = 0
for recommended_segment, score in recommended_segments.items():
    i+=1
    render_row(
        recommended_segment, 
        transform_items_for_row(
            rec.recommend_items(
                user,
                segment=recommended_segment,
                k=k,
            ),
        ), 
        row_id=f"rail_{0}",
    )


# render table of content
toc()

