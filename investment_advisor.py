import streamlit as st
import plotly.graph_objects as go
from modules.calculations import calculate_future_value, generate_investment_growth_data
from modules.suggestions import get_fund_suggestions

# --- Page Configuration ---
st.set_page_config(
    page_title="Personalized Investment Advisor",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Main App ---
st.title("Your Personalized Investment Advisor 📈")

st.write("Welcome to your go-to tool for smart investment planning! Whether you're saving for a dream home, retirement, or simply growing your wealth, this advisor helps you:")
st.markdown("- **Project Future Value:** See how your SIPs or lump sum investments can grow over time.")
st.markdown("- **Get Tailored Suggestions:** Receive mutual fund category recommendations based on your risk tolerance and financial goals.")
st.markdown("Let's get started on your financial journey!")

# --- Sidebar for User Input ---
st.sidebar.header("Your Investment Details")

# Investment Type
investment_type = st.sidebar.selectbox("Investment Type", ["SIP (Systematic Investment Plan)", "Lump Sum"])

# Investment Amount
if investment_type == "SIP (Systematic Investment Plan)":
    monthly_investment = st.sidebar.number_input("Monthly Investment (INR)", min_value=500, step=100, value=5000)
else:
    lump_sum_amount = st.sidebar.number_input("Lump Sum Amount (INR)", min_value=1000, step=1000, value=50000)

# Investment Duration
investment_duration = st.sidebar.slider("Investment Duration (Years)", min_value=1, max_value=30, value=10, step=1)

# Expected Annual Return
expected_return = st.sidebar.slider("Expected Annual Return (%)", min_value=1.0, max_value=30.0, value=12.0, step=0.5)

# --- User Profile for Suggestions ---
st.sidebar.header("Your Investor Profile")
risk_tolerance = st.sidebar.selectbox("Your Risk Tolerance", ["Low", "Medium", "High"])
investment_goal = st.sidebar.selectbox("Primary Investment Goal", ["Wealth Creation", "Capital Preservation", "Tax Savings (ELSS)", "Regular Income"])

# --- Calculation Button ---
calculate_button = st.sidebar.button("Calculate & Suggest Funds")

if calculate_button:
    future_value, total_investment, estimated_returns = calculate_future_value(
        investment_type, monthly_investment if investment_type == "SIP (Systematic Investment Plan)" else 0,
        lump_sum_amount if investment_type == "Lump Sum" else 0, investment_duration, expected_return
    )

    st.subheader("Investment Projection")
    st.metric(label="Future Value", value=f"₹ {future_value:,.2f}")
    st.metric(label="Total Amount Invested", value=f"₹ {total_investment:,.2f}")
    st.metric(label="Estimated Returns", value=f"₹ {estimated_returns:,.2f}")

    # --- Investment Growth Visualization ---
    st.subheader("Investment Growth Over Time")
    growth_data = generate_investment_growth_data(
        investment_type, monthly_investment if investment_type == "SIP (Systematic Investment Plan)" else 0,
        lump_sum_amount if investment_type == "Lump Sum" else 0, investment_duration, expected_return
    )

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=growth_data["Year"], y=growth_data["Current Value"], mode='lines', name='Current Value'))
    fig.add_trace(go.Scatter(x=growth_data["Year"], y=growth_data["Total Invested"], mode='lines', name='Total Invested'))
    fig.update_layout(title='Investment Growth', xaxis_title='Years', yaxis_title='Amount (INR)')
    st.plotly_chart(fig, use_container_width=True)

    # --- Fund Suggestion Logic ---
    st.subheader("Personalized Fund Suggestions")
    suggestions = get_fund_suggestions(risk_tolerance, investment_goal)

    if not suggestions:
        st.warning("Could not determine a specific fund category. Please review your selections.")
    else:
        for fund_type, description in suggestions:
            st.markdown(f"**- {fund_type}:** {description}")

# --- FAQ Section ---
st.subheader("Frequently Asked Questions (FAQ)")

with st.expander("What is a Mutual Fund?"):
    st.write("A mutual fund is a professionally managed investment fund that pools money from many investors to purchase securities like stocks, bonds, money market instruments, and other assets. Mutual funds are operated by money managers, who invest the fund's capital and attempt to produce capital gains and income for the fund's investors.")

with st.expander("What is SIP?"):
    st.write("SIP stands for Systematic Investment Plan. It is a method of investing a fixed amount regularly (e.g., monthly) into a mutual fund. SIPs help in rupee cost averaging and inculcate a disciplined approach to investing.")

with st.expander("How is 'Expected Annual Return' determined?"):
    st.write("The 'Expected Annual Return' is an estimated rate of return you anticipate from your investment. It's crucial to understand that this is a projection and actual returns can vary. Historical performance of similar funds or market conditions can be used as a guide, but past performance does not guarantee future results.")

with st.expander("Why are there different 'Risk Tolerances'?"):
    st.write("Risk tolerance refers to an investor's ability and willingness to take on financial risk. Different mutual fund categories carry different levels of risk. Understanding your risk tolerance helps in choosing funds that align with your comfort level and financial goals. Low risk tolerance typically means preferring stable, less volatile investments, while high risk tolerance may involve investments with higher potential returns but also higher potential losses.")

with st.expander("How accurate are the fund suggestions?"):
    st.write("The fund suggestions provided are based on general investment principles and common mutual fund categories. They are intended as a guide to help you understand which types of funds might align with your stated risk tolerance and investment goals. However, these are not financial recommendations. Always consult with a qualified financial advisor before making any investment decisions.")

# --- Developer Info ---
st.sidebar.markdown("---")
st.sidebar.write("Developed by: Manoj Kumar")
st.sidebar.markdown("[LinkedIn Profile](https://www.linkedin.com/in/iam-manoj/)")