# TODO Найдите количество книг, которое можно разместить на дискете
V = 1.44

simvol = 25
strok = 50
stranic = 100
vsego = simvol*strok*stranic
ves = 4
vsego_ves = ((vsego*ves)/1024)/1024
knig = V//vsego_ves
knig_int = int(knig)
print("Количество книг, помещающихся на дискету:",knig_int)
