import streamlit as st

from meeting_cost_calculator.model.meeting import MeetingInfo

# ----------- HEADER ----------- #
st.set_page_config(
    page_title="Meeting Cost Calculator",
    page_icon="⎈",
)

st.title("Meeting Cost Calculator")
st.header("How much does this meeting really cost?")


#######################
# MAIN PAGE
#######################
input_col, output_col = st.columns(2)

# ----------- INPUT ----------- #
with input_col:
    with st.container():
        meeting_info = MeetingInfo()

        attendees = st.number_input(
            label="Number of attendees",
            min_value=1,
            step=1,
            value=meeting_info.attendees,
        )
        meeting_duration_minutes = st.number_input(
            label="Meeting duration (minutes)",
            min_value=15,
            step=15,
            value=meeting_info.meeting_duration_minutes,
        )
        times_per_week = st.number_input(
            label="Times per week",
            min_value=1,
            step=1,
            value=meeting_info.times_per_week,
        )
        avg_salary = st.number_input(
            label="Average attendee salary (per year)",
            min_value=meeting_info.avg_salary,
        )

# ----------- OUTPUT ----------- #
with output_col:
    avg_salary_per_hour = avg_salary / 12 / 174
    cost_per_meeting = int(
        round(
            attendees
            * meeting_duration_minutes
            / 60
            * times_per_week
            * avg_salary_per_hour
        )
    )
    cost_per_minute = int(round(cost_per_meeting / meeting_duration_minutes))
    cost_per_year = int(
        round(
            attendees
            * meeting_duration_minutes
            / 60
            * times_per_week
            * avg_salary_per_hour
            * 52
        )
    )

    with st.container():
        st.header(f"${cost_per_meeting}")
        st.write("per meeting")

    with st.container():
        st.header(f"${cost_per_minute}")
        st.write("per minute")

    with st.container():
        st.header(f"${cost_per_year}")
        st.write("per year")
