# Entrega1-Duarte-MartinezR-Dahir
El proyecto consiste en una web a la que hay que acceder ingresando el url /GruposSociales/ el cuál es nuestra planilla de inicio.
En ella veremos el título escrito en el medio de ésta. En el encabezado de página se observan los distintos accesos, si ingresamos
a por ejemplo "Familiares", nos llevará a la planilla de familiares, donde se puede observar una tabla con los familiares agregados
y sus distintos atributos. Por encima de esa tabla existe un acceso a la planilla de "formulario de familiares", donde el usuario
podrá cargar manualmente un nuevo "familiar" con sus distintos atributos. Los accesos "Amigos" y "Compañeros" funcionan de igual
forma. cuando se carga un nuevo miembro de cualquiera de estos grupos, el programa nos lleva de vuelta al inicio. Si volvemos a ingresar a dicho acceso se podrá ver dicho miembro ya formando parte de su respectiva tabla, por lo tanto ya formando parte de la 
base de datos.
Otro acceso que tienen los distintos campos (Familiares, Amigos, Compañeros) es el de búsqueda. Al ingresar a por ejemplo "buscar
compañero", nos lleva a la plantilla con el formulario de busqueda, ahi con ingresar el nombre nos va a devolver a la plantilla de "Compañeros" mostrando solo aquel dato que deseabamos encontrar. En caso de que nuestra búsqueda sea de alguien que no pertenece a 
la base de datos, nos volverá a la plantilla "Compañeros" con el mensaje de que esa persona no forma parte del grupo. 
A su vez existe el acceso a el administrador de Django con la url /admin/ donde al ingresar con usuario y contraseña, se puede alterar los datos que ya formen parte de nuestra base de datos.
