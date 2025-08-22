# Project Emotion Detector

---

## 🧩 Introduction

This project demonstrates the end-to-end development of a **machine learning-powered web application**, including:

* **Backend development** with Flask.
* **Frontend integration** with HTML, JavaScript, and Flask templates.
* **Deployment using Docker** for easy portability.
* **Unit testing** to ensure the reliability of the emotion detection logic.

The project leverages **IBM Watson’s embeddable AI services** to extract emotions from user-provided text.

Unlike traditional sentiment analysis (which only identifies polarity: positive, negative, or neutral), **emotion detection** captures more **fine-grained emotions** such as:

* 😊 Joy
* 😢 Sadness
* 😡 Anger
* 😨 Fear
* 🤢 Disgust

Such emotion-aware systems are increasingly important in:

* Customer feedback analytics.
* AI-driven recommendation engines.
* Automated chatbots with empathetic responses.
* Market research and consumer insights.

---

## 🛠️ Technologies Used

### **Backend**

* [Python 3.10+](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/) – lightweight web framework.
* [Requests](https://pypi.org/project/requests/) – HTTP client for Watson API.

### **Frontend**

* HTML5
* CSS3
* JavaScript (AJAX for async communication with backend)

### **DevOps / Deployment**

* [Docker](https://www.docker.com/) – containerization of the application.
* [Docker Compose](https://docs.docker.com/compose/) – orchestration.
* [GitHub Action](https://github.com/features/actions) - CI/CD

### **Testing**

* [unittest](https://docs.python.org/3/library/unittest.html) – Python’s built-in test framework.

---

## 📂 Project Structure

```
final-project-emb-ai/
├── backend/
│   ├── EmotionDetection/
│   │   ├── __init__.py
│   │   └── emotion_detection.py
│   ├── server.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   └── static/
│       └── mywebscript.js
└── docker-compose.yml
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/final-project-emb-ai.git
cd final-project-emb-ai
```

### 2. Run with Docker Compose

```bash
docker-compose up --build
```

### 3. Access the App

Open your browser at 👉 [http://localhost:5000](http://localhost:5000)

---

## 📊 Example Output

For the given input:

```
I am really mad about this
```

The system response is:

```
'anger': 0.85, 'disgust': 0.05, 'fear': 0.03, 'joy': 0.01, 'sadness': 0.06
The dominant emotion is: anger
```

---

## 🏆 Takeaway

This project showcases how **AI + Web Development + Docker** can be combined to deliver a scalable, production-ready solution.

It serves as a strong foundation for:

* Building emotion-aware chatbots.
* Enhancing customer support systems.
* Running analytics on customer feedback at scale.

---

## 📊 Example Output

**Input:**

```
I am really mad about this
```

**System Response:**

```
'anger': 0.85, 'disgust': 0.05, 'fear': 0.03, 'joy': 0.01, 'sadness': 0.06
Dominant emotion: anger
```

**Screenshot of the Web App:**

![Screenshot placeholder](https://via.placeholder.com/800x400?text=Web+App+Screenshot)

<!--**GIF Demonstration:**

![GIF placeholder](https://via.placeholder.com/800x400?text=App+Interaction+GIF)-->

---

```markdown
![Screenshot](images/screenshot1.png)
```
