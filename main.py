import streamlit as st
import numpy as np
import pandas as pd

st.title('title基礎')
st.write('aaaa')

df = pd.DataFrame({
    '1列目':[3,4,6],
    '2列目':[5,7,1],
}
)
st.dataframe(df)
st.dataframe(df.style.highlight_max(axis=0),width=5000,height=150)
# st.dataframe
st.table(df)

df = pd.DataFrame(
    np.random.rand(10,3),
    columns=['a','b','c']
)

#折れ線グラフ
st.line_chart(df)

#円グラフ
st.area_chart(df)

#棒グラフ
st.bar_chart(df)

df = pd.DataFrame(



    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns = ['lat','lon']
)

#マップをプロット
st.map(df)

from PIL import Image
img = Image.open("Iris.jpg")
st.image(img,caption="Iris",use_column_width=True)

if st.checkbox('Show image'):
    img = Image.open("Iris.jpg")
    st.image(img,caption="iris",use_column_width=True)

option  =st.selectbox(
    '好きな数字を入力してください',
    list(range(1,11))
)
'あなたの好きな数字は' , option , 'です。'
tx  = st.sidebar.text_input('あなたの好きなスポーツを教えてください')
'あなたの好きなスポーツは',tx
condition = st.sidebar.slider('調子はどう？',0,100,50)
condition

# expander
expander1 = st.expander('質問1')
expander1.write('質問1の回答')
expander2 = st.expander('質問2')
expander2.write('質問2の回答')
expander3 = st.expander('質問3')
expander3.write('質問3の回答')

import time

latest_iteration = st.empty()
bar = st.progress(0)

# プログレスバーを0.1秒毎に進める
for i in range(100):
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done'