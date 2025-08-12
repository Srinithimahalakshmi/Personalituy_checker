
#  Personality Checker (Elastic Net Regression)

##  Overview
A **Personality Checker** system that predicts key personality traits using **Elastic Net Regression**—a hybrid of Lasso and Ridge regularization. Leveraging behavioral, demographic, and survey data, this project offers preprocessing, modeling, and evaluation for accurate trait prediction.

---

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📬 Contact](#-contact)  

---

##  Installation
```bash
git clone https://github.com/Srinithimahalakshmi/Personalituy_checker.git
cd Personalituy_checker

python3 -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate
pip install -r requirements.txt
````

---

## Usage

1. Launch the Jupyter notebook for an end-to-end walkthrough of training and evaluation:

   ```bash
   jupyter notebook model_training.ipynb
   ```
2. To make interactive predictions via the web interface:

   ```bash
   python app.py
   ```

   Visit **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser to explore.

---

## Project Structure

```text
Personalituy_checker/
├── personality_synthetic_dataset.csv    # Dataset
├── model_training.ipynb                 # Notebook for data prep & modeling
├── elasticnet_model.joblib              # Trained Elastic Net model
├── label_encoder.joblib                 # Encoder for categorical features
├── app.py                               # Flask web app
├── templates/
│   └── index.html                       # UI template
├── static/
│   └── style.css                        # Frontend styling
├── requirements.txt                     
└── README.md                            
```

---

## Results

* Predict personality traits such as Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism.
* Visual performance metrics and error analysis provided within the notebook and accessible via the app interface.

---

## Contributing

Your contributions are welcome! You can help by:

* Improving data preprocessing or feature engineering
* Exploring other regression models or ensembled methods
* Enhancing UI with richer visual feedback
* Expanding evaluation metrics and validation approaches

To contribute:

1. Fork the repository
2. Create a branch: `git checkout -b feature/YourFeature`
3. Make changes and commit: `git commit -m "Add feature description"`
4. Push and open a Pull Request

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com](mailto:srinithiarumugam2003@gmail.com)
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

⭐ *If you find this project useful or enlightening, please consider giving it a star!*


```
