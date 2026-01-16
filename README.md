# Migration Validator
### Metadata-Driven Migration Validation Tool

---

## Overview

Migration Validator is a Streamlit-based application used to validate data migrations by dynamically applying business rules stored in a CSV file.

The application independently calculates the expected target data from legacy data and compares it with the actual migrated target data to identify discrepancies.

---

## Business Problem

During enterprise migrations (e.g., Legacy systems to SAP S/4HANA), transformation rules are:

- Complex
- Frequently changing
- Maintained by business users

Hardcoding these rules is not scalable.  
This application solves the problem using a metadata-driven rule engine.

---

## Features

- Upload three CSV files:
  - Transformation Rules
  - Legacy Data
  - Target Data
- Dynamic rule execution (no hardcoding)
- Vectorized Pandas processing
- Validation KPIs
- Failed record drill-down
- Export mismatches as CSV

---

## Supported Rule Operations

### MAP_VALUE
Maps a source value to a target value based on a condition.

Example:
```
Active → 10
```

---

### CALC_ADD
Adds a numeric value to a source column.

Example:
```
100 + 5 → 105
```

---

### CONCAT
Appends a string to a source column.

Example:
```
ORD-99 + _ARCHIVED → ORD-99_ARCHIVED
```

---

## Project Structure

```
migration_assessment/
├── src/
│   ├── app.py
│   ├── engine.py
│   ├── validator.py
│   └── __init__.py
│
├── data/
│   ├── legacy_data.csv
│   ├── target_data.csv
│   └── transformation_rules.csv
│
├── requirements.txt
└── README.md
```

---

## Technology Stack

- Python 3.9+
- Streamlit
- Pandas
- NumPy

---

## Setup Instructions

### Create Virtual Environment
```
python -m venv venv
```

Activate:
```
venv\Scripts\activate
```

---

### Install Dependencies
```
pip install -r requirements.txt
```

---

### Run the Application
```
streamlit run src/app.py
```

Open in browser:
```
http://localhost:8501
```

---

## How to Use

1. Upload Rules CSV
2. Upload Legacy CSV
3. Upload Target CSV
4. Click **Run Validation**
5. Review metrics and mismatches

---

## Output Metrics

- Total Records
- Failed Records
- Accuracy Percentage
- Failed Records Table

---

## Design Principles

- Metadata-driven architecture
- Modular code structure
- Scalable and maintainable
- Enterprise-ready validation logic

---

## Conclusion

Migration Validator provides a robust and flexible solution for validating enterprise data migrations using dynamic business rules.