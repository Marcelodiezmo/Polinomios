# Polinomios
en el script llamado "traductor" podemos ver una clase llamada "traductor_a_bases" con sus respectivos metodos.
esta clase lo que hace es obtener la base de los coeficientes ordenadamente segun su exponente de un polinomio. Si se da el polinomio x^3+x^5+x+1, el
algoritmo lo recibe en este orden (1+x+x^3+5x^5),luego de esto pone sus respectivos coeficientes y sus exponentes en un diccionario (si el polinomio se salta un exponente, se pone 0

 ejemplo 1: 
  ```
 traductor=Traductor_a_bases()
 b="6x^4-10x+5" 
 print(traductor.traducir(b))
 ```

 resultado:
  ```
 [5, -10, 0, 0, 6]
  ```
  el indice del diccionario va los exponentes y el valor el coeficiente

 la clase Algebra dara uso de la clase traductor.                                 


en el script polinomio_poo tenemos una clase llamada "algebra" con sus respectivos metodos  especiales.
en el metodo  string_a_bases sirve para pasar string a bases usando la clase 'traductor'
en el metodo __call__ lo que hace es evaluar la funcion que se desee.
en el metodo  bases_a_string se hace un algoritmo en donde se lee la base que se creó en la clase "traductor_a_bases" y asi poderlo organizar, y hacer su respectiva suma de polinomios

ejemplo 2:
 ```
polinomio1=Algebra()
a="6x^3-5x^2+2x-1"  
b="6x^4+10x" 
"1+12x+5x^2+6x^3+6x^2"
polinomio1 =Algebra(a)
polinomio2=Algebra(b)
 ```
 asi se podria instanciar polinomios, la clase algebra internamente convierte el string a bases usando la clase traductor_a_bases
 
 ejemplo  3:
 si se ejecuta el codigo:
 print(polinomio1) saldra lo siguiente :  -1+2x-5x^2+6x^3
 
 ejemplo 4:
 si se ejecuta el siguiente codigo se podra imprimir la suma de dos polinomios
 ```
 polinomio3=polinomio2+polinomio1
 print(polinomio3)
 resultado : -1+12x-5x^2+6x^3+6x^4
 
 ```
