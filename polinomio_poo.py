# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:04:25 2020

@author: chelo
"""


from traductor import Traductor_a_bases

class Algebra:
    def __init__(self,string=None,bases=None):
        self.string=string
        self.bases=bases
        if self.bases is None:
            self.string_a_bases()
        self.string_limpio=self.bases_a_string()
            
    def string_a_bases(self):
        ''' este metodo sirve para pasar string a bases usando la clase traductor'''
        traductor=Traductor_a_bases()
        self.bases=traductor.traducir(self.string)
        

    def __add__(self,other):
        tamaño_largo=max(len(self.bases),len(other.bases))   
        bases_resultado=[]
        for i in range(tamaño_largo):
            coeficiente=0
            if i<len(self.bases):
                coeficiente=coeficiente+self.bases[i]
            if i<len(other.bases):
                coeficiente=coeficiente+other.bases[i]
            bases_resultado.append(coeficiente)
      
        nuevo_polinomio=Algebra(bases=bases_resultado)
        return nuevo_polinomio     
    def __str__(self):
        return self.string_limpio
    def __call__(self,valor):
        resultado=0
        for i in range(len(self.bases)):
            resultado=resultado+valor**i*self.bases[i]        
        return resultado
    def __mul__(self,other):
         bases1 = self.bases
         bases2 = self.bases
         print("multiplicando")       
    def bases_a_string(self):
        string=''
        contador=0
        for i in self.bases :
            if i!=0:
                if contador==0:
                    string+=str(i)
                elif contador==1:
                    if  i<0:
                        string+=str(i)+'x'
                    else:
                        
                        string+="+"+str(i)+'x'
                else:
                    if i<0:
                      string+=str(i)+'x^'+str(contador)
                    else:
                         string+="+"+str(i)+'x^'+str(contador)
            contador+=1
        return string
    
    def funcion(base1,base2):
        bases = [0] * maximo_exponente_que_salga_de_la_multiplicacion
        for i in range(len(base1)):
            for j in range(len(base2)):
                 bases[nueva_posicion] += base1[i] + base2[j]
        return bases
                
                


       
a="6x^3-5x^2+2x-1"  
b="6x^4+10x" 
"1+12x+5x^2+6x^3+6x^2"
polinomio1 =Algebra(a)
polinomio2=Algebra(b)
polinomio3=polinomio2+polinomio1


print("polinomio uno :" , polinomio1)
print("polinimio dos :", polinomio2)
print("resultado de la suma de polinomio  :", polinomio3)
print("evaluacion del polinomio : " ,     polinomio1(2))



polinomio3=polinomio2*polinomio1
