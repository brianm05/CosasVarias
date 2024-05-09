from PIL import Image, ImageDraw, ImageFont
import random
import datetime

hora_actual = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')

nombre_usuario=""
posiciones_restantes=["1","2","3","4","5","6","7","8","9","10","11"]


#plantel de River del 2014-2015 segun www.livefutbol.com
plantel2014=['2014-2015','Barovero', 'Batalla', 'Francese', 'Funes Mori', 'Mammana', 'Mercado', 'Urribarri', 'Vega', 'Aimar', 'Cirigliano', 'Martinez', 'Pisculichi', 'Rodriguez', 'Sanchez', 'Boye', 'Driussi', 'Kaprof', 'Mora', 'Krane', 'Piscu', 'Teo']

#plantel de River del 2015-2016 segun www.livefutbol.com
plantel2015=['2015-2016','Barovero', 'Batalla', 'Chiarini', 'Velazco', 'Balanta', 'Casco', 'Maidana', 'Mammana', 'Mercado', 'Montiel', 'Olivera', 'Sibille', 'Vangioni', 'Vega', 'Andrade', 'Arzura', 'Bertolo', 'Carreras', 'Casquete', "D'Alessandro", 'Domingo', 'Fernández', 'González', 'Martínez', 'Mayada', 'Morán', 'Palacios', 'Pisculichi', 'Ponzio', 'Viudez', 'Alario', 'Alonso', 'Driussi', 'Franco', 'López', 'Mora', 'Salto', 'Nacho', 'Pity', 'Piscu']

#plantel de River del 2016-2017 segun www.livefutbol.com
plantel2016=['2016-2017','Batalla', 'Bologna', 'Velazco', 'Casco', 'Lollo', 'Maidana', 'Martinez Quarta', 'Medina', 'Mina', 'Montiel', 'Olivera', 'Andrade', 'Arzura', 'Auzqui', 'Domingo', 'Fernandez', 'Martinez', 'Mayada', 'Moran', 'Moreira', 'Moya', 'Palacios', 'Ponzio', 'Rodriguez', 'Rojas', 'Rossi', 'Alario', 'Alonso', 'Driussi', 'Larrondo', 'Lopez', 'Mora', 'Nacho', 'Pity']

#plantel de River del 2017-2018 segun www.livefutbol.com
plantel2017=['2017-2018','Armani', 'Bologna', 'Lux', 'Casco', 'Lollo', 'Maidana', 'Martinez', 'Martinez Quarta', 'Montiel', 'Pinola', 'Saracchi', 'Auzqui', 'de la Cruz', 'Fernandez', 'Ferreira', 'Martinez', 'Mayada', 'Moreira', 'Palacios', 'Perez', 'Ponzio', 'Quintero', 'Rojas', 'Rossi', 'Zuculini', 'Borre', 'Larrondo', 'Mora', 'Pratto', 'Rollheiser', 'Scocco', 'Nacho', 'Pity', 'Enzo', 'Enzo Perez', 'Juanfer']

#plantel de River del 2018-2019 segun www.livefutbol.com
plantel2018=['2018-2019', 'Armani', 'Bologna', 'Lux', 'Angileri', 'Casco', 'Gallardo', 'Lollo', 'Martinez', 'Martinez Quarta', 'Montiel', 'Pinola', 'Rojas', 'Sibille', 'Carrascal', 'de la Cruz', 'Fernandez', 'Fernandez', 'Ferreira', 'Lopez Muñoz', 'Mayada', 'Palacios', 'Perez', 'Ponzio', 'Quintero', 'Sosa', 'Vera', 'Zuculini', 'Alvarez', 'Beltran', 'Borre', 'Girotti', 'Marcel', 'Pratto', 'Rollheiser', 'Scocco', 'Suarez', 'Enzo', 'Nacho', 'Juanfer', 'Enzo Perez', 'Enzo F']

#plantel de River del 2019-2020 segun www.livefutbol.com
plantel2019=['2019-2020', 'Armani', 'Bologna', 'Centurion', 'Lux', 'Angileri', 'Casco', 'Diaz', 'Lopez', 'Martinez Quarta', 'Montiel', 'Paredes', 'Pinola', 'Rojas', 'Sibille', 'Carrascal', 'de la Cruz', 'Fernandez', 'Fernandez', 'Ferreira', 'Perez', 'Ponzio', 'Quintero', 'Rossi', 'Sosa', 'Zuculini', 'Alvarez', 'Beltran', 'Borre', 'Girotti', 'Pratto', 'Rollheiser', 'Scocco', 'Suarez', 'Enzo', 'Nacho', 'Enzo F', 'Enzo Perez', 'Juanfer']

#plantel de River del 2020-2021 segun www.livefutbol.com
plantel2020=['2020-2021', 'Armani', 'Bologna', 'Diaz', 'Lux', 'Petroli', 'Angileri', 'Casco', 'Diaz', 'Lecanda', 'Maidana', 'Martinez', 'Montiel', 'Moreira', 'Peña Biafore', 'Pinola', 'Rojas', 'Vigo', 'Carrascal', 'Castro Ponce', 'de la Cruz', 'Galvan', 'Palavecino', 'Paradela', 'Perez', 'Ponzio', 'Simon', 'Zuculini', 'Alvarez', 'Beltran', 'Borre', 'Fontana', 'Girotti', 'Rollheiser', 'Suarez', 'Enzo', 'Enzo Perez']

#plantel de River del 2021-2022 segun www.livefutbol.com
plantel2021=['2021-2022', 'Armani', 'Centurion', 'Petroli', 'Angileri', 'Casco', 'Diaz', 'Gomez', 'Gonzalez Pírez', 'Herrera', 'Maidana', 'Mammana', 'Martinez', 'Peña Biafore', 'Pinola', 'Rojas', 'Aliendro', 'Barco', 'de la Cruz', 'Fernandez', 'Ferreira', 'Palavecino', 'Paradela', 'Perez', 'Pochettino', 'Quintero', 'Simon', 'Zuculini', 'Alvarez', 'Beltran', 'Rollheiser', 'Romero', 'Suarez', 'Enzo', 'Enzo Perez', 'Nacho', 'Juanfer']

#plantel de River del 2022-2023 segun www.livefutbol.com
plantel2022=['2022-2023', 'Armani', 'Centurion', 'Lavagnino', 'Casco', 'Diaz', 'Diaz', 'Gomez', 'Gonzalez Pírez', 'Herrera', 'Lopez', 'Maidana', 'Mammana', 'Martinez', 'Rojas', 'Alfonso', 'Aliendro', 'Barco', 'Castro Ponce', 'de la Cruz', 'Echeverri', 'Fernandez', 'Kranevitter', 'Palavecino', 'Paradela', 'Perez', 'Simon', 'Zuculini', 'Beltran', 'Borja', 'Fontana', 'Rondon', 'Solari', 'Suarez', 'Enzo', 'Enzo Diaz', 'Paulo Diaz', 'Nacho', 'Enzo Perez']

#plantel de River del 2023-2024 segun www.livefutbol.com
plantel2023=['2023-2024', 'Armani', 'Centurion', 'Lavagnino', 'Boselli', 'Casco', 'Diaz', 'Diaz', 'Funes Mori', 'Gonzalez Pirez', 'Herrera', 'Martinez', 'SantAnna', 'Zabala', 'Aliendro', 'Barco', 'Echeverri', 'Fernandez', 'Fonseca', 'Kranevitter', 'Lanzini', 'Leiva', 'Luna', 'Martinez', 'Mastantuono', 'Palavecino', 'Simon', 'Villagra', 'Borja', 'Colidio', 'Ruberto', 'Solari', 'Subiabre', 'Enzo', 'Enzo Diaz', 'Paulo Diaz', 'Nacho', 'Pity']

#plantel de River del 2024-2025 segun www.livefutbol.com
plantel2024=["2024"] #no jugable aun 

planteles=[plantel2014,plantel2015,plantel2016,plantel2017,plantel2018,plantel2019,plantel2020,plantel2021,plantel2022,plantel2023]

pos1=["(----)","1"]
pos2=["(----)","2"]
pos3=["(----)","3"]
pos4=["(----)","4"]
pos5=["(----)","5"]
pos6=["(----)","6"]
pos7=["(----)","7"]
pos8=["(----)","8"]
pos9=["(----)","9"]
pos10=["(----)","10"]
pos11=["(----)","11"]
posiciones=[pos1,pos2,pos3,pos4,pos5,pos6,pos7,pos8,pos9,pos10,pos11]

#exportar foto
def Exportar():
    font = ImageFont.truetype("times.ttf", 14) #establece rfuente
    img = Image.new('RGB', (300, 500), color=(0, 150, 0)) #crear lienzo + color verde
    draw = ImageDraw.Draw(img) 

    #establecer posiciones 
    draw.multiline_text( (75, 50), pos9[1]+"\n"+pos9[0], font=font, fill=(0, 0, 0), align="center")
    draw.multiline_text( (150, 75), pos7[1]+"\n"+pos7[0], font=font, fill=(0, 0, 0), align="center")

    draw.multiline_text( (125,155), pos10[1]+"\n"+pos10[0], font=font, fill=(0, 0, 0), align="center")

    draw.multiline_text( (40, 225), pos11[1]+"\n"+pos11[0], font=font, fill=(0, 0, 0), align="center")
    draw.multiline_text( (195, 220), pos8[1]+"\n"+pos8[0], font=font, fill=(0, 0, 0), align="center")

    draw.multiline_text( (125, 300), pos5[1]+"\n"+pos5[0], font=font, fill=(0, 0, 0), align="center")

    draw.multiline_text( (20, 335), pos3[1]+"\n"+pos3[0], font=font, fill=(0, 0, 0), align="center")
    draw.multiline_text( (70, 390), pos6[1]+"\n"+pos6[0], font=font, fill=(0, 0, 0), align="center")
    draw.multiline_text( (160, 400), pos2[1]+"\n"+pos2[0], font=font, fill=(0, 0, 0), align="center")
    draw.multiline_text( (210, 350), pos4[1]+"\n"+pos4[0], font=font, fill=(0, 0, 0), align="center")

    draw.multiline_text( (125, 450), pos1[1]+"\n"+pos1[0], font=font, fill=(0, 0, 0), align="center")

    img.save(nombre_usuario+"_"+hora_actual+'.png')


print("Bienvenido a Futbol11.")
print("¿Con que nombre quiere guardar la imagen?")
nombre_usuario=input()

Exportar()

i=0
while i < 11:
    posicion=""
    
    año= random.choice(planteles)
    print("Tienes que elegir un jugador de la temporada: "+año[0]+". ¿Que posicion quieres completar?")
    
    verificacion2=False
    while verificacion2==False:
        try:
            posicion=int(input())
            if  12>posicion>0:
                verificacion2=True
            else:
                verificacion2=False
                print("NO INGRESASTE UN NUMERO VALIDO. Intentalo de vuelta. ¿Que posicion quieres completar?")

        except ValueError:
            print("NO INGRESASTE UN NUMERO. Intentalo de vuelta. ¿Que posicion quieres completar?")
            verificacion2=False

    posiciones[posicion-1][0] = año[0]

    verificacion=False
    while verificacion==False:
        print("¿Que jugador quieres colocar?")
        posiciones[posicion-1][1] = str(input())

        for n in año:
            if n.upper()==str(posiciones[posicion-1][1]).upper():
                    verificacion=True
                    break
            elif n!=posiciones[posicion-1][1]:
                    verificacion=False
        if verificacion==False:
                print("No se encontro el jugador. ¿Que jugador quieres colocar?")
                
    Exportar()
    i+=1
