<div align="center">

<!-- Animated Banner -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=32&duration=3000&pause=1000&color=E63946&center=true&vCenter=true&width=600&lines=🚦+Traffic+Sign+Recognizer;Deep+Learning+%7C+Computer+Vision;Powered+by+MobileNet+%2B+TensorFlow" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-tf--keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.45-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

<br/>

> **AI-powered web app that classifies traffic signs instantly using Deep Learning.**  
> Built with MobileNet + TensorFlow + Streamlit — trained on the GTSRB dataset.

<br/>

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://traffic-sign-recognizer.streamlit.app)

</div>

---

## 🎬 Demo

<div align="center">
<img src="assets/sample_images/00000_00002_00019" alt="Demo" width="700"/>
</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Instant Prediction** | Upload any traffic sign image and get results in milliseconds |
| 📊 **Confidence Charts** | Bar & pie charts showing confidence scores for all classes |
| 🕓 **Prediction History** | Session-based history with stats and CSV export |
| 🌐 **Bilingual UI** | Full Arabic & English support |
| 🎨 **Dark / Light Theme** | Auto-detects system theme |
| ⚡ **Cached Model** | Model loads once and stays in memory across sessions |

---

## 🚦 Supported Classes

| # | Emoji | Sign |
|---|---|---|
| 0 | 🛑 | Stop |
| 1 | ⛔ | No Entry |
| 2 | ➡️ | Keep Right |
| 3 | 🔵 | Speed Limit 20 km/h |
| 4 | 🔵 | Speed Limit 30 km/h |

---

## 🧠 Model Details

```
Architecture  : MobileNet (Google Teachable Machine)
Framework     : TensorFlow 2.16 + tf-keras
Input Size    : 224 × 224 px
Output        : 5-class Softmax
Training Data : ~6,390 images
Dataset       : GTSRB (German Traffic Sign Recognition Benchmark)
Accuracy      : 95%
```

---

## 🗂️ Project Structure

```
traffic-sign-recognizer/
├── 📁 .streamlit/
│   └── config.toml
├── 📁 assets/
│   └── sample_images/
├── 📁 components/
│   ├── __init__.py
│   ├── charts.py        ← Plotly confidence charts
│   ├── predictor.py     ← Model loading & inference
│   ├── sidebar.py       ← Sidebar + bilingual support
│   └── ui.py            ← Shared UI components
├── 📁 core/
│   ├── __init__.py
│   ├── config.py        ← App config & team info
│   └── constants.py     ← CLASS_LABELS, MODEL_PATH
├── 📁 model/
│   ├── keras_model.h5   ← Trained MobileNet model
│   └── labels.txt
├── 📁 pages/
│   ├── 1_🏠_Home.py
│   ├── 2_🔍_Predict.py
│   ├── 3_📊_Results.py
│   └── 4_ℹ️_About.py
├── 📁 styles/
│   └── main.css
├── 📁 utils/
│   └── image_utils.py
├── app.py               ← Entry point
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1 — Clone the repo

```bash
git clone https://github.com/Goda-Emad/traffic-sign-recognizer-.git
cd traffic-sign-recognizer-
```

### 2 — Install dependencies

```bash
pip install -r requirements.txt
```

### 3 — Run the app

```bash
streamlit run app.py
```

---

## 📦 Requirements

```txt
streamlit==1.45.0
tensorflow==2.16.1
tf-keras
Pillow
numpy
plotly
pandas
h5py
```

---

## 👥 Team

<div align="center">

<table>
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/goda-emad/">
        <img src="https://img.shields.io/badge/Goda%20Emad-Team%20Lead%20%26%20AI%20Developer-E63946?style=for-the-badge&logo=linkedin&logoColor=white"/>
      </a>
    </td>
  </tr>
</table>

<br/>

<table>
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/elia-fahmy/">
        <img src="https://img.shields.io/badge/Elia%20Fahmy-Member-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
      </a>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/in/a-s-abdelbakey/">
        <img src="https://img.shields.io/badge/Ahmed%20Salama-Member-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
      </a>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/in/wafa-ashour/">
        <img src="https://img.shields.io/badge/Alwafa%20Ashour-Member-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
      </a>
    </td>
    <td align="center">
      <a href="https://www.linkedin.com/in/ibrahim-elshafey/">
        <img src="https://img.shields.io/badge/Ibrahim%20Elshafey-Member-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
      </a>
    </td>
  </tr>
</table>

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=4000&pause=1000&color=E63946&center=true&vCenter=true&width=400&lines=Made+with+❤️+by+Goda+Emad+%26+Team;Traffic+Sign+Recognizer+%7C+2026" alt="Footer" />

</div>
