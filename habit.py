import streamlit as st
import pandas as pd

default_habits = ['Exercise', 'Mediation', 'Reading', 'Writing']
df = pd.DataFrame(columns=['Date', 'Habit', 'Progress'])

st.sidebar.title('Habits Tracker')
selected_habits = st.sidebar.multiselect('Select habits:', default_habits)
selected_date = st.sidebar.date_input('Select date:')

for habit in selected_habits:
    progress = st.sidebar.slider(f'{habit} progress:', min_value=0, max_value=100, value=50, step=1)
    df = df.append({'Date':selected_date, 'Habit':habit, 'Progress':progress})

if st.sidebar.button('Save progress'):
    df.to_csv('progress.csv', index=False)

if st.sidebar.button('Load progress'):
    df = pd.read_csv('progress.csv')


new_habit = st.sidebar.text_input('Add a new habit:')
if st.sidebar.button('Add habit'):
    default_habits.append(new_habit)
    selected_habits.append(new_habit)
    progress = st.sidebar.slider(f'{habit} progress:', min_value=0, max_value=100, value=50, step=1)
    df = df.append({'Date':selected_date, 'Habit':habit, 'Progress':progress})

removed_habit = st.sidebar.selectbox('Remove a habit:', default_habits)
if st.sidebar.button('Remove habit'):
    default_habits.remove(removed_habit)
    selected_habits.remove(removed_habit)

import plotly.express as px
for habit in default_habits:
    df_habit = df[df['Habit'] == habit]
    fig = px.line(df_habit, x='Date', y='Progress', title=habit)
    st.plotly_chart(fig)
    
