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
- valid_claims.csv [valid_claims.csv](https://github.com/user-attachments/files/27488619/valid_claims.csv)
claim_id,patient_id,provider_id,diagnosis_code,procedure_code,claim_amount,insurance_plan,claim_status,service_date,submitted_date,state,age_group,rejection_reason
CLM2001,PAT301,PRV401,DX201,PROC1001,250.5,Gold,Approved,2024-01-01,2024-01-03,OH,Adult,
CLM2009,PAT309,PRV409,DX209,PROC1009,200.0,Gold,Approved,2024-01-09,2024-01-11,TX,Child,

- rejected_claims.csv[rejected_claims.csv](https://github.com/user-attachments/files/27488623/rejected_claims.csv)
claim_id,patient_id,provider_id,diagnosis_code,procedure_code,claim_amount,insurance_plan,claim_status,service_date,submitted_date,state,age_group,rejection_reason
CLM2002,PAT302,PRV402,DX202,PROC1002,-150.0,Silver,Approved,2024-01-02,2024-01-04,CA,Senior,Invalid claim_amount; 
CLM2003,PAT303,PRV403,DX203,PROC1003,0.0,Bronze,Pending,2024-01-03,2024-01-05,TX,Adult,Invalid claim_amount; 
,PAT304,PRV404,DX204,PROC1004,300.0,Gold,Approved,2024-01-04,2024-01-06,FL,Child,Missing claim_id; 
CLM2005,PAT305,PRV405,DX205,PROC1005,450.0,Silver,InvalidStatus,2024-01-05,2024-01-07,NY,Senior,Invalid claim_status; 
CLM2006,PAT306,PRV406,DX206,PROC1006,120.0,Gold,Denied,2024-01-10,2024-01-08,IL,Adult,service_date after submitted_date; 
CLM2007,PAT307,PRV407,DX207,PROC1007,275.99,Bronze,Approved,,2024-01-09,OH,Adult,Invalid service_date; 
CLM2008,PAT308,PRV408,DX208,PROC1008,600.0,Silver,Pending,2024-01-08,,CA,Senior,Invalid submitted_date; 
CLM2010,PAT310,PRV410,DX210,PROC1010,350.0,Bronze,Approved,2024-01-10,2024-01-12,FL,Unknown,Invalid age_group; 

- validation_summary.txt[validation_summary.txt](https://github.com/user-attachments/files/27488624/validation_summary.txt)

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
