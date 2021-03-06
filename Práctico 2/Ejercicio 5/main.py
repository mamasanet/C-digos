from manejadorAlumnos import manejadorAlumno
from claseAlumno import claseAlumno
import os
os.system("cls")

def opcion1():
    print()
    año = int(input('Ingrese año: '))
    div = int(input('Ingrese división: '))
    print()
    print('{:25}{}'.format('Alumno', 'Porcentaje') + '\n')
    ma.porcentAlum(año, div)
    os.system("pause")

def opcion2():
    print()
    max_inasis = int(input('Ingrese la nueva cantidad máxima de inasistencias: '))
    print()
    print('Asistencia antes de actualizar:')
    alumno = claseAlumno()
    alumno.verAsistencias()
    alumno.actualizarMaxInas(max_inasis)
    print()
    print('Asistencia actualizada.')
    alumno.verAsistencias()
    print()
    os.system("pause")

def salir():
    print()
    print('Salio del programa.')
    print()

def menu():
    op = 0
    while op != 3:
        os.system("cls")
        print('>>>>>MENÚ<<<<<')
        print('1 - Ingrese año y división para listar alumnos en malas condiciones.')
        print('2 - Modificar la cantidad máxima de inasistencias permitidas.')
        print('3 - Salir.')
        op = int(input('Ingrese opción: '))

        if(op == 1):
            opcion1()

        elif(op == 2):
            opcion2()

        elif(op == 3):
            salir()

if __name__ == '__main__':
    ma = manejadorAlumno()
    ma.testAlumnos()
    print(ma)
    os.system("pause")
    menu()