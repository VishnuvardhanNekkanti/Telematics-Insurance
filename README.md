    # 🚗 Telematics-Based Usage Insurance System

A smart, AI-powered application that uses real-time driver behavior to determine **risk scores**, adjust **insurance premiums**, and provide **personalized safety tips** — all with a modern frontend and intelligent backend.

---

## 🎯 Objective

To build a telematics-based system that:

- Analyzes **driving behavior**
- Computes a **risk score**
- Adjusts **insurance premium** dynamically
- Provides **AI-generated safety suggestions**

---

## 🧠 Features

- 📊 Real-time behavior inputs (speed, braking, night drives, phone usage)
- 💡 Intelligent risk scoring and premium adjustment logic
- 🤖 AI-driven natural language safety recommendations using **Groq API**
- 🎨 Modern UI with **Dark Mode toggle**
- 🔁 Fallback logic when AI API fails
- 🔐 `.env` file support for secure API key management

---

## 🧰 Technologies Used

| Component   | Tech Stack                         |
|------------|-------------------------------------|
| Backend    | Python, Flask, Flask-CORS           |
| AI Layer   | Groq API (free-tier LLM)            |
| Frontend   | HTML, CSS, JavaScript               |
| Secrets    | `.env` via `python-dotenv`          |

---

## 🧾 Requirements

Install the following Python libraries:

```bash
pip install -r requirements.txt


---

## 🚨 Important for Reviewers

Before running the application, please follow these steps:

### 1️⃣ Get a Free API Key (Groq)

- Go to: [https://console.groq.com](https://console.groq.com)
- Sign in or sign up
- Generate your own **Groq API key**

### 2️⃣ Create a `.env` File

In the **root directory** (where `app.py` exists)

