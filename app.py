import streamlit as st

st.set_page_config(
    page_title="Roushan Kumar | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --bg: #0d0d12;
    --surface: #13131a;
    --card: #1a1a24;
    --accent: #c084fc;
    --accent2: #818cf8;
    --accent3: #34d399;
    --text: #f1f0f7;
    --muted: #9b97b4;
    --border: #2a2a3a;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

.stApp { background: var(--bg) !important; }

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* Hero */
.hero {
    background: linear-gradient(135deg, #0d0d12 0%, #13101f 50%, #0d0d12 100%);
    padding: 90px 60px 70px;
    position: relative;
    overflow: hidden;
    border-bottom: 1px solid var(--border);
}
.hero::before {
    content: '';
    position: absolute;
    top: -100px; right: -100px;
    width: 500px; height: 500px;
    background: radial-gradient(circle, rgba(192,132,252,0.15) 0%, transparent 70%);
    border-radius: 50%;
}
.hero::after {
    content: '';
    position: absolute;
    bottom: -80px; left: 200px;
    width: 350px; height: 350px;
    background: radial-gradient(circle, rgba(129,140,248,0.1) 0%, transparent 70%);
    border-radius: 50%;
}

.badge {
    display: inline-block;
    background: rgba(52, 211, 153, 0.12);
    color: var(--accent3);
    border: 1px solid rgba(52, 211, 153, 0.3);
    padding: 6px 16px;
    border-radius: 100px;
    font-size: 13px;
    font-weight: 500;
    letter-spacing: 0.5px;
    margin-bottom: 28px;
}
.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: clamp(52px, 6vw, 82px);
    font-weight: 900;
    line-height: 1.05;
    background: linear-gradient(135deg, #f1f0f7 30%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 16px;
}
.hero-subtitle {
    font-size: 18px;
    color: var(--muted);
    font-weight: 300;
    margin-bottom: 12px;
}
.hero-tags { display: flex; flex-wrap: wrap; gap: 10px; margin: 28px 0 36px; }
.tag {
    background: rgba(192,132,252,0.1);
    color: var(--accent);
    border: 1px solid rgba(192,132,252,0.25);
    padding: 6px 14px;
    border-radius: 6px;
    font-size: 13px;
    font-weight: 500;
}
.tag.indigo {
    background: rgba(129,140,248,0.1);
    color: var(--accent2);
    border-color: rgba(129,140,248,0.25);
}
.hero-desc {
    max-width: 620px;
    font-size: 16px;
    line-height: 1.75;
    color: #b8b4d0;
    margin-bottom: 40px;
}
.hero-stats { display: flex; gap: 40px; flex-wrap: wrap; }
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    font-weight: 700;
    color: var(--accent);
    line-height: 1;
}
.stat-label {
    font-size: 12px;
    color: var(--muted);
    margin-top: 4px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

/* Sections */
.section {
    padding: 70px 60px;
    border-bottom: 1px solid var(--border);
}
.section-alt { background: var(--surface); }
.section-tag {
    font-size: 11px;
    font-weight: 600;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 10px;
}
.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    font-weight: 700;
    margin: 0 0 12px;
    color: var(--text);
}
.section-sub {
    color: var(--muted);
    font-size: 15px;
    margin-bottom: 48px;
    max-width: 560px;
    line-height: 1.7;
}

/* Cards */
.card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 20px;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 4px; height: 100%;
    background: linear-gradient(180deg, var(--accent), var(--accent2));
    border-radius: 4px 0 0 4px;
}
.card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 12px;
    flex-wrap: wrap;
    gap: 8px;
}
.card-title { font-size: 17px; font-weight: 600; color: var(--text); }
.card-org { font-size: 14px; color: var(--accent); margin-top: 3px; }
.card-status {
    font-size: 12px;
    background: rgba(52, 211, 153, 0.12);
    color: var(--accent3);
    border: 1px solid rgba(52, 211, 153, 0.25);
    padding: 4px 12px;
    border-radius: 100px;
    white-space: nowrap;
}
.card-body { font-size: 14px; color: var(--muted); line-height: 1.7; }

/* Project Cards */
.project-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 20px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s;
}
.project-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 3px;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
}
.project-title {
    font-size: 18px;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 8px;
}
.project-desc {
    font-size: 14px;
    color: var(--muted);
    line-height: 1.7;
    margin-bottom: 18px;
}
.project-stack { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }
.stack-pill {
    background: rgba(129,140,248,0.12);
    color: var(--accent2);
    border: 1px solid rgba(129,140,248,0.25);
    padding: 4px 11px;
    border-radius: 5px;
    font-size: 12px;
    font-weight: 500;
}
.project-links { display: flex; gap: 12px; }
.proj-link {
    font-size: 13px;
    color: var(--accent);
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 5px;
    border: 1px solid rgba(192,132,252,0.25);
    padding: 5px 14px;
    border-radius: 6px;
    background: rgba(192,132,252,0.08);
}

/* Skills */
.skill-group {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px;
    height: 100%;
    margin-bottom: 20px;
}
.skill-group-title {
    font-size: 14px;
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 18px;
}
.skill-pills { display: flex; flex-wrap: wrap; gap: 8px; }
.pill {
    background: rgba(255,255,255,0.05);
    border: 1px solid var(--border);
    color: #d0cce8;
    padding: 5px 12px;
    border-radius: 6px;
    font-size: 13px;
}

/* Education */
.edu-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 20px;
    display: flex;
    gap: 24px;
    align-items: flex-start;
}
.edu-year {
    font-family: 'Playfair Display', serif;
    font-size: 13px;
    color: var(--muted);
    min-width: 90px;
    padding-top: 4px;
}
.edu-degree { font-size: 17px; font-weight: 600; color: var(--text); margin-bottom: 4px; }
.edu-field { font-size: 14px; color: var(--accent); margin-bottom: 4px; }
.edu-inst { font-size: 14px; color: var(--muted); }

/* Grid helpers */
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.three-col { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; }

/* Nav */
.nav {
    background: rgba(13,13,18,0.92);
    backdrop-filter: blur(20px);
    padding: 18px 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border);
}
.nav-logo {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 700;
    background: linear-gradient(135deg, var(--text), var(--accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.nav-links { display: flex; gap: 28px; }
.nav-link { color: var(--muted); text-decoration: none; font-size: 14px; }

/* Contact */
.contact-section {
    background: linear-gradient(135deg, #13101f, #0d0d12);
    padding: 80px 60px;
    text-align: center;
}
.contact-grid {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 40px;
}
.contact-btn {
    background: rgba(192,132,252,0.12);
    border: 1px solid rgba(192,132,252,0.3);
    color: var(--accent);
    padding: 14px 28px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 500;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

hr { border-color: var(--border) !important; }
.stMarkdown { color: var(--text); }
h1, h2, h3 { color: var(--text) !important; }
</style>
""", unsafe_allow_html=True)

# ── NAV ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="nav">
    <div class="nav-logo">RK</div>
    <div class="nav-links">
        <a class="nav-link" href="#">About</a>
        <a class="nav-link" href="#">Experience</a>
        <a class="nav-link" href="#">Projects</a>
        <a class="nav-link" href="#">Skills</a>
        <a class="nav-link" href="#">Education</a>
        <a class="nav-link" href="#">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="badge">✦ Available for opportunities</div>
    <div class="hero-name">Roushan Kumar</div>
    <div class="hero-subtitle">B.Tech CSE Student · Full Stack & AI Enthusiast</div>
    <div class="hero-tags">
        <span class="tag">Python</span>
        <span class="tag">SQL</span>
        <span class="tag indigo">React.js</span>
        <span class="tag indigo">HTML5 / CSS3</span>
        <span class="tag">Streamlit</span>
        <span class="tag">Machine Learning</span>
    </div>
    <div class="hero-desc">
        Passionate about building real-world solutions through code. Combining full stack skills
        with AI/ML knowledge to create applications that are both functional and impactful.
        Always learning, always shipping.
    </div>
    <div class="hero-stats">
        <div class="stat">
            <div class="stat-num">5+</div>
            <div class="stat-label">Projects Built</div>
        </div>
        <div class="stat">
            <div class="stat-num">4+</div>
            <div class="stat-label">Certifications</div>
        </div>
        <div class="stat">
            <div class="stat-num">2027</div>
            <div class="stat-label">Graduating</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── ABOUT ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-tag">01 — About</div>
    <div class="section-title">Who I Am</div>
    <div class="section-sub">
        Hello! I'm Roushan Kumar, pursuing B.Tech in Computer Science at Shobhit Institute of
        Engineering & Technology, Meerut. I love turning ideas into real applications.
    </div>
    <div class="two-col">
        <div class="card">
            <div class="card-title" style="margin-bottom:12px">💻 Development</div>
            <div class="card-body">HTML5, CSS3, JavaScript, React.js, Python, Streamlit — building
            full-stack apps and data-driven tools that solve real problems.</div>
        </div>
        <div class="card">
            <div class="card-title" style="margin-bottom:12px">🤖 AI & Data</div>
            <div class="card-body">Machine Learning, Prompt Engineering, Data Science Methodology —
            exploring intelligent systems and data-powered applications.</div>
        </div>
        <div class="card">
            <div class="card-title" style="margin-bottom:12px">🎯 Focus Areas</div>
            <div class="card-body">Full Stack Development · AI/ML Integration · Open Source
            contributions · Building projects that matter.</div>
        </div>
        <div class="card">
            <div class="card-title" style="margin-bottom:12px">📍 Location</div>
            <div class="card-body">Based in Meerut, UP. Open to remote collaborations, internships,
            and full-time opportunities in tech.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── EXPERIENCE ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="section section-alt">
    <div class="section-tag">02 — Experience</div>
    <div class="section-title">What I've Done</div>
    <div class="section-sub">Roles, contributions, and milestones across academia and industry.</div>

    <div class="card">
        <div class="card-header">
            <div>
                <div class="card-title">Virtual Internship — Artificial Intelligence</div>
                <div class="card-org">PBEL · Equivalent to Virtual Internship</div>
            </div>
            <span class="card-status" style="background:rgba(129,140,248,0.12);color:#818cf8;border-color:rgba(129,140,248,0.3)">✓ Completed</span>
        </div>
        <div class="card-body">
            Completed an AI-focused virtual internship covering machine learning fundamentals,
            AI tools, and practical project work. Earned certification on completion.
        </div>
    </div>

    <div class="card">
        <div class="card-header">
            <div>
                <div class="card-title">Open Source Contributor</div>
                <div class="card-org">GitHub · Personal & Collaborative Projects</div>
            </div>
            <span class="card-status">● Active</span>
        </div>
        <div class="card-body">
            Actively building and maintaining projects on GitHub. Contributing to the open
            source community through utilities, web apps, and AI integrations.
        </div>
    </div>

    <div class="card">
        <div class="card-header">
            <div>
                <div class="card-title">Academic Project Lead</div>
                <div class="card-org">Shobhit Institute of Engineering & Technology, Meerut</div>
            </div>
            <span class="card-status">● Ongoing</span>
        </div>
        <div class="card-body">
            Leading and collaborating on academic projects involving web development, 
            Python scripting, and data analysis as part of the B.Tech curriculum.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── PROJECTS ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-tag">03 — Projects</div>
    <div class="section-title">What I've Built</div>
    <div class="section-sub">A selection of projects that showcase my skills in web development, Python, and AI.</div>

    <div class="two-col">

        <div class="project-card">
            <div class="project-title">🤖 AI Chatbot with Streamlit</div>
            <div class="project-desc">
                An interactive AI-powered chatbot built with Streamlit and integrated with a language model API.
                Features chat history, custom personas, and a clean dark-themed UI.
            </div>
            <div class="project-stack">
                <span class="stack-pill">Python</span>
                <span class="stack-pill">Streamlit</span>
                <span class="stack-pill">OpenAI API</span>
                <span class="stack-pill">REST API</span>
            </div>
            <div class="project-links">
                <a class="proj-link" href="https://github.com/Roushan2006" target="_blank">🐙 GitHub</a>
            </div>
        </div>

        <div class="project-card">
            <div class="project-title">📊 Student Result Management System</div>
            <div class="project-desc">
                A Python + SQL based system for managing student academic records.
                Supports CRUD operations, grade calculation, and report generation with
                a simple CLI interface.
            </div>
            <div class="project-stack">
                <span class="stack-pill">Python</span>
                <span class="stack-pill">MySQL</span>
                <span class="stack-pill">SQL</span>
            </div>
            <div class="project-links">
                <a class="proj-link" href="https://github.com/Roushan2006" target="_blank">🐙 GitHub</a>
            </div>
        </div>

        <div class="project-card">
            <div class="project-title">🌐 Personal Portfolio Website</div>
            <div class="project-desc">
                A responsive personal portfolio built with HTML5, CSS3, and JavaScript.
                Includes animated sections, project showcase, skills display, and a contact form.
                Deployed on GitHub Pages.
            </div>
            <div class="project-stack">
                <span class="stack-pill">HTML5</span>
                <span class="stack-pill">CSS3</span>
                <span class="stack-pill">JavaScript</span>
                <span class="stack-pill">GitHub Pages</span>
            </div>
            <div class="project-links">
                <a class="proj-link" href="https://github.com/Roushan2006" target="_blank">🐙 GitHub</a>
            </div>
        </div>

        <div class="project-card">
            <div class="project-title">🔢 DSA Visualizer</div>
            <div class="project-desc">
                An interactive web-based tool to visualize common Data Structures and Algorithms —
                sorting algorithms, linked lists, stacks & queues — with step-by-step animations
                to aid learning.
            </div>
            <div class="project-stack">
                <span class="stack-pill">JavaScript</span>
                <span class="stack-pill">HTML5</span>
                <span class="stack-pill">CSS3</span>
            </div>
            <div class="project-links">
                <a class="proj-link" href="https://github.com/Roushan2006" target="_blank">🐙 GitHub</a>
            </div>
        </div>

        <div class="project-card">
            <div class="project-title">📈 Data Analysis Dashboard</div>
            <div class="project-desc">
                A Streamlit dashboard for exploratory data analysis. Upload any CSV, get instant
                charts, summary stats, correlation heatmaps, and export-ready reports.
            </div>
            <div class="project-stack">
                <span class="stack-pill">Python</span>
                <span class="stack-pill">Streamlit</span>
                <span class="stack-pill">Pandas</span>
                <span class="stack-pill">Matplotlib</span>
            </div>
            <div class="project-links">
                <a class="proj-link" href="https://github.com/Roushan2006" target="_blank">🐙 GitHub</a>
            </div>
        </div>

        <div class="project-card">
            <div class="project-title">🧠 ML Model Trainer (No-Code)</div>
            <div class="project-desc">
                A no-code machine learning app where users upload a dataset, select a target
                column, choose an ML algorithm, and get a trained model with accuracy metrics
                — all without writing a single line of code.
            </div>
            <div class="project-stack">
                <span class="stack-pill">Python</span>
                <span class="stack-pill">Scikit-learn</span>
                <span class="stack-pill">Streamlit</span>
                <span class="stack-pill">Pandas</span>
            </div>
            <div class="project-links">
                <a class="proj-link" href="https://github.com/Roushan2006" target="_blank">🐙 GitHub</a>
            </div>
        </div>

    </div>
</div>
""", unsafe_allow_html=True)

# ── SKILLS ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section section-alt">
    <div class="section-tag">04 — Skills</div>
    <div class="section-title">My Toolkit</div>
    <div class="section-sub">Technical and AI skills built through coursework, personal projects, and hands-on exploration.</div>

    <div class="three-col">
        <div class="skill-group">
            <div class="skill-group-title">🌐 Frontend</div>
            <div class="skill-pills">
                <span class="pill">HTML5</span><span class="pill">CSS3</span>
                <span class="pill">JavaScript</span><span class="pill">React.js</span>
            </div>
        </div>
        <div class="skill-group">
            <div class="skill-group-title">💻 Languages</div>
            <div class="skill-pills">
                <span class="pill">Python</span><span class="pill">C</span>
                <span class="pill">C++</span><span class="pill">Java</span>
                <span class="pill">SQL</span>
            </div>
        </div>
        <div class="skill-group">
            <div class="skill-group-title">🛠️ Frameworks & Tools</div>
            <div class="skill-pills">
                <span class="pill">Streamlit</span><span class="pill">Pandas</span>
                <span class="pill">Scikit-learn</span><span class="pill">Git</span>
                <span class="pill">GitHub</span><span class="pill">VS Code</span>
            </div>
        </div>
        <div class="skill-group">
            <div class="skill-group-title">📐 CS Concepts</div>
            <div class="skill-pills">
                <span class="pill">OOP</span><span class="pill">DSA</span>
                <span class="pill">Arrays</span><span class="pill">Linked Lists</span>
                <span class="pill">Stacks</span><span class="pill">Queues</span>
                <span class="pill">MySQL</span>
            </div>
        </div>
        <div class="skill-group">
            <div class="skill-group-title">🤖 AI & Data</div>
            <div class="skill-pills">
                <span class="pill">Machine Learning</span>
                <span class="pill">Prompt Engineering</span>
                <span class="pill">AI Literacy</span>
                <span class="pill">Design Thinking</span>
                <span class="pill">Data Analysis</span>
            </div>
        </div>
        <div class="skill-group">
            <div class="skill-group-title">🏆 Certifications</div>
            <div class="skill-pills">
                <span class="pill">Data Science Methodology</span>
                <span class="pill">YUVA AI For All</span>
                <span class="pill">PBEL AI Internship</span>
                <span class="pill">Design Thinking</span>
                <span class="pill">Python</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── EDUCATION ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="section">
    <div class="section-tag">05 — Education</div>
    <div class="section-title">Academic Journey</div>
    <div class="section-sub">Building a strong foundation in Computer Science and beyond.</div>

    <div class="edu-card">
        <div class="edu-year">2023 – 2027</div>
        <div class="edu-content">
            <div class="edu-degree">Bachelor of Technology (B.Tech)</div>
            <div class="edu-field">Computer Science Engineering</div>
            <div class="edu-inst">Shobhit Institute of Engineering & Technology, Meerut</div>
        </div>
    </div>
    <div class="edu-card">
        <div class="edu-year">2022 – 2023</div>
        <div class="edu-content">
            <div class="edu-degree">Senior Secondary — 12th Grade</div>
            <div class="edu-field">Physics, Chemistry & Mathematics (PCM)</div>
            <div class="edu-inst">S.N.S.R.K.S College, Saharsa</div>
        </div>
    </div>
    <div class="edu-card">
        <div class="edu-year">2021 – 2022</div>
        <div class="edu-content">
            <div class="edu-degree">Secondary School — 10th Grade</div>
            <div class="edu-field">General</div>
            <div class="edu-inst">Utkramit Madhyamik Vidyalay Dhanupura, Saharsa</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── CONTACT ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="contact-section">
    <div class="section-tag" style="text-align:center">06 — Contact</div>
    <div class="section-title" style="text-align:center">Let's Connect</div>
    <div class="section-sub" style="text-align:center;margin:0 auto;">
        Open to internships, collaborations, and conversations about tech and building cool things.
    </div>
    <div class="contact-grid">
        <a class="contact-btn" href="mailto:roushan60000@gmail.com">✉ Mail me</a>
        <a class="contact-btn" href="https://www.linkedin.com/in/roushan-kumar-aa9a1a293" target="_blank">💼 LinkedIn</a>
        <a class="contact-btn" href="https://github.com/Roushan2006" target="_blank">🐙 GitHub</a>
    </div>
</div>
<div style="text-align:center;padding:28px;color:#4a4a6a;font-size:13px;border-top:1px solid #2a2a3a;">
    Designed & built with ❤️ · Roushan Kumar © 2026
</div>
""", unsafe_allow_html=True)