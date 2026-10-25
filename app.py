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
#le script est exécuté plusieurs fois quand on déplace le slider.

##4. L'application : widgets et graphique

#4.1 Préparer app.py
import streamlit as st
import autograd.numpy as np
from autograd import grad
from math import factorial
import matplotlib.pyplot as plt
[]
def taylor1(X, derivatives):
    Y=np.zeros(len(X))
    for i in range (len(derivatives)):
        Y+=derivatives[i]/factorial(i)*X**i
    return Y

def taylor2(X, f, n):
    Y=[]
    g=f
    for i in range (n+1):
        Y.append(g(0.0))
        g=grad(g)
    return taylor1(X,Y)

def custom(X):
    return 2*np.sin(X) + np.cos(X/4)

#4.2 Catalogue de fonctions
FONCTIONS={"sin":np.sin,"cos":np.cos,"exp":np.exp, "ln(1+x)": lambda x: np.log(1+x),"custom":custom}

#4.3 Widgets dans la barre latérale
with st.sidebar: 
    fonction = st.selectbox("choisir la fonction",list(FONCTIONS.keys()))
    n=st.slider("ordre n",0,10,3)
    largeur=st.slider("largeur de l'intervalle",2.0,20.0,12.6)

#4.4 Calculs et tracé
f=FONCTIONS[fonction]
X=np.linspace(-largeur/2,largeur/2,400)
Y=f(X)
Y_taylor=taylor2(X,f,n)
plt.figure()
plt.plot(X,Y,label="f")
plt.plot(X,Y_taylor,label="taylor")
plt.legend()
st.pyplot(plt.gcf()) #on met plt.gcf() pour récuperer la figure courante

#Question:Pour n fixé, la qualité de l'approximation quand on s'éloigne de 0 diminue (les courbes finissent par ne plus correspondre).
#Quand on augmente n, au-delà de |x|=1, l'approximation de ln(1+x) diverge vers +infini ou -infini (alors que la fonction reste à 0)

##5.Qualité de l'approximation

#5.1 Taux de coïncidence
def taux_coincidence(Y,Y_taylor,seuil):
    return np.mean(np.abs(Y-Y_taylor)<=seuil)*100

seuils = [10**(-6), 10**(-5), 10**(-4), 10**(-3), 10**(-2)]
with st.sidebar:
    seuil=st.select_slider("Seuil",seuils,10**(-3)) 

#Question : Pour ln(1+x), une comparaison avec nan renvoie False.
#Quand l'intervalle contient des x<=1, le taux de coincidence baisse (car la comparaison renvoie False pour les valeurs hors du domaine de définition de notre fonction).

#5.2 Courbe d'erreur
erreur=st.checkbox("Afficher l'erreur")

if erreur:
    erreur=np.abs(Y-Y_taylor)
    plt.figure()
    plt.plot(X,erreur,label="|f(x)-Pn(x)|")
    plt.legend()
    st.pyplot(plt.gcf())

##6.Comparer plusieurs ordres
#on stocke les ordres dans une liste
if "ordres" not in st.session_state:
    st.session_state.ordres=[]

#ajout du bouton "Ajouter cet ordre à la comparaison"
with st.sidebar:
    if st.button("Ajouter cet ordre à la comparaison"): #on cré le bouton
        if n not in st.session_state.ordres:
            st.session_state.ordres.append(n)
    if st.button ("Réinitialiser"): #on cré un second bouton "Réinitialiser"
        st.session_state.ordres=[]
#on trace tous les ordres sélectionnés
plt.figure()
for k in st.session_state.ordres:
    Yk=taylor2(X,f,k)
    plt.plot(X,Yk,label=f"P{k}") #f devant les guillements pour transformer le texte en une f-string (chaîne de caractères formatée)
plt.legend()
st.pyplot(plt.gcf())