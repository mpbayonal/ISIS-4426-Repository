
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import psycopg2

query = 'select \
        nombre,\
        email,\
        estado,\
        fecha,\
        pago,\
        url_archivo,\
        apellido,\
        proyecto_id,\
        id \
    from \
        "backApp_diseno"  b\
    where \
        b.estado = \'No Procesado\''

connection = psycopg2.connect(user="designmatch",
                                password="Segur@12",
                                host="172.24.42.30",
                                database='designmatch')

cursor = connection.cursor()
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    nombre = row[0]
    email = row[1]
    estado = row[2]
    fecha = row[3]
    pago = row[4]
    url_archivo = row[5]
    apellido = row[6]
    proyecto_id = row[7]
    id_diseno = row[8]

    img = Image.open(url_archivo, "r")
    img.thumbnail(800, 600, Image.ANTIALIAS)
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), "{0} {1}".format(nombre, apellido), (255, 255, 255))
    img.save(url_archivo.split(".", 1)[
             0]+"_modificado."+url_archivo.split(".", 1)[1])
    serializer = DiseñoSerializer(data, many=False)

    cursor.execute("UPDATE backApp_disenos set estado = %s where id = %s", ("Disponible", id_diseno))
    connection.commit()
