from pickle import dump, load, dumps, loads

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")
        self.dni = int(input("Ingrese el documento: "))
        self.edad = int(input("Ingrese la edad: "))

class Docente(Persona):
    def __init__(self):
        super().__init__()
        self.especialidad = input("Ingrese matería que enseña: ")
    def getEspecialidad(self):
        return self.especialidad
    def setEspecialidad(self,x):
        self.especialidad = x
    def __str__(self):
        texto = f"Nombre: {self.nombre} {self.apellido}. Especialidad: {self.especialidad}."
        return texto

class Estudiante(Persona):
    def __init__(self):
        super().__init__()
        self.actividadExtracurricular = None
        op = 0
        lista = [("Educación Física",700),("Teatro",1000),("Música",800),(None,0)]
        while op < 1 or op > 4:
            print("Seleccione el número de la actividad extracurricular que corresponda:")
            for x in range(len(lista)):
                print(f"{x+1} - {lista[x][0]}, costo: ${lista[x][1]}.")
            op = int(input(""))
            if op < 1 and op > 4:
                print("Opción ingresada inválida")
        self.actividadExtracurricular = lista[op-1]
    def calcularCuota(self):
        valor = 1500 + self.actividadExtracurricular[1]
        return float(valor)

class Curso:
    def __init__(self):
        self.año = int(input("Ingrese el número del año que es el curso: "))
        self.profesores = []
        cant = int(input("¿Cuantos docentes enseñan en este curso?: "))
        for x in range(cant):
            print(f"Ingresamos al {x+1}° docente: ")
            docente = Docente()
            self.profesores.append(docente)
        self.estudiantes = []
        cant2 = int(input("¿Cuantos estudiantes componen este curso?: "))
        for x in range(cant2):
            print(f"Ingresamos al {x+1}° estudiante: ")
            estudiante = Estudiante()
            self.estudiantes.append(estudiante)
    def agregarDocente(self):
        cant = int(input("¿Cuantos docentes desea agregar?: "))
        for x in range(cant):
            print(f"Ingresamos al {x+1}° docente: ")
            docente = Docente()
            self.profesores.append(docente)
    def agregarEstudiante(self):
        cant2 = int(input("¿Cuantos estudiantes desea agregar?: "))
        for x in range(cant2):
            print(f"Ingresamos al {x+1}° estudiante: ")
            estudiante = Estudiante()
            self.estudiantes.append(estudiante)
    def calcularRecaudacion(self):
        total = 0.0
        for x in self.estudiantes:
            monto = x.calcularCuota()
            total += monto
        return total
    def __str__(self):
        texto = f"Curso: {self.año}° grado\nDocentes:\n"
        for x in self.profesores:
            profe = f"  {x.nombre} {x.apellido}, {x.especialidad} \n"
            texto += profe
        texto += "Estudiantes:\n"
        for x in self.estudiantes:
            alumno = f"  {x.nombre} {x.apellido}, Act. Extracurricular {x.actividadExtracurricular[0]} \n"
            texto += alumno
        return texto

class GestionAcademica:
    def __init__(self):
        self.cursos = []
    def agregarCurso(self):
        cant = int(input("¿Cuantos cursos desea agregar?: "))
        for x in range(cant):
            print(f"Cargando el {x+1}° curso...")
            curso = Curso()
            self.cursos.append(curso)
    def calcularRecaudacionTotal(self):
        monto = 0.0
        for x in self.cursos:
            valor = x.calcularRecaudacion()
            monto += valor
        return monto
    def guardar(self):
        serializado = dumps(self.cursos)
        with open("backup","wb") as archivo:
            dump(serializado, archivo)
    def cargar(self):
        try:
            with open("backup","rb") as archivo:
                informacion = load(archivo)
                lista = loads(informacion)
            if len(lista) != 0:
                self.cursos = lista
                print("Se cargó la última información")
        except:
            print("No hay información aún")  