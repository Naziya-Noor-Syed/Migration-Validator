import pandas as pd

class RuleEngine:
    def __init__(self, rules_df: pd.DataFrame):
        self.rules_df = rules_df

    def apply_rules(self, legacy_df: pd.DataFrame) -> pd.DataFrame:
        df = legacy_df.copy()

        # Sort rules by priority
        rules = self.rules_df.sort_values("Priority")

        for _, rule in rules.iterrows():
            operation = rule["Operation"].strip()
            source = rule["Source_Column"].strip()
            target = rule["Target_Column"].strip()
            condition = str(rule["Condition_Keyword"]).strip()
            result = rule["Result_Value"]

            if operation == "MAP_VALUE":
                mask = df[source].astype(str).str.strip() == condition
                df.loc[mask, target] = result

            elif operation == "CALC_ADD":
                df[target] = (
                    pd.to_numeric(df[source], errors="coerce")
                    + int(result)
                )

            elif operation == "CONCAT":
                df[target] = df[source].astype(str).str.strip() + str(result)

        # 🔴 IMPORTANT: return ONLY target columns
        target_columns = self.rules_df["Target_Column"].unique()
        df = df[target_columns]

        return df
