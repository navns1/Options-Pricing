# Define the Streamlit app for European option pricing

def main():
    st.title("European Options Pricing APP")
    
    st.sidebar.header("Options Pricing Parameters")
    S = st.sidebar.number_input("Current Stock Price", min_value=0.0, value=100.0, step=0.1)
    K = st.sidebar.number_input("Strike Price", min_value=0.0, value=100.0, step=0.1)
    r = st.sidebar.number_input("Risk-free rate", min_value=0.0, value=0.05, step=0.1)
    T = st.sidebar.number_input("Time to maturity", min_value=0.0, value=1.0, step=0.1)
    sigma = st.sidebar.number_input("Volatility", min_value=0.0, value=0.2, step=0.1)
    
    # Option type selector
    option_type=st.sidebar.selectbox("Option Type", ['call', 'put'])
    
    # Calculate and display results
    result = eu_pricing(S, K, r, T, sigma, type=option_type)
    
    st.subheader("Options Pricing Result")
    st.write(result)

# Allows the function to be callable when imported into another Python program
if __name__ == "__main__":
    main()