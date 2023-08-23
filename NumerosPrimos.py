from math import isqrt

# Definimos una función lambda llamada 'es_primo' que toma un argumento 'n'
# para determinar si un número es primo
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, isqrt(n) + 1))
    # version no funcional
    # def es_primo(n):
    #     if n <= 1:
    #         return False
    #     for i in range(2, isqrt(n) + 1):
    #         if n % i == 0:
    #             return False
    #     return True

# Función que genera una lista de números primos en un rango dado
def find_primes_in_range(start, end):
    return list(filter(is_prime, range(start, end + 1))) # alternativa: return [n for n in range(start, end + 1) if is_prime(n)]
    #la funcion filter solo agrega a la lista lo 
    #argumentos que son devueltos como true por is_prime
    
# Función para mostrar los números primos en una lista
def display_primes(primes):
    print("Números primos encontrados:")
    for prime in primes:
        print(prime, end = ' ')
    #alternativa: print(" ".join(map(str, primes)))  -> usamos map para convertir los números primos en cadenas y luego usamos join para imprimirlos como una sola cadena.

# Entrada de usuario para el rango
start = int(input("Ingrese el número de inicio del rango: "))
end = int(input("Ingrese el número final del rango: "))

# Encontrar y mostrar los números primos en el rango
primes = find_primes_in_range(start, end)
display_primes(primes)

# Si un número n tiene un divisor mayor que su raíz cuadrada, ese divisor debe 
# estar relacionado con otro divisor más pequeño que la raíz cuadrada de n. 
# En otras palabras, si n es divisible por un número mayor que su raíz cuadrada,
# entonces también debe ser divisible por un número menor que su raíz cuadrada. 