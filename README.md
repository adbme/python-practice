# python-practice

![preview](https://user-images.githubusercontent.com/98839796/227801190-b74be45a-5be0-430e-b749-307c1e5d0d13.png)

## doc :

deux manière différentes pour importer tkinter en module

- la première :

``` PYTHON
import tkinter as tk
```
ça permet d'accéder aux fonctions et aux classe de tkinter sans importer tout de base, exemple :
``` PYTHON
menu1 = tk.Menu(root)
```
Pour faire un menu tkinter on y accéde par le préfixe **.tk**

- la deuxième :
``` PYTHON
from tkinter import *
```
On importe globalement tkinter (*) et il peut y avoir peut etre des conflits de noms ou autres problèmes. Donc le menu sera deja reconnu par tkinter : 
``` PYTHON
menu1 = Menu(fenetre)
```
A la place d'un add cascade qui ajoute un sous menu on fait la méthode add command qui quand on clique sur l'option "app 1" lance une fonction :
``` PYTHON
menu1.add_command(label="app 1", command=hello)
```