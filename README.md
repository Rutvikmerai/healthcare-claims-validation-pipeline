# Healthcare Claims Validation Pipeline

## Project Overview
This project validates healthcare insurance claim records using Python and Pandas. The pipeline checks data quality, applies business validation rules, separates valid and rejected claims, and generates a summary report.

## Business Problem
Healthcare organizations need accurate claims data for billing, reporting, and compliance. Invalid claims can cause payment delays, reporting errors, and operational inefficiencies.

## Validation Rules
- Required columns must exist
- Claim amount must be greater than 0
- Claim ID cannot be missing
- Duplicate claim IDs are rejected
- Service date cannot be after submitted date
- Claim status must be Approved, Denied, or Pending
- Age group must be Child, Adult, or Senior

## Project Structure
```text
healthcare-claims-validation/
├── data/
│   ├── claims_clean.csv
│   └── claims_broken.csv
├── output/
│   ├── valid_claims.csv
│   ├── rejected_claims.csv
│   └── validation_summary.txt
├── src/
│   ├── main.py
│   ├── validator.py
│   └── cleaner.py
├── README.md
└── requirements.txt
```

## Output
- [valid_claims.csv](https://github.com/user-attachments/files/27488619/valid_claims.csv)

- [rejected_claims.csv](https://github.com/user-attachments/files/27488623/rejected_claims.csv)

- [validation_summary.txt](https://github.com/user-attachments/files/27488624/validation_summary.txt)

Healthcare Claims Validation Summary

Total records processed: 10
Valid records: 2
Rejected records: 8
Rejection rate: 80.0%

Top Rejection Reasons:
rejection_reason
Invalid claim_amount;                  2
Missing claim_id;                      1
Invalid claim_status;                  1
service_date after submitted_date;     1
Invalid service_date;                  1
Invalid submitted_date;                1
Invalid age_group;                     1


## Tools Used
- Python
- Pandas
- VS Code
- GitHub

## How to Run
```bash
pip install -r requirements.txt
python src/main.py
