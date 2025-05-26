# 📈 Sales Predictor

A simple machine learning API built with **FastAPI** to predict sales based on advertising spend.  
The model is trained using a Linear Regression algorithm on dummy sales data.

---

## 🧱 Project Structure

```

sales-predictor/
│
├── app/
│   ├── model.py         # Script to train and save the ML model
│   ├── predictor.py     # Loads the model and runs predictions
│   ├── main.py          # FastAPI app defining API endpoints
│   ├── model.pkl        # Saved ML model (generated after training)
│
├── data/
│   └── sales_data.csv   # Dummy dataset with 1000 rows of advertising & sales data
│
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── .gitignore           # Git ignore rules

````

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- `pip` package manager

### Installation

1. **Clone the repo**

```bash
git clone https://github.com/harryongit/sales-predictor.git
cd sales-predictor
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Train the ML model**

```bash
python app/model.py
```

This loads the CSV data from `data/sales_data.csv`, trains a linear regression model, and saves it as `app/model.pkl`.

4. **Run the FastAPI server**

```bash
uvicorn app.main:app --reload
```

5. **Open the API docs**

Visit the interactive API docs at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

You can test the `/predict` endpoint here by sending JSON like:

```json
{
  "advertising": 250.5
}
```

---

## 📦 API Endpoints

| Method | Endpoint   | Description                                   |
| ------ | ---------- | --------------------------------------------- |
| POST   | `/predict` | Predict sales from advertising budget (float) |

**Response example:**

```json
{
  "advertising_budget": 250.5,
  "predicted_sales": 26.32
}
```

---

## 📊 Dataset

The project uses a dummy dataset with 1000 data points stored in `data/sales_data.csv`.
Each row has:

* `advertising`: Advertising budget in dollars (float)
* `sales`: Sales achieved in dollars (float)

---

## 🛠️ Tools & Libraries Used

* [FastAPI](https://fastapi.tiangolo.com/) — Web framework for the API
* [scikit-learn](https://scikit-learn.org/stable/) — ML model training and prediction
* [pandas](https://pandas.pydata.org/) — Data manipulation
* [uvicorn](https://www.uvicorn.org/) — ASGI server for FastAPI

---

## 💡 Future Improvements

* Add more features (e.g., seasonality, region, product category)
* Use more advanced regression or neural network models
* Add user authentication for API access
* Deploy on cloud services (Heroku, Render, Railway, etc.) with CI/CD pipelines

---

## 📜 License

MIT License — feel free to use and modify!

---

## 👤 Author

Created by [Harry](https://github.com/harryongit)

---

If you want me to help create a GitHub Actions workflow or deploy this API somewhere, just ask!

```

