```python
a=("title", [3,4]) # uplet immuable
x,y=a

y.append(5) #identité de y inchangé
print(a)

a=("title", [3,4]) # uplet immuable
x,y=a
# MAIS
y+=[5] #changement d'identité ???
print(a)

```

```python
a=3
id (a)
```

```python
a+=1 #changement
id(a)
```

```python
import pygame 

clock=pygame.time.Clock

print(clock in dir())  # dir() ensmble des variables existantes
 
"Clock" in dir(pygame.time) #ensemble des variables de pygame.time
```

### Convention

```python
k=1

def f():
    k=3
    print(dir()) #liste des vaiables locales de f car appeler dans f
    print(locals()) # dictionnaire qui associe à une variable locales (clés du dictionnaire) les valeurs correspondantes
    
f()

print (k) #1

# "k" in globals() False sans le k=1 
```

```python
k=1

def f():
    print(k)
    print (k in locals())
    
f() # 1 si la fonction ne trouve pas de variable locale il va dans les variables globales pour les lires 
#(ne peut influer sur ces dernières)




```

# Influencer une variable gloable à partir d'une fonction 

```python
# influencer à partir d'une fonction une variable gloable

a=0
def f():
    
     global a
     a=42
    
f()
print (a)
    
```

# Utilisation des objets

```python
rect =(0, 0, 600, 480)
type (rect)
```

```python
import pygame
dir(pygame) # on trouve rect

```

```python
from pygame import Rect
type (Rect)
```

```python
type(int)
```

```python
rect2 = Rect(0, 0, 600, 480)

rect2.width
```

```python
rect2.height=300
rect2
```

```python
rect2.move(10,20)
```
