import streamlit as st
from st_files_connection import FilesConnection
conn = st.connection('gcs', type=FilesConnection)
df = conn.read("first_gcs0/myfile.csv", input_format="csv", ttl=600)

for row in df.itertuples():
    st.write(f"{row.Owner} has a : {row.Pet}")