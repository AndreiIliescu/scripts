# Python Scripts Collection

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.14-blue)

A collection of Python scripts built while learning Python. Each script is standalone and focuses on a specific concept or real-world use case, ranging from basic CLI tools to real-time AI object detection using YOLOv5.

---

## Table of Contents

- [About](#about)
- [Scripts Overview](#scripts-overview)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About

This repository contains Python scripts and small backend applications built while learning Python. Each project focuses on a specific concept such as object oriented programming, CLI utilities, external APIs, backend development with FastAPI, and AI model integration.

The goal is to build practical programs that demonstrate real world use cases instead of isolated exercises.

---

## Scripts Overview

| Script | Description |
|---|---|
| `calculator.py` | CLI calculator supporting addition, subtraction, multiplication, division, and exponentiation |
| `password_generator.py` | Generates a random password based on a user-defined number of letters, numbers, and symbols |
| `currency_convertor.py` | Converts between currencies using live exchange rates via the `CurrencyConverter` library |
| `unit_convertor.py` | Converts values across length, volume, and mass units (metric and imperial) |
| `areas_and_perimeters.py` | OOP-based module that calculates areas and perimeters for squares, rectangles, and circles |
| `qr_code_generator.py` | Generates a QR code from any string and saves it as both SVG and PNG |
| `rock_paper_scissors_game.py` | CLI game of Rock, Paper, Scissors against the computer |
| `youtube_downloader.py` | Downloads YouTube videos to the Desktop in the best available quality using `yt-dlp` |
| `tiktok_downloader.py` | Downloads TikTok videos without watermark using the TikWM public API |
| `ai_object_recognition_project/ai_object_recognition.py` | Real-time object detection via webcam using YOLOv5 and OpenCV |
| `fast_api_backend_from_scratch/main.py` | Simple REST API built with FastAPI supporting item creation, listing, and retrieval |
| `gemini_integration_app/app.py` | CLI chat application that integrates Google's Gemini 2.5 Flash model |

---

## Tech Stack

- Python 3.14.2
- FastAPI
- Uvicorn
- Pydantic
- OpenCV 4.13.0.92
- Ultralytics YOLOv5
- yt-dlp
- CurrencyConverter
- PyQRCode
- Requests
- python-dotenv
- Google GenAI SDK

---

## Getting Started

### Prerequisites

- Python 3.11+
- pip
- A webcam (required only for `ai_object_recognition.py`)
- Git

### Installation

1. Clone the repository:

```bash
git clone https://github.com/AndreiIliescu/scripts.git
cd scripts
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows - CMD
.\.venv\Scripts\activate

# Windows - PowerShell
.\.venv\Scripts\activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Each script runs independently. Navigate to the project root and run the script you want.

**Calculator:**

```bash
python calculator.py
```

**Password Generator:**

```bash
python password_generator.py
```

**Currency Converter:**

```bash
python currency_convertor.py
```

**Unit Converter:**

```bash
python unit_convertor.py
```

**QR Code Generator:**

```bash
python qr_code_generator.py
```

Saves `myqrcode.svg` and `myqrcode.png` in the current directory.

**Rock, Paper, Scissors:**

```bash
python rock_paper_scissors_game.py
```

**YouTube Downloader:**

```bash
python youtube_downloader.py
```

Downloads the video to your Desktop.

**TikTok Downloader:**

```bash
python tiktok_downloader.py
```

Saves `tiktok_video_without_watermark.mp4` in the current directory.

**AI Object Recognition (requires webcam):**

```bash
python ai_object_recognition_project/ai_object_recognition.py
```

Press `Q` to stop the webcam feed.

**FastAPI Backend**

```bash
uvicorn fast_api_backend_from_scratch.main:app --reload
```

Start the local development server

```bash
http://127.0.0.1:8000/docs
```

Open the interactive API documentation

```bash
curl -X POST "http://127.0.0.1:8000/items?text=apple"

curl -X GET "http://127.0.0.1:8000/items"

curl -X GET "http://127.0.0.1:8000/items/0"
```

Example requests

**Gemini Chat Integration**

```bash
API_KEY=your_gemini_api_key_here
```

Create a `.env` file and add your API key

```bash
python gemini_integration_app/app.py
```

Run the application

Type `q` to exit the chat session

---

## Project Structure

```
scripts/
├── ai_object_recognition_project/
│   └── ai_object_recognition.py
├── fast_api_backend_from_scratch/
│   ├── main.py
│   └── running_commands.txt
├── gemini_integration_app/
│   ├── app.py
│   ├── .env.example
│   └── .env
├── areas_and_perimeters.py
├── calculator.py
├── currency_convertor.py
├── password_generator.py
├── qr_code_generator_project/
│   └── qr_code_generator.py
├── rock_paper_scissors_game.py
├── tiktok_downloader_project/
│   └── tiktok_downloader.py
├── unit_convertor.py
├── youtube_downloader.py
├── requirements.txt
├── runtime.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add feature X"`
4. Push the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

Andrei Iliescu

[![Email Outlook](https://img.shields.io/badge/Outlook-andrei.iliescu13102000%40outlook.com-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white)](mailto:andrei.iliescu13102000@outlook.com)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Andrei_Iliescu-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/andrei-iliescu-aa7910214)

[![GitHub](https://img.shields.io/badge/GitHub-Andrei_Iliescu-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AndreiIliescu)