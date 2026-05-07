import pandas as pd
from validator import check_required_columns, validate_claims
from cleaner import clean_claims


def main():

    # Input file path
    input_path = "data/claims_broken.csv"

    print("Loading claims data...")
    df = pd.read_csv(input_path)

    print("Checking required columns...")
    check_required_columns(df)

    print("Cleaning claims data...")
    df = clean_claims(df)

    print("Validating claims data...")
    valid_df, rejected_df = validate_claims(df)

    print("Saving output files...")

    # Save valid claims
    valid_df.to_csv(
        "output/valid_claims.csv",
        index=False
    )

    # Save rejected claims
    rejected_df.to_csv(
        "output/rejected_claims.csv",
        index=False
    )

    # Summary statistics
    total_records = len(df)
    valid_records = len(valid_df)
    rejected_records = len(rejected_df)

    # Rejection breakdown
    rejection_breakdown = rejected_df[
        "rejection_reason"
    ].value_counts()

    # Create summary report
    summary = f"""
Healthcare Claims Validation Summary

Total records processed: {total_records}
Valid records: {valid_records}
Rejected records: {rejected_records}
Rejection rate: {round((rejected_records / total_records) * 100, 2)}%

Top Rejection Reasons:
{rejection_breakdown.to_string()}
"""

    # Save summary report
    with open(
        "output/validation_summary.txt",
        "w"
    ) as file:

        file.write(summary)

    # Print summary
    print(summary)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()