# NeuroFlow

🏫 **School team project** for **INFOMATRIX World** — web platform with authentication, forum, and AI chat.

> Built by high school students during the INFOMATRIX international hackathon. A modern web frontend with Node.js auth backend and Python AI experiments.

---

## 👥 Team

| Name | Role |
|------|------|
| **[Ivan Gaidarov](https://github.com/IVNsell)** | Full-Stack Developer |
| **Kirill Lypenko** | Team member |
| **Ksenia Gubenko** | Team member |

*We participated as a **school student team** at INFOMATRIX World.*

---

## Overview

NeuroFlow is a full-stack web platform developed by **three high school students** as a **team hackathon project** for the [INFOMATRIX World](https://www.infomatrix.ro/) competition.

The project includes a landing website, user authentication, community forum, and AI chat integration.

**INFOMATRIX** is an international competition for school and university students in IT, programming, and innovation. World Finals are held annually in Bucharest, Romania.

---

## Features

### 🌐 Web Platform (`Site_JS/`)
- Responsive landing pages (Bootstrap template)
- About, Features, Services, Pricing sections
- Forum with likes/dislikes (`Lypenko/forum.html`)
- User authentication flow

### 🔐 Authentication (`Site_JS/Login/`)
- Sign up / Login pages
- **Google OAuth 2.0** via Passport.js
- Express session management
- Cookie-based user state

### 💬 Community Forum
- Post messages (auth required)
- Like / dislike reactions per message
- Real-time message loading via REST API
- JSON-based message storage

### 🤖 AI Integration (`Python/`)
- Ollama + DeepSeek Coder integration
- Streaming LLM responses
- Experimental AI chat backend

---

## Tech Stack

| Part | Technologies |
|------|-------------|
| Frontend | HTML, CSS, JavaScript, Bootstrap |
| Auth Backend | Node.js, Express, Passport.js, Google OAuth 2.0 |
| Data | JSON files (`base_date/messages.json`, `users.json`) |
| AI | Python, Ollama (deepseek-coder) |
| Sessions | express-session, cookie-session |

---

## Project Structure
