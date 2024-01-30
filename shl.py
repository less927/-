import pandas as pd 
import streamlit as st 
import plotly.express as px
import plotly.graph_objects as go




def main():
    st.title("Hello World")
    
    # 데이터 로드
    df = pd.read_csv("data/ss.csv") 
    
    st.header('sleep health and lifestyle', divider='blue')
    st.header('🍔')
    
    add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
    )
    
    
    
    
    
    
    # 데이터 확인
    st.write(df)
    
    df.loc[:,'Gender']
    
   
    fig = px.scatter(df, x="Age", y="Sleep Duration")
    labels=dict(Age="연령", Sleep_Duration="수면시간")
    fig.update_layout(title='연령대가 수면시간에 영향을 줄까')
    fig.update_xaxes(title_font_size =20,
                 title_font_color='black',
                 tickfont_family='Courier')
    fig.update_yaxes(title_font_size =20,
                 title_font_color='black',
                 tickfont_family='Courier')
    st.plotly_chart(fig)
    
    
    
    fig.update_layout(title='잠을 가장 많이 자는 직업은 무엇일까')
    fig = px.histogram(df, x="Occupation", y="Sleep Duration",histfunc='avg')
    fig.update_xaxes(title_font_size =20,
                 title_font_color='black',
                 tickfont_family='Courier')
    fig.update_yaxes(title_font_size =20,
                 title_font_color='black',
                 tickfont_family='Courier')
    st.plotly_chart(fig)
    
    fig = px.bar(data_frame= df, x='Age', y='Heart Rate')
    st.plotly_chart(fig)
    
    fig = px.scatter(df, x='Age', y='Heart Rate', color='Stress Level', title='스트레스가 많은 사람은 심박이 높을까')
    st.plotly_chart(fig)
   
    

if __name__ == "__main__":
    main()























