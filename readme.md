# Heart Disease Prediction Web App

**Streamlit · Scikit‑learn · Joblib · Pandas**

A simple web application that predicts the likelihood of heart disease using a trained machine learning pipeline (Random Forest pipeline). The app collects basic medical attributes and returns a probability and a binary prediction (High / Low chance of heart disease).

---

## Project Contents

```
/ (root)
├─ app.py                           # Streamlit web app
├─ heart_rf_pipeline.joblib         # Trained model + pipeline (required to run app)
├─ "Heart disease prediction.ipynb" # Notebook: data exploration, model training, evaluation
├─ "heart disease dataset.csv"     # Dataset used for training and experimentation
├─ requirements.txt                 # Python dependencies (optional)
└─ README.md                        # This file
```

> Note: If `heart_rf_pipeline.joblib` is missing, open the notebook to retrain/export the model.

---

## Quick demo (run locally)

1. Clone this repository:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

2. (Recommended) Create and activate a virtual environment:

```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

3. Install dependencies. If `requirements.txt` is not present, install the common ones used in this project:

```bash
pip install streamlit pandas scikit-learn joblib
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

5. The app will open in your browser (usually at `http://localhost:8501`).

---

## How the app works

- `app.py` creates a small Streamlit UI for entering patient attributes (age, sex, chest pain type, blood pressure, cholesterol, etc.).
- Inputs are collected into a `pandas.DataFrame` and fed to the saved pipeline (`heart_rf_pipeline.joblib`).
- The pipeline returns a binary prediction and a probability for the positive class.
- The UI shows an error message for high risk and a success message for low risk, together with the probability.

---

## Files of interest

- **app.py** — Streamlit application front-end. Edit this to change field labels, allowed ranges and UI layout.
- **Heart disease prediction.ipynb** — Notebook containing EDA, preprocessing, model training, cross‑validation, and how the pipeline was exported to `joblib`.
- **heart disease dataset.csv** — Raw dataset (used in the notebook). Check the notebook for column mapping and preprocessing steps.
- **heart_rf_pipeline.joblib** — Serialized `sklearn` pipeline (load with `joblib.load`).

---

## Training or re-training the model

1. Open `"Heart disease prediction.ipynb"` in Jupyter or Colab.
2. Follow the notebook cells: preprocess the data, train the model, evaluate performance.
3. Export the pipeline:

```python
import joblib
joblib.dump(pipeline, 'heart_rf_pipeline.joblib')
```

4. Place `heart_rf_pipeline.joblib` in the repository root next to `app.py`.

---

## Notes & suggestions

- Make sure categorical mapping in `app.py` matches the pipeline's expected feature order and encoding.
- Validate ranges and labels when sharing the app with non-technical users.
- Consider adding unit tests and CI to ensure reproducibility and catch changes to input schema.

---

## Contributing

Contributions are welcome! Typical contributions include:
- Improving the UI and UX of the Streamlit app.
- Improving data cleaning and preprocessing in the notebook.
- Trying different models and reporting results.

Please open an issue or a pull request with a clear description of your change.

---

## License

This project is released under the MIT License. See `LICENSE` for details.

---

## Contact

If you need help, describe the issue in the repository issues tab or contact the repository owner.

---

*Generated README for Heart Disease Prediction — adapt fields like `git clone` URL, license, and contact details before publishing.*

