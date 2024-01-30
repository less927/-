import pandas as pd 
import streamlit as st 
import plotly.express as px




def main():
    st.title("Hello World")
    
    # 데이터 로드
    df = pd.read_csv("data/ss.csv") 
    
    # 데이터 확인
    st.write(df)

if __name__ == "__main__":
    main()























