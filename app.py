import streamlit as st
from PIL import Image
import base64
import os

# --------- CONFIG DE PÁGINA ---------
st.set_page_config(
    page_title="Portfolio | Juan Mera",
    page_icon="💼",
    layout="wide"
)

# --------- FUNCIONES DE IDIOMA ---------
def traducir(texto_es, texto_en, idioma):
    return texto_en if idioma == "English" else texto_es

# --------- CARGA Y PROCESO DE IMAGEN ---------
with open("Profile.jpeg", "rb") as file:
    img_data = file.read()
img_base64 = base64.b64encode(img_data).decode()

# --------- SELECTOR DE IDIOMA ---------
st.markdown(
    f"""
    <div style='text-align: center; margin-bottom: 20px;'>
        <img src="data:image/jpeg;base64,{img_base64}" 
             style="width: 350px; height: 350px; object-fit: cover; border-radius: 50%; border: 3px solid #ddd;" 
             alt="Foto de perfil" />
    </div>
    """,
    unsafe_allow_html=True
)

idioma = st.selectbox("Seleccionar idioma / Select language", ["Español", "English"], index=0)

# --------- ENCABEZADO ---------
st.markdown(f"<h1 style='text-align: center;'>Juan Ignacio Francisco Mera</h1>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align: center;'>Backend Developer | Python | Data Analysis | Automation</h4>", unsafe_allow_html=True)

st.markdown(f"""
<p style='text-align: center;'>
📧 <a href='mailto:juanignaciofmera@gmail.com'>juanignaciofmera@gmail.com</a> &nbsp;|&nbsp;
🔙 <a href='https://github.com/juanifmera' target='_blank'>GitHub</a> &nbsp;|&nbsp;
💼 <a href='https://www.linkedin.com/in/juan-ignacio-francisco-mera-426bb0174/' target='_blank'>LinkedIn</a>
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# --------- SOBRE MÍ ---------
st.subheader(traducir("👋 Sobre mí", "👋 About Me", idioma))
st.write(traducir(
    """
Soy **Licenciado en Comercio Internacional**, con formación sólida en **Economía** por la Universidad de Buenos Aires (UBA),
y actualmente me estoy especializando en programación con una **Diplomatura en Python en la UTN**.

Mi perfil combina lo mejor del mundo de los negocios con el poder de la tecnología: sé cómo leer datos, entender contextos
comerciales complejos y transformarlos en **soluciones automatizadas e inteligentes** que aporten valor real.

Me destaco por mi capacidad de aprendizaje autodidacta, una actitud proactiva y mi pasión por el desarrollo backend,
la automatización de procesos y el análisis de datos. Disfruto colaborar en equipos, liderar proyectos con impacto
y enfrentar nuevos desafíos tecnológicos con creatividad y precisión.

Si estás buscando a alguien que entienda tanto de **estrategia como de código**, ¡acá estoy!
""",
    """
I hold a **Bachelor's degree in International Trade**, with a solid background in **Economics** from the University of Buenos Aires (UBA),
and I'm currently specializing in programming through a **Python Diploma at UTN**.

My profile blends the best of the business world with the power of technology: I know how to read data, understand complex
business contexts, and turn them into **automated and intelligent solutions** that deliver real value.

I stand out for my self-learning abilities, proactive attitude, and passion for backend development,
process automation, and data analysis. I enjoy collaborating in teams, leading impactful projects,
and tackling new technological challenges with creativity and precision.

If you're looking for someone who understands both **strategy and code**, here I am!
""",
    idioma
))

# --------- EXPERIENCIA ---------
st.markdown("---")
st.subheader(traducir("💼 Experiencia Laboral", "💼 Work Experience", idioma))

experiencias = [
    {
        "titulo": traducir("EY GDS - Junior Project Manager", "EY GDS - Junior Project Manager", idioma),
        "fecha": traducir("Octubre 2023 - Diciembre 2024", "October 2023 - December 2024", idioma),
        "desc": traducir(
            "Liderazgo y gestión de proyectos estratégicos y financieros de grandes bancos comerciales.",
            "Leadership and management of strategic and financial projects for large commercial banks.", idioma)
    },
    {
        "titulo": traducir("EY GDS - Especialista Financiero", "EY GDS - Financial Specialist", idioma),
        "fecha": traducir("Septiembre 2022 - Octubre 2023", "September 2022 - October 2023", idioma),
        "desc": traducir(
            "Análisis, creación y actualización de reportes interactivos con Power BI y Power Query.",
            "Analysis, creation and update of interactive reports using Power BI and Power Query.", idioma)
    },
    {
        "titulo": traducir("EY GDS - Analista Mercury", "EY GDS - Mercury Analyst", idioma),
        "fecha": traducir("Julio 2022 - Septiembre 2022", "July 2022 - September 2022", idioma),
        "desc": traducir(
            "Gestión de contactos con clientes y generación de oportunidades comerciales.",
            "Client contact management and generation of commercial opportunities.", idioma)
    },
    {
        "titulo": traducir("Benevia S.R.L - Empleado Administrativo y Financiero", "Benevia S.R.L - Administrative and Financial Employee", idioma),
        "fecha": traducir("Noviembre 2021 - Julio 2022", "November 2021 - July 2022", idioma),
        "desc": traducir("Gestión administrativa y financiera de la empresa",
                        "Administrative and financial management of the company", idioma)
    },
]

rows = [experiencias[i:i + 2] for i in range(0, len(experiencias), 2)]
for row in rows:
    cols = st.columns(2)
    for col, exp in zip(cols, row):
        with col:
            with st.container(border=True):
                st.markdown(f"### {exp['titulo']}")
                st.caption(exp["fecha"])
                st.write(exp["desc"])

# --------- PROYECTOS ---------
st.markdown("---")
st.subheader(traducir("🚀 Proyectos", "🚀 Projects", idioma))

proyectos = [
    {
        "titulo": "💸 Expense Tracker App",
        "imagen": "assets/expense_tracker.png",
        "repo": "https://github.com/juanifmera/Expense-Tracker-App",
        "tecnologias": "Python, Tkinter, SQLite, Peewee ORM, Matplotlib, Pandas",
        "desc": traducir(
            "Aplicación de escritorio que permite gestionar gastos personales, clasificarlos por categoría y visualizar resúmenes con gráficos.",
            "Desktop app for managing personal expenses, categorizing them and visualizing summaries with charts.", idioma),
        "aprendizaje": traducir(
            "Arquitectura MVC, uso del patrón Observer, integración de base de datos local, visualización con Matplotlib, manejo de eventos con Tkinter.",
            "MVC architecture, Observer pattern, local DB integration, Matplotlib visualizations, Tkinter event handling.", idioma)
    },
    {
        "titulo": "🤖 Dollar Tweet Bot",
        "imagen": "assets/selenium_bot.png",
        "repo": "https://github.com/juanifmera/Selenium",
        "tecnologias": "Python, Selenium, BeautifulSoup, Tkinter",
        "desc": traducir(
            "Bot que realiza scraping de cotizaciones del dólar y publica automáticamente tweets diarios.",
            "Bot that scrapes dollar exchange rates and automatically posts daily tweets.", idioma),
        "aprendizaje": traducir(
            "Automatización web avanzada, manejo de cookies, navegación dinámica, scraping con BeautifulSoup.",
            "Advanced web automation, cookie handling, dynamic navigation, scraping with BeautifulSoup.", idioma)
    },
    {
        "titulo": "🌐 MongoDB + FastAPI",
        "imagen": "assets/fastapi_mongo.png",
        "repo": "https://github.com/juanifmera/MongoDB-FAST-API",
        "tecnologias": "Python, FastAPI, MongoDB Atlas, Pydantic",
        "desc": traducir(
            "API REST que permite gestionar usuarios y tareas con conexión segura a MongoDB.",
            "REST API for managing users and tasks with secure MongoDB connection.", idioma),
        "aprendizaje": traducir(
            "Construcción de APIs modernas, validaciones con Pydantic, conexión con bases NoSQL en la nube, organización modular.",
            "Modern API development, Pydantic validation, NoSQL cloud DB, modular architecture.", idioma)
    },
    {
        "titulo": "🌐 Flask Web App",
        "imagen": "assets/flask_app.png",
        "repo": "https://github.com/juanifmera/Flask-Web-App",
        "tecnologias": "Python, Flask, HTML, CSS",
        "desc": traducir(
            "Aplicación web construida con Flask para experimentar con rutas, formularios y templates.",
            "Web app built with Flask to experiment with routes, forms and templates.", idioma),
        "aprendizaje": traducir(
            "Fundamentos de desarrollo web backend, diseño de rutas, lógica de templates, manejo de formularios.",
            "Backend web fundamentals, route design, template logic, form handling.", idioma)
    },
    {
        "titulo": "🤖 MELI Automation",
        "imagen": "assets/meli_automation.png",
        "repo": "https://github.com/juanifmera/MELI-Automation",
        "tecnologias": "Python, BeautifulSoup, Requests, Pandas",
        "desc": traducir(
            "Herramienta para obtener datos de productos de MercadoLibre y calcular valor en USD.",
            "Tool to scrape MercadoLibre product data and calculate USD value.", idioma),
        "aprendizaje": traducir(
            "Scraping avanzado, manejo de HTML dinámico, consumo de múltiples fuentes, exportación a Excel.",
            "Advanced scraping, dynamic HTML parsing, multi-source ingestion, Excel export.", idioma)
    },
    {
        "titulo": "🌐 Portfolio Web",
        "imagen": "assets/portfolio_web.png",
        "repo": "",
        "tecnologias": "Python, Streamlit, HTML, CSS",
        "desc": traducir(
            "Sitio web personal interactivo desarrollado con Streamlit, presentación, CV descargable y resumen de proyectos.",
            "Personal website built with Streamlit, resume download, and project showcase.", idioma),
        "aprendizaje": traducir(
            "Streamlit, layouts personalizados, descarga de archivos, organización visual moderna.",
            "Streamlit development, custom layouts, file downloads, modern visual organization.", idioma)
    }
]

tabs = st.tabs([p["titulo"] for p in proyectos])
for i, tab in enumerate(tabs):
    with tab:
        p = proyectos[i]
        st.markdown(f"### {p['titulo']}")
        st.image(p['imagen'], use_container_width=True)
        if p['repo']:
            st.markdown(f"**{traducir('Repositorio', 'Repository', idioma)}:** [{p['titulo']}]({p['repo']})")
        st.markdown(f"**{traducir('Tecnologías', 'Technologies', idioma)}:** {p['tecnologias']}")
        st.markdown(f"**{traducir('Descripción', 'Description', idioma)}:** {p['desc']}")
        st.markdown(f"**{traducir('Aprendizaje', 'Learning', idioma)}:** {p['aprendizaje']}")


# --------- CV ---------
st.markdown("---")
st.subheader(traducir("📄 Descargar mi CV", "📄 Download my CV", idioma))

col1, col2 = st.columns(2)

with col1:
    with open("Curriculum - Juan Ignacio Francisco Mera - Español.pdf", "rb") as file_es:
        data_es = file_es.read()
        st.download_button(
            label=traducir("📎 Descargar CV en Español", "📎 Download CV in Spanish", idioma),
            data=data_es,
            file_name="Curriculum - Juan Ignacio Francisco Mera - Español.pdf",
            mime="application/pdf",
            use_container_width=True
        )

with col2:
    with open("Curriculum - Juan Ignacio Francisco Mera - Ingles.pdf", "rb") as file_en:
        data_en = file_en.read()
        st.download_button(
            label=traducir("📎 Descargar CV en Inglés", "📎 Download CV in English", idioma),
            data=data_en,
            file_name="Curriculum - Juan Ignacio Francisco Mera - Ingles.pdf",
            mime="application/pdf",
            use_container_width=True
        )

st.info(traducir(
    "⚠️ Por el momento, la descarga del archivo PDF no está funcionando correctamente desde esta web. Si querés acceder a mi CV, escribime directamente por [LinkedIn](https://www.linkedin.com/in/juan-ignacio-francisco-mera-426bb0174/). ¡Gracias por tu interés!",
    "⚠️ At the moment, the PDF download is not working properly from this site. If you'd like to access my resume, please contact me directly via [LinkedIn](https://www.linkedin.com/in/juan-ignacio-francisco-mera-426bb0174/). Thank you for your interest!",
    idioma
))

# --------- FOOTER ---------
st.markdown("---")
st.markdown(f"<p style='text-align: center;'>© {traducir('Todos los derechos reservados', 'All rights reserved', idioma)} | Juan Ignacio Francisco Mera</p>", unsafe_allow_html=True)
