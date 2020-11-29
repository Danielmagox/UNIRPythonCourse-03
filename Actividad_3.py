#!/usr/bin/env python
# coding: utf-8

# En la siguiente celda, completa los siguientes ejercicios:
# 
# ## Ejercicio 1
# 
# Escribe una clase llamada Numero. Esta clase debe tener una constructora que reciba un número y almacene ese número en 2 atributos: romano que almacenará el número en el formato de número romanos como una cadena de caracteres y normal que guardará el número que nos han dado en la constructora.
# 
# ## Ejercicio 2
# Crea dos nuevos métodos en la clase Numero. El primer método, llamado imprime() imprime un mensaje mostrando el valor de ambos atributos; el segundo atributo, suma_romano() tendrá como parámetros una cadena de caracteres que representará otro número romano y que sumaremos a los atributos que ya teníamos.
# 
# ## Ejercicio 3
# 
# Define una función dentro de la clase Numero que a partir de una cadena de caracteres, devuelve True si esa cadena de caracteres corresponde con un número romano y falso en caso contrario. Después, modifica el método para que lance un error en el caso de que el valor que nos pasan por parámetro no se corresponde con el patrón de un número romano

# In[ ]:


import re


# In[ ]:


class Numero:
    def __init__(self,numero):
        self.normal = numero
        self.romano = self.numero_to_romano(numero)

    def numero_to_romano(self,num):
        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
    
    def romano_to_numero(self,s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in roman:
                num+=roman[s[i:i+2]]
                i+=2
            else:
                num+=roman[s[i]]
                i+=1
        return num
    
    def imprime(self):
        print(self.normal,self.romano)
        
    def suma_romano(self,num_romano):
        try:
            num_a_sumar = self.romano_to_numero(num_romano)
            self.normal = num_a_sumar + self.normal
            self.romano =  self.numero_to_romano(self.normal)
            return self.romano
        except:
            print("Ha fallado el número", num_romano)
    
    def is_romano(self,roman_number):
        regex = re.compile("^M{0,4}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$")
        if regex.match(roman_number):
            return True
        else:
            return False


# En la siguiente celda, completa los siguientes ejercicios:
# 
# ## Ejercicio 4
# 
# Implementa una clase MejorNumero. Esta clase heredará las propiedades de Numero e incluirá dos métodos nuevos para restar y multiplicar los atributos recibiendo por parámetro otro número romano.
# 
# ## Ejercicio 5
# 
# En la clase MejorNumero, crea un nuevo método que reciba una lista con 3 números romanos. A continuación, iterando sobre los elementos de la lista llamará a la función suma_romano(). Los posibles errores se tendrán que gestionar con excepciones para mostrar un mensaje y seguir ejecutando el siguiente número.

# In[ ]:


class MejorNumero(Numero):
    def __init__(self,numero):
        Numero.__init__(self,numero)
    
    def resta(self,num_romano):
        num_a_restar = self.romano_to_numero(num_romano)
        self.normal = self.normal - num_a_restar
        self.romano =  self.numero_to_romano(self.normal)
        return self.romano
    
    def multiplica(self,num_romano):
        num_a_multiplicar = self.romano_to_numero(num_romano)
        self.normal = self.normal * num_a_multiplicar
        self.romano =  self.numero_to_romano(self.normal)
        return self.romano
    
    def iterar(self,lista_romana):
        for x in lista_romana:
            self.suma_romano(x)

