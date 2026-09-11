# Lecciones medidas

Lo que se aprendió produciendo ocho piezas contra 22 referencias reales
— 22 piezas de motion graphics de referencia, recolectadas aparte; el repo no las incluye, midiendo cada afirmación en vez de estimarla.
**Cuando algo de acá contradiga al resto del skill, gana esto: está medido.**

---

## 1 · El motor captura por seek, y eso rompe cosas que parecen obvias

### `immediateRender` muerde en las dos direcciones
| | Qué muestra el elemento ANTES de que arranque su tween |
| --- | --- |
| `from()` / `fromTo()` con el default (`true`) | su estado **inicial**, desde el cuadro 0 |
| `fromTo(..., {immediateRender:false})` | su estado **FINAL**, desde el cuadro 0 |

Con `immediateRender:false` el elemento **tiene que nacer invisible** (`opacity:0`
en el CSS o en el `gsap.set` de carga). No es algo para recordar en cada tween:
va una vez a la hoja de estilos.

*Costó tres apariciones del mismo bug: tarjetas ya puestas en el cuadro 0, un
puntero visible desde el principio, un botón que se veía antes de existir.*

### Un fundido que termina en el límite de un clip necesita un `tl.set` duro
El lint lo llama `gsap_exit_missing_hard_kill`. Al saltar de cuadro, el motor
puede caer después del fundido y dejar visibilidad obsoleta.

### No hay obturador: **todo el motion blur es autoreado**
No existe estela natural. Regla: *lo que se mueve rápido se desenfoca en la
dirección en que se mueve, y recupera el foco al frenar.* A 60 fps no es opcional.

### Dos tweens sobre la misma propiedad: el que termina después gana
Cuando algo "no obedece", **buscar el otro tween que lo está pisando** antes de
tocar el valor. El lint avisa (`overlapping_gsap_tweens`) y hay que hacerle caso.

---

## 2 · La cámara

**Medido sobre la referencia albus**, cuánto del ancho del cuadro ocupa el objeto:

| tiempo | ancho |
| --- | --- |
| 0.0 s | **13 %** |
| 1.3 s | 40 % |
| 2.3 s | 62 % |
| 3.8 s | **88 %** |

**Es un travelling de 6.8× y ocupa el acto entero.** Un empuje de `1.0 → 1.15`
no es una cámara: es una imagen fija. Y el crecimiento va **cargado adelante**
(`power1.out`), no lineal.

🔑 **El error de fondo es construir el objeto a escala web.** Con una cápsula de
760 px en un cuadro de 1920, por más que se empuje nunca llena el cuadro. Se
construye el objeto **grande** (1560 px) y se lo arranca al 13 % de escala.

### Umbral de percepción
Una cámara necesita **≥1 px de desplazamiento aparente por cuadro** para que el
ojo la registre, y 2-3 px para que se sienta viva. Un giro de 12° en 5 s son
0.04° por cuadro: invisible.

### Y no alcanza con moverse: hace falta TEXTURA contra la cual verlo
Un degradado radial desplazado se ve idéntico a sí mismo. La solución es la del
cine: **grano**. Una capa de `feTurbulence` a pantalla completa, corrida ~1.4 px
por cuadro, cambia todos los píxeles del cuadro. Hace tres cosas a la vez:
da referencia visual al movimiento, **rompe el banding de H.264** en degradados
oscuros, y los negros dejan de parecer un vacío digital.

🚨 **`mix-blend-mode: overlay` sobre negro devuelve negro.** Sobre fondo oscuro va
`screen` (aditivo); sobre fondo claro va `multiply`. Con el modo equivocado el
grano está puesto y es literalmente invisible — el archivo pesa lo mismo.

---

## 3 · La luz define el objeto, no el relleno

En un cuadro oscuro **el objeto lo define su borde**. La receta medida contra la
referencia:
- contorno **continuo** de 5-7 px casi blanco
- **tres** `drop-shadow` encadenados (14 px, 44 px, 96 px) — una sola sombra da un
  borde prolijo; tres dan un objeto que emite luz
- un halo grande y desenfocado detrás: es lo que lo despega del negro
- un **segundo anillo concéntrico** exterior, más tenue
- interior **más oscuro** que el borde: el filo tiene que ganarle al relleno

**Un objeto fino no se agranda: se agranda su LUZ.** Un halo de 1720×960 hace que
un cuadro deje de leer como vacío sin tocar el objeto.

### El bokeh son círculos, no un lavado
Discos desenfocados a ~20 % de opacidad, cada uno moviéndose a su ritmo. Un
degradado radial difuso no da profundidad de campo: da niebla.

### En registro claro, el BLANCO es el material principal
El color es un acento que se insinúa en un borde. Cuatro manchas saturadas
cubriendo el cuadro no son un registro claro: son un papel de caramelo.

---

## 4 · Medir texto: la trampa más cara

🚨 **Ninguna medición de texto es válida antes de `document.fonts.ready`.**
Al ejecutarse el script la fuente embebida todavía no cargó, así que
`offsetWidth` devuelve el ancho de la **tipografía de respaldo**. Medido: **23 %
menos** del ancho real. Una caja calculada con ese número recorta la frase **para
siempre**, por más que la timeline esté perfecta.

**La solución no es un factor de corrección: es no medir.**
- recorte de tipeo → `clip-path: inset(… X% …)` animado de 100 % a 0 %
- recentrado → `xPercent` de 0 a −50 (porcentaje del propio ancho)
- cursor → un **riel** del ancho del texto que se traslada `xPercent` 0→100:
  llega exacto al final de la frase sin saber cuánto mide

Lo que sí necesita medir (titulares estáticos) se encaja en
`document.fonts.ready` — toca `font-size`, nunca la timeline:

```js
function encajar(sel, caja) {
  document.querySelectorAll(sel).forEach(el => {
    let px = parseFloat(getComputedStyle(el).fontSize);
    const piso = px * 0.45;          // fusible: si hay que bajar más, el
    while (el.scrollWidth > caja && px > piso) {   // problema es la medición
      px -= 1; el.style.fontSize = px + 'px';
    }
  });
}
encajar('.titular', CAJA);
if (document.fonts) document.fonts.ready.then(() => encajar('.titular', CAJA));
```

⚠️ **`scrollWidth` sobre un bloque de ancho 100 % mide el BLOQUE, no el texto.**
El texto a medir va en un `inline-block`. Sin eso el encaje achica la tipografía
hasta el mínimo y el titular sale del tamaño de una nota al pie.

⚠️ **Si el texto se escala después de encajarlo, la caja debe descontar esa
escala** (`CAJA / 1.07` para una deriva de 1.07).

### Y un límite del propio motor
**Solo hay 18 tipografías embebidas**, y el propio skill prohíbe la mayoría.
Las usables sin traer archivos: **Montserrat · Oswald · League Gothic ·
Archivo Black · Space Mono · IBM Plex Mono · JetBrains Mono · Source Code Pro**.
Cualquier otra necesita un `@font-face` real con su `.woff2` — y las reglas hay
que **pegarlas inline**: un `@import` a un `.css` externo el compilador no lo ve.
`scripts/lab/getfont.mjs` baja cualquier Google Font y arma el bloque.

### Logos de marca reales
`scripts/lab/logos.mjs` los baja del CDN de **Simple Icons**
(`cdn.simpleicons.org/<slug>`), sin API key y con el **color oficial de cada
marca**. Se bajan al proyecto en vez de enlazarlos: el motor renderiza sin red
garantizada y una composición tiene que ser reproducible offline.

⚠️ **No todas las marcas están.** Adobe, Canva, Slack y OpenAI devuelven **404**:
pidieron que no se use su logo. La herramienta lo reporta en vez de tragárselo.

🔑 **El logo va sobre una pastilla blanca, y eso no es decoración.** Notion,
Vercel, GitHub y OBS son casi negros: sobre fondo oscuro desaparecen.

---

## 5 · Composición del texto

> **El texto casi nunca es lo más grande del cuadro. El OBJETO lo es.**
> El texto es una etiqueta que nombra lo que estás viendo.

Siete layouts leídos de las referencias:

| # | Layout | Cuándo |
| --- | --- | --- |
| 1 | etiqueta chica arriba, objeto abajo | el objeto es el argumento — el más común |
| 2 | titular anclado a un margen, sangrando | frases largas |
| 3 | cuadro partido: objeto de un lado, texto del otro | comparaciones |
| 4 | texto tapado por el objeto | da profundidad y cuesta cero |
| 5 | una palabra enorme cortada por el borde | remates |
| 6 | una forma parte el cuadro; el texto vive en una mitad | cambios de sección |
| 7 | **centrado y SOLO** | placas de título puras, sin nada más en el cuadro |

🚨 **El 7 es el único que permite centrar, y exige que no haya nada más.**
Texto centrado con un objeto detrás no está en la lista porque **ninguna
referencia lo usa**.

🚨 **Y no alcanza con "no centrar":** si todos los bloques comparten el mismo
anclaje —todos a la izquierda— es la misma plantilla en otro eje. Lo que se varía
es el anclaje **entre bloques y entre actos**.

**Márgenes:** 58 px en 1080 no es un margen, es estar contra la pared (5 %).
Piso **122 px** (11 %). Sangrar el objeto sí; **cortar una palabra a la mitad, no**
— eso lee a desborde, no a recorte.

**El color vive en los objetos, no en las letras.** Texto blanco sobre oscuro o
negro sobre claro. Si el texto compite en color con el objeto, hay dos cosas
peleando por el mismo trabajo.

**Jerarquía adentro del bloque:** una palabra manda, notoriamente más grande y en
el peso más pesado; las secundarias finas y **en gris**, nunca en un color de acento.
Un salto de cuerpo de 2.7× es lo que lo hace leer como jerarquía y no como lista.

---

## 6 · Ritmo

- **Variación de plano (máx ÷ mediana) ≈ 3×.** El ritmo parejo es la causa
  medida de que una pieza salga lenta. El hook corta rápido, la prueba respira,
  el remate vuelve a cortar.
- **`expo.out` sobre duraciones largas es una trampa:** recorre el 80 % de la
  distancia en el primer 20 % del tiempo y después se arrastra. Para llegadas
  fluidas, **`power2.out` sobre 0.7-0.8 s**.
- **Equivalencias de curva** (los tutoriales usan nombres de Qt; GSAP numera
  distinto y es un error fácil):

| Tutorial / Qt | GSAP |
| --- | --- |
| cubic out · `OutCubic` | **`power2.out`** (no `power3`) |
| quad ease · `InOutQuad` | `power1.inOut` |
| circ ease · `InOutCirc` | `circ.inOut` |
| `OutExpo` — para **un número que aparece** | `expo.out` |

- **El corte cae en el ARRANQUE de un gesto, no en el medio.** Medido sobre 109
  cortes: movimiento antes del corte 0.84 (bajo el azar), después 1.55. Para un
  impacto, el corte va **justo antes**, para que caiga entero en el plano nuevo.
- **Punch-in:** 10 fotogramas a 30 fps = **0.333 s**. El zoom no es el plano: es
  el acento adentro del plano.
- **Pre-lap:** el acto siguiente empieza a entrar antes de que el anterior
  termine. Es el J-cut hecho imagen, y es lo que hace que los actos dejen de
  leerse como piezas pegadas.

### Tiempo de lectura
**17 caracteres por segundo, contados DESPUÉS de que el texto está completo.**
23 caracteres necesitan 1.35 s de permanencia.

⚠️ Y dar tiempo de lectura **sube los cuadros muertos**: un texto que se queda es
un cuadro que no cambia. La salida no es acortar el hold sino **sostenerlo con la
cámara** — el texto sigue acercándose mientras se lee.

---

## 7 · Audio

- **El sonido va en el PICO de la animación, no en el corte.** Y el pico no está
  al principio del archivo: el whoosh mediano de biblioteca lo tiene a 200 ms del
  inicio, así que hay que adelantar el arranque por ese offset. Sintetizar los
  sonidos resuelve el problema de raíz: el pico queda donde uno lo pone
  (`scripts/lab/sfx.sh`).
- **Dos o tres golpes en toda la pieza, nunca uno por corte.**
- **J-cut: 2.00 s de adelanto.** El sonido del acto siguiente entra dos segundos
  antes que su imagen.
- **El limitador no existe dentro de HyperFrames:** va en un pase de masterizado
  que **copia el video** (`-c:v copy`) y sólo re-encodea el audio.
- **−14 LUFS es para contenido denso.** Una pieza con tres acentos sobre silencio
  necesita **−16**, o el normalizador comprime tanto que los golpes se comen todo.
- 🚨 **`loudnorm` controla el pico de MUESTRA; el encoder AAC reconstruye picos
  ENTRE muestras y se pasa** (~1.6 dB, y depende del contenido). Hace falta un
  `alimiter` después, **verificando** el resultado: `scripts/lab/master.sh` baja el
  límite solo hasta cumplir.

---

## 8 · Método

### Medir la fluidez, no opinarla
`scripts/lab/fluidez.sh` compara cada cuadro con el anterior y dibuja el perfil.
**Objetivo: menos del 10 % de cuadros quietos.** El movimiento medio hay que
leerlo contra la familia de la pieza — una pieza minimalista sobre negro nunca va
a marcar como una pila de paneles iluminados. Calibración: las referencias del
board miden **3.06 de mediana**; las dos minimalistas miden 0.16 y 0.17.

### Mirar a resolución completa, no en miniaturas
La hoja de contactos sirve para el arco. Los defectos —un elemento fantasma, un
recorte, un choque— sólo aparecen en un cuadro a resolución completa.

### ⭐ El A/B pareado por timestamp
Extraer **el mismo instante** de la referencia y de la propia pieza y apilarlos.
Es lo que más rápido delata una copia: encuentra en un minuto diferencias de
escala, de luz y de tiempo que una hoja suelta no muestra nunca.

### Copiar antes que inventar
Copiar una referencia 1:1 enseña más rápido que diseñar de cero, porque obliga a
notar decisiones que uno nunca se habría animado a tomar — un travelling de 6.8×,
un borde de 7 px, un color que sube hasta invertir el texto.

---

## 9 · Errores propios que cuestan renders

- **`open(p,'w')` trunca antes de escribir.** Una escritura que falla deja el
  archivo vacío. Escribir a `.tmp` y `os.replace()`.
- **Nunca silenciar `stderr` en una herramienta.** Un `2>/dev/null` hizo que
  `master.sh` escribiera un archivo de 0 bytes sin avisar.
- **zsh se come `:l` después de una variable** (`$LIM:level` → `0.9evel`): es su
  modificador de minúsculas. Usar `${LIM}:level`.
- **Verificar que el elemento existe** (`grep -c`) antes de culpar a la animación.
  Un `<div>` que nunca se insertó se ve exactamente igual que un tween roto.
- **Borrar un elemento sin borrar su JS mata la timeline entera.** Síntoma:
  archivo minúsculo, render lentísimo, todos los cuadros idénticos.
