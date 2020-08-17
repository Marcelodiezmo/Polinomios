# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 18:05:19 2020

@author: chelo
"""
import numpy as np
import re

class Traductor_a_bases:
    @staticmethod
    def listar(a):
        templetra = ''
        tempnumero = ''
        tempexponente = ''
        caracteres = []
        
        for x in range(len(a)):
            #preguntar si el caracter es número
            if a[x].isnumeric() == True:
                #validar que no llegamos al final
                if x+1 < len(a):       
                    #validando números que despues tenga otros numeros
                    if a[x+1].isnumeric() == True and tempnumero == '' and tempexponente == '':
                        tempnumero = tempnumero + a[x]
                    #validando numeros que despues tengan una letra y que atras de ellos no tenga numeros    
                    elif a[x+1].isnumeric() == False and tempnumero == '' and tempexponente == '':
                        caracteres.append(a[x])
                    #validando numeros que despues tengan una letra y que antes si tengan un número
                    elif a[x+1].isnumeric() == False and tempnumero != '' and tempexponente == '':
                        tempnumero = tempnumero + a[x]
                        caracteres.append(tempnumero)
                        tempnumero = ''
                    #validando cuando el tiene el exponente en si
                    elif a[x+1].isnumeric() == True and tempexponente != '':
                        tempexponente = tempexponente + a[x]
                    #validando cuando el tiene el exponente en si y despues sigue un +
                    elif a[x+1].isnumeric() == False and tempexponente != '':
                        tempexponente = tempexponente + a[x]
                        caracteres.append(templetra + tempexponente)
                        templetra = ''
                        tempexponente = ''
                #ultimo caracter numerico        
                else:
                    #validar si termina asi: x^#
                    if templetra != '' and tempexponente != '':
                        caracteres.append(templetra + tempexponente + a[x])
                        templetra = ''
                        tempexponente = ''
                    #validar si termina asi: 12#
                    elif templetra == '' and tempexponente == '' and tempnumero != '':
                        caracteres.append(tempnumero + a[x])
                        tempnumero = ''
                    #validar si termina asi: #
                    elif templetra == '' and tempexponente == '' and tempnumero == '':
                        caracteres.append(a[x])
        
                    
                
            #validando los que son letras x,+,^
            else:    
                if a[x] == '^':
                    tempexponente = tempexponente + a[x]  
                elif a[x] != '+' and a[x] != '-' and a[x] != '^' and x < len(a) - 1:
                    templetra = templetra + a[x]
                #validamos un + y que tenga datos en templetra
                elif (a[x] == '+' or a[x] == '-') and templetra != '':
                    caracteres.append(templetra)
                    caracteres.append(a[x])
                    templetra = ''
                elif (a[x] == '+' or a[x] == '-') and templetra == '':
                    caracteres.append(a[x])
                #validar cuando termina en xy[letra]
                elif a[x] != '+' and a[x] != '-' and a[x] != '^' and x == len(a) - 1 and templetra != '':
                    caracteres.append(templetra + a[x])
                    templetra = ''
                #validar cuando termina en 123[letra]
                elif a[x] != '+' and a[x] != '-' and a[x] != '^' and x == len(a) - 1 and templetra == '' and tempnumero != '':
                    caracteres.append(tempnumero + a[x])
                    tempnumero = ''
                #validar cuando termina en [letra] solamente y es el ultimo
                elif a[x] != '+' and a[x] != '-' and a[x] != '^' and x == len(a) - 1 and templetra == '' and tempnumero == '':
                    caracteres.append(a[x])
                
        return caracteres 
        
    @staticmethod
    def bases(concatenado_b):
        diccionario={}
        for i in range(len(concatenado_b)):
            if "x" in concatenado_b[i]:
                posicion_x=concatenado_b[i].find("x")
                intento_base=concatenado_b[i][:posicion_x]
                if len(intento_base)==0:
                    base=1
                elif len(intento_base)==1:
                    if intento_base=="+":
                        base=1
                    elif   intento_base=="-":
                        base=-1
                    else:
                        base=int(intento_base)
                else:
                    base=int(intento_base)
                
                if "^" in concatenado_b[i]:              
                    posicion_mas=+concatenado_b[i].find("^")+1
                    exponente=int(concatenado_b[i][posicion_mas:])
                    diccionario[exponente]=base                
                else:   
                    diccionario[1]=base                
            else:       
                diccionario[0]=int(concatenado_b[i])  
        max(diccionario)
        bases=[0]*(max(diccionario)+1)
        for k,v in diccionario.items():
            bases[k]=v
      
    
        return bases
    @staticmethod
    def conc_resta(bases_uno):
        i=0
        x=0
        for i in range(len(bases_uno)):  
            if i<len(bases_uno):
                if  bases_uno[i][x].find("-")!=-1:
                
               
                    bases_uno[i+1][x]=bases_uno[i][x]+bases_uno[i+1][x]
                    bases_uno.pop(i)
        return bases_uno
    
    
    
    @staticmethod
    def concatenar(bases):
        concatenado=[] 
        x=0
        
        for i in range(len(bases)):
           
            if len(bases[i])==1:
                if bases[i][x]!="+":
                 concatenado.append(bases[i][x])
                 
            else:
                    concatenado.append("".join(bases[i]))
                    
        return concatenado
    
    
    def traducir(self,string):
        uno=re.split('([-+])',string)

        bases_uno=[]
        for i in uno:
            bases_uno.append(self.listar(i))
        
      
        bases_uno=traductor.conc_resta(bases_uno)
        concatenado=traductor.concatenar(bases_uno)
        resultado_bases_total=traductor.bases(concatenado)
        return resultado_bases_total
        
    




        
traductor=Traductor_a_bases()
#a="6x^3+5x^2-2x-1+2x^5-3x"  
b="6x^4-10x+5" 
