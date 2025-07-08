def get_fund_suggestions(risk_tolerance, investment_goal):
    suggestions = []
    if investment_goal == "Tax Savings (ELSS)":
        suggestions.append(("ELSS (Equity Linked Savings Scheme)", "Invest in equities with a 3-year lock-in period, offering tax benefits under Section 80C. Suitable for long-term goals."))
    elif risk_tolerance == "Low":
        if investment_goal == "Capital Preservation":
            suggestions.extend([
                ("Debt - Liquid Funds", "For very short-term goals (days to months). Highly stable."),
                ("Debt - Ultra Short Duration Funds", "For short-term goals (3-6 months). Slightly higher returns than liquid funds."),
                ("Debt - Corporate Bond Funds", "Invests in high-quality company bonds. Good for 2-3 year goals.")
            ])
        else:
            suggestions.append(("Hybrid - Conservative Hybrid Funds", "Primarily invests in debt with a small equity portion for some growth. Balances safety and returns."))
    elif risk_tolerance == "Medium":
        suggestions.extend([
            ("Hybrid - Balanced Advantage Funds", "Dynamically adjusts equity/debt allocation based on market conditions. A good all-weather fund."),
            ("Equity - Large Cap Funds", "Invests in the top 100 largest companies. Relatively stable for equity."),
            ("Equity - Flexi Cap Funds", "Invests across large, mid, and small-cap stocks, giving the fund manager flexibility.")
        ])
    elif risk_tolerance == "High":
        suggestions.extend([
            ("Equity - Mid Cap Funds", "Invests in medium-sized companies with high growth potential and higher risk."),
            ("Equity - Small Cap Funds", "Invests in small companies. Very high risk but also very high return potential."),
            ("Equity - Thematic/Sectoral Funds", "Focuses on a specific sector like Technology or Healthcare. High risk due to lack of diversification.")
        ])
    return suggestions
