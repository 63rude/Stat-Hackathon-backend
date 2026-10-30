# Smart Gradients PBC stage API

This is the FastAPI backend our team built for Stat Hackathon 2025. It is preserved as a portfolio project. The API loads a bundled H2O model and returns a predicted PBC stage with class probabilities for the supplied example values. The companion [frontend](https://github.com/63rude/Stat-Hackathon-Website) provides the form.

This is an experimental classifier, not a clinical tool. The dataset's original source, model evaluation, and clinical validation are not documented here. Do not enter identifiable patient information or use predictions for diagnosis or care.

## Run locally

This setup was checked with Python 3.14 and Java 17. H2O starts a local Java process when the API imports the model. From this repository's root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

On macOS or Linux, activate with `source .venv/bin/activate`. Open `http://127.0.0.1:8000/docs` for the request schema and an interactive `/predict` form. The model is loaded from `models/` using a path relative to this repository.

The request uses `F` or `M` for `Sex`, `N` or `Y` for `Ascites`, `Hepatomegaly`, and `Spiders`, and `N`, `S`, or `Y` for `Edema`. The remaining fields are numeric. The API calculates `SGOTxALKPHOS` and `SGOTxBILIRUBIN` from the values you supply.

For a local check, paste these example values into the `/predict` form at `/docs`:

```json
{
  "Age": 50, "Sex": "F", "Ascites": "N", "Hepatomegaly": "N",
  "Spiders": "N", "Edema": "N", "Bilirubin": 1.0,
  "Cholesterol": 200, "Albumin": 3.5, "Copper": 100,
  "Alk_Phos": 150, "SGOT": 60, "Tryglicerides": 180,
  "Platelets": 250, "Prothrombin": 11.0
}
```

`CORS_ORIGINS` can hold a comma-separated list of allowed frontend origins. It defaults to `http://localhost:5173,http://127.0.0.1:5173` for local development. Set it to your website's origin if you host the frontend separately.

## Repository layout

- `app/main.py`: FastAPI endpoint and local CORS configuration.
- `app/schemas.py`: request fields and category values.
- `app/model.py`: H2O model loading and prediction response.
- `models/`: the saved model used by the API.
- `dataset.csv` and `Test.py`: the hackathon dataset and a separate random forest training experiment. `Test.py` does not create the model loaded by the API.
