import streamlit as st

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def main():
    st.title("💪 BMI Calculator")
    st.subheader("Body Mass Index (BMI) Calculator using Streamlit")

    # Input fields
    name = st.text_input("👤 Enter your name:")
    age = st.number_input("🎂 Enter your age:", min_value=1, max_value=120, step=1)
    height = st.number_input("📏 Enter your height (in cm):", min_value=50.0, max_value=250.0, step=1.0)
    weight = st.number_input("⚖️ Enter your weight (in kg):", min_value=10.0, max_value=300.0, step=1.0)

    # Button to calculate
    if st.button("Calculate BMI"):
        if height > 0 and weight > 0:
            bmi = calculate_bmi(weight, height)

            st.success(f"✅ {name}, your BMI is: {bmi}")

            # Result interpretation
            if bmi < 18.5:
                st.warning("🔎 You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.info("👍 You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.warning("⚠️ You are overweight.")
            else:
                st.error("🚨 You are obese. Consider consulting a doctor.")
        else:
            st.error("Please enter valid height and weight.")

if __name__ == "__main__":
    main()