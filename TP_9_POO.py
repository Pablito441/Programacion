#Ejercicio 1
"""1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
Construye los siguientes métodos para la clase:
•	Un constructor, donde los datos pueden estar vacíos.
•	Los setters y getters para cada uno de los atributos. Hay que validar las
entradas de datos.
•	mostrar(): Muestra los datos de la persona.
•	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad."""


class Persona: 
    def __init__(self,name = "",age = None,dni = "") -> None:
        self.name = name
        self.age = age
        self.dni = dni
    
    #Getters
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_dni(self):
        return self.dni
    
    #Setters
    def set_name(self,name):
        if isinstance(name, str):
            self.name = name
        else: 
            print("ERROR! the name must be a string of characters.")
    
    def set_age(self,age):
        if isinstance(age,int) and age>0:
            self.age = age
        else: 
            print("Error! The number must be a positive integer.")

    def set_dni(self,dni):
        if isinstance(dni,str) and len(dni) == 8:
            self.dni = dni
        else:
            print("Error, the dni must be a string of 8 characteres. ")

#mostrar()
    def show(self):
        print(f"Name: {self.name}\nAge: {self.age}\nDNI: {self.dni}")
#esMayorDeEdad()
    def is_adult(self):
        return self.age >= 18

# Crear una persona
persona1 = Persona()
persona1.set_name("Pablo")
persona1.set_age(21)
persona1.set_dni("44403734")
"""
# Mostrar los datos de la persona
persona1.show()

# Verificar si la persona es mayor de age
print("¿Es mayor de age?", persona1.is_adult())

"""
#EJercicio 2
"""Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular 
(que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la 
cantidad es opcional. Construye los siguientes métodos para la clase:
•	Un constructor, donde los datos pueden estar vacíos.
•	Los setters y getters para cada uno de los atributos. El atributo no se puede 
modificar directamente, sólo ingresando o retirando dinero.
•	mostrar(): Muestra los datos de la cuenta.
•	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
•	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos."""

class Cuenta:

    def __init__(self,headline = None, amount = 0.0):
        self.headline = headline
        self.amount = amount 

    #getters
    def get_headline(self):
        return self.headline
    
    def get_amount(self):
        return self.amount
    
    #setters
    def set_headline(self,headline):
        if isinstance(headline, Persona):
            self.headline = headline
        else:
            print("Error! The headline must be an objet of the Persona class.")
    
    def set_amount(self,amount):
        if isinstance(amount, (int,float)):
            self.amount = amount
        else: 
            print("Error!! The amount must be a integer o float number.")

#Show
    def show(self):
        print(f"headline: {self.headline.get_name()}\namount: {self.amount}")
#ingresar(cantidad)
    def enter(self,amount):
        if isinstance(amount,(int,float)) and amount > 0:
            self.amount += amount
        else:
            print("The amount must be a positive number")

    def remove(self,amount): 
        if isinstance(amount,(int,float)) and amount > 0:
            self.amount -= amount
        else:
            print("The amount must be a positive number")        

#Ejemplos de uso:
#utilizo la persona que cree en el primer ejercicio
headline_person1 = persona1
#crear cuenta para la persona:
cuenta_person1 = Cuenta(headline_person1, 10000)
#Muestra los datos de la cuenta de la persona 1 
cuenta_person1.show()

cuenta_person1.enter(1200)
cuenta_person1.show()

cuenta_person1.remove(100)
cuenta_person1.show()


"""3.	Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con 
los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y
el tipo de triángulo que es (equilátero, isósceles o escaleno)."""

class Triangulo:
    
    def __init__(self,side_left = None,side_right = None ,base = None):
        self.side_left = side_left
        self.side_right = side_right
        self.base = base

    #setters
    def setSideleft(self,side_left):
        if isinstance(side_left, (float,int)):
            self.side_left = side_left
        else:
            print("Error!! The left side must be an number integer or float.")

    def setSideRight(self,side_right):
        if isinstance(side_right, (float,int)):
            self.side_right = side_right
        else:
            print("Error!! The right side must be an number integer or float.")
    
    def setbase(self,base):          
        if isinstance(base , (float,int)):
            self.base = base
        else:
            print("Error!! The base must be an number integer or float.")

    #getters

    def getSideLeft(self):
        return self.side_left 
    
    def getSideRight(self):
        return self.side_right
    
    def getBase(self,base):
        return self.base

    #Mostrar todos los datos
    def show(self):
        print(f"left side of Triangule: {self.side_left}\nRight side of Triangule: {self.side_right}\nBase of Triangule: {self.base}")
    #Mostrar el lado mayor:

    def geater_side(self):
        if self.side_left > self.side_right > self.base:
            print(f"The largest side is the left: {self.side_left}")
        elif self.side_right > self.side_left > self.base:
            print(f"The largest side is the right: {self.side_right}")
        elif self.base >self.side_right > self.side_left:
            print(f"the largest side is the base: {self.base}")
        else:
            print("the triangle has all its sides equal")
    #tipo de triángulo que es (equilátero, isósceles o escaleno)
    def type_of_triangule(self):
        if self.side_left == self.side_right == self.base:
            print(f"The triangule is equilateral.")
        elif self.side_left != self.side_right != self.base:
            print(f"The triangule is scalene.")
        elif self.side_left == self.side_right and self.side_left != self.base or self.side_left == self.base and self.side_left != self.side_right or self.side_right == self.base and self.side_right != self.side_left:
            print(f"The triangule is isosceles.")


"""4.	Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el 
nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
•	Añadir contacto
•	Lista de contactos
•	Buscar contacto
•	Editar contacto
•	Cerrar agenda"""

class Agenda:

    def __init__(self,name = "",phone = None,email = "",contacts = []):
        self.name = name
        self.phone = phone
        self.email = email
        self.contacts = contacts

#Guarda los contactos en una lista 
    def add_contact(self,name,phone,email):
        contact = {'name':name , 'phone': phone , 'email': email}
        self.contacts.append(contact)
        print(f"Contact {name} added.")

#Muestra los contactos
    def list_of_contact(self):
        print('List of contacts:')
        for contact in self.contacts:
            print(f"Name: {self.contacts['name']}\nPhone: {self.contacts['phone']}\nEmail: {self.contacts['email']}\n ")
    
#Buscar contacto la lista de diccionarios
    def search_contact(self,name):
        for contact in self.contacts:
            if contact['name'] == name:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                return
        print(f"Contact {name} not found.")

#edicar un contacto
    def edit_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                new_name = input('New name: ')
                new_phone = input('New phone: ')
                new_email = input('New email: ')
                contact['name'] = new_name
                contact['phone'] = new_phone
                contact['email'] = new_email
                print(f'Contact {name} edited.')
                return
        print(f"Contact {name} not found.")

    def close_agenda(self):
        print('Agenda closed.')

#Main
my_agenda = Agenda()

while True:
    print('\nMenu:')
    print('1. Add contact')
    print('2. List contacts')
    print('3. Search contact')
    print('4. Edit contact')
    print('5. Close agenda')

    option = input('Select an option: ')

    if option == '1':
        name = input('Name: ')
        phone = input('Phone: ')
        email = input('Email: ')
        my_agenda.add_contact(name, phone, email)
    elif option == '2':
        my_agenda.list_of_contact()
    elif option == '3':
        name = input('Name to search: ')
        my_agenda.search_contact(name)
    elif option == '4':
        name = input('Name to edit: ')
        my_agenda.edit_contact(name)
    elif option == '5':
        my_agenda.close_agenda()
        break
    else:
        print('Invalid option. Please try again.')
