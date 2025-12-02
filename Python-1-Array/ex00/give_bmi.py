import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Function to calculate BMI from height and weight lists"""
    try:
        if len(height) != len(weight):
            raise ValueError(
                "Height and weight lists must have the same length")
        if (height == [] or weight == []):
            return []
        height_array = np.array(height)
        bmi_array = np.array(weight) / (height_array ** 2)
        return bmi_array.tolist()
    except Exception as e:
        print(f"Error calculating BMI: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Function to apply a limit to the BMI values"""
    try:
        bmi_array = np.array(bmi)
        limit_array = bmi_array > limit
        return limit_array.tolist()
    except Exception as e:
        print(f"Error applying limit: {e}")
        return []
