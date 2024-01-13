import streamlit as st
import pandas as pd
from google.cloud import firestore
import matplotlib.pyplot as plt

db = firestore.Client.from_service_account_json("./serviceAccountKey.json")
docs = db.collection("penguins").stream()
penguins = []
for d in docs:
    penguins.append(d.to_dict())

species = st.sidebar.selectbox("species", ["Adelie", "Chinstrap", "Gentoo"])

df = pd.DataFrame(penguins)
df = df[df["species"]==species].reset_index(drop=True)
st.write(df)
# st.line_chart(df[["bill_length_mm","flipper_length_mm","bill_depth_mm","body_mass_g"]])
fig, ax = plt.subplots()
ax.scatter(x=df["bill_length_mm"], y=df["body_mass_g"])
st.pyplot(fig)