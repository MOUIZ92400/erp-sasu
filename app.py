import streamlit as st
import pandas as pd

# Titre de l'application
st.set_page_config(page_title="ERP SASU Mobile", page_icon="📊")
st.title("📊 Mon ERP SASU")

# Menu de navigation
menu = ["Saisie de Stock", "Consulter l'Inventaire"]
choix = st.sidebar.selectbox("Menu", menu)

if choix == "Saisie de Stock":
    st.subheader("📦 Ajouter un produit")
    with st.form("form1"):
        produit = st.text_input("Nom du produit")
        quantite = st.number_input("Quantité", min_value=0)
        prix = st.number_input("Prix d'achat (€)", min_value=0.0)
        valider = st.form_submit_button("Enregistrer")
        
        if valider:
            st.success(f"Enregistré : {quantite} x {produit}")

elif choix == "Consulter l'Inventaire":
    st.subheader("🔎 État du stock")
    st.info("La connexion Google Sheets sera la prochaine étape !")
  
