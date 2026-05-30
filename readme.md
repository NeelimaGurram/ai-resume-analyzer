# 🤖 AI Resume Matcher

> An AI-powered resume analyzer that parses resumes, extracts structured data, and matches candidates to job descriptions using NLP and semantic search.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?style=flat-square&logo=fastapi)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=flat-square&logo=openai)
![React](https://img.shields.io/badge/React-18-61DAFB?style=flat-square&logo=react)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange?style=flat-square)

---

## What it does

Upload a resume PDF and the app will:

- Extract contact info, skills, education, experience and projects automatically using GPT
- Score your resume against a job description (ATS-style keyword matching)
- Rank matching jobs using semantic similarity (not just keywords)
- Show you exactly which skills you have vs which ones you're missing
- Generate a tailored cover letter and interview prep questions

---

## Tech stack

| Layer | Technology |
|---|---|
| Frontend | React 18, Vite, Tailwind CSS, shadcn/ui, React Query |
| Backend | Python 3.11, FastAPI, Pydantic v2 |
| AI / NLP | OpenAI GPT-4o-mini, LangChain, Sentence Transformers, spaCy |
| Vector search | FAISS, ChromaDB |
| Database | PostgreSQL, SQLAlchemy 2.0, Alembic |
| Caching | Redis |
| DevOps | Docker, GitHub Actions, Railway, Vercel |

---

## Project structure

```
ai-resume-matcher/
├── backend/
│   ├── main.py              # FastAPI app entry point
│   ├── parser.py            # AI-powered resume parser
│   ├── extractor.py         # PDF text extraction
│   ├── nlp_engine.py        # spaCy NLP logic
│   └── config.py            # Environment settings
├── frontend/
│   └── src/
│       ├── pages/           # Upload, Results, Dashboard
│       └── components/      # UI components
├── data/
│   └── jobs.json            # Seed job descriptions
├── docs/
│   ├── architecture.md
│   └── db-schema.md
├── .env.example
├── docker-compose.yml
└── requirements.txt
```

---

## Getting started

### Prerequisites

- Python 3.11+
- Node.js 18+
- PostgreSQL
- Redis
- OpenAI API key

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ai-resume-matcher.git
cd ai-resume-matcher
```

### 2. Set up the backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set up environment variables

```bash
cp .env.example .env
```

Edit `.env`:

```
OPENAI_API_KEY=your_key_here
DATABASE_URL=postgresql://user:password@localhost/resume_matcher
REDIS_URL=redis://localhost:6379
SECRET_KEY=your_secret_key_here
```

### 4. Run the backend

```bash
uvicorn main:app --reload
```

API is live at `http://localhost:8000`
Swagger docs at `http://localhost:8000/docs`

### 5. Run the frontend

```bash
cd frontend
npm install
npm run dev
```

App is live at `http://localhost:5173`

---

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/upload-resume` | Upload PDF, returns parsed JSON |
| POST | `/ats-score` | Score resume against job description |
| POST | `/match-jobs` | Return ranked job matches |
| POST | `/generate-cover-letter` | Generate tailored cover letter |
| POST | `/interview-prep` | Generate interview questions |
| POST | `/register` | Create account |
| POST | `/login` | Get JWT token |
| GET | `/me` | Current user profile |
| GET | `/matches/{resume_id}` | Match history |

---

## Current progress

- [x] PDF text extraction with pdfplumber
- [x] AI-powered resume parsing with GPT-4o-mini
- [x] Regex contact info extraction
- [ ] FastAPI server setup
- [ ] ATS keyword scoring with spaCy
- [ ] Semantic matching with Sentence Transformers + FAISS
- [ ] PostgreSQL database integration
- [ ] JWT authentication
- [ ] Redis caching
- [ ] React frontend
- [ ] Docker + deployment

---

## How the matching works

```
Resume PDF
    │
    ▼
PDF Text Extraction (pdfplumber)
    │
    ▼
AI Parsing (GPT-4o-mini) ──► structured JSON
    │
    ├──► ATS Score (spaCy keyword match)     weight: 40%
    │
    └──► Semantic Score (Sentence Transformers + FAISS)  weight: 60%
              │
              ▼
         Final Score = 0.4 × ATS + 0.6 × Semantic
              │
              ▼
         Ranked job matches
```

---

## Local development with Docker

```bash
docker-compose up
```

This starts FastAPI + PostgreSQL + Redis together.

---

## Contributing

This project is being built as a learning project. Issues and suggestions welcome.

---

## License

MIT