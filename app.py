import streamlit as st
import sqlite3
import pandas as pd
from datetime import date

st.set_page_config(layout="wide")

st.title("Fitness Progress Tracker")

st.divider()

conn = sqlite3.connect("fitness_data.db")
cursor = conn.cursor()

data = pd.read_sql("SELECT * FROM workout", conn)
records = pd.read_sql("SELECT * FROM records", conn)

num_max_pushups_per_set = int(records['max_push_ups'].max())
num_max_pullups_per_set = int(records['max_pull_ups'].max())

current_date = st.sidebar.date_input(
    label='Date',
    value='today',
    min_value='today',
    format='YYYY-MM-DD'
)

push_ups = st.sidebar.number_input(
    label='Push-ups',
    min_value=0
)

pull_ups = st.sidebar.number_input(
    label='Pull-ups',
    min_value=0
)

max_pushups_per_set = st.sidebar.number_input(
    label="Max push-ups per set",
    value=num_max_pushups_per_set
)

if max_pushups_per_set > num_max_pushups_per_set:
    num_max_pushups_per_set = max_pushups_per_set

max_pullups_per_set = st.sidebar.number_input(
    label="Max pull-ups per set",
    value=num_max_pullups_per_set
)

if max_pullups_per_set > num_max_pullups_per_set:
    num_max_pullups_per_set = max_pullups_per_set

if 'submitted_today' not in st.session_state:
    st.session_state['submitted_today'] = str(
        data['date'].max()) == str(date.today())

disabled = st.session_state['submitted_today']

is_submitted = st.sidebar.button(
    label='Submit',
    disabled=disabled
)

if is_submitted:
    cursor.execute("INSERT OR REPLACE INTO workout VALUES (?, ?, ?)",
                   (current_date, push_ups, pull_ups))
    cursor.execute("INSERT OR REPLACE INTO records VALUES (?, ?, ?)",
                   (current_date, num_max_pushups_per_set, num_max_pullups_per_set))
    conn.commit()
    st.success("Workout data saved!")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        label="Max push-ups per set",
        value=num_max_pushups_per_set
    )

    st.divider()

    st.subheader(body="Push-ups progress")

    st.line_chart(
        data=data,
        x='date',
        y='push_ups',
        height=300
    )

with col2:

    st.metric(
        label="Max pull-ups per set",
        value=num_max_pullups_per_set
    )

    st.divider()

    st.subheader(body="Pull-ups progress")

    st.line_chart(
        data=data,
        x='date',
        y='pull_ups',
        height=300
    )

st.subheader(body="Workout History")
st.dataframe(data=data)
