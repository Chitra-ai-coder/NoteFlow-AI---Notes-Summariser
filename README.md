# NoteFlow AI - Intelligent Study Companion 🧠✨
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=FastAPI&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)
![Groq](https://img.shields.io/badge/Powered%20by-Groq-f55036?style=flat)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**NoteFlow AI** is a premium, AI-powered web application designed to accelerate the learning process. It instantly transforms unstructured educational materials—such as massive textbook PDFs or messy lecture transcripts—into perfectly structured executive summaries and active-recall flashcards. 

Built with a stunning, Apple-inspired glassmorphism UI, NoteFlow AI leverages the blazing-fast inference speeds of **Groq** and **Llama 3** to deliver a zero-latency study preparation experience.

---

## ✨ Key Features

*   **📄 Seamless Data Ingestion:** Drag-and-drop PDF uploads (up to 50MB) or manual text pasting.
*   **⚡ Zero-Latency AI Synthesis:** Powered by Groq's LPU inference engine for instant text comprehension and entity extraction.
*   **🧠 Interactive Mastery:** Automatically generates a digestible "Executive Summary" and an interactive grid of Q&A flashcards optimized for spaced repetition.
*   **🖨️ Print-Optimized PDF Export:** A highly customized `html2pdf.js` implementation that builds a clean, hidden 8.5x11 print-ready document in the background. This ensures your downloaded study guides are perfectly formatted and flashcards are never sliced in half.
*   **🎨 Premium Glassmorphism UI:** A fully responsive Single Page Application (SPA) utilizing a Bento-box dashboard layout, 3D color-graded glass panels, dynamic parallax scrolling, and dual-font typography (Outfit & Inter).

---

## 🛠️ Technology Stack

### **Frontend**
*   **HTML5 & Vanilla JavaScript**: For a lightweight, ultra-fast Single Page Application (SPA).
*   **Tailwind CSS**: For rapid, utility-first styling and responsive design.
*   **html2pdf.js**: For client-side PDF generation using raw HTML string injection.
*   **Google Fonts**: `Outfit` for modern headings and `Inter` for highly readable body text.

### **Backend**
*   **Python 3.x**: Core backend logic.
*   **FastAPI**: High-performance asynchronous web framework serving the API.
*   **Groq API**: Utilizing the **Llama 3 70B** model for advanced reasoning and summarization.
*   **PyPDF2 / pdfplumber**: For extracting raw text from user-uploaded PDF files.

---

## 📂 Project Architecture & File Structure

```text
noteflow-ai/
│
├── frontend/
│   └── index.html          # The complete Single Page Application (SPA).
│                           # Contains Tailwind styling, glassmorphism CSS, 
│                           # UI interactions, and PDF generation logic.
│
├── backend/
│   ├── main.py             # FastAPI entry point. Defines the API routes.
│   ├── ai_engine.py        # Logic for connecting to Groq and prompting.
│   ├── pdf_parser.py       # Helper functions to extract text from PDFs.
│   ├── requirements.txt    # Python dependencies (fastapi, uvicorn, groq, etc.)
│   └── .env                # Environment variables (e.g., GROQ_API_KEY)
│
├── .gitignore              # Ignores __pycache__, .env, and virtual environments.
└── README.md               # Project documentation (this file).
```

### 🧠 How it Works (The Data Flow)

1. **Upload**: The user uploads a PDF on the frontend.
2. **API Request**: The frontend sends the file via a `multipart/form-data` POST request to the FastAPI backend.
3. **Extraction & Truncation**: The backend extracts the text from the PDF and safely truncates it to ~25,000 characters to stay within optimal API token limits.
4. **AI Generation**: The text is sent to the Groq API with a strict system prompt to return a JSON object containing a `summary` and an array of `flashcards`.
5. **Rendering**: The frontend receives the JSON, dynamically builds the DOM elements, and applies the slide-up animations for the user to review.

---

## 🚀 Getting Started

Follow these steps to get a local development environment up and running.

### 1. Prerequisites
*   **Python 3.8+** installed.
*   A free API key from the **Groq Console**.

### 2. Backend Setup
Clone the repository and set up the Python environment:

```bash
git clone [https://github.com/Chitra-ai-coder/NoteFlow-AI---Notes-Summariser.git](https://github.com/Chitra-ai-coder/NoteFlow-AI---Notes-Summariser.git)
cd NoteFlow-AI---Notes-Summariser/backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Start the FastAPI server:

```bash
uvicorn main:app --reload --port 8000
```
*The backend will now be listening for requests at `http://127.0.0.1:8000`.*

### 3. Frontend Setup
Because the frontend is a pure HTML/JS file using CDNs, no Node.js or npm installation is required!

1. Open a new terminal window and navigate to the frontend folder:
```bash
cd ../frontend
```
2. Open `index.html` in your web browser to view the application. *(Note: For the best development experience and to avoid CORS issues with local files, use an extension like **Live Server** in VS Code).*

---

## 🔌 Main API Endpoint

### `POST /api/generate-notes`
Accepts a PDF file or a raw text string and returns an AI-generated study guide.

**Request Form Data:**
*   `file` (File, optional): The uploaded PDF document.
*   `pasted_text` (String, optional): Raw text input.

**Response (JSON):**
```json
{
  "summary": "<p>A structured HTML paragraph summarizing the text...</p>",
  "flashcards": [
    {
      "q": "What is horizontal scaling?",
      "a": "Adding more machines or servers to handle increased load."
    }
  ]
}
```

---

## 🔮 Future Enhancements
*   **Authentication:** Add user login to save historical study guides to a database.
*   **Markdown Support:** Allow users to edit the generated flashcards before exporting.
*   **PDF Chunking:** Implement sliding-window chunking to process massive 200+ page textbooks without hitting rate limits.

---

## 📝 License
This project is open-source and available under the **MIT License**.
