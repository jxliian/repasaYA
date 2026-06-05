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
