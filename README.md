# 🐾 Animals Data Pipeline

A **FastAPI pipeline** that fetches, transforms, and posts animal data from an external Docker API.  

- **Single endpoint:** `/animals/pipeline/run`  
  This endpoint runs the complete pipeline: fetch → transform → post.

---

## 🗂 API Path

- **Run full pipeline:**  
`POST /animals/pipeline/run`  

This endpoint will automatically fetch all animals, transform the fields, and post them in batches to the external API.

---

## ⚙️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/salmanakhtar57/Animals-Data-Pipeline.git
cd Animals-Data-Pipeline
```

2. **Create a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**

- **Windows:**  
```bash
venv\Scripts\activate
```

- **Linux / MacOS:**
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Start FastAPI server**
```bash
python -m app.main
```

6. **Open Swagger UI**
```bash
http://127.0.0.1:8000/docs
```

7. **Run the pipeline**
```bash
Click POST /animals/pipeline/run → Try it out → Execute.
```
The endpoint will:

- Fetch all animals from the Docker API (paginated).

- Transform friends to an array and born_at to ISO8601 UTC timestamp.

- Post animals in batches of 100 to the API endpoint.
