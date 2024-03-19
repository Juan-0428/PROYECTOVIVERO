PROYECTO SISTEMA PARA LA ADMINISTRACIÓN DE VIVEROS
MODELO DEL DOMINIO - ORM - PRUEBAS UNITARIAS

Usted ha sido contratado para realizar un sistema para Viveros. Este sistema está orientado a
llevar un registro de los Productores, sus Viveros, las Labores respectivas realizadas.
Tenga en cuenta que un Productor puede ser identificado a través de su documento de identidad,
nombre, apellido, teléfono, correo. Cada Productor puede tener varias Fincas, las cuales son
identificadas por su número de catastro, municipio de ubicación. Del mismo modo, cada Finca
puede tener varios Viveros. Cada Vivero es identificado por un código que el mismo Productor
puede asignar y el tipo de cultivo.
Por otro lado, cada Vivero debe ser sometido a una serie de actividades propio de la actividad
agrícola, esto es definida como una Labor. La Labor se define como una actividad importante
dentro del cultivo. Esta tiene los siguientes atributos: fecha en que se realiza la labor y la
descripción de la misma. Dentro de tipos de Labores que pueden existir se encuentra el empleo de
Producto de Control Hongo, Producto Control de Plaga y Producto Control de Fertilizantes
Los Productos de Control tendrán como características un registro ICA, el nombre del producto y la
frecuencia de aplicación (es decir, cada cuanto periodo se aplica el producto. Cada 15 días, cada
30 días, etc) así como también el valor del producto.
Tenga en cuenta que el Control de Plagas tiene como característica un periodo de carencia (es el
tiempo legalmente establecido, expresado usualmente en número de días que debe transcurrir
entre la última aplicación de un fitosanitario y la cosecha) y Producto Control de Fertilizantes la
fecha de la última aplicación de este Producto. Igualmente, Producto de Control Hongo (periodo de
carencia, nombre del hongo que afecta la planta).
DESARROLLO DE LA ACTIVIDAD
1. Deben de crear el Modelo con las Entidades respectivas. Tanto Diagrama de Clases como
instanciación tecnológica con el ORM (debe de existir correspondencia entre los dos).
2. Se deben de crear como mínimo 3 pruebas unitarias para cada Entidad. Las pruebas
unitarias básicamente sirven para comprobar los Requerimientos Funcionales y No
Funcionales.
3. Todos los campos de las Entidades SON OBLIGATORIOS.
4. Se deben de crear pruebas unitarias que verifiquen las correctas relaciones entre las
Entidades.
5. El proyecto debe de tener su repositorio en Github o GitLab.
