import streamlit as st

# Define the pages
page_1 = st.Page("storage_organisation.py", title="Book Storage and Organization", icon="📚")
page_2 = st.Page("search_retrieval.py", title="Book Search and retrieval", icon="🔍")
page_3 = st.Page("data_analysis.py", title="Insights", icon="📈")

# Set up navigation
pg = st.navigation([page_1, page_2, page_3])

# Run the selected page
pg.run()