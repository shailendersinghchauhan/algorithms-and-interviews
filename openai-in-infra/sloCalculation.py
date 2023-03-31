class SLOCalculator:
    def __init__(self, error_budget, time_window):
        self.error_budget = error_budget
        self.time_window = time_window

    def calculate_slo(self, errors):
        error_rate = sum(errors) / self.time_window
        slo = 1 - (error_rate / self.error_budget)
        return slo
