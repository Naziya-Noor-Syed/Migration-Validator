import pandas as pd

class Validator:
    @staticmethod
    def validate(expected_df: pd.DataFrame, actual_df: pd.DataFrame):

        # Align schema
        expected_df = expected_df[actual_df.columns]

        # Reset index
        expected_df = expected_df.reset_index(drop=True)
        actual_df = actual_df.reset_index(drop=True)

        # Normalize values (string compare safety)
        expected_df = expected_df.astype(str).apply(lambda x: x.str.strip())
        actual_df = actual_df.astype(str).apply(lambda x: x.str.strip())

        comparison = expected_df.eq(actual_df)
        row_match = comparison.all(axis=1)

        failed_rows = expected_df.loc[~row_match].copy()

        total = len(expected_df)
        failed = len(failed_rows)
        accuracy = round(((total - failed) / total) * 100, 2)

        return {
            "total": total,
            "failed": failed,
            "accuracy": accuracy,
            "failed_rows": failed_rows
        }
