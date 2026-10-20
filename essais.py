##2.Découverte d'autograd
# À LA PLACE de l'habituel 'import numpy as np'
import autograd.numpy as np
from autograd import grad

#2.1 Domaine
X=np.linspace(0,2*np.pi,10)

#2.2 Dérivée
sin_der=np.vectorize(grad(np.sin))
print('sin_der(X)=',sin_der(X))

#2.3 Vérification

print('cos(X)=',np.cos(X))
#sin_der(X) est bien égal à np.cos(X).

##Formule de Taylor

#3.1Version 1 : dérivées fournies

from math import factorial
import matplotlib.pyplot as plt

def taylor1(X, derivatives):
    Y=np.zeros(len(X))
    for i in range (len(derivatives)):
        Y+=derivatives[i]/factorial(i)*X**i
    return Y

sinus10 = [0, 1, 0, -1, 0, 1, 0, -1, 0, 1]
X = np.linspace(-2 * np.pi, 2 * np.pi, 400)
Y1=taylor1(X,sinus10)
plt.plot(X,Y1,label="taylor1(X,sinus10)")
plt.legend()
plt.show()

#3.2 Version 2 : dérivées calculées avec autograd

def taylor2(X, f, n):
    Y=[]
    g=f
    for i in range (n+1):
        Y.append(g(0.0))
        g=grad(g)
    return taylor1(X,Y)

#1.
Y=np.sin(X)
Y2=taylor2(X,np.sin,10)
plt.plot(X,Y)
plt.plot(X,Y2,label="taylor2(X,np.sin,10)")
plt.legend()
plt.show()

#2.

#3.
Z=np.cos(X)
Z2=taylor2(X,np.cos,10)
plt.plot(X,Z)
plt.plot(X,Z2,label="taylor2(X,np.cos,10)")
plt.legend()
plt.show()

#3.3 Une fonction personnalisée

def custom(X):
    return 2*np.sin(X) + np.cos(X/4)

Y3 = custom(X)
Y4 = taylor2(X, custom, 14)
