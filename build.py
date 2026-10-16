"""Builds index.html (Spanish) and en/index.html (English) from one template.
Edit the text in T below, then run: python3 build.py
"""
from pathlib import Path

WA = "50762078779"
EMAIL = "ventas@qcti.digital"
IG = "https://instagram.com/qcti.digital"
BEHOLD = "ZJGMYx6UoQaLjsUKSfDc"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSe6XqBtSs-Q9NquqeVwQROhagyp8VaxZxzmzQJxmTKVOXbT4Q/viewform?embedded=true"

ICON = {
 "wifi": '<path d="M2 8.8a15 15 0 0 1 20 0"/><path d="M5 12.6a10 10 0 0 1 14 0"/><path d="M8.5 16.4a5 5 0 0 1 7 0"/><circle cx="12" cy="20" r="1"/>',
 "cam": '<path d="M3 7h12l3 3v4l-3 3H3z"/><circle cx="9" cy="12" r="2.5"/><path d="M18 10l3-2v8l-3-2"/>',
 "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/><circle cx="12" cy="16" r="1.2"/>',
 "phone": '<path d="M4 4h4l2 5-2.5 1.5a11 11 0 0 0 6 6L15 14l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 2 6a2 2 0 0 1 2-2z"/>',
 "home": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M12 13a2.5 2.5 0 0 0-1.5 4.5V19h3v-1.5A2.5 2.5 0 0 0 12 13z"/>',
 "tool": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/>',
}
WA_SVG = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.6A8.4 8.4 0 1 1 21 11.5z"/></svg>'

T = {
 "es": dict(
  lang="es", root="", other="en/", other_label="EN", other_name="English",
  title="QCTI — Integración tecnológica en Panamá",
  desc="Redes, cámaras, control de acceso, telefonía IP y casas inteligentes. Diseñamos, instalamos y mantenemos. Proyectos en toda la República de Panamá.",
  nav=["Servicios", "Cómo trabajamos", "Trabajos", "Contacto"],
  wa_text="Hola QCTI, quisiera información",
  eyebrow="Integración tecnológica · Todo Panamá",
  h1='Tecnología que trabaja para ti, <span>no al revés.</span>',
  hero_p="Redes, cámaras, control de acceso y casas inteligentes. Lo diseñamos, lo instalamos y lo mantenemos funcionando, para que tú solo tengas que tocar un botón (o pedírselo a Alexa).",
  cta_wa="Escríbenos por WhatsApp", cta_svc="Ver servicios",
  hero_alt="Sala con TV empotrado y barra de sonido instalados por QCTI",
  facts=[("+20 años", "metidos en tecnología"), ("Casa y oficina", "residencial y comercial"), ("Todo Panamá", "proyectos en todo el país")],
  svc_eyebrow="Servicios", svc_h="Lo que hacemos (y hacemos bien)",
  svc_lead="Desde el Wi‑Fi que no llega al cuarto del fondo hasta la central telefónica de tu oficina. Si tiene cable, señal o app, probablemente es lo nuestro.",
  svc=[("wifi", "Redes y Wi‑Fi", "Cobertura en toda la casa u oficina, no solo al lado del router. Cableado, puntos de acceso y redes ordenadas."),
       ("cam", "Cámaras y seguridad", "Mira tu casa o negocio desde el celular, con grabación confiable y cámaras donde de verdad hacen falta."),
       ("lock", "Control de acceso", "Puertas con tarjeta, código o app. Tú decides quién entra, cuándo, y te enteras de todo."),
       ("phone", "Telefonía IP (PBX)", "Centrales telefónicas para oficinas: extensiones, recepción automática y llamadas desde el celular."),
       ("home", "Casa inteligente", "Luces, aires, cortinas y escenas que responden a tu voz o a un toque. Cómodo, no complicado."),
       ("tool", "Soporte y mantenimiento", "Actualizaciones, monitoreo y una mano amiga cuando algo falla o quieres cambiar algo.")],
  dim_eyebrow="Cómo trabajamos", dim_h='Le damos <span style="color:var(--blue)">DIM</span> a tus ideas',
  dim=[("D", "Diseñamos", "Escuchamos lo que necesitas (y lo que no) y armamos una solución a tu medida."),
       ("I", "Instalamos", "Cableado, adaptaciones y configuración. Nosotros coordinamos todo; tú no tienes que perseguir a nadie."),
       ("M", "Mantenemos", "Software al día, sistemas vigilados y soporte a la mano para cualquier duda o cambio.")],
  tips_eyebrow="Tips tech", tips_h="Consejos rápidos para tu casa",
  tips_lead="Trucos cortos y sin complicaciones, directo de nuestro Instagram.",
  tips_box="Cada semana publicamos tips para que tu red, tus cámaras y tu casa inteligente funcionen mejor.",
  tips_btn="Síguenos @qcti.digital",
  work_eyebrow="Trabajos recientes", work_h="Hecho por QCTI",
  work=[("rack-residencial.jpg", "Residencial — rack de red organizado"),
        ("centro-monitoreo.jpg", "Comercial — centro de monitoreo de seguridad"),
        ("tv-empotrado.jpg", "Residencial — TV empotrado y audio/video"),
        ("gabinete-cctv.jpg", "Comercial — gabinete de CCTV"),
        ("rack-principal.jpg", "Residencial — rack principal de la casa"),
        ("panel-compacto.jpg", "Residencial — panel de red compacto")],
  c_eyebrow="Contacto", c_h="¿Hablamos?",
  c_lead="Cuéntanos qué tienes en mente. Te respondemos rápido y sin rodeos, aunque solo sea una pregunta.",
  c_area="Proyectos en toda la República de Panamá", c_email="Correo",
  form_title="Formulario de contacto",
  foot="Quality Computer &amp; Tech Integration",
 ),
 "en": dict(
  lang="en", root="../", other="../", other_label="ES", other_name="Español",
  title="QCTI — Technology integration in Panama",
  desc="Networks, cameras, access control, IP phone systems and smart homes. We design, install and maintain. Projects across all of Panama.",
  nav=["Services", "How we work", "Work", "Contact"],
  wa_text="Hi QCTI, I'd like some info",
  eyebrow="Tech integration · All of Panama",
  h1='Technology that works for you, <span>not the other way around.</span>',
  hero_p="Networks, cameras, access control and smart homes. We design it, install it and keep it running, so all you have to do is tap a button (or ask Alexa).",
  cta_wa="Message us on WhatsApp", cta_svc="See services",
  hero_alt="Living room with a built-in TV and soundbar installed by QCTI",
  facts=[("20+ years", "deep in technology"), ("Home &amp; office", "residential and commercial"), ("All of Panama", "projects nationwide")],
  svc_eyebrow="Services", svc_h="What we do (and do well)",
  svc_lead="From the Wi‑Fi that never reaches the back bedroom to your office phone system. If it has a cable, a signal or an app, it's probably our thing.",
  svc=[("wifi", "Networks &amp; Wi‑Fi", "Coverage across the whole home or office, not just next to the router. Cabling, access points and tidy networks."),
       ("cam", "Cameras &amp; security", "Check on your home or business from your phone, with reliable recording and cameras where they actually matter."),
       ("lock", "Access control", "Doors that open with a card, code or app. You decide who gets in and when, and you see it all."),
       ("phone", "IP phone systems (PBX)", "Office phone systems with extensions, an auto‑attendant and calls right from your cell."),
       ("home", "Smart home", "Lights, A/C, blinds and scenes that answer to your voice or a tap. Comfortable, not complicated."),
       ("tool", "Support &amp; maintenance", "Updates, monitoring and a helping hand when something breaks or you want a change.")],
  dim_eyebrow="How we work", dim_h='We <span style="color:var(--blue)">DIM</span> your ideas',
  dim=[("D", "Design", "We listen to what you need (and what you don't) and build a solution that fits."),
       ("I", "Install", "Wiring, site work and configuration. We coordinate everything, so you never chase anyone."),
       ("M", "Manage", "Software kept current, systems monitored, and support on hand for any question or change.")],
  tips_eyebrow="Tech tips", tips_h="Quick tips for your home",
  tips_lead="Short, no‑nonsense tricks, straight from our Instagram.",
  tips_box="Every week we post tips to make your network, cameras and smart home work better.",
  tips_btn="Follow @qcti.digital",
  work_eyebrow="Recent work", work_h="Made by QCTI",
  work=[("rack-residencial.jpg", "Residential — organized network rack"),
        ("centro-monitoreo.jpg", "Commercial — security monitoring center"),
        ("tv-empotrado.jpg", "Residential — built-in TV and A/V"),
        ("gabinete-cctv.jpg", "Commercial — CCTV cabinet"),
        ("rack-principal.jpg", "Residential — main home rack"),
        ("panel-compacto.jpg", "Residential — compact network panel")],
  c_eyebrow="Contact", c_h="Let's talk",
  c_lead="Tell us what you have in mind. We'll get back to you fast and straight to the point, even if it's just a question.",
  c_area="Projects nationwide, across all of Panama", c_email="Email",
  form_title="Contact form",
  foot="Quality Computer &amp; Tech Integration",
 ),
}


def page(d):
    r = d["root"]
    wa = f"https://wa.me/{WA}?text=" + d["wa_text"].replace(" ", "%20").replace(",", "%2C").replace("'", "%27")
    ids = ["servicios", "como", "trabajos", "contacto"]
    nav = "".join(f'<a href="#{i}">{n}</a>' for i, n in zip(ids, d["nav"]))
    svc = "".join(
        f'<div class="card"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[i]}</svg><h3>{t}</h3><p>{x}</p></div>'
        for i, t, x in d["svc"])
    dim = "".join(f'<div class="step"><div class="l">{l}</div><h3>{t}</h3><p>{x}</p></div>' for l, t, x in d["dim"])
    facts = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in d["facts"])
    work = "".join(
        f'<figure><img src="{r}assets/img/{f}" alt="{c}" loading="lazy" width="1400" height="788"><figcaption>{c}</figcaption></figure>'
        for f, c in d["work"])
    return f"""<!doctype html>
<html lang="{d['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{d['title']}</title>
<meta name="description" content="{d['desc']}">
<meta property="og:title" content="{d['title']}">
<meta property="og:description" content="{d['desc']}">
<meta property="og:image" content="https://qcti.digital/assets/img/og.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="{r}favicon.png">
<link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
<link rel="alternate" hreflang="es" href="https://qcti.digital/">
<link rel="alternate" hreflang="en" href="https://qcti.digital/en/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;700;800&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/site.css">
</head>
<body>
<header><div class="wrap bar">
<a class="logo" href="#top" aria-label="QCTI"><img src="{r}assets/img/qcti-logo-white.png" alt="QCTI" width="640" height="200"></a>
<nav aria-label="Menu">{nav}<a class="lang" href="{d['other']}" hreflang="{'en' if d['lang']=='es' else 'es'}" aria-label="{d['other_name']}">{d['other_label']}</a></nav>
</div></header>
<main id="top">
<section class="hero"><div class="wrap">
<div class="hero-text">
<p class="eyebrow">{d['eyebrow']}</p>
<h1>{d['h1']}</h1>
<p>{d['hero_p']}</p>
<div class="ctas"><a class="btn btn-red" href="{wa}">{WA_SVG}{d['cta_wa']}</a><a class="btn btn-line" href="#servicios">{d['cta_svc']}</a></div>
</div>
<img class="hero-img" src="{r}assets/img/hero-av-wall.jpg" alt="{d['hero_alt']}" width="1400" height="787">
</div></section>
<section class="facts" aria-label="QCTI"><div class="wrap">{facts}</div></section>
<section id="servicios" class="section"><div class="wrap">
<p class="eyebrow">{d['svc_eyebrow']}</p><h2>{d['svc_h']}</h2><p class="lead">{d['svc_lead']}</p>
<div class="grid">{svc}</div>
</div></section>
<section id="como" class="section dark"><div class="wrap">
<p class="eyebrow">{d['dim_eyebrow']}</p><h2 style="margin-bottom:44px">{d['dim_h']}</h2>
<div class="steps">{dim}</div>
</div></section>
<section id="tips" class="section ice"><div class="wrap">
<div class="tips-head"><div><p class="eyebrow">{d['tips_eyebrow']}</p><h2>{d['tips_h']}</h2><p class="lead">{d['tips_lead']}</p></div></div>
<!-- Instagram feed (Behold) -->
<div class="ig-feed"><behold-widget feed-id="{BEHOLD}"></behold-widget></div>
<div class="ig-box"><p>{d['tips_box']}</p><a class="btn btn-red" href="{IG}">{d['tips_btn']}</a></div>
</div></section>
<section id="trabajos" class="section"><div class="wrap">
<p class="eyebrow">{d['work_eyebrow']}</p><h2 style="margin-bottom:40px">{d['work_h']}</h2>
<div class="grid gallery">{work}</div>
</div></section>
<section id="contacto" class="section dark contact"><div class="wrap">
<div class="contact-info">
<p class="eyebrow">{d['c_eyebrow']}</p><h2>{d['c_h']}</h2><p class="lead" style="margin-bottom:30px">{d['c_lead']}</p>
<a class="btn btn-red" href="{wa}">{WA_SVG}WhatsApp +507 6207-8779</a>
<ul><li>{d['c_email']}: <a href="mailto:{EMAIL}">{EMAIL}</a></li><li>Instagram: <a href="{IG}">@qcti.digital</a></li><li>{d['c_area']}</li></ul>
</div>
<div class="form-box"><iframe src="{FORM}" title="{d['form_title']}" loading="lazy"></iframe></div>
</div></section>
</main>
<footer><div class="wrap"><div>© 2026 QCTI — {d['foot']}</div><a href="{IG}">Instagram @qcti.digital</a></div></footer>
<a class="wa-float" href="{wa}" aria-label="WhatsApp">{WA_SVG}</a>
<script type="module" src="https://w.behold.so/widget.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    base = Path(__file__).parent
    (base / "index.html").write_text(page(T["es"]), encoding="utf-8")
    (base / "en").mkdir(exist_ok=True)
    (base / "en" / "index.html").write_text(page(T["en"]), encoding="utf-8")
    print("built")
