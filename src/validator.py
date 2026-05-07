import pandas as pd

# Required dataset columns
REQUIRED_COLUMNS = [
    "claim_id",
    "patient_id",
    "provider_id",
    "diagnosis_code",
    "procedure_code",
    "claim_amount",
    "insurance_plan",
    "claim_status",
    "service_date",
    "submitted_date",
    "state",
    "age_group"
]

# Valid business values
VALID_STATUSES = ["Approved", "Denied", "Pending"]

VALID_AGE_GROUPS = ["Child", "Adult", "Senior"]


# Step 1: Check required columns exist
def check_required_columns(df):

    missing_columns = [
        col for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )


# Step 2: Validate claims data
def validate_claims(df):

    df = df.copy()

    # Create rejection reason column
    df["rejection_reason"] = ""

    # Missing claim_id
    df.loc[
        df["claim_id"].isna(),
        "rejection_reason"
    ] += "Missing claim_id; "

    # Duplicate claim_id
    df.loc[
        df["claim_id"].duplicated(keep=False),
        "rejection_reason"
    ] += "Duplicate claim_id; "

    # Invalid claim_amount
    df.loc[
        df["claim_amount"] <= 0,
        "rejection_reason"
    ] += "Invalid claim_amount; "

    # Invalid claim_status
    df.loc[
        ~df["claim_status"].isin(VALID_STATUSES),
        "rejection_reason"
    ] += "Invalid claim_status; "

    # Invalid age_group
    df.loc[
        ~df["age_group"].isin(VALID_AGE_GROUPS),
        "rejection_reason"
    ] += "Invalid age_group; "

    # Convert dates
    df["service_date"] = pd.to_datetime(
        df["service_date"],
        errors="coerce"
    )

    df["submitted_date"] = pd.to_datetime(
        df["submitted_date"],
        errors="coerce"
    )

    # Invalid service_date
    df.loc[
        df["service_date"].isna(),
        "rejection_reason"
    ] += "Invalid service_date; "

    # Invalid submitted_date
    df.loc[
        df["submitted_date"].isna(),
        "rejection_reason"
    ] += "Invalid submitted_date; "

    # service_date after submitted_date
    df.loc[
        df["service_date"] > df["submitted_date"],
        "rejection_reason"
    ] += "service_date after submitted_date; "

    # Separate valid and rejected claims
    valid_df = df[
        df["rejection_reason"] == ""
    ].copy()

    rejected_df = df[
        df["rejection_reason"] != ""
    ].copy()

    return valid_df, rejected_df