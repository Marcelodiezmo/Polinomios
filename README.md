# Polinomios
en el script llamado "traductor" podemos ver una clase llamada "traductor_a_bases" con sus respectivos metodos.
esta clase lo que hace es obtener la base de los coeficientes ordenadamente segun su exponente de un polinomio. Si se da el polinomio x^3+x^5+x+1, el
algoritmo lo recibe en este orden (1+x+x^3+5x^5),luego de esto pone sus respectivos coeficientes y sus exponentes en una lista (si el polinomio se salta un exponente, se pone 0)
                 ejemplo 1:         [1,1,0,1,0,5]
                                  

ejemplo 2:
si se lee el polinomio 6x^4+10x el resultado es : [0, 10, 0, 0, 6], el  0 indica que no hay un coeficiente sin su  grado respectivo.

en el script polinomio_poo tenemos una clase llamada "algebra" con sus respecitos metodos  especiales.
en el metodo  string_a_bases sirve para pasar string a bases usando la clase traductor'
en el metodo __call__ lo que hace es evaluar la funcion que se desee.
en el metodo  bases_a_string se hace un algoritmo en donde se lee la base que se creó en la clase "traductor_a_bases" y asi poderlo organizar, y hacer su respectiva suma de polinomios
