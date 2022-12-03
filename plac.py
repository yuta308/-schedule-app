import streamlit as st
import datetime
import streamlit as st
import pandas as pd
import japanize_matplotlib
import matplotlib.pyplot as plt

def TablePlot(df,outputPath,w,h):
    fig, ax = plt.subplots(figsize=(w,h))
    ax.axis('off')
    ax.table(cellText=df.values,
             colLabels=df.columns,
             loc='center',
             bbox=[0,0,1,1],)
    plt.savefig(outputPath)

if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(columns=['日程', '開始時刻', '終了時刻', 'ラベル', 'メモ','確定/未確定','チェック'])

col0, col1, col2, col3, col4, col5, col6,= st.columns(7)
priority = col0.selectbox("優先順位",('大','中','小'))
date = col1.date_input( "date", datetime.date(2022, 12, 1))
stime = col2.time_input('start', datetime.time(1, 00))
ftime = col3.time_input('finish', datetime.time(1, 00))
label = col4.selectbox('ラベル',('仕事', '旅','バイト', '部活動', '学校', '娯楽'))
memo = col5.text_area('メモ')
confirm = col6.selectbox('未確定/確定',('未確定', '確定'))


run = st.button('Submit')

df_new = pd.DataFrame({'日程': str(date), 
                        '開始時刻': str(stime), 
                        '終了時刻': str(ftime), 
                        'ラベル': label, 
                        'メモ': memo, 
                        '確定/未確定': confirm,
                        'チェック':'□'}, index=[priority])    
        
if run:
    st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)
    st.table(st.session_state.mdf)
    TablePlot(st.session_state.mdf,"スケジュール.png",10,10)
    with open("スケジュール.png", "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="スケジュール.png",
            mime="image/png"
        )

st.write(f"Total Rows: {st.session_state.mdf.shape[0]}")