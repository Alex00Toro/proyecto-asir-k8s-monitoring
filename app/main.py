import time

def stress_cpu():
    print("Iniciando test de estrés en el nodo...")
    while True:
        # Generamos carga de CPU para que el monitor detecte algo
        [x**2 for x in range(5000)]

if __name__ == "__main__":
    stress_cpu()
