import orm
from Tablas.Autores import Autores
from Tablas.Libros import Libros
from Tablas.Usuarios import Usuarios   
db=orm.SQLiteORM("db_biblioteca")
db.crear_tabla(Autores)
db.crear_tabla(Libros)
db.crear_tabla(Usuarios)

# autor_uno={
#     "dni":7492834,
#     "nombre":"quevedo",
#     "apellidos":"lopez"}
# db.insertarUno("Autores", autor_uno)

usuarios_varios=[
    {   "dni":"235232",
        "nombre":"nando",
        "apellidos":"lopez",
        "f_nacimiento":"27-11-2003",
        "estado":"activo"

    },
    {
        "dni":"553242",
        "nombre":"maria",
        "apellidos":"calle",
        "f_nacimiento":"04-12-2003",
        "estado":"activo"
    },
    {
        "dni":"973443",
        "nombre":"cristian",
        "apellidos":"poma",
        "f_nacimiento":"23-04-2000",
        "estado":"inactivo"
    },
    {
        "dni":"237884",
        "nombre":"jhonatan",
        "apellidos":"auccasi",
        "f_nacimiento":"24-05-2005",
        "estado":"inactivo"
    },
    {
        "dni":"238957",
        "nombre":"hans",
        "apellidos":"ortiz",
        "f_nacimiento":"27-09-2006",
        "estado":"activo"
    }]
# db.insertarVarios("Usuarios", usuarios_varios)
#muestra una lista de tuplas
# print(db.mostrar("Usuarios"))
#muestra un objeto con sus campos y sus valores
# print(db.mostrar("Usuarios" ,type="objeto"))
# #tambien puedo filtrar informacion
# print(db.mostrar("Usuarios",where="nombre LIKE 'ha%'",type="objeto"))
# print(db.mostrar("Usuarios",where="dni=238957",type="objeto"))
# print(db.actualizar("Usuarios",{"estado":"activo"},where="nombre='cristian'"))
db.eliminar("Usuarios",where="nombre='hans'")
print(db.mostrar("Usuarios",type="objeto"))
