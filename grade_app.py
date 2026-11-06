import streamlit as st

st.title("Student Grade Manager")

# Calculate Grade
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"

# Initialize student storage
if "students" not in st.session_state:
    st.session_state.students = []

# Student Input Form
with st.form("add_student_form"):

    name = st.text_input("Enter student name")

    mark = st.number_input(
        "Enter student mark",
        min_value=0.0,
        step=0.5,
        format="%.1f"
    )

    submit = st.form_submit_button("Add Student")

# Process Student Submission
if submit:

    if name.strip() == "":
        st.error("Name cannot be blank.")

    else:
        grade = get_grade(mark)

        student = {
            "name": name.strip(),
            "mark": mark,
            "grade": grade
        }

        st.session_state.students.append(student)

        st.success("Student added successfully!")

# Display Student Results
if st.session_state.students:

    st.subheader("Student Results")

    # Format marks to one decimal place for display
    display_students = [
        {
            "name": student["name"],
            "mark": f"{student['mark']:.1f}",
            "grade": student["grade"]
        }
        for student in st.session_state.students
    ]

    st.table(display_students)

    # Calculate Class Statistics
    marks = [student["mark"] for student in st.session_state.students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Display Class Statistics
    st.subheader("Class Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Average", f"{average:.1f}")
    col2.metric("Highest", f"{highest:.1f}")
    col3.metric("Lowest", f"{lowest:.1f}")