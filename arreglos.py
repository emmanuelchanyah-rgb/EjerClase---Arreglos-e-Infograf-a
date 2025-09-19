import random
import time

def imprimir_matriz(matriz):
    print("\nMatriz de 500 alumnos x 6 materias:\n")

    print("        ", end="")
    for j in range(len(matriz[0])):
        print(f"Materia{j+1:<8}", end=" ")
    print("\n" + "-" * (10 + len(matriz[0]) * 12))
 
    for i, fila in enumerate(matriz, start=1):
        print(f"Alumno {i:03} ", end="")  
        for valor in fila:
            print(f"\t\t{valor:<11}", end=" ")  
        print()  

def main():
    alumnos = 500
    materias = 6

    matriz_B = [[random.randint(10, 100) for _ in range(materias)] for _ in range(alumnos)]

    imprimir_matriz(matriz_B)

    inicio = time.time()
    resultado = matriz_B[320][4]
    fin = time.time()

    print(f"\nLa calificación del Alumno321 en la Materia5 es: {resultado}")
    print(f"Tiempo de acceso: {fin - inicio:.10f} segundos")

if __name__ == "__main__":
    main()
