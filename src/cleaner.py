def clean_claims(df):
    df = df.copy()

    # Standardize text columns
    df["claim_status"] = df["claim_status"].str.strip()
    df["insurance_plan"] = df["insurance_plan"].str.strip()
    df["state"] = df["state"].str.upper().str.strip()
    df["age_group"] = df["age_group"].str.strip()

    # Round claim amount
    df["claim_amount"] = df["claim_amount"].round(2)

    return df