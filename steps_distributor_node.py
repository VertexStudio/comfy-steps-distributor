class StepsDistributor:
    CATEGORY = "Sortium"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Steps": ("INT", {"default": 30, "min": 1}),
                "Percentage_1": ("FLOAT", {"default": 26.66, "min": 0.0, "max": 100.0, "step": 0.01}),
                "Percentage_2": ("FLOAT", {"default": 40.0, "min": 0.0, "max": 100.0, "step": 0.01}),
                "Percentage_3": ("FLOAT", {"default": 33.33, "min": 0.0, "max": 100.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("Value 1", "Value 2")
    FUNCTION = "distribute_steps"

    def distribute_steps(self, Steps, Percentage_1, Percentage_2, Percentage_3):
        # Ensure the sum of percentages is approximately 100%, allowing small tolerance
        total_percentage = Percentage_1 + Percentage_2 + Percentage_3
        if not (99.99 <= total_percentage <= 100.01):
            raise ValueError("The sum of the percentages must be approximately 100%.")

        # Convert percentages to fractions
        percentage_1 = Percentage_1 / 100
        percentage_2 = Percentage_2 / 100
        percentage_3 = Percentage_3 / 100

        # Calculate the number of steps for each KSampler
        steps_1 = max(round(Steps * percentage_1), 1)  # Ensure minimum value is 1
        steps_2 = max(round(Steps * percentage_2), 1)  # Ensure minimum value is 1
        steps_3 = Steps - steps_1 - steps_2  # Ensure the total is exactly "Steps"

        # If steps_3 becomes 0 or negative, adjust the distribution
        if steps_3 < 1:
            steps_3 = 1
            if steps_2 > 1:
                steps_2 -= 1
            elif steps_1 > 1:
                steps_1 -= 1

        # Calculate the end steps (Value 1 and Value 2)
        value_1 = steps_1  # End at step for KSampler 1
        value_2 = steps_1 + steps_2  # End at step for KSampler 2

        # Print the distribution of steps for each KSampler
        print(f"KSampler 1: {steps_1} steps ({Percentage_1}%)")
        print(f"KSampler 2: {steps_2} steps ({Percentage_2}%)")
        print(f"KSampler 3: {steps_3} steps ({Percentage_3}%)")

        return (value_1, value_2)
