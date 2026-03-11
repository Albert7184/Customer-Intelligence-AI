# 🤖 AI Customer Intelligence Platform

An end-to-end **Customer Analytics & AI Intelligence Platform** built with Machine Learning and Streamlit.

This project analyzes customer purchasing behavior, automatically segments customers, predicts churn risk, and provides business insights through an interactive dashboard.

The platform helps companies **make data-driven marketing decisions** and understand their customers more deeply.

---

# 🚀 Demo

AI Dashboard includes:

• Customer Segmentation  
• AutoML Model Comparison  
• Churn Prediction  
• Global Customer Analytics  
• AI Business Insights  

Built with an interactive **Streamlit dashboard**.

---

# 📊 Project Architecture


Raw Dataset
↓
Data Cleaning
↓
Feature Engineering (RFM)
↓
Customer Segmentation (K-Means)
↓
Churn Prediction Model
↓
Model Evaluation
↓
AI Business Insights
↓
Interactive Dashboard


---

# 🧠 Machine Learning Features

### Customer Segmentation

Customers are segmented using **K-Means clustering** based on **RFM analysis**.

RFM variables:

| Metric | Meaning |
|------|------|
Recency | Days since last purchase |
Frequency | Number of purchases |
Monetary | Total money spent |

Customer segments:

• VIP Customers  
• Loyal Customers  
• At Risk Customers  
• Normal Customers

---

### 🤖 AutoML Model Comparison

The system automatically compares multiple ML models for **churn prediction**.

Models used:

• Logistic Regression  
• Random Forest

The dashboard automatically selects the **best performing model**.

---

### 🌍 Global Customer Analytics

Interactive **world map visualization** showing customer distribution across countries.

Helps businesses identify:

• high-value markets  
• international demand patterns

---

### 💡 AI Business Insights

The system automatically generates insights such as:

• Focus marketing campaigns on high-value customers  
• Retarget inactive customers  
• Improve retention strategies  

---

# 📁 Project Structure


Customer-Intelligence-AI
│
├── dashboard
│ ├── dashboard.py
│ └── style.css
│
├── data
│ └── Online Retail.xlsx
│
├── models
│
├── src
│ ├── data_cleaning.py
│ ├── feature_engineering.py
│ ├── clustering.py
│ ├── cluster_optimization.py
│ └── churn_prediction.py
│
├── requirements.txt
├── README.md


---

# ⚙️ Installation

Clone the repository


git clone https://github.com/Albert7184/Customer-Intelligence-AI.git


Navigate to project folder


cd Customer-Intelligence-AI


Create virtual environment


python -m venv venv


Activate environment

Windows:


venv\Scripts\activate


Mac/Linux:


source venv/bin/activate


Install dependencies


pip install -r requirements.txt


---

# ▶️ Run the Dashboard

Start the Streamlit application


streamlit run dashboard/dashboard.py


Open your browser


http://localhost:8501


You will see the **AI Customer Intelligence Dashboard**.

---

# 📂 Dataset Format

The system expects a dataset with these columns:

| Column | Description |
|------|------|
CustomerID | Unique customer identifier |
InvoiceNo | Transaction ID |
InvoiceDate | Purchase date |
Quantity | Product quantity |
UnitPrice | Product price |
Country | Customer location |

Example:

CustomerID , InvoiceNo , InvoiceDate , Quantity , UnitPrice , Country
17850         536365     2010-12-01    6          2.55        United Kingdom


Users can upload datasets directly in the dashboard.

Supported formats:

• CSV  
• Excel (.xlsx)

---

# 🏢 Business Applications

This platform helps companies:

### Customer Segmentation
Identify high-value customers.

### Marketing Optimization
Create targeted marketing campaigns.

### Churn Prediction
Detect customers likely to stop purchasing.

### Revenue Growth
Focus on high-spending customer segments.

---

# 🛠 Technology Stack

### Programming

Python

### Data Processing

• pandas  
• numpy  

### Machine Learning

• scikit-learn  

### Visualization

• plotly  
• matplotlib  
• seaborn  

### Dashboard

• streamlit  

---

# 📈 Future Improvements

Possible upgrades:

• Customer Lifetime Value prediction  
• Recommendation System  
• AI Chat with dataset  
• Real-time analytics pipeline  
• Cloud deployment  

---

# ☁️ Deployment

The project can be deployed on:

• Streamlit Cloud  
• AWS  
• Google Cloud  
• Docker  

---

# 👨‍💻 Author

Albert

AI / Data Science Portfolio Project

Focus areas:

• Machine Learning  
• Customer Analytics  
• AI Product Development  

---

# ⭐ If you find this project useful

Consider giving it a **star** on GitHub.