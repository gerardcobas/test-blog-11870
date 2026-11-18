"""Builds a static test blog for Marfeel site 11870 (whisky + metalcore)."""
import html
import json
import os
import sys
import urllib.request

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://gerardcobas.github.io/test-blog-11870/"
SITE = "Malta & Breakdown"
ACCOUNT_ID = 11870

SDK = """<script type="text/javascript">
!function(){"use strict";function e(e){var t=!(arguments.length>1&&void 0!==arguments[1])||arguments[1],c=document.createElement("script");c.src=e,t?c.type="module":(c.async=!0,c.type="text/javascript",c.setAttribute("nomodule",""));var n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(c,n)}!function(t,c){!function(t,c,n){var a,o,r;n.accountId=c,null!==(a=t.marfeel)&&void 0!==a||(t.marfeel={}),null!==(o=(r=t.marfeel).cmd)&&void 0!==o||(r.cmd=[]),t.marfeel.config=n;var i="https://sdk.mrf.io/statics";e("".concat(i,"/marfeel-sdk.js?id=").concat(c),!0),e("".concat(i,"/marfeel-sdk.es5.js?id=").concat(c),!1)}(t,c,arguments.length>2&&void 0!==arguments[2]?arguments[2]:{})}(window,%d,{ useLocalstorageForUserVars: true, identity: { active: true } } /* Config */)}();
</script>""" % ACCOUNT_ID

ARTICLES = [
    {
        "slug": "islay-la-isla-donde-el-whisky-sabe-a-turba",
        "section": "Whisky",
        "date": "2026-11-10T09:30:00+01:00",
        "keywords": "islay,scotland,coast",
        "title": "Islay, la isla donde el whisky sabe a turba",
        "excerpt": "Una isla de las Hébridas Interiores concentra algunas de las destilerías más reconocibles del mundo por su perfil ahumado.",
        "body": [
            "Islay es una pequeña isla de las Hébridas Interiores, en la costa oeste de Escocia, con poco más de tres mil habitantes. Aun así, su nombre aparece en las etiquetas de algunos de los whiskies más reconocibles del planeta: Laphroaig, Lagavulin, Ardbeg, Bowmore, Bruichladdich o Kilchoman, entre otras.",
            "El rasgo que las une es la turba. Durante el malteado, la cebada se seca con el humo de este combustible vegetal, muy abundante en la isla, y ese humo deja compuestos fenólicos que se trasladan al destilado. El resultado son whiskies con notas de hoguera, yodo, alquitrán o salitre que dividen a los aficionados: o se adoran o se evitan.",
            "La intensidad del ahumado se mide en partes por millón de fenoles en la malta. No todas las destilerías de la isla trabajan igual: algunas apuestan por niveles muy altos y otras elaboran también versiones sin turba, lo que demuestra que el carácter de Islay no depende solo del humo, sino también del clima marítimo en el que envejecen las barricas.",
            "Para quien quiera iniciarse, la recomendación habitual es empezar por un ahumado moderado y avanzar poco a poco. Añadir unas gotas de agua ayuda a abrir los aromas y a distinguir la fruta y la vainilla que se esconden detrás del humo.",
        ],
    },
    {
        "slug": "bourbon-y-scotch-en-que-se-diferencian",
        "section": "Whisky",
        "date": "2026-11-11T11:00:00+01:00",
        "keywords": "bourbon,whiskey,barrel",
        "title": "Bourbon y scotch: en qué se diferencian realmente",
        "excerpt": "El origen, el cereal y la barrica marcan la frontera entre los dos estilos más populares de whisky.",
        "body": [
            "Bourbon y scotch comparten la palabra whisky, pero las normas que los regulan son muy distintas. La primera diferencia es geográfica: el scotch solo puede elaborarse y envejecerse en Escocia, mientras que el bourbon es un producto de Estados Unidos, aunque no tiene por qué proceder de Kentucky.",
            "El cereal también cambia. El bourbon debe partir de un mosto con al menos un 51 % de maíz, lo que le da un perfil más dulce, con notas de caramelo y vainilla. El scotch de malta se elabora únicamente con cebada malteada, y los blends combinan whisky de malta con whisky de grano.",
            "La madera es la tercera gran frontera. El bourbon tiene que envejecer en barricas nuevas de roble carbonizado, que aportan mucho color y sabor en pocos años. El scotch, en cambio, envejece un mínimo de tres años y suele reutilizar barricas que antes contuvieron bourbon, jerez u otros vinos, por lo que la influencia de la madera es más sutil y variada.",
            "Ninguno es mejor que el otro. El bourbon suele resultar más accesible para quien empieza, mientras que el scotch ofrece una paleta más amplia de estilos, desde los whiskies florales de las Lowlands hasta los ahumados de Islay.",
        ],
    },
    {
        "slug": "como-catar-whisky-en-casa",
        "section": "Whisky",
        "date": "2026-11-13T18:15:00+01:00",
        "keywords": "whisky,glass,tasting",
        "title": "Cómo catar whisky en casa sin equipo profesional",
        "excerpt": "Un vaso adecuado, unas gotas de agua y algo de paciencia bastan para sacar mucho más partido a cualquier botella.",
        "body": [
            "Catar whisky no requiere un laboratorio. Lo más importante es el vaso: uno con forma de tulipán, como el Glencairn o una simple copa de vino blanco, concentra los aromas en la parte superior y facilita apreciarlos.",
            "El primer paso es observar el color, que da pistas sobre la barrica, aunque algunos whiskies llevan colorante. Después llega la nariz: conviene acercar la copa con la boca entreabierta y sin inspirar con fuerza, porque el alcohol puede saturar el olfato.",
            "En boca, el primer sorbo sirve para acostumbrar el paladar. A partir del segundo se distinguen mejor el dulzor, la fruta, las especias o el humo. Finalmente, el final o retrogusto indica cuánto permanecen esos sabores después de tragar.",
            "Unas gotas de agua a temperatura ambiente cambian mucho la experiencia, sobre todo en whiskies de alta graduación. El hielo, en cambio, adormece los aromas, así que es mejor reservarlo para cuando el objetivo sea refrescarse y no analizar.",
            "Tomar notas, aunque sean breves, ayuda a comparar botellas con el tiempo y a descubrir qué estilos encajan con cada uno.",
        ],
    },
    {
        "slug": "el-auge-del-whisky-japones",
        "section": "Whisky",
        "date": "2026-11-15T10:45:00+01:00",
        "keywords": "japan,whisky,distillery",
        "title": "El auge del whisky japonés, de imitador a referente",
        "excerpt": "Japón aprendió el oficio en Escocia hace un siglo y hoy sus botellas compiten con las mejores del mundo.",
        "body": [
            "La historia del whisky japonés arranca en los años veinte del siglo pasado, cuando Masataka Taketsuru viajó a Escocia para estudiar química y aprender a destilar. A su regreso participó en la puesta en marcha de Yamazaki, la primera destilería comercial del país, y más tarde fundó Nikka.",
            "Durante décadas, el whisky japonés siguió de cerca el modelo escocés, pero con matices propios: una obsesión por el equilibrio, el uso de barricas de roble japonés mizunara y una gran variedad de alambiques dentro de una misma destilería, lo que permite elaborar muchos estilos sin intercambiar whisky con otras casas.",
            "El reconocimiento internacional llegó a principios de este siglo con premios en certámenes especializados. La demanda creció tanto que muchas referencias con indicación de edad desaparecieron temporalmente de las tiendas por falta de existencias envejecidas.",
            "El éxito también trajo polémica, porque algunas marcas embotellaban en Japón whisky importado. Para ordenar el sector, los productores japoneses aprobaron en 2021 unas normas de etiquetado que definen qué puede llamarse whisky japonés.",
        ],
    },
    {
        "slug": "metalcore-cuando-el-hardcore-y-el-metal-se-encontraron",
        "section": "Metalcore",
        "date": "2026-11-09T20:00:00+01:00",
        "keywords": "metal,concert,guitar",
        "title": "Metalcore: cuando el hardcore y el metal se encontraron",
        "excerpt": "Nació en los noventa en la escena hardcore estadounidense y hoy llena festivales de todo el mundo.",
        "body": [
            "El metalcore surgió en los años noventa en Estados Unidos, cuando bandas de la escena hardcore empezaron a incorporar riffs y afinaciones propios del metal. Grupos como Earth Crisis, Integrity o Converge sentaron las bases de un sonido agresivo, con mensajes muy ligados a la ética de esa escena.",
            "A principios de los dos mil llegó la oleada que lo llevó al gran público. Killswitch Engage, Shadows Fall, Unearth o As I Lay Dying mezclaron las guitarras melódicas del death metal sueco con los breakdowns del hardcore y estribillos con voces limpias, una fórmula que se convirtió en la seña de identidad del género.",
            "En la década siguiente, bandas británicas y australianas como Architects, Bring Me the Horizon o Parkway Drive ampliaron sus límites con producción más pulida, electrónica y estructuras cercanas al rock alternativo.",
            "Hoy el metalcore convive con el deathcore, el post-hardcore y el nu metal en los carteles de los grandes festivales, y sigue atrayendo a un público joven que descubre el género a través de plataformas de streaming y redes sociales.",
        ],
    },
    {
        "slug": "anatomia-de-un-breakdown",
        "section": "Metalcore",
        "date": "2026-11-12T19:30:00+01:00",
        "keywords": "drums,metal,stage",
        "title": "Anatomía de un breakdown: por qué hace temblar la sala",
        "excerpt": "Ralentizar el tempo, golpear cuerdas al aire y sincronizar bombo y guitarra: así se construye el momento más esperado del concierto.",
        "body": [
            "El breakdown es el pasaje en el que la canción parece frenar de golpe. El tempo se reduce o se percibe a la mitad, la guitarra repite golpes secos sobre las cuerdas más graves y la batería sincroniza el bombo con cada uno de ellos. El efecto es físico: el público lo siente en el pecho antes que en los oídos.",
            "Para conseguir esa contundencia, muchas bandas usan afinaciones muy bajas, como drop C o incluso más graves, y guitarras de siete u ocho cuerdas. El silencio entre golpes es tan importante como las notas, porque crea la tensión que luego estalla.",
            "El breakdown suele anunciarse. Un cambio de ritmo, un grito del vocalista o un breve silencio avisan al público de que llega el momento de abrir el pit. Por eso es habitual ver cómo el centro de la sala se vacía unos segundos antes.",
            "Aunque nació en el hardcore, el recurso se ha extendido a otros estilos y se ha vuelto más elaborado, con cambios de compás y efectos electrónicos. Bien usado, sigue siendo el clímax de cualquier canción del género.",
        ],
    },
    {
        "slug": "voces-limpias-y-guturales-en-el-metalcore",
        "section": "Metalcore",
        "date": "2026-11-14T21:00:00+01:00",
        "keywords": "singer,microphone,concert",
        "title": "Voces limpias y guturales, el diálogo que define el metalcore",
        "excerpt": "La alternancia entre el grito y la melodía es una de las claves del género y también una de las más difíciles de ejecutar.",
        "body": [
            "Pocas cosas identifican tanto al metalcore como el contraste entre estrofas gritadas y estribillos cantados. Esa alternancia permite que una misma canción combine agresividad y melodía, y explica buena parte del éxito del género fuera de la escena más extrema.",
            "Las voces guturales no consisten en gritar sin más. Los cantantes que mantienen giras largas trabajan técnicas de distorsión que reparten el esfuerzo entre el diafragma y las falsas cuerdas vocales, y muchos reciben clases para evitar lesiones.",
            "En algunas bandas un mismo vocalista se encarga de los dos registros, y en otras se reparten entre el cantante principal y un guitarrista o bajista. Ambas opciones tienen ventajas: la primera da coherencia al directo, la segunda permite más capas en el estudio.",
            "En los últimos años la frontera se ha difuminado. Hay grupos que apenas usan voces limpias y otros que se acercan al pop en los estribillos, pero el diálogo entre ambos registros sigue siendo el centro del género.",
        ],
    },
    {
        "slug": "guia-para-tu-primer-concierto-de-metalcore",
        "section": "Metalcore",
        "date": "2026-11-16T17:00:00+01:00",
        "keywords": "festival,crowd,concert",
        "title": "Guía de supervivencia para tu primer concierto de metalcore",
        "excerpt": "Tapones, agua y algunas normas no escritas del pit para disfrutar del directo sin sustos.",
        "body": [
            "Un concierto de metalcore puede impresionar la primera vez. El volumen es alto, el público se mueve mucho y algunas dinámicas, como el circle pit o el wall of death, pueden parecer caóticas a quien no las conoce. Con un poco de preparación, la experiencia es mucho mejor.",
            "Los tapones para los oídos son imprescindibles. Los de espuma sirven, pero los de filtro reducen el volumen sin apagar la música y se pueden reutilizar. También conviene hidratarse bien y llevar calzado cerrado y cómodo.",
            "El pit tiene sus propias normas. Si alguien cae al suelo, se le levanta de inmediato. Si no quieres participar, basta con colocarte en los laterales o cerca de la barra, donde el movimiento es menor. Y el crowdsurfing se hace con cuidado, sin patadas y respetando a quien está debajo.",
            "Por último, llega con tiempo para ver a los teloneros. Muchas de las bandas que hoy encabezan carteles empezaron abriendo conciertos ante salas medio vacías.",
        ],
    },
]

CSS = """
:root{--bg:#f7f5f0;--fg:#1d1b18;--muted:#6b665d;--accent:#9a3b12;--card:#fff;--line:#e4dfd5}
@media (prefers-color-scheme:dark){:root{--bg:#141311;--fg:#ece8e1;--muted:#a39d92;--accent:#e07a45;--card:#1d1c19;--line:#2e2c28}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:18px/1.6 Georgia,"Times New Roman",serif}
a{color:inherit}
header.site{border-bottom:1px solid var(--line);padding:18px 16px;text-align:center}
header.site a{text-decoration:none;font:700 28px/1.1 system-ui,-apple-system,sans-serif;letter-spacing:-.02em}
header.site p{margin:4px 0 0;color:var(--muted);font:14px system-ui,sans-serif}
main{max-width:760px;margin:0 auto;padding:24px 16px 64px}
.layout{max-width:1120px;margin:0 auto;padding:24px 16px 64px;display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:48px;align-items:start}
.layout main{max-width:none;margin:0;padding:0}
.sidebar{position:sticky;top:24px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:24px;max-width:1080px;margin:0 auto;padding:24px 16px 64px}
.card{background:var(--card);border:1px solid var(--line);border-radius:8px;overflow:hidden;text-decoration:none;display:block}
.card img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block}
.card div{padding:14px 16px 18px}
.card h2{font:700 20px/1.25 system-ui,sans-serif;margin:6px 0}
.card p{margin:0;color:var(--muted);font-size:16px}
.section{font:600 12px system-ui,sans-serif;text-transform:uppercase;letter-spacing:.08em;color:var(--accent)}
article h1{font:800 36px/1.15 system-ui,sans-serif;letter-spacing:-.02em;margin:8px 0 12px}
.meta{color:var(--muted);font:14px system-ui,sans-serif;margin-bottom:20px}
article figure{margin:0 0 24px}
article figure img{width:100%;border-radius:6px;display:block}\narticle figcaption{color:var(--muted);font:12px system-ui,sans-serif;margin-top:6px}
.lead{font-size:20px;color:var(--muted)}
.related{border-top:1px solid var(--line);margin-top:40px;padding-top:16px}
.related h3{font:700 16px system-ui,sans-serif;text-transform:uppercase;letter-spacing:.06em}
.related li{margin:8px 0}
.nl-box{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--accent);border-radius:8px;padding:20px;font-family:system-ui,sans-serif}
.nl-box h3{margin:0 0 6px;font-size:20px;line-height:1.2}
.nl-box p{margin:0 0 14px;color:var(--muted);font-size:15px;line-height:1.45}
.nl-box input{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:6px;font:16px system-ui,sans-serif;background:var(--bg);color:var(--fg);margin-bottom:8px}
.nl-box button{width:100%;padding:11px 16px;border:0;border-radius:6px;background:var(--accent);color:#fff;font:600 15px system-ui,sans-serif;cursor:pointer}
.nl-box .ok{display:none;color:var(--accent);font-weight:600;margin:0}
.nl-box.done .nl-form{display:none}.nl-box.done .ok{display:block}
@media (max-width:900px){.layout{grid-template-columns:1fr;gap:32px}.sidebar{position:static}}
footer{text-align:center;color:var(--muted);font:13px system-ui,sans-serif;padding:24px 16px;border-top:1px solid var(--line)}
@media (max-width:600px){article h1{font-size:28px}}
"""


def esc(s):
    return html.escape(s, quote=True)


def head(title, description, url, image, extra=""):
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<meta property="og:site_name" content="{esc(SITE)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta property="og:locale" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
{extra}
<link rel="stylesheet" href="{BASE}style.css">
{SDK}
</head>
<body>
<header class="site"><a href="{BASE}">{esc(SITE)}</a><p>Whisky y metalcore, sin filtros</p></header>
"""


CONVERSION_JS = """<script>
document.querySelectorAll('.nl-box .nl-cta').forEach(function (btn) {
  btn.addEventListener('click', function () {
    window.marfeel = window.marfeel || { cmd: [] };
    window.marfeel.cmd.push(["compass", function(compass) {
      compass.trackConversion("CTA Newsletter");
    }]);
    btn.closest('.nl-box').classList.add('done');
  });
});
</script>"""

FOOT = f'<footer>{esc(SITE)} · blog de pruebas</footer>\n</body>\n</html>\n'


def fmt_date(iso):
    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto",
              "septiembre", "octubre", "noviembre", "diciembre"]
    y, m, d = iso[:10].split("-")
    return f"{int(d)} de {months[int(m) - 1]} de {y}"


IMAGES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "images.json")))


def fetch_image(a):
    path = os.path.join(OUT, "img", a["slug"] + ".jpg")
    if not (os.path.exists(path) and os.path.getsize(path) > 10000):
        raise SystemExit(f"missing image {path}")


def main():
    os.makedirs(os.path.join(OUT, "img"), exist_ok=True)
    with open(os.path.join(OUT, "style.css"), "w") as f:
        f.write(CSS.strip() + "\n")
    open(os.path.join(OUT, ".nojekyll"), "w").close()

    for a in ARTICLES:
        fetch_image(a)
        url = f"{BASE}{a['slug']}/"
        img = f"{BASE}img/{a['slug']}.jpg"
        ld = {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "headline": a["title"],
            "description": a["excerpt"],
            "url": url,
            "mainEntityOfPage": url,
            "datePublished": a["date"],
            "dateModified": a["date"],
            "articleSection": a["section"],
            "inLanguage": "es-ES",
            "image": {"@type": "ImageObject", "url": img},
            "author": {"@type": "Organization", "name": SITE},
            "publisher": {"@type": "Organization", "name": SITE},
        }
        extra = (f'<meta property="og:type" content="article">\n'
                 f'<meta property="article:published_time" content="{a["date"]}">\n'
                 f'<meta property="article:section" content="{a["section"]}">\n'
                 f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>')
        related = [r for r in ARTICLES if r is not a]
        related = [r for r in related if r["section"] == a["section"]] + \
                  [r for r in related if r["section"] != a["section"]][:2]
        rel = "\n".join(f'<li><a href="{BASE}{r["slug"]}/">{esc(r["title"])}</a></li>' for r in related)
        body = "\n".join(f"<p>{esc(p)}</p>" for p in a["body"])
        page = head(a["title"], a["excerpt"], url, img, extra) + f"""<div class="layout">
<main>
<article>
<span class="section">{a['section']}</span>
<h1>{esc(a['title'])}</h1>
<div class="meta">{fmt_date(a['date'])} · Redacción</div>
<p class="lead">{esc(a['excerpt'])}</p>
<figure><img src="{img}" alt="{esc(a['title'])}"><figcaption>Foto: <a href="{IMAGES[a['slug']]['source']}" rel="nofollow">{esc(IMAGES[a['slug']]['credit'])}</a>, {IMAGES[a['slug']]['license']}</figcaption></figure>
{body}
</article>
<aside class="related"><h3>Te puede interesar</h3><ul>
{rel}
</ul></aside>
</main>
<aside class="sidebar"><div class="nl-box"><h3>La newsletter de {esc(SITE)}</h3><p>Whisky, metalcore y lo mejor de la semana en tu correo, cada viernes.</p>
<div class="nl-form"><input type="email" name="email" placeholder="tu@email.com" aria-label="Email"><button type="button" class="nl-cta">Apúntate gratis</button></div>
<p class="ok">¡Hecho! Ya estás en la lista.</p></div></aside>
</div>
""" + CONVERSION_JS + "\n" + FOOT
        os.makedirs(os.path.join(OUT, a["slug"]), exist_ok=True)
        with open(os.path.join(OUT, a["slug"], "index.html"), "w") as f:
            f.write(page)

    ordered = sorted(ARTICLES, key=lambda x: x["date"], reverse=True)
    cards = "\n".join(f"""<a class="card" href="{BASE}{a['slug']}/"><img src="{BASE}img/{a['slug']}.jpg" alt="" loading="lazy"><div><span class="section">{a['section']}</span><h2>{esc(a['title'])}</h2><p>{esc(a['excerpt'])}</p></div></a>""" for a in ordered)
    home_extra = '<meta property="og:type" content="website">'
    home = head(SITE, "Whisky y metalcore, sin filtros", BASE,
                f"{BASE}img/{ordered[0]['slug']}.jpg", home_extra) + \
        f'<div class="grid">\n{cards}\n</div>\n' + FOOT
    with open(os.path.join(OUT, "index.html"), "w") as f:
        f.write(home)

    with open(os.path.join(OUT, "urls.txt"), "w") as f:
        f.write(BASE + "\n" + "".join(f"{BASE}{a['slug']}/\n" for a in ARTICLES))
    print("ok", len(ARTICLES), "articles ->", OUT)


if __name__ == "__main__":
    sys.exit(main())
