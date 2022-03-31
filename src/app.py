import streamlit as st
import numpy as np
import pandas as pd


DEFAULT_MEMBERS_FILEPATH = './src/members.txt'

def read_members(filepath):
    with open(filepath, 'r') as fin:
        lines = fin.readlines()
    return [line.strip() for line in lines]

def setup_streamlit_app(members):
    st.title('SBE_VAL_TEAM lasertag teams sampler')
    selected_members = st.multiselect(
        label='Members who come to lasertag',
        options=members,
        default=members
    )
    button_pressed = st.button('Sample!')
    if button_pressed:
        st.text('Your sampled teams')
        members_array = np.array(selected_members)
        np.random.shuffle(members_array)
        team_1, team_2 = np.array_split(members_array, 2)
        df = pd.DataFrame({'Team 1': pd.Series(team_1), 'Team 2': pd.Series(team_2)})
        df = df.fillna('')
        st.dataframe(data=df)

def main():
    members = read_members(DEFAULT_MEMBERS_FILEPATH)
    setup_streamlit_app(members=members)

if __name__ == '__main__':
    main()