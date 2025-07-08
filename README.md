# Your Personalized Investment Advisor 📈

## Overview
This interactive web application, "Your Personalized Investment Advisor," is designed to empower individuals with tools to plan their mutual fund investments effectively. Leveraging the power of Streamlit, it provides a user-friendly interface for projecting future investment values (both SIP and Lump Sum) and offers tailored mutual fund category suggestions based on individual risk tolerance and financial goals.

## Features
- **Investment Projection:** Calculate the future value of your Systematic Investment Plans (SIPs) or one-time (Lump Sum) investments based on expected returns and investment duration.
- **Personalized Fund Suggestions:** Receive recommendations for mutual fund categories (e.g., ELSS, Debt Funds, Equity Funds) aligned with your risk appetite (Low, Medium, High) and primary investment goals (Wealth Creation, Capital Preservation, Tax Savings, Regular Income).
- **Interactive Interface:** User-friendly sliders and dropdowns for easy input of investment details and personal profile.
- **Comprehensive FAQ:** A built-in Frequently Asked Questions section to clarify common queries about mutual funds, SIPs, and investment concepts.
- **Modular Codebase:** Organized into logical modules for better maintainability and scalability. (Planned for next steps)
- **Data Visualization:** (Planned for next steps) Visualize investment growth over time.

## Getting Started

### Prerequisites
To run this application locally, you need to have Python installed on your system.
- Python 3.8+

### Local Installation and Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```
    *(Note: You'll replace `your-username/your-repo-name` with your actual GitHub repository details once you create it.)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    -   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    -   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application Locally
Once the dependencies are installed, you can run the Streamlit application:
```bash
streamlit run investment_advisor.py
```
This command will open the application in your default web browser, usually at `http://localhost:8501`.

## Deployment

This application is designed for easy deployment on **Streamlit Community Cloud**.

1.  **Push to GitHub:** Ensure your project (including `investment_advisor.py` and `requirements.txt`) is pushed to a public GitHub repository.
2.  **Connect to Streamlit Cloud:**
    -   Go to [share.streamlit.io](https://share.streamlit.io/).
    -   Sign up or log in with your GitHub account.
    -   Click "New app" and select your repository, branch, and the main file (`investment_advisor.py`).
    -   Click "Deploy!".
3.  **Share:** Once deployed, Streamlit Cloud will provide you with a public URL to share your application.

## Project Structure (Planned)
```
.
├── investment_advisor.py       # Main Streamlit application file
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── modules/                    # Directory for modularized code
│   ├── calculations.py         # Financial calculation functions
│   └── suggestions.py          # Fund suggestion logic
└── data/                       # Placeholder for any data files (e.g., historical data)
    └── sample_data.csv
```

## Future Enhancements
-   **Advanced Visualization:** Integrate more sophisticated charts (e.g., Plotly) to show investment growth, compare scenarios, or display historical market data.
-   **Data Integration:** Connect to external APIs (e.g., financial data providers) to fetch real-time or historical mutual fund data.
-   **More Granular Suggestions:** Implement a more complex suggestion engine that considers additional factors like investment horizon, specific financial goals (e.g., retirement, child's education), and current market conditions.
-   **User Authentication:** (For a more complex version) Allow users to save their profiles and investment scenarios.
-   **Performance Benchmarking:** Compare projected returns against market benchmarks.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License
This project is open-source and available under the MIT License.

## Contact
For any questions or feedback, please contact Manoj Kumar:
- Email: manojkumar.du.or.21@gmail.com
- LinkedIn: https://www.linkedin.com/in/iam-manoj/
