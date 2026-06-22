# AI Software Compiler

A multi-stage pipeline for converting natural language prompts into structured configurations.

## Structure

- **backend/** - Python processing engine with FastAPI
- **frontend/** - React.js user interface

## Getting Started

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```