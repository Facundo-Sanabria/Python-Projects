from clases import Persona, Docente, Estudiante, Curso, GestionAcademica
import os

app = GestionAcademica()
app.cargar()
if len(app.cursos) == 0:
    print("Para comenzar, necesitaremos generar un primer curso...")
    app.agregarCurso()
op = 0
while op != 8:
    print("-------------------------------------------")
    print("Ingrese una opción")
    print("1. Agregar un curso")
    print("2. Agregar integrantes a un curso")
    print("3. Ver información de un curso")
    print("4. Ver información de todos los cursos")
    print("5. Calcular recaudación de un curso")
    print("6. Calcular recaudación total")
    print("7. Guardar la información")
    print("8. Salir")
    print("-------------------------------------------")
    op = int(input())
    while op > 8 or op < 1:
        op = int(input("VALOR INCORRECTO. Ingrese otra opción."))
    if op == 1:
        os.system("cls")
        app.agregarCurso()
    elif op == 2:
        os.system("cls")
        texto = "Elija entre los siguientes cursos: \n"
        for x in app.cursos:
            texto += str(x.año) + "\n"
        curso = int(input(texto + " - "))
        for x in app.cursos:
            if curso == x.año:
                op2 = int(input("¿Desea agregar docentes(1) o estudiantes(2): "))
                while op2 > 2 or op < 1:
                    op2 = int(input("VALOR INCORRECTO. Ingrese otra opción."))
                if op2 == 1:
                    x.agregarDocente()
                if op2 == 2:
                    x.agregarEstudiante()
    elif op == 3:
        os.system("cls")
        texto = "Elija entre los siguientes cursos: \n"
        for x in app.cursos:
            texto += str(x.año) + "\n"
        curso = int(input(texto + " - "))
        for x in app.cursos:
            if curso == x.año:
                print(x)
    elif op == 4:
        os.system("cls")
        for x in app.cursos:
            print(x)
    elif op == 5:
        os.system("cls")
        texto = "Elija entre los siguientes cursos: \n"
        for x in app.cursos:
            texto += str(x.año) + "\n"
        curso = int(input(texto + " - "))
        for x in app.cursos:
            if curso == x.año:
                print(f"El total recaudado por el {x.año}° grado es de: {x.calcularRecaudacion()}")
    elif op == 6:
        os.system("cls")
        print(f"El total recaudado por la académia es de: {app.calcularRecaudacionTotal()}")
    elif op == 7:
        os.system("cls")
        app.guardar()
os.system("cls")
print("Hasta la próxima")