import streamlit as st


def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def main():
    st.title("Grade Calculator")

    score = st.number_input("Enter the numerical score:", min_value=0.0, max_value=100.0, step=0.1)

    if st.button("Calculate Grade"):
        grade = calculate_grade(score)
        st.write("The grade for the score", score, "is:", grade)


if __name__ == "__main__":
    main()
