# Data Analysis App

## 📌 Overview
This is a **Streamlit-based Data Analysis App** that allows users to **upload, explore, analyze, and visualize datasets** easily. The app provides multiple functionalities, including:
- Uploading datasets
- Exploring data (shape, columns, statistics, missing values, etc.)
- Viewing value counts of categorical variables
- Performing group-by operations
- Generating various visualizations (line chart, bar chart, scatter plot, etc.)

## 🚀 Features
✅ **Upload Data:** Supports CSV file uploads for analysis.
✅ **Explore Data:** Displays dataset structure, summary statistics, and missing values.
✅ **Value Counts:** Shows frequency distribution of categorical columns.
✅ **Group By:** Performs aggregation operations on selected columns.
✅ **Visualizations:** Generates multiple chart types using Matplotlib and Plotly.

---

## 🏗️ Project Structure
```
📂 DataXplorer
│── main.py                 # Main entry point of the app
│── data_upload.py          # Handles file upload functionality
│── data_exploration.py     # Displays dataset structure and stats
│── value_counts.py         # Shows frequency distribution of categorical data
│── group_by.py             # Performs group-by and aggregation operations
│── visualizations.py       # Generates different types of charts
│── requirements.txt        # Lists required Python dependencies
│── README.md               # Project documentation
```

---

## 🛠️ Installation & Setup
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Danyal-Rana/DataXplorer.git
cd DataXplorer
```

### 2️⃣ **Create Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the App**
```bash
streamlit run main.py
```

---

## 📊 Usage Guide
1️⃣ **Open the app** in a browser once Streamlit starts.
2️⃣ **Navigate using the sidebar** to upload and analyze data.
3️⃣ **Select options** to explore, group, or visualize data.
4️⃣ **Generate plots** using different charting options.

---

## 📦 Dependencies
The app requires the following Python libraries:
- `streamlit`
- `pandas`
- `matplotlib`
- `plotly`

All dependencies are listed in `requirements.txt`.

---

## 📜 License
This project is open-source under the MIT License.

---

## 🤝 Contributing
1. Fork the repository.
2. Create a new branch (`feature/your-feature-name`).
3. Commit your changes and push to your branch.
4. Open a Pull Request.

---

## 📞 Contact
For any issues or suggestions, feel free to reach out!

📧 Email: temp@mdrana.com  
🔗 GitHub: [Your GitHub Profile](https://github.com/Danyal-Rana)