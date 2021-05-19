# ======================================================================================================
#  ___          _              _  __        ___         _     _    _           _   ___ ___             
# | __|_ ____ _| |_  _ __ _ __(_)/_/ _ _   |_ _|_ ___ _(_)_ _(_)__| |_  _ __ _| | |_ _|_ _|            
# | _|\ V / _` | | || / _` / _| / _ \ ' \   | || ' \ V / \ V / / _` | || / _` | |  | | | |             
# |___|\_/\__,_|_|\_,_\__,_\__|_\___/_||_| |___|_||_\_/|_|\_/|_\__,_|\_,_\__,_|_| |___|___|            
# 
#        __         __
#       /  \.-"""-./  \           |          Universidad del Valle de Guatemala
#      \    -   -    /            |          Facultad de Ingeniería
#       |   o   o   |             |          Departamento de Cienciad de la Computación
#       \  .-'''-.  /             |          Juan Pablo Muralles - 21856
#        '-\__Y__/-'              |          CC2005 - Algoritmos y Programación Básica
#           `---`                 |          More info: https://github.com/juampam/UVW_Stats.git          
#
# =======================================================================================================

import pandas as pd
import csv

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def mean():
    df = pd.read_csv('registroUVW.csv',index_col = 'carnet')
    notas = df[['matematicas','algoritmos','sociales']]
    promedio =  notas.mean(axis=1)
    print(promedio)
    print("------------------------------------------------------------------------------------------------------------------")
def cracks():
    df = pd.read_csv('registroUVW.csv',index_col = 'carnet')
    notas = df[['sexo','matematicas','algoritmos','sociales']]
    promedio =  notas.mean(axis=1)
    df['Mean'] = promedio
    aplican = df[ (df['Mean'] <= 80)].index
    df.drop(aplican , inplace=True)
    df["distinction"] = df.apply(lambda x: "Maximus Brillantum" if int(x["Mean"]) >= 90 else "Brillantum", axis=1)
    res = df['distinction'].value_counts()
    
    print(res)
    df.groupby('sexo')['distinction'].count().plot(kind = 'bar')
    print("¿Desea ver la tabla? [S/n] ")
    op = str(input())
    if op.lower() == "s":
        print(df)
    else:
        print("desea ver la gráfica? [S/n]")
        ope = str(input())
        if ope.lower() == "s":
            print(df)
        menuAlumnos()
def promedioClases():
    df = pd.read_csv('registroUVW.csv',index_col = 'carnet')
    df.columns.str.match("Unnamed: 0")
    df.loc[:,~df.columns.str.match("Unnamed: 0")]
    dataF = df[['matematicas','algoritmos','sociales']]
    clasmean = dataF.mean(axis=0)
    print(clasmean)
    print("¿Desea ver el promedio general? [S/n] ")
    op = str(input())
    if op.lower() == "s":
        hola = clasmean.tolist()
        suma = sum(hola)
        su =  float(suma)
        promediog = su/3
        pr = str(promediog)
        print("Promedio General: " + pr)
    else:
        menuAlumnos()

def dificultad():
    
    df = pd.read_csv('registroUVW.csv',index_col = 'carnet')
    indexM = df[ (df['matematicas'] >= 61)].index
    df.drop(indexM , inplace=True)
    dataM = df['matematicas']
    x = len(dataM.index)
    y = str(x)
    print("Matemática Reprobados: " + y)
   

    df = pd.read_csv('registroUVW.csv',index_col = 'carnet')
    indexA = df[ (df['algoritmos'] >= 61)].index
    df.drop(indexA , inplace=True)
    dataA = df['algoritmos']
    a = len(dataA.index)
    b = str(a)
    print("Algoritmos Reprobados: " + b)
    
    df = pd.read_csv('registroUVW.csv',index_col = 'carnet')
    indexS = df[ (df['sociales'] >= 61)].index
    df.drop(indexS , inplace=True)
    dataS = df['sociales']
    s = len(dataS.index)
    p = str(s)
    print("Sociales Reprobados: " + p)
    print("El curso más difícil es el de valor mas alto. ")


def lose():
    df = pd.read_csv('registroUVW.csv',index_col = 'carnet')
    indexNames = df[ (df['matematicas'] >= 61) & (df['algoritmos'] >=61) & (df['sociales'] >=61 )].index
    df.drop(indexNames , inplace=True)
    dataF = df[['matematicas','algoritmos','sociales']]
    x = len(dataF.index)
    y = str(x)
    print("Alumnos Reprobados: " + y)
    print("¿Desea ver la tabla? [S/n] ")
    op = str(input())
    if op.lower() == "s":
        print(dataF)
    else:
        menuAlumnos()


def win():
    df = pd.read_csv('registroUVW.csv',index_col = 'carnet')
    indexNames = df[ (df['matematicas'] <61) & (df['algoritmos'] <61) & (df['sociales']<61 )].index
    df.drop(indexNames , inplace=True)
    clases = df[['matematicas','algoritmos','sociales']]
    x = len(clases.index)
    y = str(x)
    print("Alumnos Aprobados: " + y)
    print("¿Desea ver la tabla? [S/n] ")
    op = str(input())
    if op.lower() == "s":
        print(clases)
    else:
        menuAlumnos()

def mainMenu():
    cero = 0
    while cero == 0:
        print(f"{bcolors.BOLD}\nUniversidad de Valores Wronskianos{bcolors.ENDC}\nControl de notas")
        print(f"{bcolors.HEADER}\nseleccione una opción{bcolors.ENDC}")
        print(f"{bcolors.WARNING}a){bcolors.ENDC} Alumnos",f"{bcolors.WARNING}b){bcolors.ENDC} Cursos", sep = "           ")
        print(f"{bcolors.WARNING}c){bcolors.ENDC} Salir")
        option = str(input())
        if option.lower() == "a":
            menuAlumnos()
        elif option.lower() == "b":
            menuCurso()
        elif option.lower() == "c":
            exit()
        else:
            print(f"{bcolors.FAIL}Por favor seleccione una opción válida{bcolors.ENDC}")
def menuAlumnos():
    print(f"{bcolors.BOLD}\nCONTROL DE ALUMNOS{bcolors.ENDC}\nSeleccione una opción")
    print(f"{bcolors.WARNING}a){bcolors.ENDC} Promedio",f"{bcolors.WARNING}b){bcolors.ENDC} Aprobados", sep = "           ")
    print(f"{bcolors.WARNING}c){bcolors.ENDC} Reprobados",f"{bcolors.WARNING}d){bcolors.ENDC} Distinguidos", sep = "         ")
    print(f"{bcolors.WARNING}e){bcolors.ENDC} Salir")
    select = str(input())
    if select.lower()=="a":
        print("Promedio")
        mean()
    elif select.lower() == "b":
        print("Aprobados")
        win()
    elif select.lower()=="c":
        print("Reprobados")
        lose()
    elif select.lower() == "d":
        print("Distinguidos")
        cracks()
    elif select.lower() == "e":
        mainMenu()  

def menuCurso():
    print(f"{bcolors.BOLD}\nCONTROL DE CURSOS{bcolors.ENDC}\nSeleccione una opción")
    print(f"{bcolors.WARNING}a){bcolors.ENDC} Promedio General",f"{bcolors.WARNING}b){bcolors.ENDC} Cantidad de reprobados/Dificultad de cursos", sep = "           ")
    print(f"{bcolors.WARNING}d){bcolors.ENDC} Salir")
    select = str(input())
    if select.lower()=="a":
        print("Promedio")
        promedioClases()
    elif select.lower() == "b":
        dificultad()
    elif select.lower()=="c":
        print("Reprobados")
        lose()
    elif select.lower() == "d":
        mainMenu()











































mainMenu()
