##1.Découverte de Streamlit

#1.1Première application
import streamlit as st

st.title("Approximation de Taylor")
st.write("Bienvenue dans votre outil de visualisation.")

#1.2Afficher une formule
st.latex(r''' sum_{k=0}^{n} \frac{f^{(k)}(0)}{k!} (x)^k ''')


#1.3 Modèle d'exécution
#valeur = st.slider("Choisissez une valeur", 0, 10)
#st.write("Vous avez choisi :", valeur)


