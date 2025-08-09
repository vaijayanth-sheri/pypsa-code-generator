# ⚡ PyPSA Code Generator Dashboard

**A modular, no-code interface for configuring and generating PyPSA component scripts**  
*Built with Python, Streamlit, and Jinja2 — designed for energy professionals, researchers, and students.*

---

## 📌 Overview

The **PyPSA Code Generator Dashboard** is an open-source, Streamlit-based tool that enables users to visually configure **PyPSA** (Python for Power System Analysis) components and instantly generate valid, copy-ready Python code blocks — without writing any scripts manually.

It supports both **Basic** and **Advanced** modes, making it equally valuable for beginners exploring power system modeling and experts working on complex network setups.

---

## 🎯 Key Features

- **Tabbed Component Workflow** — configure all major PyPSA elements:
  - Bus
  - Load
  - Generator
  - StorageUnit
  - Line
  - Link
  - Transformer
  - Carrier
- **Basic & Advanced Modes** — choose between essential fields or full parameter control.
- **Instant Code Preview** — generated Python code displayed in real time.
- **Validation & Error Checking** — ensures parameters are complete and technically correct.
- **Tooltips & Documentation Links** — embedded guidance and direct access to official PyPSA docs.
- **Lightweight & Portable** — works locally or deployable to cloud platforms.

---

## 🛠️ Tech Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/)  
- **Backend:** Python 3.x  
- **Template Engine:** Jinja2  
- **Framework:** [PyPSA](https://pypsa.readthedocs.io/en/stable/)  
- **Version Control:** Git, GitHub

---

## 📂 Project Structure
```bash 
├── main.py           # Main application entry point
├── components/       # UI modules for each PyPSA component
├── utils/            # Helper functions, template rendering, validation
├── templates/        # Jinja2 templates for code generation
├── data/             # Sample input data (if any)
├── outputs/          # Generated code or files
├── .streamlit/       # Streamlit configuration
├── requirements.txt  # Python dependencies
├── README.md         # Project documentation
└── .gitignore        # Ignored files and folders
```
---

## 🚀 Getting Started

1️⃣ Clone the repository
```bash
git clone https://github.com/vaijayanth-sheri/pypsa-code-generator.git
cd pypsa-code-generator
```
2️⃣ Create a virtual environment
```bash
python -m venv venv
```
Activate it:

Windows (PowerShell)
```bash
venv\Scripts\activate
```
Mac/Linux
```bash
source venv/bin/activate
```
3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Run the app
```bash
streamlit run main.py
```
## 📸 Screenshots
---

## 📖 Usage
1. Select the component tab (e.g., Generator, Bus, Line, etc.).
2. Enter parameters — choose Basic or Advanced mode.
3. Validate inputs — errors will appear if required fields are missing.
4. Click Show Code to view the generated PyPSA Python script.
5. Copy the code and paste it into your PyPSA project or save it for later use.

## 🌱 Future Improvements
- YAML/CSV export for full PyPSA networks.
- Multi-component integration previews.
- PyPSA version selection.
- Pre-configured examples for common energy systems.

## 🤝 Contributing
Contributions are welcome!
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a pull request

## 📜 License
This project is licensed under the MIT License — you are free to use, modify, and distribute it.

## 📚 References
- PyPSA Official Documentation
- PyPSA Handbook: Integrated Power System Analysis and Renewable Energy Modeling by Neeraj Dhanraj Bokde & Carlo Fanara
- Streamlit Documentation

Author: Vaijayanth Sheri

Contact: Sheri.vaijayanth@gmail.com

Linkedin: https://www.linkedin.com/in/vaijayanth-sheri/


