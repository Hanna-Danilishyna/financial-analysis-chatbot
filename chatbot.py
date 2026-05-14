import pandas as pd

# Load cleaned dataset
df = pd.read_csv("financial_data_cleaned.csv")


# Function for chatbot responses
def simple_chatbot(user_query):

    # Microsoft revenue
    if user_query.lower() == "what is microsoft's revenue in 2025?":

        revenue = df[(df["Company"] == "Microsoft") & (df["Year"] == 2025)][
            "Revenue"
        ].values[0]

        return f"Microsoft's revenue in 2025 was {revenue:,.0f} million USD."

    # Apple net income
    elif user_query.lower() == "what is apple's net income in 2025?":

        income = df[(df["Company"] == "Apple") & (df["Year"] == 2025)][
            "Net Income"
        ].values[0]

        return f"Apple's net income in 2025 was {income:,.0f} million USD."

    # Tesla revenue growth
    elif user_query.lower() == "what was tesla's revenue growth in 2025?":

        growth = df[(df["Company"] == "Tesla") & (df["Year"] == 2025)][
            "Revenue Growth (%)"
        ].values[0]

        return f"Tesla's revenue growth in 2025 was {growth:.2f}%."

    # Microsoft net income growth
    elif user_query.lower() == "what was microsoft's net income growth in 2025?":

        growth = df[(df["Company"] == "Microsoft") & (df["Year"] == 2025)][
            "Net Income Growth (%)"
        ].values[0]

        return f"Microsoft's net income growth in 2025 was {growth:.2f}%."

    # Apple OCF growth
    elif user_query.lower() == "what was apple's operating cash flow growth in 2025?":

        growth = df[(df["Company"] == "Apple") & (df["Year"] == 2025)][
            "OCF Growth (%)"
        ].values[0]

        return f"Apple's operating cash flow growth in 2025 was {growth:.2f}%."

    # Highest revenue company
    elif user_query.lower() == "which company had the highest revenue in 2025?":

        top = df[df["Year"] == 2025].sort_values("Revenue", ascending=False).iloc[0]

        return f"{top['Company']} had the highest revenue in 2025 with {top['Revenue']:,.0f} million USD."

    # Most profitable company
    elif user_query.lower() == "which company had the highest net income in 2025?":

        top = df[df["Year"] == 2025].sort_values("Net Income", ascending=False).iloc[0]

        return f"{top['Company']} had the highest net income in 2025 with {top['Net Income']:,.0f} million USD."

    else:
        return "Sorry, I can only answer predefined financial questions."


# Chat loop
print("Financial Chatbot Prototype")
print("Type 'exit' to stop the chatbot.\n")

while True:

    user_input = input("Ask a financial question: ")

    if user_input.lower() == "exit":
        print("Chatbot ended.")
        break

    response = simple_chatbot(user_input)
    print(response)
