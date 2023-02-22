print("Bienvenido a la comparación de bocadillos")
print("Por favor, califica del 1 al 5 cada uno de los siguientes bocadillos: ")

# Preguntar por la valoración del bocadillo de jamón
jamon = int(input("¿Qué puntuación le das al bocadillo de jamón? "))
if jamon < 1 or jamon > 5:
    print("La puntuación debe estar entre 1 y 5.")
    exit()

# Preguntar por la valoración del bocadillo de pollo
pollo = int(input("¿Qué puntuación le das al bocadillo de pollo? "))
if pollo < 1 or pollo > 5:
    print("La puntuación debe estar entre 1 y 5.")
    exit()

# Preguntar por la valoración del bocadillo vegetal
vegetal = int(input("¿Qué puntuación le das al bocadillo vegetal? "))
if vegetal < 1 or vegetal > 5:
    print("La puntuación debe estar entre 1 y 5.")
    exit()

# Preguntar por la valoración del bocadillo de tortilla
tortilla = int(input("¿Qué puntuación le das al bocadillo de tortilla? "))
if tortilla < 1 or tortilla > 5:
    print("La puntuación debe estar entre 1 y 5.")
    exit()

# Calcular el puntaje promedio de cada bocadillo
promedio_jamon = jamon
promedio_pollo = pollo
promedio_vegetal = vegetal
promedio_tortilla = tortilla

# Comparar los puntajes promedio de cada bocadillo
if promedio_jamon > promedio_pollo and promedio_jamon > promedio_vegetal and promedio_jamon > promedio_tortilla:
    print("El bocadillo de jamón es el mejor.")
elif promedio_pollo > promedio_jamon and promedio_pollo > promedio_vegetal and promedio_pollo > promedio_tortilla:
    print("El bocadillo de pollo es el mejor.")
elif promedio_vegetal > promedio_jamon and promedio_vegetal > promedio_pollo and promedio_vegetal > promedio_tortilla:
    print("El bocadillo vegetal es el mejor.")
else:
    print("El bocadillo de tortilla es el mejor.")
