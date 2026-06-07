# TIPO TEST — Metodología de la Programación
## Banco completo de preguntas (con respuestas)

---

## PUNTUACIÓN ESTIMADA

Si incorporan tipo test al examen de este año, basándome en el estilo de la asignatura y las preguntas de Prado:

- **~10-15 preguntas** de tipo test
- **~1.5 - 2 puntos** del total del examen
- **Penalización probable**: -1/3 de punto por respuesta incorrecta (sistema habitual en UGR)
- **Consejo**: no respondas si tienes menos del 50% de seguridad — la penalización hace que sea peor

---

## PREGUNTAS REALES DE PRADO (con respuestas)
> Estas son exactamente las que ha puesto la profesora en ejercicios de Prado

---

**P1.** Dado el siguiente código:
```cpp
int v1 = 4, v2 = 7;
int *p1 = &v1, *p2 = &v2;
p2 = p1;
*p1 += 10;
int res = 0;
if (*p1 == *p2) res++;
if (p1 == p2) res += 2;
```
¿Cuál es el valor de `res` al finalizar?

a) 0
b) 1
c) 2
d) **3** ✓

> `p2 = p1` hace que p2 apunte a v1. `*p1 += 10` → v1=14. Como p1 y p2 apuntan a la misma dirección, `*p1==*p2` (14==14) → res=1, y `p1==p2` (misma dirección) → res=3.

---

**P2.** Dado el siguiente código:
```cpp
float v1=2.7, v2=1.7;
float *p1=&v1, *p2=&v2;
(*p1) += 1;
(*p2) += 2;
int res = 0;
if (*p1 == *p2) res++;
if (p1 == p2) res += 2;
```
¿Cuál es el valor de `res`?

a) 0
b) **1** ✓
c) 2
d) 3

> v1 = 3.7, v2 = 3.7 → `*p1 == *p2` es true → res=1. p1 y p2 siguen apuntando a variables distintas → `p1 == p2` es false.

---

**P3.** Para recorrer `int array1[DIM]` con puntero en `for (p1=array1; p1 < array1+util_array1; p1++)`, ¿cuál es la declaración correcta de `p1`?

a) `int p1;`
b) **`int *p1;`** ✓
c) `int &p1;`
d) `const int *p1;`

> p1 debe ser un puntero a int que se pueda incrementar y comparar con una dirección.

---

**P4.** La declaración más adecuada para `reinicializar()` que reinicializa los campos de un objeto al valor por defecto es:

a) **`void reinicializar();`** ✓
b) `int reinicializar() const;`
c) `void reinicializar(Complejo & c);`
d) `void reinicializar() const;`

> Modifica el objeto → no puede ser `const`. No devuelve nada → `void`. No necesita parámetros.

---

**P5.** La declaración más adecuada para `contar(valor)` que cuenta cuántas veces aparece un valor en `SecuenciaEnteros` es:

a) `int contar(int value);`
b) **`int contar(int value) const;`** ✓
c) `void contar(SecuenciaEnteros c, int value, int & r);`
d) `int contar(int value, int & r) const;`

> No modifica el objeto → `const`. Devuelve el resultado → `int`. El valor es de entrada → por valor (int primitivo).

---

**P6.** La declaración más adecuada para `title(cad)` que recibe una cadena como entrada y devuelve una copia donde cada palabra empieza por mayúscula es:

a) **`void title(const string & cad, string & res);`** ✓
b) `void title(string cad, int util, string res);`
c) `void title(string & cad, int util, string res);`
d) `void title(string & cad, string res);`

> `cad` es entrada → `const string&`. El resultado sale por parámetro de salida `string&`. El `int util` es innecesario (los strings ya saben su tamaño). La opción d no protege `cad` con `const`.

---

**P7.** La declaración más adecuada para `media(v1, v2)` que recibe dos `float` de entrada y calcula el promedio es:

a) `float media(float & v1, float & v2) const;`
b) `float media(float & v1, float & v2);`
c) **`float media(float v1, float v2);`** ✓
d) `float media(float v1, float v2, float & result);`

> Tipos primitivos de solo lectura → por valor. Devuelve el resultado → por `return`. `const` no aplica a funciones libres.

---

**P8.** La declaración más adecuada para `interseccion()` método de `SecuenciaEnteros` que devuelve la intersección de dos secuencias es:

a) `SecuenciaEnteros interseccion(SecuenciaEnteros & c1, SecuenciaEnteros & c2);`
b) `SecuenciaEnteros interseccion(const SecuenciaEnteros & c2);`
c) `void interseccion(const SecuenciaEnteros c1, const SecuenciaEnteros c2, SecuenciaEnteros & c3);`
d) **`SecuenciaEnteros interseccion(const SecuenciaEnteros & c2) const;`** ✓

> Es método de la clase (ya tiene acceso a *this), el otro operando va por `const &`, no modifica ninguna → `const` al final.

---

**P7.** Dada la función `int funcion(int num)` que recibe `a` por valor, ¿qué relación hay entre `a`, `b` y `num`?

a) **`a`, `b` y `num` son tres variables diferentes** ✓
b) `num` es la referencia y `a` es la variable origen
c) `num` es la referencia y `b` es la variable origen
d) `a` es la referencia y `num` es la variable origen

> Paso por valor: `num` es una copia de `a`. Son variables independientes.

---

**P8.** La declaración más adecuada para `desplazar(char, int)` que desplaza un carácter en la tabla ASCII es:

a) `char desplazar(char & v1, int & n);`
b) **`char desplazar(char v1, int n);`** ✓
c) `void desplazar(char v1, int n, char & result);`
d) `char desplazar(const char & v1, const int & n);`

> Tipos primitivos de entrada → por valor es lo más adecuado. Devuelve el resultado → por return.

---

**P9.** Dadas estas instrucciones, ¿cuántas **variables** hay?
```cpp
string cadena1, cadena2 = "Feliz ";
string & cadena3 = cadena2;
```

a) ninguna válida
b) **2** ✓
c) 3
d) 4

> `cadena3` es una referencia (alias) de `cadena2`, no una variable nueva. Variables: `cadena1` y `cadena2`.

---

**P10.** ¿Qué ocurre al ejecutar esto?
```cpp
void insertaPrefijo(string & cadena) { cadena = "des" + cadena; }
const string otraCadena = "aprender";
insertaPrefijo(otraCadena);
```

a) Error de compilación en la asignación.
b) El parámetro es entrada/salida, asignación permitida, se modifica cadena.
c) Asignación permitida, se modifica cadena (copia de otraCadena), otraCadena no cambia.
d) **Error de compilación en la llamada: `const string` no puede pasarse como `string &`** ✓

> Una referencia no-const no puede enlazarse con una variable const.

---

**P11.** La declaración más adecuada para `toString(bool)` que devuelve un string es:

a) `void toString(bool v1);`
b) `string toString(bool & v1) const;`
c) **`string toString(bool v1);`** ✓
d) `string toString(bool v1, string & s);`

> Devuelve string por return. bool es primitivo → por valor. No hay objeto implicado → no `const` como función libre.

---

## TEMA 0 — Funciones y paso de parámetros

---

**P12.** ¿Cuál es la diferencia entre paso por valor y paso por referencia?

a) En paso por valor se crea una copia del argumento; en paso por referencia se trabaja directamente con el argumento original.
b) En paso por referencia se crea una copia; en paso por valor se trabaja con el original.
c) No hay diferencia en tiempo de ejecución.
d) **a) es correcta** ✓

---

**P13.** ¿Qué imprime el siguiente código?
```cpp
void f(int x) { x = x * 2; }
int a = 5;
f(a);
cout << a;
```

a) 10
b) **5** ✓
c) Error de compilación
d) Comportamiento indefinido

> Paso por valor: `x` es copia de `a`. Modificar `x` no afecta a `a`.

---

**P14.** ¿Qué imprime el siguiente código?
```cpp
void f(int& x) { x = x * 2; }
int a = 5;
f(a);
cout << a;
```

a) 5
b) **10** ✓
c) Error de compilación
d) Comportamiento indefinido

---

**P15.** ¿Cuál de estas declaraciones de función tiene un parámetro con valor por defecto correcto?

a) `void f(int x = 0, int y);`
b) **`void f(int x, int y = 0);`** ✓
c) `void f(int x = 0, int y = );`
d) `void f(int = x, int y);`

> Los parámetros con valor por defecto deben ir al final.

---

**P16.** Dado:
```cpp
void swap(int& a, int& b) { int tmp = a; a = b; b = tmp; }
int x = 3, y = 7;
swap(x, y);
```
¿Cuánto vale `x` tras la llamada?

a) 3
b) **7** ✓
c) 0
d) Error de compilación

---

**P17.** La sobrecarga de funciones permite:

a) Que una función tenga distintos valores de retorno con el mismo nombre y parámetros.
b) **Que existan varias funciones con el mismo nombre pero distinta lista de parámetros.** ✓
c) Que una función se llame a sí misma.
d) Que una función ignore sus parámetros.

---

**P18.** ¿Cuándo es obligatorio pasar un parámetro por referencia constante (`const T&`) en lugar de por valor?

a) Siempre que el parámetro sea de tipo `int`.
b) **Cuando el tipo es grande (objetos, strings, arrays) y no queremos modificarlo.** ✓
c) Solo cuando el parámetro es un puntero.
d) Nunca, siempre se puede pasar por valor.

---

## TEMA 1 — Arrays, cadenas y matrices

---

**P19.** ¿Cuál es el índice del último elemento de `int v[10]`?

a) 10
b) **9** ✓
c) 1
d) -1

---

**P20.** ¿Qué hace este código?
```cpp
int v[5] = {1, 2, 3};
cout << v[4];
```

a) Imprime 0
b) **Comportamiento indefinido** ✓
c) Error de compilación
d) Imprime 3

> `v[3]` y `v[4]` no están inicializados. Acceder a ellos es comportamiento indefinido (aunque en muchos compiladores se inicializa a 0 en arrays globales, no en locales).

> Nota: si fuera global o estático, imprimiría 0. En stack es indefinido.

---

**P21.** ¿Cuánto ocupa en memoria `double m[3][4]`?

a) 12 bytes
b) **96 bytes** ✓ (en sistemas con double de 8 bytes)
c) 7 bytes
d) 24 bytes

> 3 × 4 = 12 elementos × 8 bytes = 96 bytes.

---

**P22.** Al pasar un array a una función en C++:

a) Se pasa una copia completa del array.
b) **Se pasa un puntero al primer elemento.** ✓
c) Se produce un error si el array es grande.
d) Se pasa por referencia usando `&`.

---

**P23.** ¿Cuál es la forma correcta de declarar una función que recibe y modifica un array de int?

a) `void f(int v);`
b) `void f(const int* v, int n);`
c) **`void f(int* v, int n);`** ✓
d) `void f(int &v, int n);`

---

## TEMA 2 — Punteros y memoria dinámica

---

**P24.** ¿Qué es un puntero en C++?

a) Una variable que almacena un valor entero.
b) **Una variable que almacena una dirección de memoria.** ✓
c) Una referencia constante a otra variable.
d) Un tipo de array dinámico.

---

**P25.** Dado `int* p = nullptr;`, ¿qué ocurre al ejecutar `*p = 5;`?

a) Se asigna 5 a la variable apuntada correctamente.
b) Error de compilación.
c) **Error en tiempo de ejecución (segfault).** ✓
d) Se asigna 5 a p.

---

**P26.** ¿Cuál es la diferencia entre `delete p` y `delete[] p`?

a) No hay diferencia.
b) `delete p` libera más memoria.
c) **`delete` es para un solo objeto (`new T`); `delete[]` es para arrays (`new T[n]`).** ✓
d) `delete[]` solo funciona con arrays de tamaño conocido.

---

**P27.** ¿Qué problema tiene este código?
```cpp
int* p = new int[10];
delete p;
```

a) No hay ningún problema.
b) Error de compilación.
c) **Comportamiento indefinido: se usó `new[]` pero se libera con `delete` en lugar de `delete[]`.** ✓
d) Solo libera el primer elemento.

---

**P28.** Dado:
```cpp
int a = 10;
int* p = &a;
*p = 20;
cout << a;
```
¿Qué imprime?

a) 10
b) **20** ✓
c) La dirección de memoria de a
d) Error de compilación

---

**P29.** ¿Qué hace `int** pp`?

a) Un puntero a int.
b) **Un puntero a un puntero a int (permite matrices dinámicas 2D).** ✓
c) Una matriz de punteros.
d) Un error de sintaxis.

---

**P30.** ¿Cuál es el valor de `p` después de `int v[5]; int* p = v; p++;`?

a) La dirección de `v[0]`.
b) **La dirección de `v[1]`.** ✓
c) La dirección de `v[5]`.
d) Error de compilación.

---

**P31.** ¿Qué problema representa el siguiente código?
```cpp
int* crearArray(int n) {
    int v[n];
    return v;
}
```

a) No compila porque n no es constante.
b) **Devuelve un puntero a una variable local que deja de existir al salir de la función.** ✓
c) Funciona correctamente.
d) Solo falla si n > 100.

---

**P32.** ¿Cómo se crea correctamente un array dinámico de 50 doubles?

a) `double v = new double[50];`
b) **`double* v = new double[50];`** ✓
c) `double[] v = new double(50);`
d) `double *v = malloc(50);`

---

## TEMA 4 — Clases con datos dinámicos

---

**P33.** ¿Cuándo es necesario implementar el destructor en una clase?

a) Siempre.
b) Nunca, C++ lo gestiona automáticamente.
c) **Cuando la clase tiene datos miembro que son punteros a memoria dinámica.** ✓
d) Solo cuando la clase tiene más de 5 atributos.

---

**P34.** ¿Por qué es necesario el constructor de copia cuando la clase tiene un puntero `T* _datos`?

a) No es necesario, el compilador hace una copia correcta.
b) **Porque la copia por defecto copiaría el puntero (shallow copy), haciendo que dos objetos apunten al mismo bloque de memoria.** ✓
c) Para mejorar el rendimiento.
d) Solo es necesario si la clase tiene más de un puntero.

---

**P35.** ¿Qué es el "autocheck" en el operador de asignación y por qué es necesario?

a) Es opcional y solo mejora el rendimiento.
b) **Es `if (this != &otro)` y evita que un objeto se destruya a sí mismo al hacer `a = a`.** ✓
c) Comprueba que los tipos sean compatibles.
d) Verifica que el objeto esté inicializado.

---

**P36.** ¿Qué ocurre si no implementas `operator=` en una clase con puntero `T* _datos`?

a) Error de compilación.
b) El compilador genera uno correcto automáticamente.
c) **El compilador genera una copia superficial (shallow copy): dos objetos apuntan al mismo bloque y el segundo `delete[]` provoca error.** ✓
d) La asignación siempre falla en tiempo de ejecución.

---

**P37.** En el patrón `allocate/deallocate/copy`, ¿cuál es el orden correcto en el operador de asignación?

a) `allocate → copy → deallocate`
b) `copy → deallocate → allocate`
c) **`deallocate → allocate → copy`** ✓
d) `copy → allocate → deallocate`

> Primero liberar la memoria antigua, luego reservar la nueva, luego copiar los datos.

---

**P38.** ¿Qué le falta a este destructor?
```cpp
VectorInt::~VectorInt() {
    delete _values;
    _values = nullptr;
}
```

a) Nada, está correcto.
b) **Debe usar `delete[]` en lugar de `delete` porque `_values` apunta a un array.** ✓
c) Debe poner `_size = 0` también.
d) No hace falta destructor.

---

**P39.** En tu proyecto Fraud4, `VectorInt` tiene `static const int BLOCK_SIZE = 20`. ¿Para qué sirve?

a) Para limitar el tamaño máximo del vector.
b) **Para redimensionar el array en bloques de 20 en lugar de elemento a elemento, reduciendo el número de realocaciones.** ✓
c) Es el tamaño inicial obligatorio.
d) Para controlar el índice máximo accesible.

---

**P40.** En `DataSet` de Fraud4, `_values` es `int**`. ¿Cómo se libera correctamente?

a) `delete[] _values;`
b) `delete _values;`
c) **Bucle liberando cada fila con `delete[] _values[i]`, luego `delete[] _values`.** ✓
d) No hace falta liberarlo, string lo gestiona.

---

**P41.** ¿Qué significa que un método sea `const`?
```cpp
int getSize() const;
```

a) El parámetro que recibe es constante.
b) El valor devuelto no puede modificarse.
c) **El método no puede modificar ningún dato miembro del objeto.** ✓
d) Solo puede llamarse sobre objetos constantes.

---

**P42.** ¿Por qué se implementan DOS versiones del `operator[]`?
```cpp
T& operator[](int i);
const T& operator[](int i) const;
```

a) Para mejorar la velocidad.
b) Para compatibilidad con versiones antiguas de C++.
c) **La versión `const` se usa cuando el objeto es constante (solo lectura); la no-const permite modificación.** ✓
d) Son equivalentes, solo una es necesaria.

---

## TEMA 5 — Sobrecarga de operadores

---

**P43.** ¿Cuáles de estos operadores NO pueden sobrecargarse en C++?

a) `+=`, `-=`
b) `<<`, `>>`
c) **`::`  (scope), `.` (miembro), `sizeof`** ✓
d) `[]`, `()`

---

**P44.** ¿Por qué `operator<<` y `operator>>` deben implementarse como funciones externas (`friend`) y no como métodos?

a) Por convención, no por obligación técnica.
b) **Porque el operando izquierdo es `ostream` o `istream`, que no es nuestra clase.** ✓
c) Porque los métodos no pueden devolver referencias.
d) Para poder acceder a los datos privados.

---

**P45.** ¿Qué devuelve correctamente `operator+=`?

a) `void`
b) El valor del objeto modificado por valor
c) **Una referencia al objeto modificado: `X& operator+=(const T& e)`** ✓
d) Un puntero al objeto

> Devolver referencia permite encadenar: `a += b += c`.

---

**P46.** ¿Qué problema tiene este `operator=`?
```cpp
Tienda Tienda::operator=(const Tienda& otra) {
    deallocate();
    allocate(otra.capacidad);
    copy(otra);
    return *this;
}
```

a) Falta el autocheck `if (this != &otra)`.
b) Devuelve por valor en vez de por referencia.
c) **Ambas: falta el autocheck Y debe devolver `Tienda&` no `Tienda`.** ✓
d) No hay ningún problema.

---

**P47.** Si implementas `operator>` como el único operador relacional basado en una métrica, ¿cómo implementas `operator<` eficientemente?

a) `return b.metrica() < a.metrica();`
b) **`return b > a;`** ✓ (reutiliza operator>)
c) `return !(a > b);`
d) No se puede implementar solo con `operator>`.

---

**P48.** ¿Cuál es la firma correcta de `operator<<` para una clase `Tienda`?

a) `ostream operator<<(ostream os, Tienda t);`
b) `void operator<<(ostream& os, const Tienda& t);`
c) **`ostream& operator<<(ostream& os, const Tienda& t);`** ✓
d) `Tienda& operator<<(ostream& os);`

---

## TEMA 6 — Ficheros E/S

---

**P49.** ¿Qué include es necesario para usar `ifstream` y `ofstream`?

a) `#include <iostream>`
b) **`#include <fstream>`** ✓
c) `#include <file>`
d) `#include <stream>`

---

**P50.** ¿Qué hace `getline(is, s)` frente a `is >> s`?

a) Son equivalentes.
b) `getline` lee solo una palabra; `>>` lee la línea completa.
c) **`getline` lee hasta el salto de línea (puede incluir espacios); `>>` lee hasta el primer espacio/salto.** ✓
d) `getline` funciona solo con ficheros, no con `cin`.

---

**P51.** ¿Por qué se necesita `is.ignore()` entre `is >> n` y `getline(is, s)`?

a) Para limpiar el buffer de errores.
b) **Porque `>>` deja el `\n` en el buffer; `getline` lo leería como línea vacía si no se descarta.** ✓
c) Para avanzar al siguiente campo.
d) No es necesario, es opcional.

---

**P52.** En el patrón de constructor con fichero (cadena mágica), ¿qué ocurre si la primera línea del fichero no coincide con la cadena mágica?

a) Se lanza una excepción automáticamente.
b) El programa termina.
c) **El objeto queda inicializado como vacío/por defecto y no se leen datos.** ✓
d) Se lee el fichero igualmente ignorando la primera línea.

---

**P53.** ¿Cuál es la forma correcta de abrir un fichero para lectura y comprobar que se abrió?

a) `ifstream f(nombre); f.read();`
b) **`ifstream f(nombre); if (f) { /* leer */ } `** ✓
c) `FILE* f = open(nombre);`
d) `ifstream f; f = nombre;`

---

**P54.** ¿Qué diferencia hay entre `ofstream` e `ifstream`?

a) `ofstream` es más rápido.
b) **`ifstream` es para lectura; `ofstream` es para escritura.** ✓
c) `ifstream` solo funciona con ficheros binarios.
d) Son intercambiables.

---

**P55.** Para guardar un objeto con cadena mágica al fichero, ¿cuál es el patrón correcto?

a) `f << *this;`
b) `f.write(nombre);`
c) **`f << "CADENA_MAGICA" << endl; f << *this;`** ✓
d) `f >> *this;`

---

## PREGUNTAS SOBRE EL PROYECTO FRAUD4

---

**P56.** En `VectorInt` del proyecto Fraud4, ¿cuándo se produce la redimensión del array?

a) Cada vez que se añade un elemento.
b) Cuando `_size` supera `INT_MAX`.
c) **Cuando `_size` alcanza `_capacity`, se añaden `BLOCK_SIZE` (20) posiciones adicionales.** ✓
d) La redimensión no existe en VectorInt.

---

**P57.** En `Clustering` de Fraud4, ¿qué representa `_sumWCV`?

a) El número total de iteraciones del algoritmo.
b) El número de clusters.
c) **La suma de varianzas dentro de cada cluster (Within Cluster Variance), medida de calidad del clustering.** ✓
d) La distancia entre el centroide más cercano y el más lejano.

---

**P58.** En `DataSet` de Fraud4, `_values` es `int**`. ¿Qué estructura representa?

a) Un array de punteros a enteros.
b) **Una matriz 2D dinámica donde `_values[i][j]` es el valor j de la instancia i.** ✓
c) Un array de arrays de tamaño fijo.
d) Un puntero a un vector de enteros.

---

**P59.** ¿Por qué `Location` en Fraud4 NO necesita destructor ni constructor de copia?

a) Porque es una clase pequeña.
b) Porque la profesora no lo pidió.
c) **Porque sus datos miembro (`_x`, `_y`, `_name`) son tipos que gestionan su propia memoria (double, string). No hay punteros.** ✓
d) Porque tiene un `operator=` definido.

---

**P60.** El algoritmo K-means en `Clustering::run()` itera hasta que:

a) Se completen exactamente 100 iteraciones.
b) La suma WCV sea menor que un umbral.
c) **Ningún punto cambie de cluster entre dos iteraciones consecutivas.** ✓
d) Todos los clusters tengan el mismo número de puntos.

---

## PREGUNTAS DIFÍCILES (trampa habitual)

---

**P61.** ¿Qué imprime este código?
```cpp
int a = 5;
int& b = a;
b = 10;
cout << a << " " << b;
```

a) `5 10`
b) `5 5`
c) **`10 10`** ✓
d) Error de compilación

> `b` es alias de `a`. Modificar `b` es modificar `a`.

---

**P62.** ¿Qué diferencia hay entre estos dos métodos?
```cpp
// A
string toString() const { return _name; }
// B
string& toString() { return _name; }
```

a) A no puede llamarse, B sí.
b) Ninguna diferencia práctica.
c) **A devuelve una copia (seguro). B devuelve una referencia a dato interno (peligroso si el objeto se destruye).** ✓
d) B no compila.

---

**P63.** ¿Cuál de estas clases necesita destructor?

a) `class A { int x; string s; };`
b) `class B { int x; double y; };`
c) **`class C { int* datos; int n; };`** ✓
d) `class D { string nombre; vector<int> v; };`

> Solo C tiene un puntero a memoria dinámica que hay que liberar manualmente.

---

**P64.** ¿Qué ocurre si llamas a `delete[]` dos veces sobre el mismo puntero?

a) No pasa nada, está permitido.
b) El compilador lo detecta y lo ignora.
c) **Comportamiento indefinido (double free), puede causar crash o corrupción de memoria.** ✓
d) Solo se libera la memoria una vez.

> Por eso en `deallocate()` siempre se hace `_data = nullptr` después de `delete[]`.

---

**P65.** ¿Qué hace `allocate(0)` en el patrón habitual de este temario?

a) Error: no se puede reservar 0 bytes.
b) Reserva 1 posición para evitar el nullptr.
c) **Pone `_capacity = 0` y `_data = nullptr` (objeto vacío pero válido).** ✓
d) Libera la memoria existente.

---

## TABLA RESUMEN DE RESPUESTAS

| P | R | P | R | P | R | P | R | P | R |
|---|---|---|---|---|---|---|---|---|---|
| 1 | d | 2 | b | 3 | b | 4 | a | 5 | b |
| 6 | d | 7 | a | 8 | b | 9 | b | 10 | d |
| 11 | c | 12 | a | 13 | b | 14 | b | 15 | b |
| 16 | b | 17 | b | 18 | b | 19 | b | 20 | b |
| 21 | b | 22 | b | 23 | c | 24 | b | 25 | c |
| 26 | c | 27 | c | 28 | b | 29 | b | 30 | b |
| 31 | b | 32 | b | 33 | c | 34 | b | 35 | b |
| 36 | c | 37 | c | 38 | b | 39 | b | 40 | c |
| 41 | c | 42 | c | 43 | c | 44 | b | 45 | c |
| 46 | c | 47 | b | 48 | c | 49 | b | 50 | c |
| 51 | b | 52 | c | 53 | b | 54 | b | 55 | c |
| 56 | c | 57 | c | 58 | b | 59 | c | 60 | c |
| 61 | c | 62 | c | 63 | c | 64 | c | 65 | c |

---

## ESTRATEGIA PARA EL TIPO TEST

1. **Lee todas las opciones** antes de elegir — las opciones trampa son muy similares.
2. **Las preguntas de declaración de métodos**: pregúntate siempre — ¿modifica el objeto? (¿`const`?), ¿qué devuelve? (¿`void` o tipo?), ¿cómo se pasan los parámetros? (valor, referencia, const referencia).
3. **Las preguntas de punteros**: traza la ejecución línea a línea con un diagrama mental de cajas y flechas.
4. **Con penalización -1/3**: si dudas entre 2 opciones y no sabes → no respondas. Si tienes 3 opciones descartadas → responde siempre aunque no estés seguro.
5. **Las preguntas de Prado son exactamente del mismo estilo** que lo que pondrán en el examen — repásalas hasta que las sepas de memoria.


---

# BANCO AMPLIADO — Generado de los apuntes

## TEMA 0 — Funciones y paso de parámetros (preguntas nuevas)

---

**P66.** ¿Cuál es la diferencia entre una función y un procedimiento en C++?

a) En C++ no existen procedimientos.
b) Un procedimiento puede devolver varios valores; una función solo uno.
c) **Una función devuelve un valor con `return`; un procedimiento tiene tipo de retorno `void` y no devuelve nada.** ✓
d) Solo las funciones pueden recibir parámetros.

> En C++ los "procedimientos" son simplemente funciones con tipo de retorno `void`. Toda función que devuelve algo usa `return`.

---

**P67.** ¿Qué imprime el siguiente código?
```cpp
int f(int& x, int y) {
    x = x + y;
    y = y * 2;
    return x + y;
}
int a = 3, b = 4;
int r = f(a, b);
cout << a << " " << b << " " << r;
```

a) `3 4 15`
b) `7 4 15`
c) `7 8 7`
d) **`7 4 15`** ✓

> `x` es referencia a `a`: `a` pasa a 3+4=7. `y` es copia de `b`: `y`=8 (local). `return` = 7+8=15. `b` no cambia → salida: `7 4 15`.

---

**P68.** En C++, ¿qué regla se aplica cuando hay varios candidatos en la resolución de sobrecarga de funciones?

a) Se llama a la primera función declarada con ese nombre.
b) Se produce siempre un error de ambigüedad.
c) **Se elige la función cuya lista de parámetros hace coincidir los tipos del argumento de manera más exacta (mejor conversión).** ✓
d) Se elige la función con más parámetros.

> El compilador aplica las reglas de "mejor coincidencia": coincidencia exacta > promoción > conversión estándar > conversión definida por usuario.

---

**P69.** Dado el prototipo `void f(int x, double y = 3.14, bool z = false);`, ¿cuál de estas llamadas es INCORRECTA?

a) `f(1);`
b) `f(1, 2.0);`
c) `f(1, 2.0, true);`
d) **`f(1, , true);`** ✓

> No se puede omitir un argumento intermedio dejando el hueco vacío. Los valores por defecto se omiten siempre por la derecha.

---

**P70.** ¿Qué devuelve una función con tipo de retorno `void` si se ejecuta `return;`?

a) El valor 0.
b) El valor `nullptr`.
c) Error de compilación, `void` no puede tener `return`.
d) **Nada; termina la ejecución de la función y devuelve el control al punto de llamada.** ✓

> `return;` sin expresión es válido en funciones `void` y simplemente termina la función.

---

**P71.** ¿Cuál es la declaración correcta para una función `potencia` que recibe una base `double` y un exponente entero (ambos de entrada) y devuelve el resultado como `double`?

a) `double potencia(double& base, int& exp);`
b) `void potencia(double base, int exp, double& res);`
c) **`double potencia(double base, int exp);`** ✓
d) `double potencia(const double& base, const int& exp);`

> Tipos primitivos de solo lectura se pasan por valor. El resultado se devuelve por `return`. La opción d es técnicamente válida pero redundante e innecesaria para primitivos.

---

**P72.** ¿Qué significa que una función sea `inline`?

a) Solo puede llamarse una vez.
b) **Es una sugerencia al compilador para que sustituya la llamada por el cuerpo de la función, evitando el coste de la llamada.** ✓
c) La función se compila en un fichero separado.
d) Solo puede usarse con funciones sin parámetros.

> `inline` es una optimización para funciones pequeñas. El compilador puede ignorar la sugerencia.

---

**P73.** Dado:
```cpp
void incrementa(int* p) { (*p)++; }
int x = 10;
incrementa(&x);
cout << x;
```
¿Qué imprime?

a) 10
b) **11** ✓
c) Error de compilación
d) La dirección de x

> Se pasa la dirección de `x` como puntero. `(*p)++` desreferencia y modifica el valor original.

---

**P74.** ¿Cuál de estas afirmaciones sobre la recursividad es CORRECTA?

a) Una función recursiva nunca puede sustituirse por un bucle.
b) La recursividad es siempre más eficiente que la iteración.
c) Una función recursiva sin caso base compila pero da error de enlace.
d) **Una función recursiva sin caso base provoca desbordamiento de pila (stack overflow) en tiempo de ejecución.** ✓

> Sin caso base, la función se llama a sí misma indefinidamente hasta agotar la pila.

---

**P75.** ¿Qué imprime este código?
```cpp
int suma(int n) {
    if (n == 0) return 0;
    return n + suma(n - 1);
}
cout << suma(4);
```

a) 4
b) 6
c) **10** ✓
d) 24

> suma(4) = 4+3+2+1+0 = 10.

---

**P76.** ¿Cuál es la declaración más adecuada para `mayor(a, b)` que determina cuál de dos objetos `Complejo` tiene mayor módulo, sin modificarlos?

a) `bool mayor(Complejo a, Complejo b);`
b) `bool mayor(Complejo& a, Complejo& b);`
c) **`bool mayor(const Complejo& a, const Complejo& b);`** ✓
d) `Complejo mayor(const Complejo& a, const Complejo& b) const;`

> Objetos grandes: se pasan por referencia. Solo lectura: `const`. `const` al final solo aplica a métodos de clase, no a funciones libres.

---

**P77.** ¿Qué problema tiene este código?
```cpp
double& leerValor() {
    double x;
    cin >> x;
    return x;
}
```

a) `cin >> x` no funciona con `double`.
b) No se puede devolver `double&` desde una función.
c) **Devuelve una referencia a una variable local que deja de existir al salir de la función (dangling reference).** ✓
d) Falta `return 0` al final.

> Las variables locales se destruyen al salir de su función. Devolver una referencia a ellas produce comportamiento indefinido.

---

**P78.** En el paso de parámetros, ¿cuándo se usa `T&` (referencia no const) en lugar de `const T&`?

a) Cuando el tipo es primitivo.
b) Cuando el parámetro es de solo lectura.
c) **Cuando la función necesita modificar el valor original del argumento (parámetro de entrada/salida o salida).** ✓
d) `T&` y `const T&` son equivalentes.

> `T&` permite lectura y escritura del objeto original. `const T&` solo permite lectura.

---

**P79.** ¿Cuál es la declaración más adecuada para `leerSecuencia(s)`, que lee desde `cin` los datos de un objeto `SecuenciaEnteros` y lo rellena?

a) `void leerSecuencia(const SecuenciaEnteros& s);`
b) `SecuenciaEnteros leerSecuencia();`
c) **`void leerSecuencia(SecuenciaEnteros& s);`** ✓
d) `void leerSecuencia(SecuenciaEnteros s);`

> La función modifica `s` → no puede ser `const`. Se pasa por referencia para que los cambios persistan. Devolver por copia (opción b) es válido pero menos eficiente y no es el patrón habitual del temario.

---

**P80.** ¿Qué ocurre en C++ si defines dos funciones con el mismo nombre y exactamente los mismos tipos de parámetros pero diferente tipo de retorno?

a) Se usa la que tiene el tipo de retorno más preciso.
b) La segunda definición sobreescribe a la primera.
c) **Error de compilación: el tipo de retorno no forma parte de la firma de la función para la resolución de sobrecarga.** ✓
d) La sobrecarga es válida si se usan en contextos distintos.

> Solo los tipos y número de parámetros determinan la firma. El tipo de retorno no se considera.

---

**P81.** Dado:
```cpp
void f(int a, int b = 5, int c = 10) {
    cout << a + b + c;
}
f(1, 2);
```
¿Qué imprime?

a) 16
b) **13** ✓
c) 6
d) Error de compilación

> `a=1, b=2, c=10` (valor por defecto). 1+2+10=13.

---

**P82.** ¿Cuál de los siguientes prototipos de función es INVÁLIDO en C++?

a) `void f(int x = 0);`
b) `int f(int x, int y = 1);`
c) **`int f(int x = 0, int y);`** ✓
d) `void f(int x, double y = 3.14);`

> Los parámetros con valor por defecto deben estar todos a la derecha. En c), `y` sin valor por defecto está después de `x` que sí lo tiene: inválido.

---

**P83.** ¿Qué ventaja tiene devolver un resultado mediante parámetro de salida (`T& resultado`) en lugar de por `return`?

a) Es obligatorio para tipos no primitivos.
b) Mejora la legibilidad siempre.
c) **Permite que la función devuelva múltiples resultados simultáneamente mediante varios parámetros de salida.** ✓
d) No hay ninguna ventaja; siempre se prefiere `return`.

> Con `return` solo se puede devolver un valor. Los parámetros de salida permiten devolver varios resultados a la vez.

---

**P84.** ¿Cuál es la declaración más adecuada para `convertir(cad, n)` que transforma una cadena `cad` en el entero `n` (resultado de salida) y devuelve `true` si la conversión fue exitosa?

a) `void convertir(string cad, int n);`
b) `int convertir(const string& cad);`
c) **`bool convertir(const string& cad, int& n);`** ✓
d) `bool convertir(string& cad, int& n);`

> `cad` es entrada → `const string&`. `n` es resultado de salida → `int&`. El éxito/fracaso se devuelve como `bool`.

---

**P85.** ¿Qué imprime el siguiente código?
```cpp
int x = 1;
void f() { int x = 2; cout << x; }
f();
cout << x;
```

a) `1 1`
b) `2 2`
c) **`2 1`** ✓
d) Error de compilación

> La `x` local de `f()` oculta a la global dentro de `f()`. Al salir de `f()`, la `x` global sigue siendo 1.

---

## TEMA 1 — Arrays, cadenas y matrices (preguntas nuevas)

---

**P86.** ¿Qué imprime el siguiente código?
```cpp
int v[5] = {10, 20, 30, 40, 50};
int* p = v + 2;
cout << *(p + 1);
```

a) 30
b) **40** ✓
c) 20
d) Error de compilación

> `p = v+2` apunta a `v[2]=30`. `*(p+1)` apunta a `v[3]=40`.

---

**P87.** ¿Cuál es el resultado de `strlen("hola")` en C++?

a) 5 (incluye el terminador `\0`)
b) **4** ✓
c) Error: `strlen` no existe en C++
d) Depende del compilador

> `strlen` devuelve el número de caracteres sin contar el `\0` final.

---

**P88.** ¿Cuál es la diferencia entre `string` de C++ y las cadenas de estilo C (`char[]`)?

a) No hay diferencia funcional.
b) `string` no puede concatenarse con `+`.
c) **`string` gestiona automáticamente su memoria y tamaño; `char[]` tiene tamaño fijo y requiere `\0` manual.** ✓
d) `char[]` es más seguro porque tiene comprobación de límites.

---

**P89.** Dado `string s = "Hola Mundo";`, ¿qué devuelve `s.substr(5, 3)`?

a) `"Hola"`
b) `"Mund"`
c) **`"Mun"`** ✓
d) `"und"`

> `substr(pos, len)`: empieza en índice 5 (`'M'`), toma 3 caracteres → `"Mun"`.

---

**P90.** ¿Cómo se pasa correctamente una matriz `int m[3][4]` a una función?

a) `void f(int m[][])`
b) `void f(int** m)`
c) **`void f(int m[][4], int filas)`** ✓
d) `void f(int m[3][])`

> Al pasar una matriz a una función, se puede omitir la primera dimensión pero la segunda (y siguientes) deben especificarse para que el compilador calcule correctamente los desplazamientos.

---

**P91.** ¿Qué hace `s.find("lo")` si `s = "hola"`?

a) Devuelve 0
b) **Devuelve 2** ✓
c) Devuelve -1
d) Devuelve `string::npos`

> `"lo"` empieza en el índice 2 de `"hola"` (`h`=0, `o`=1, `l`=2, `a`=3).

---

**P92.** ¿Qué valor devuelve `s.find("xyz")` cuando la subcadena NO existe?

a) -1
b) 0
c) **`string::npos`** ✓
d) Error en tiempo de ejecución

> `string::npos` es el valor centinela que devuelve `find` cuando no encuentra la subcadena (equivale a `size_t(-1)`).

---

**P93.** ¿Cuál es la forma correcta de recorrer un array `int v[N]` con sus elementos válidos en `v[0]..v[util-1]`?

a) `for (int i = 1; i <= util; i++)`
b) `for (int i = 0; i < N; i++)`
c) **`for (int i = 0; i < util; i++)`** ✓
d) `for (int i = 0; i <= util; i++)`

> El recorrido correcto es desde 0 hasta `util-1` (no hasta `N-1`, ya que el array puede no estar lleno).

---

**P94.** ¿Qué imprime este código?
```cpp
string s = "abcde";
s[2] = 'X';
cout << s;
```

a) `abcde`
b) `abXde`
c) **`abXde`** ✓
d) Error: `string` es inmutable

> `operator[]` de `string` devuelve referencia y permite modificar el carácter en esa posición.

---

**P95.** Dado `int m[2][3] = {{1,2,3},{4,5,6}};`, ¿cuánto vale `m[1][2]`?

a) 3
b) 4
c) 5
d) **6** ✓

> `m[1]` es la segunda fila `{4,5,6}`. `m[1][2]` es el tercer elemento: 6.

---

**P96.** ¿Cuál es la declaración correcta para una función que busca un valor en un array y devuelve su posición (o -1 si no está)?

a) `void buscar(int v[], int n, int val, int& pos);`
b) **`int buscar(const int v[], int n, int val);`** ✓
c) `int buscar(int* v, int n, int val);`
d) Las opciones b y c son igualmente correctas.

> b) y c) son técnicamente equivalentes para el compilador (`const int v[]` = `const int* v`). Sin embargo, el uso de `[]` expresa más claramente la intención de tratar el parámetro como array. Ambas son aceptables; b) es el estilo preferido en el temario.

---

**P97.** ¿Qué hace `s.erase(2, 3)` si `s = "abcdefg"`?

a) Borra el carácter en posición 2.
b) **Borra 3 caracteres a partir de la posición 2, dejando `s = "abfg"`.** ✓
c) Borra desde la posición 2 hasta el final.
d) Error: `erase` solo acepta un parámetro.

> `erase(pos, len)` borra `len` caracteres desde `pos`. `"abcdefg"` → borra `"cde"` → `"abfg"`.

---

**P98.** ¿Cuántas variables de tipo array se crean con `int v[5];` declarado localmente?

a) 5 variables enteras independientes.
b) **1 variable array (bloque contiguo de 5 enteros en la pila).** ✓
c) 1 puntero y 5 enteros en el heap.
d) Depende del valor de inicialización.

> Un array local es un único bloque de memoria contigua en la pila (stack). No hay asignación dinámica.

---

**P99.** ¿Qué hace `s.insert(2, "XY")` si `s = "abcd"`?

a) Reemplaza los caracteres en posición 2 y 3.
b) **Inserta `"XY"` a partir de la posición 2, resultando `"abXYcd"`.** ✓
c) Inserta `"XY"` al final.
d) Error: se necesita especificar el número de caracteres.

> `insert(pos, str)` inserta `str` antes de la posición `pos`.

---

**P100.** ¿Cuál es la diferencia entre `v[i]` y `*(v+i)` para un array `int v[]`?

a) `*(v+i)` solo funciona si `v` es un puntero dinámico.
b) `v[i]` es más rápido en tiempo de ejecución.
c) **Son completamente equivalentes: `v[i]` es azúcar sintáctica de `*(v+i)`.** ✓
d) `v[i]` devuelve el valor; `*(v+i)` devuelve la dirección.

> En C++, `a[b]` se define exactamente como `*(a+b)`. Son intercambiables.

---

**P101.** Dado:
```cpp
char s[] = "hola";
cout << sizeof(s);
```
¿Qué imprime?

a) 4
b) **5** ✓
c) 8
d) Depende del compilador

> `sizeof` de un array `char[]` incluye el terminador `\0`. `"hola"` tiene 4 letras + 1 terminador = 5 bytes.

---

**P102.** ¿Qué hace `s.compare("abc")` si `s = "abc"`?

a) Devuelve `true`.
b) **Devuelve 0.** ✓
c) Devuelve 1.
d) Error de compilación.

> `compare` devuelve 0 si las cadenas son iguales, negativo si `s` < argumento, positivo si `s` > argumento.

---

**P103.** Para ordenar un array `int v[]` de menor a mayor con el algoritmo de selección, ¿cuántos intercambios se realizan como máximo para un array de 5 elementos?

a) 25
b) 10
c) **4** ✓
d) 5

> El algoritmo de selección hace exactamente `n-1` intercambios (uno por pasada), independientemente de los datos.

---

**P104.** ¿Qué es la búsqueda binaria y cuál es su precondición?

a) Busca en cualquier array comparando todos los elementos.
b) **Busca en un array ORDENADO dividiendo el espacio de búsqueda por la mitad en cada paso.** ✓
c) Solo funciona con arrays de tamaño potencia de 2.
d) Requiere que el array esté en memoria dinámica.

> La búsqueda binaria tiene complejidad O(log n) pero EXIGE que el array esté ordenado.

---

**P105.** ¿Qué imprime el siguiente código?
```cpp
string s = "12345";
cout << s.length() << " " << s.size();
```

a) `5 4`
b) `6 6`
c) **`5 5`** ✓
d) Error de compilación

> `length()` y `size()` son sinónimos en `std::string`; ambos devuelven el número de caracteres sin `\0`.

---

## TEMA 2 — Punteros y memoria dinámica (preguntas nuevas)

---

**P106.** ¿Qué imprime el siguiente código?
```cpp
int v[] = {10, 20, 30, 40};
int* p = v;
p += 2;
cout << *p << " " << *(p-1);
```

a) `20 10`
b) `30 20`
c) **`30 20`** ✓
d) `40 30`

> `p = v` apunta a `v[0]=10`. `p+=2` → `v[2]=30`. `*(p-1)` → `v[1]=20`. Salida: `30 20`.

---

**P107.** ¿Qué diferencia hay entre `int* p` y `int* const p`?

a) No hay diferencia.
b) **`int* p` es un puntero que puede redirigirse a otra dirección; `int* const p` es un puntero constante que siempre apunta a la misma dirección.** ✓
c) `int* const p` no permite modificar el valor apuntado.
d) `int* p` no puede inicializarse con `nullptr`.

> `int* const p` = puntero constante (no se puede cambiar a dónde apunta). `const int* p` = puntero a constante (no se puede modificar el valor apuntado).

---

**P108.** ¿Cuántos bytes reserva `new int[10]` asumiendo `sizeof(int) = 4`?

a) 10
b) **40** ✓
c) 4
d) Depende del sistema operativo

> `new int[10]` reserva espacio para 10 enteros: 10 × 4 bytes = 40 bytes.

---

**P109.** ¿Qué problema tiene este código?
```cpp
int* p = new int(5);
p = new int(10);
```

a) Error de compilación: no se puede reasignar un puntero.
b) Funciona correctamente, el primer `new` se libera automáticamente.
c) **Memory leak: el primer bloque asignado con `new int(5)` queda sin liberar.** ✓
d) Comportamiento indefinido porque se usa `new` dos veces.

> Al reasignar `p`, se pierde la única referencia al primer bloque. Ese bloque queda inaccesible pero no liberado: memory leak.

---

**P110.** Dado:
```cpp
int a = 5, b = 10;
int *p = &a, *q = &b;
int **pp = &p;
**pp = 99;
cout << a;
```
¿Qué imprime?

a) 5
b) 10
c) **99** ✓
d) Error de compilación

> `pp` apunta a `p`, que apunta a `a`. `**pp` desreferencia dos veces → modifica `a` directamente → `a = 99`.

---

**P111.** ¿Cuál es la aritmética de punteros correcta para avanzar un `double*` en 3 posiciones?

a) `p = p + 24;` (3 × 8 bytes)
b) **`p = p + 3;`** ✓
c) `p = p + 3 * sizeof(double);`
d) `p += sizeof(double) * 3;`

> La aritmética de punteros ya tiene en cuenta el tamaño del tipo. `p+3` avanza 3 elementos `double` (equivalente a 24 bytes internamente, pero se escribe simplemente como `p+3`).

---

**P112.** ¿Qué ocurre si `new` no puede reservar la memoria solicitada?

a) Devuelve `nullptr` siempre.
b) El programa se termina automáticamente.
c) **Por defecto lanza la excepción `std::bad_alloc`.** ✓
d) Devuelve un puntero a memoria no válida.

> Con `new` estándar, si la asignación falla se lanza `bad_alloc`. Con `new(nothrow)` se devuelve `nullptr` en su lugar.

---

**P113.** ¿Cuál es la diferencia entre `const int* p` y `int* const p`?

a) Son lo mismo.
b) **`const int* p`: el valor apuntado no se puede modificar; `int* const p`: el puntero no puede redirigirse.** ✓
c) `int* const p` no puede desreferenciarse.
d) `const int* p` no puede inicializarse.

> La posición del `const` respecto al `*` determina qué es constante: el dato o el puntero.

---

**P114.** ¿Qué imprime este código?
```cpp
int v[4] = {1, 2, 3, 4};
int* ini = v;
int* fin = v + 4;
int suma = 0;
for (int* p = ini; p != fin; p++) suma += *p;
cout << suma;
```

a) 4
b) 6
c) **10** ✓
d) Error de compilación

> Recorre v[0]=1, v[1]=2, v[2]=3, v[3]=4. Suma = 10.

---

**P115.** ¿Qué es un puntero colgante (dangling pointer)?

a) Un puntero inicializado a `nullptr`.
b) Un puntero a un array dinámico.
c) **Un puntero que apunta a memoria que ya ha sido liberada o a una variable que ya no existe.** ✓
d) Un puntero que apunta a otro puntero.

> Usar un dangling pointer produce comportamiento indefinido. Por eso se asigna `nullptr` tras `delete`.

---

**P116.** ¿Qué hace `p++` si `p` es de tipo `char*` y apunta al primer carácter de `"Hola"`?

a) Suma 4 a la dirección de `p`.
b) **Avanza `p` un byte (un carácter), apuntando ahora a `'o'`.** ✓
c) Incrementa el valor del carácter apuntado.
d) Error de compilación: no se puede incrementar `char*`.

> `sizeof(char) = 1`, así que `char*++` avanza exactamente 1 byte.

---

**P117.** ¿Cuál es la forma correcta de crear dinámicamente una matriz 2D de 3 filas y 4 columnas?

a) `int** m = new int[3][4];`
b) `int m[][] = new int[3][4];`
c) **`int** m = new int*[3]; for(int i=0;i<3;i++) m[i] = new int[4];`** ✓
d) `int* m = new int[12];` (válida pero no permite acceso `m[i][j]`)

> Para una matriz 2D dinámica con acceso `m[i][j]`, se necesita primero reservar el array de punteros (filas) y luego cada fila individualmente.

---

**P118.** ¿Qué imprime el siguiente código?
```cpp
int* p = nullptr;
if (p) cout << "válido";
else cout << "nulo";
```

a) `válido`
b) **`nulo`** ✓
c) Error en tiempo de ejecución
d) Error de compilación

> `nullptr` se convierte a `false` en un contexto booleano. La condición `if(p)` es `false`.

---

**P119.** ¿Para qué sirve poner `_p = nullptr` después de `delete[] _p` en el destructor?

a) Para liberar la memoria nuevamente.
b) Para indicar al compilador que la memoria fue liberada.
c) **Para evitar que el puntero sea un dangling pointer y que un doble `delete` cause comportamiento indefinido.** ✓
d) Es obligatorio para que `delete[]` funcione.

> Tras `delete[]`, la memoria está liberada pero `_p` aún contiene la dirección antigua. Asignar `nullptr` hace que `delete nullptr` sea una operación segura (no hace nada).

---

**P120.** ¿Cuál es el resultado de `p - q` si `p` y `q` son punteros a elementos del mismo array `int v[10]`, con `p = &v[6]` y `q = &v[2]`?

a) 16 (6-2 multiplicado por sizeof(int))
b) 8
c) **4** ✓
d) Error de compilación

> La diferencia de punteros da el número de elementos entre ellos: 6 - 2 = 4.

---

**P121.** ¿Qué hace `new int(5)` frente a `new int[5]`?

a) Son equivalentes.
b) `new int(5)` crea un array de 5 enteros.
c) **`new int(5)` crea UN entero inicializado a 5; `new int[5]` crea un array de 5 enteros.** ✓
d) `new int[5]` inicializa todos los elementos a 5.

> Los paréntesis `()` son para el valor inicial; los corchetes `[]` son para el tamaño del array.

---

**P122.** ¿Cuál es el valor de `p` después de ejecutar `int* p = new int[5]; delete[] p; p = nullptr;`?

a) Apunta al bloque de memoria recién liberado.
b) Apunta al primer elemento libre del heap.
c) **`nullptr`** ✓
d) Valor indeterminado.

> Tras `p = nullptr`, `p` vale exactamente `nullptr` (la dirección nula).

---

**P123.** ¿Por qué no se puede hacer aritmética entre dos punteros que apuntan a arrays distintos?

a) El compilador lo prohíbe siempre.
b) Solo funciona si los arrays tienen el mismo tipo.
c) **Porque el resultado sería sin significado y produce comportamiento indefinido según el estándar C++.** ✓
d) Sí se puede, simplemente da la diferencia de bytes entre las dos direcciones.

> La aritmética de punteros solo está definida cuando ambos punteros pertenecen al mismo array (o uno más allá del último elemento).

---

**P124.** ¿Qué imprime el siguiente código?
```cpp
int x = 42;
const int* p = &x;
x = 100;
cout << *p;
```

a) 42
b) **100** ✓
c) Error de compilación
d) Comportamiento indefinido

> `const int* p` significa que no se puede modificar `x` a través de `p`, pero `x` puede modificarse directamente. `*p` refleja el valor actual de `x`.

---

**P125.** ¿Cuál es la declaración más adecuada para `buscarMax` que recibe un array de doubles y devuelve el puntero al elemento máximo?

a) `double buscarMax(double* v, int n);`
b) `double& buscarMax(double* v, int n);`
c) **`double* buscarMax(double* v, int n);`** ✓
d) `const double* buscarMax(const double* v, int n);`

> Devolver un puntero al elemento máximo permite tanto leer como modificar el elemento. Si se quisiera solo lectura, sería `const double*`.

---

## TEMA 4 — Clases con datos dinámicos (preguntas nuevas)

---

**P126.** ¿En qué orden se llama automáticamente el destructor de los atributos de una clase?

a) En el mismo orden en que fueron declarados.
b) En el orden en que fueron inicializados en el constructor.
c) **En orden inverso al de su declaración.** ✓
d) El orden no está definido.

> C++ destruye los miembros en orden inverso al de su declaración (y al de su construcción).

---

**P127.** ¿Cuándo se invoca automáticamente el constructor de copia?

a) Solo cuando se usa explícitamente `Clase c = Clase(otro);`
b) Nunca, siempre se invoca manualmente.
c) **Al inicializar un objeto con otro (`Clase b = a;`), al pasar por valor, y al devolver por valor.** ✓
d) Solo al devolver un objeto por valor.

> El constructor de copia se invoca en tres situaciones: inicialización por copia, paso por valor y retorno por valor.

---

**P128.** ¿Qué es la "regla de los tres" (rule of three) en C++?

a) Una clase debe tener exactamente 3 constructores.
b) **Si una clase necesita destructor personalizado, probablemente también necesita constructor de copia y `operator=` personalizados.** ✓
c) Un objeto puede copiarse como máximo 3 veces.
d) Toda clase debe implementar 3 métodos: constructor, destructor y `toString`.

> La regla de los tres: si gestionas recursos manualmente, los tres van de la mano: destructor, constructor de copia y operador de asignación.

---

**P129.** ¿Qué imprime este código si `VectorInt` tiene constructor de copia correcto (deep copy)?
```cpp
VectorInt a;
a.push_back(1);
a.push_back(2);
VectorInt b = a;      // copia
b.push_back(3);
cout << a.size() << " " << b.size();
```

a) `3 3`
b) `2 2`
c) **`2 3`** ✓
d) Comportamiento indefinido

> Con deep copy, `b` tiene su propio array independiente. Añadir a `b` no afecta a `a`.

---

**P130.** ¿Qué función especial se genera automáticamente por el compilador si NO la defines?

a) Solo el constructor por defecto.
b) **Constructor por defecto, constructor de copia, `operator=` y destructor (todos con comportamiento de copia superficial).** ✓
c) Solo el destructor.
d) Ninguna función se genera automáticamente.

> El compilador genera las cuatro funciones especiales con copia miembro a miembro (shallow copy) si no las defines.

---

**P131.** ¿Cuál es el problema de la copia superficial (shallow copy) cuando la clase tiene un `int* _datos`?

a) Copia los datos incorrectamente.
b) Solo copia el primer elemento.
c) **Dos objetos quedan apuntando al mismo bloque de memoria: modificar uno afecta al otro, y el `delete[]` doble al destruir ambos produce comportamiento indefinido.** ✓
d) El compilador detecta el problema y lanza un error.

---

**P132.** ¿Qué hace el siguiente constructor de copia?
```cpp
VectorInt::VectorInt(const VectorInt& otro) {
    _capacity = otro._capacity;
    _size = otro._size;
    _values = new int[_capacity];
    for (int i = 0; i < _size; i++)
        _values[i] = otro._values[i];
}
```

a) Realiza una copia superficial.
b) Comparte el bloque de memoria con `otro`.
c) **Realiza una copia profunda (deep copy): reserva nuevo array y copia elemento a elemento.** ✓
d) Error de compilación: falta `const` en el bucle.

---

**P133.** En el patrón `allocate/deallocate/copy`, ¿qué debe hacer `allocate(n)`?

a) Liberar la memoria existente y reservar nueva.
b) Solo inicializar `_size` y `_capacity` a 0.
c) **Reservar un array de tamaño `n` con `new`, asignar `_capacity = n` y `_size = 0`.** ✓
d) Copiar los datos de otro objeto.

---

**P134.** ¿Qué debe devolver un operador de asignación `operator=` bien implementado?

a) `void`
b) Una copia del objeto por valor
c) Un `bool` indicando éxito
d) **Una referencia al objeto modificado (`*this`)** ✓

> Devolver `*this` permite el encadenamiento: `a = b = c;`.

---

**P135.** ¿Cuándo se llama el destructor de un objeto local?

a) Cuando el objeto se pasa por valor a una función.
b) Al inicio del programa.
c) **Al salir del bloque (`{}`) en el que fue declarado.** ✓
d) Solo cuando se usa `delete` explícitamente.

> Los objetos locales se destruyen automáticamente al salir de su ámbito (RAII).

---

**P136.** ¿Qué problema detecta el siguiente operador de asignación?
```cpp
VectorInt& VectorInt::operator=(const VectorInt& otro) {
    deallocate();
    allocate(otro._capacity);
    copy(otro);
    return *this;
}
```

a) Falta devolver por valor.
b) `deallocate` debería ir al final.
c) **Falta el autocheck `if (this != &otro)`: si se asigna un objeto a sí mismo, `deallocate()` destruye los datos que `copy()` luego intenta leer.** ✓
d) No hay ningún problema.

---

**P137.** ¿Qué método de `VectorInt` debería ser `const`?

a) `push_back(int val)`
b) `operator=(const VectorInt&)`
c) **`size()` que devuelve el número de elementos.** ✓
d) El destructor.

> `size()` solo consulta el estado del objeto sin modificarlo → debe marcarse `const`.

---

**P138.** ¿Por qué en el constructor de `VectorInt` con parámetro `int n` se suele inicializar `_size = 0` y `_capacity = n`?

a) Por eficiencia: `_size = n` sería incorrecto.
b) Porque `_capacity` siempre debe ser menor que `_size`.
c) **Porque el vector empieza vacío (0 elementos útiles) pero con capacidad reservada para `n` elementos.** ✓
d) Para que `operator[]` no compruebe límites.

---

**P139.** ¿Qué ocurre si el destructor de una clase lanza una excepción?

a) La excepción se propaga normalmente.
b) El programa continúa.
c) **Comportamiento indefinido o terminación del programa: los destructores no deben lanzar excepciones.** ✓
d) La excepción se ignora automáticamente.

> Si un destructor se llama durante el desenrollado de la pila (por otra excepción) y lanza otra excepción, el programa llama a `std::terminate`.

---

**P140.** ¿Cuál es la firma correcta del constructor de copia de una clase `MiClase`?

a) `MiClase(MiClase otro);`
b) `MiClase(MiClase* otro);`
c) **`MiClase(const MiClase& otro);`** ✓
d) `void MiClase(const MiClase& otro);`

> El constructor de copia DEBE recibir por referencia (si fuera por valor se llamaría a sí mismo recursivamente infinitamente). `const` porque no modifica el original.

---

**P141.** En `VectorInt`, cuando `_size == _capacity` y se intenta hacer `push_back`, ¿cuál es la secuencia correcta de operaciones?

a) Aumentar `_size`, copiar datos, reservar nuevo array.
b) Reservar nuevo array, liberar el antiguo, aumentar `_size`.
c) **Reservar nuevo array más grande, copiar datos, liberar el antiguo, actualizar `_capacity`.** ✓
d) Aumentar `_capacity` en 1 y continuar sin reservar.

> La secuencia es: reservar nuevo (más grande), copiar datos al nuevo, liberar el viejo, reasignar el puntero y actualizar `_capacity`.

---

**P142.** ¿Para qué sirve el especificador `explicit` en un constructor de un solo parámetro?

a) Para que el constructor solo pueda llamarse en ficheros `.cpp`.
b) **Para evitar conversiones implícitas no deseadas: el compilador no usará ese constructor automáticamente en conversiones.** ✓
c) Para que el constructor no pueda copiarse.
d) Para que el constructor sea `inline` automáticamente.

> Sin `explicit`, `MiClase obj = 5;` podría funcionar si hay un constructor `MiClase(int)`. Con `explicit`, solo funciona `MiClase obj(5);`.

---

**P143.** ¿Cuál es la diferencia entre un atributo declarado como `static` en una clase y un atributo normal?

a) Los atributos `static` solo pueden ser `const`.
b) Los atributos `static` no pueden inicializarse.
c) **Un atributo `static` es compartido por todos los objetos de la clase; uno normal es independiente en cada objeto.** ✓
d) Los atributos `static` se destruyen antes que los normales.

> `static const int BLOCK_SIZE = 20;` en `VectorInt` existe una sola vez para toda la clase, no una copia por objeto.

---

**P144.** ¿Qué significa que un método sea `private` en una clase?

a) Solo puede llamarse desde otras clases.
b) No puede tener parámetros.
c) **Solo puede llamarse desde otros métodos de la misma clase (encapsulación).** ✓
d) Es más lento que un método `public`.

> Los métodos `private` como `allocate`, `deallocate`, `copy` son de implementación interna y no forman parte de la interfaz pública.

---

**P145.** ¿Qué imprime el siguiente código si `A` tiene un constructor que imprime `"C"` y un destructor que imprime `"D"`?
```cpp
{ A obj1; A obj2; }
```

a) `C C D D`
b) `C D C D`
c) **`C C D D`** ✓
d) `C C D` (solo un destructor)

> Se construyen en orden: `obj1` luego `obj2`. Se destruyen en orden inverso: `obj2` luego `obj1`. Salida: `C C D D`.

---

## TEMA 5 — Sobrecarga de operadores (preguntas nuevas)

---

**P146.** ¿Cuál es la firma correcta del `operator+` binario para sumar dos objetos `Complejo`?

a) `void operator+(const Complejo& a, const Complejo& b);`
b) `Complejo operator+(Complejo a);`
c) **`Complejo operator+(const Complejo& a, const Complejo& b);`** ✓
d) `Complejo& operator+(const Complejo& a, const Complejo& b);`

> Devuelve un nuevo objeto (no referencia). Los operandos son `const&`. Puede implementarse como función libre o como método (recibiendo un operando por `const&`).

---

**P147.** ¿Por qué `operator+` debe devolver por valor y no por referencia?

a) Por convención histórica.
b) Por razones de rendimiento.
c) **Porque el resultado es un objeto temporal creado dentro de la función; devolver referencia a él sería un dangling reference.** ✓
d) Las dos formas son equivalentes.

---

**P148.** ¿Cuál es la relación correcta para implementar `operator+` a partir de `operator+=`?

a) `operator+=` se implementa a partir de `operator+`.
b) No hay relación entre ellos.
c) **`operator+(a, b)` se implementa creando una copia de `a` y aplicando `+= b` a la copia.** ✓
d) `operator+` llama a `operator+=` con el objeto original.

> El idioma habitual: `Complejo operator+(Complejo a, const Complejo& b) { return a += b; }`.

---

**P149.** ¿Qué es la sobrecarga del `operator()` (operador de llamada)?

a) Permite llamar a la clase como si fuera una función puntero.
b) **Hace que los objetos de la clase sean "llamables" como funciones: `obj(args)`.** ✓
c) Es equivalente a sobrecargar `operator[]`.
d) Solo se usa para iteradores.

> Un objeto con `operator()` sobrecargado se llama "functor" o "objeto función".

---

**P150.** Dado el `operator<` sobrecargado para `Fraccion`:
```cpp
bool operator<(const Fraccion& a, const Fraccion& b) {
    return a.num * b.den < b.num * a.den;
}
```
Si `a = 1/2` y `b = 3/4`, ¿devuelve `true` o `false`?

a) `false`
b) **`true`** ✓
c) Error de compilación
d) Comportamiento indefinido

> 1×4 < 3×2 → 4 < 6 → `true`. 1/2 < 3/4 efectivamente.

---

**P151.** ¿Cuál es la diferencia entre el `operator++` prefijo y postfijo?

a) No hay diferencia funcional.
b) El prefijo es más lento.
c) **El prefijo `++obj` incrementa y devuelve `*this` por referencia; el postfijo `obj++` guarda el estado anterior, incrementa y devuelve la copia antigua por valor.** ✓
d) El postfijo no puede sobrecargarse.

> El postfijo recibe un parámetro `int` ficticio para distinguirlo del prefijo: `operator++(int)`.

---

**P152.** ¿Cuál es la firma correcta del `operator++` POSTFIJO para una clase `Contador`?

a) `Contador& operator++();`
b) `Contador operator++();`
c) `Contador& operator++(int);`
d) **`Contador operator++(int);`** ✓

> El postfijo lleva un parámetro `int` (sin nombre, solo para distinguirlo). Devuelve por valor (copia del estado anterior).

---

**P153.** ¿Qué ocurre si sobrecargas `operator=` pero NO el constructor de copia en una clase con punteros?

a) Todo funciona correctamente.
b) El constructor de copia generado es correcto porque usa el `operator=`.
c) **El constructor de copia generado realiza shallow copy; solo las asignaciones posteriores a la construcción usarán tu `operator=` correcto.** ✓
d) Error de compilación al intentar copiar el objeto.

> El constructor de copia generado por el compilador NO usa `operator=`: realiza copia miembro a miembro directamente. Ambos deben implementarse.

---

**P154.** ¿Cuándo es obligatorio que `operator<<` sea función `friend` de la clase?

a) Siempre.
b) Nunca, se puede implementar con getters.
c) **Solo cuando necesita acceder a atributos privados de la clase y no hay getters disponibles.** ✓
d) Solo cuando la clase tiene punteros.

> Si la clase tiene getters para todos sus datos, `operator<<` puede implementarse sin `friend`. Si necesita acceder directamente a privados, debe ser `friend`.

---

**P155.** ¿Qué imprime el siguiente código?
```cpp
struct Punto {
    int x, y;
    Punto operator+(const Punto& o) const {
        return {x + o.x, y + o.y};
    }
};
Punto a{1,2}, b{3,4};
Punto c = a + b;
cout << c.x << " " << c.y;
```

a) `1 2`
b) `3 4`
c) **`4 6`** ✓
d) Error de compilación

> `c.x = 1+3 = 4`, `c.y = 2+4 = 6`.

---

**P156.** ¿Cuál es la firma correcta de `operator[]` no constante en `VectorInt`?

a) `int operator[](int i) const;`
b) `const int& operator[](int i) const;`
c) **`int& operator[](int i);`** ✓
d) `int operator[](int i);`

> La versión no-`const` devuelve `int&` para permitir escritura: `v[i] = 5;`. La versión `const` devuelve `const int&` para solo lectura.

---

**P157.** ¿Qué operadores NO pueden sobrecargarse en C++?

a) `+`, `-`, `*`, `/`
b) `<<`, `>>`
c) `==`, `!=`, `<`, `>`
d) **`::`  (resolución de ámbito), `.` (acceso a miembro), `.*`, `?:` (ternario), `sizeof`** ✓

> Estos operadores tienen significado especial en el lenguaje y no pueden redefinirse.

---

**P158.** ¿Cuál es la implementación correcta de `operator!=` usando `operator==`?

a) `bool operator!=(const T& a, const T& b) { return a != b; }` (recursivo)
b) `bool operator!=(const T& a, const T& b) { return !a; }`
c) **`bool operator!=(const T& a, const T& b) { return !(a == b); }` ✓**
d) No se puede implementar `!=` a partir de `==`.

> Reutilizar `operator==` es el idioma correcto y evita duplicar la lógica de comparación.

---

**P159.** ¿Por qué el `operator=` devuelve `T&` y no `T`?

a) Por requisito del compilador.
b) Para evitar la copia.
c) **Para permitir el encadenamiento `a = b = c` y para ser consistente con el comportamiento de los tipos primitivos.** ✓
d) Devolver `T` y `T&` son equivalentes para `operator=`.

---

**P160.** Si una clase `Matriz` tiene `operator*` para multiplicar dos matrices, ¿cuál es la firma más adecuada?

a) `void operator*(Matriz& a, Matriz& b, Matriz& res);`
b) `Matriz& operator*(const Matriz& otra) const;`
c) `Matriz operator*(Matriz otra) const;`
d) **`Matriz operator*(const Matriz& otra) const;`** ✓

> Devuelve nuevo objeto (no referencia). El operando derecho por `const&`. El operando izquierdo es `*this` → método `const`.

---

**P161.** ¿Qué hace el siguiente código?
```cpp
Complejo a(1, 2), b(3, 4);
a += b;
```
Asumiendo `operator+=` correctamente implementado, ¿cuánto vale `a`?

a) `(1, 2)` (no cambia)
b) `(3, 4)`
c) **`(4, 6)`** ✓
d) Error de compilación

> `operator+=` modifica `a` en lugar: parte real 1+3=4, parte imaginaria 2+4=6.

---

**P162.** ¿Cuál de las siguientes afirmaciones sobre la sobrecarga de operadores es INCORRECTA?

a) Se puede cambiar la precedencia de un operador al sobrecargarlo.
b) No se puede cambiar el número de operandos (aridad) de un operador.
c) El significado de los operadores para tipos primitivos no se puede cambiar.
d) **Se puede cambiar la precedencia de un operador al sobrecargarlo.** ✓ (esta afirmación es incorrecta)

> La precedencia y asociatividad de los operadores NO pueden cambiarse mediante sobrecarga.

---

**P163.** ¿Qué diferencia hay entre implementar `operator+` como método o como función libre?

a) Como método puede acceder a privados; como función libre no.
b) Como función libre es más eficiente.
c) **Como método, el operando izquierdo es `*this`; como función libre, ambos operandos son parámetros explícitos, lo que permite conversiones implícitas en el operando izquierdo.** ✓
d) No hay diferencia.

> Si `operator+` es método, `5 + obj` no funciona (int no tiene ese operador). Como función libre, ambos lados pueden tener conversiones implícitas.

---

**P164.** ¿Cuál es la firma correcta del `operator-` unario (negación) para una clase `Complejo`?

a) `Complejo operator-(const Complejo& a, const Complejo& b);`
b) `void operator-();`
c) **`Complejo operator-() const;`** ✓
d) `Complejo& operator-(int);`

> El operador unario `-` es un método sin parámetros (el único operando es `*this`). Devuelve un nuevo objeto negado. `const` porque no modifica `*this`.

---

**P165.** ¿Qué imprime el siguiente código asumiendo que `operator<<` está bien sobrecargado para `Complejo` con formato `(a+bi)`?
```cpp
Complejo c(2, -3);
cout << c;
```

a) `2 -3`
b) `Complejo(2,-3)`
c) **`(2+-3i)`** ✓ (o el formato exacto definido)
d) Error de compilación

> El formato exacto depende de la implementación. La opción c muestra el formato típico del temario. Lo esencial es que `operator<<` llama a la salida del flujo con los datos del objeto.

---

## TEMA 6 — Ficheros E/S (preguntas nuevas)

---

**P166.** ¿En qué se diferencian los ficheros de texto y los ficheros binarios?

a) Los ficheros binarios son más grandes.
b) Los ficheros de texto solo pueden contener letras.
c) **En los ficheros de texto los datos se guardan como caracteres imprimibles; en los binarios se guardan en la representación interna del tipo (bits).** ✓
d) Los ficheros binarios no pueden leerse con `ifstream`.

> En texto, `float 123.4` ocupa 5 caracteres. En binario, ocupa exactamente `sizeof(float)` = 4 bytes, independientemente del valor.

---

**P167.** ¿Cuál es la forma correcta de abrir un fichero binario para escritura?

a) `ofstream f("datos.bin");`
b) `ifstream f("datos.bin", ios::binary);`
c) **`ofstream f("datos.bin", ios::binary);`** ✓
d) `fstream f("datos.bin", ios::binary);`

> Para escritura binaria: `ofstream` con el flag `ios::binary`. Sin el flag, el fichero se abre en modo texto.

---

**P168.** ¿Qué bandera de estado del flujo se activa cuando se intenta leer más allá del final del fichero?

a) `failbit`
b) `badbit`
c) `goodbit`
d) **`eofbit`** ✓

> `eofbit` se activa al encontrar el fin de fichero (EOF). `failbit` se activa cuando no se pudo realizar la operación de E/S.

---

**P169.** ¿Qué hace `cin.clear()` tras un error de lectura?

a) Vacía el buffer de entrada.
b) Reinicia el flujo desde el principio.
c) **Borra las banderas de error del flujo, permitiendo nuevas operaciones de lectura.** ✓
d) Cierra y reabre el flujo.

> `clear()` borra los flags de error. Para vaciar además el buffer, se necesita `cin.ignore(numeric_limits<streamsize>::max(), '\n')`.

---

**P170.** ¿Cuál es la jerarquía correcta de clases de flujo en C++?

a) `istream` hereda de `ifstream`
b) `fstream` hereda de `iostream` directamente
c) **`ios_base` → `ios` → `istream`/`ostream` → `ifstream`/`ofstream`** ✓
d) `ifstream` y `ofstream` no tienen relación de herencia con `istream` y `ostream`

> La jerarquía es: `ios_base` → `ios` → `istream` → `ifstream`, y `ios` → `ostream` → `ofstream`. `fstream` hereda de `iostream` (que hereda de ambos).

---

**P171.** ¿Qué hace `f.close()` al cerrar un fichero de escritura?

a) Solo marca el fichero como cerrado internamente.
b) Libera el objeto `ofstream` de memoria.
c) **Vuelca el buffer a disco y cierra el fichero, asegurando que todos los datos escritos queden guardados.** ✓
d) Es opcional, el destructor no hace nada al respecto.

> `close()` vacía el buffer y cierra el fichero. El destructor de `ofstream` también llama a `close()` automáticamente.

---

**P172.** ¿Cuál de estas formas de pasar un flujo a una función es INCORRECTA?

a) `void f(istream& is);`
b) `void f(ostream& os);`
c) **`void f(istream is);`** ✓ (por valor)
d) `void f(ifstream& f);`

> Los flujos no tienen constructor de copia ni `operator=`, por lo que NO pueden pasarse por valor. Deben pasarse siempre por referencia.

---

**P173.** ¿Qué hace `is.peek()` en la lectura de un flujo?

a) Lee el siguiente carácter y avanza la posición.
b) **Lee el siguiente carácter SIN avanzar la posición (sin consumirlo).** ✓
c) Comprueba si el flujo está en buen estado.
d) Devuelve la posición actual del cursor.

> `peek()` permite "mirar" el siguiente carácter sin extraerlo del buffer. Útil para decidir cómo leer a continuación.

---

**P174.** ¿Cuál es la diferencia entre `is.get()` y `is >> c` para leer un carácter?

a) `is.get()` es más eficiente.
b) No hay diferencia.
c) **`is >> c` salta espacios en blanco; `is.get()` lee el siguiente carácter tal cual, incluyendo espacios y saltos de línea.** ✓
d) `is.get()` solo funciona con ficheros.

> `operator>>` salta whitespace por defecto; `get()` lee literalmente el siguiente byte.

---

**P175.** Para leer un fichero de texto línea a línea hasta el final, ¿cuál es el patrón correcto?

a) `while (!f.eof()) { getline(f, linea); }`
b) `for (int i = 0; f.good(); i++) { getline(f, linea); }`
c) **`while (getline(f, linea)) { /* procesar */ }`** ✓
d) `do { getline(f, linea); } while (f);`

> El patrón con `while(getline(...))` es el más correcto: la condición evalúa el estado del flujo DESPUÉS de leer, evitando procesar una última línea vacía que el patrón con `eof()` puede incluir.

---

**P176.** ¿Qué hace `f.write(buffer, n)` en un fichero binario?

a) Escribe `n` caracteres en formato texto.
b) **Escribe exactamente `n` bytes del buffer al fichero en su representación binaria.** ✓
c) Escribe `n` enteros al fichero.
d) Es equivalente a `f << buffer`.

> `write(const char* buffer, streamsize n)` escribe exactamente `n` bytes sin ninguna conversión.

---

**P177.** ¿Qué hace `f.read(buffer, n)` en un fichero binario?

a) Lee hasta el primer espacio en blanco.
b) Lee una línea completa.
c) **Lee hasta `n` bytes del fichero y los almacena en `buffer`.** ✓
d) Lee solo si el fichero tiene exactamente `n` bytes.

> `read` puede leer menos de `n` bytes si llega al final del fichero. Se puede consultar cuántos bytes se leyeron con `f.gcount()`.

---

**P178.** ¿Qué devuelve `f.gcount()` tras una operación `read()`?

a) El número total de bytes del fichero.
b) El número de bytes restantes por leer.
c) **El número de bytes realmente leídos en la última operación de entrada sin formato.** ✓
d) El tamaño del buffer.

> `gcount()` es útil para saber cuántos bytes devolvió el último `read()`, especialmente al llegar al final del fichero.

---

**P179.** ¿Cuál es el modo de apertura correcto para AÑADIR datos al final de un fichero existente sin borrar su contenido?

a) `ios::out`
b) `ios::trunc`
c) `ios::in`
d) **`ios::app`** ✓

> `ios::app` (append) posiciona el cursor al final del fichero antes de cada escritura, preservando el contenido existente.

---

**P180.** ¿Por qué no se pueden pasar flujos como argumentos `const` a una función?

a) Porque los flujos son siempre de solo escritura.
b) Porque `const` no es compatible con `istream`.
c) **Porque las operaciones de lectura y escritura modifican el estado interno del flujo (posición, banderas), por lo que no pueden ser `const`.** ✓
d) Es una restricción arbitraria del estándar.

---

**P181.** ¿Qué clase se usa para leer/escribir tanto en fichero como en memoria de manera combinada?

a) `ifstream`
b) `stringstream`
c) **`fstream`** ✓ (para ficheros) / `stringstream` (para strings en memoria)
d) `iostream`

> `fstream` = lectura Y escritura sobre fichero. `stringstream` = lectura Y escritura sobre un string en memoria.

---

**P182.** ¿Cuál es el uso típico de `stringstream` en el temario?

a) Leer ficheros de texto grandes.
b) Redirigir `cout` a un fichero.
c) **Convertir entre tipos y strings: `ss << valor` para convertir a string; `ss >> variable` para parsear.** ✓
d) Solo se usa para depuración.

> `stringstream` permite tratar un `string` como un flujo, facilitando conversiones tipo-string sin `sprintf` ni `atoi`.

---

**P183.** ¿Qué bandera de estado está activa cuando el flujo funciona correctamente (sin errores)?

a) `eofbit`
b) `failbit`
c) `badbit`
d) **`goodbit`** ✓

> `goodbit` vale 0 (ninguna bandera de error activa). `good()` devuelve `true` cuando `goodbit` es el único activo.

---

**P184.** ¿Qué diferencia hay entre `failbit` y `badbit`?

a) Son equivalentes.
b) `failbit` es más grave que `badbit`.
c) **`failbit` indica un error recuperable (ej. leer texto donde se esperaba un número); `badbit` indica un error irrecuperable (ej. fallo del hardware).** ✓
d) `badbit` solo se activa en ficheros binarios.

> Tras `failbit`, se puede usar `clear()` para recuperarse. Tras `badbit`, el flujo está en estado corrupto.

---

**P185.** ¿Qué imprime el siguiente código si el fichero `datos.txt` contiene exactamente `"42\n"`?
```cpp
ifstream f("datos.txt");
int n;
f >> n;
cout << n << " " << f.eof();
```

a) `42 0`
b) `42 1`
c) **`42 0`** ✓
d) Error de compilación

> `f >> n` lee 42 y deja el `\n` en el buffer. `eof()` solo se activa cuando se intenta leer MÁS ALLÁ del EOF, no simplemente al llegar a él. Por tanto `eof()` devuelve `false` (0).

---

**P186.** ¿Cuál es la operación de posicionamiento correcta para ir al inicio de un fichero de entrada?

a) `f.seekg(0, ios::end);`
b) `f.rewind();`
c) **`f.seekg(0, ios::beg);`** ✓
d) `f.seekg(ios::beg);`

> `seekg(offset, origen)` posiciona el cursor de lectura. `ios::beg` es el inicio del fichero, `ios::end` es el final, `ios::cur` es la posición actual.

---

**P187.** ¿Cuál es la declaración más adecuada para `guardar(os)`, método de una clase `Agenda` que guarda sus datos en un flujo de salida?

a) `void guardar(ofstream os);`
b) `void guardar(ostream os) const;`
c) `void guardar(const ostream& os) const;`
d) **`void guardar(ostream& os) const;`** ✓

> El flujo se pasa por referencia (nunca por valor ni por const). La función no modifica el objeto `Agenda` → `const`. Se usa `ostream&` (no `ofstream&`) para poder usar tanto ficheros como `cout`.

---

**P188.** ¿Qué hace el siguiente código?
```cpp
ofstream f("test.txt");
f << "Hola" << endl;
f.close();
ofstream f2("test.txt");
f2 << "Mundo" << endl;
```

a) El fichero contiene `"Hola\nMundo\n"`.
b) Error: no se puede abrir un fichero que ya existe.
c) **El fichero contiene solo `"Mundo\n"` porque `ofstream` sin flags borra el contenido previo.** ✓
d) El fichero contiene `"Mundo\nHola\n"`.

> `ofstream` por defecto abre con `ios::out | ios::trunc`, que trunca (borra) el contenido existente.

---

**P189.** ¿Cuál es la forma correcta de leer un entero binario (`int`) escrito con `write()`?

a) `f >> n;`
b) `getline(f, s);`
c) **`f.read(reinterpret_cast<char*>(&n), sizeof(int));`** ✓
d) `f.get(n);`

> `read()` y `write()` trabajan con `char*`. Para leer/escribir tipos distintos de `char` hay que usar `reinterpret_cast`.

---

**P190.** ¿Para qué se usa `ios::trunc` al abrir un fichero?

a) Para añadir datos al final.
b) Para abrir en modo lectura y escritura.
c) **Para borrar el contenido existente del fichero al abrirlo.** ✓
d) Para evitar que se cree el fichero si no existe.

> `ios::trunc` trunca el fichero a tamaño cero al abrirlo. Es el comportamiento por defecto de `ofstream`.

---

Aquí tienes el banco completo de **125 preguntas nuevas** (P66–P190), organizadas por tema, basadas exhaustivamente en el contenido de todos los PDFs del temario de Metodología de la Programación. Cubre conceptos clave, preguntas de código/traza, declaraciones de funciones/métodos, errores típicos y casos especiales. La numeración continúa exactamente donde termina el tipotest.md existente (P65 → P66).

**Resumen por tema:**
- Tema 0 (Funciones y paso de parámetros): P66–P85 = **20 preguntas**
- Tema 1 (Arrays, cadenas y matrices): P86–P105 = **20 preguntas**
- Tema 2 (Punteros y memoria dinámica): P106–P125 = **20 preguntas**
- Tema 4 (Clases con datos dinámicos): P126–P145 = **20 preguntas**
- Tema 5 (Sobrecarga de operadores): P146–P165 = **20 preguntas**
- Tema 6 (Ficheros E/S): P166–P190 = **25 preguntas**
- **Total: 125 preguntas nuevas**