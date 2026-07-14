import streamlit as st
import sqlite3
import pandas as pd

def main():
    st.title('SQL Joins Visualizer')

    # Database connection
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Fetch table names
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in c.fetchall()]

    # Select tables for join
    st.sidebar.header('Select Tables for Join')
    table1 = st.sidebar.selectbox('Table 1', tables)
    table2 = st.sidebar.selectbox('Table 2', tables)

    # Select join type
    join_type = st.sidebar.selectbox('Join Type', ['INNER', 'LEFT', 'RIGHT', 'FULL'])

    # Select join column
    st.sidebar.header('Select Join Column')
    c.execute(f'PRAGMA table_info({table1})')
    cols1 = [row[1] for row in c.fetchall()]
    c.execute(f'PRAGMA table_info({table2})')
    cols2 = [row[1] for row in c.fetchall()]
    common_cols = list(set(cols1) & set(cols2))
    join_col = st.sidebar.selectbox('Join Column', common_cols)

    # Execute join and display results
    if st.sidebar.button('Execute Join'):
        query = f"SELECT * FROM {table1} {join_type} JOIN {table2} ON {table1}.{join_col} = {table2}.{join_col}"
        df = pd.read_sql_query(query, conn)
        st.write(df)

    conn.close()

if __name__ == '__main__':
    main()