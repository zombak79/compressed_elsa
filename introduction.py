import streamlit as st
from utils import TOC

# prepare placeholder for table of contents
toc = TOC(st.sidebar.empty())

static_content = """

# Intro

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse quis tincidunt nibh. Sed eleifend, mi ultricies hendrerit iaculis, ligula nibh ornare massa, quis tincidunt felis dui sit amet metus. Vivamus a mollis orci. Quisque quis mi ac nisl ullamcorper fermentum in consectetur ipsum. Ut sagittis consectetur nisl consequat sodales. Donec a efficitur erat. In sodales est nec eros commodo, ac feugiat quam congue. Nam metus lorem, semper a luctus et, condimentum vel quam. Aliquam tincidunt fermentum mollis.

## One

Nulla vestibulum convallis odio, eget pharetra mi laoreet a. Morbi at felis sollicitudin, fermentum felis et, ornare nibh. Vivamus tincidunt in neque at elementum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In hendrerit commodo porttitor. Pellentesque lobortis vel diam et sagittis. Proin nec posuere libero. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In faucibus mi eget sem euismod, ac rhoncus ex interdum. Integer ut metus pulvinar felis vulputate dignissim sed ultrices purus. Aenean feugiat faucibus leo sit amet convallis. Aliquam vel aliquet nunc. Donec dignissim arcu ut turpis sodales, sed ultrices justo consectetur. Vestibulum vestibulum odio diam, at placerat elit tincidunt ut.

## Two

Morbi tempor lobortis elit, in rutrum velit iaculis quis. Etiam varius sem at nibh placerat efficitur. Aenean risus urna, commodo eget nisl et, tempus imperdiet sem. Etiam ultrices eros dui, in tristique diam mattis id. Quisque lobortis vestibulum ante, non elementum lacus. Integer dignissim lacus fermentum vehicula dictum. Nullam eleifend et eros vel porta. Etiam est ante, dictum vitae placerat non, feugiat sed quam. Donec euismod condimentum orci, quis accumsan quam finibus id. Aenean rutrum pulvinar metus, a tristique tellus tincidunt vitae. Donec euismod nibh eget tristique mattis.

## Three Lines

In dui quam, lobortis ut libero et, consequat dapibus lectus. Curabitur in purus sem. Sed in orci porttitor justo convallis tempus. Donec eget sapien id mauris aliquet semper. Mauris porta quam non sem placerat, vitae laoreet leo iaculis. Fusce sapien urna, mattis ut orci sit amet, tristique blandit orci. Aenean pretium ex tincidunt condimentum iaculis. Curabitur mi nisl, consequat vel libero at, semper fringilla 

"""
toc.append_md(static_content)

st.markdown(static_content)

# render table of content
toc()
