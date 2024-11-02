
import os

import streamlit as st

st.set_page_config(page_title="Beispiele", page_icon="🕗")

st.markdown("# Beispiele")

#txt_dateien = os.listdir("/data")

liste_personen = ["Paul", "Anna", "Dieter", "Karl", "Sabrina", "Wiebke"]
liste_obst = ["Apfel", "Birne", "Pflaume", "Banane", "Orange"]
liste_staedte = ["Berlin", "München", "Hamburg", "Köln", "Frankfurt", "Dortmund", "Leipzig"]

auswahl_person = st.selectbox("Bitte eine Person auswählen", liste_personen)
auswahl_obst = st.selectbox("Bitte eine Obstsorte auswählen", liste_obst)
auswahl_stadt = st.selectbox("Bitte eine Stadt auswählen", liste_staedte)

if auswahl_person in ["Paul", "Dieter", "Karl"]:
  geschlecht = "Er"
else:
  geschlecht = "Sie"

st.write(f"{auswahl_person} kommt aus {auswahl_stadt}. {geschlecht} isst gerne {auswahl_obst}.")
