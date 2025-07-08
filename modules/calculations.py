import pandas as pd

def calculate_future_value(investment_type, monthly_investment, lump_sum_amount, investment_duration, expected_return):
    if investment_type == "SIP (Systematic Investment Plan)":
        monthly_rate = (expected_return / 100) / 12
        months = investment_duration * 12
        future_value = monthly_investment * ((((1 + monthly_rate)**months) - 1) / monthly_rate) * (1 + monthly_rate)
        total_investment = monthly_investment * months
    else: # Lump Sum
        future_value = lump_sum_amount * ((1 + (expected_return / 100)) ** investment_duration)
        total_investment = lump_sum_amount

    estimated_returns = future_value - total_investment
    return future_value, total_investment, estimated_returns

def generate_investment_growth_data(investment_type, monthly_investment, lump_sum_amount, investment_duration, expected_return):
    data = []
    if investment_type == "SIP (Systematic Investment Plan)":
        monthly_rate = (expected_return / 100) / 12
        months = investment_duration * 12
        current_value = 0
        total_invested = 0
        for month in range(1, months + 1):
            total_invested += monthly_investment
            current_value = (current_value + monthly_investment) * (1 + monthly_rate)
            data.append({"Month": month, "Year": month / 12, "Total Invested": total_invested, "Current Value": current_value})
    else: # Lump Sum
        annual_rate = (expected_return / 100)
        current_value = lump_sum_amount
        total_invested = lump_sum_amount
        for year in range(1, investment_duration + 1):
            current_value = lump_sum_amount * ((1 + annual_rate) ** year)
            data.append({"Year": year, "Total Invested": total_invested, "Current Value": current_value})

    return pd.DataFrame(data)
