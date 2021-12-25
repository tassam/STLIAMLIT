
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# タイトルの表示
st.title('株価予測')

st.write('Ⅰ：株価')
st.write('Ⅱ：自己資本比率')
st.write('Ⅲ：株価収益率')

df = pd.DataFrame({
  '1列目':[1,2,3,4],
  '2列目':[10,20,30,40]
})

##
# データフレームの表示
##
st.write(df)

# px単位で表示を変えることができる
st.dataframe(df, width=1000, height=1000)

# 最大数値に色を付ける
st.dataframe(df.style.highlight_max(axis=0))

# 静的な表を表示させたい場ケース  
st.table(df.style.highlight_max(axis=0))


##
# Markdown 使用方法 
##

# markdown
st.markdown("## markdown")

"""
# 章
## 説
### 項

```python
python main.py
```
"""




##
# チャートの確認
##

# 折れ線グラフ
st.markdown("## 折れ線グラフ")

df = pd.DataFrame(
  np.random.rand(20,3),
  columns=['a','b','c']
)

st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)



##
# チャートの確認
##

df = pd.DataFrame(
  np.random.rand(100,2) / [50,50] + [35.69, 139.70],
  columns=['lat','lon']
)

st.map(df)


##
# 画像の表示
##
# st.title("Display Image")

## サイドバーの作成

# options = st.sidebar.selectbox(
#   '好きな数字を教えてください。',
#   list(range(1,11)), 
# )
# 'あなたの好きな数字は、' + str(options) + 'です。'

# text = st.sidebar.text_input("あなたの趣味を教えてください。")
# 'あなたの趣味は、' + text + 'です。'

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 1000, 50)
# 'コンディション：', condition

## FAQ

# left_column, right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')

# if button:
#   right_column.write("ここは右カラムです。")

# expandar = st.expander('問い合わせ：Ⅰ')
# expandar.write('つくしちゃん')
# expandar = st.expander('問い合わせ：Ⅱ')
# expandar.write('つくしちゃん')
# expandar = st.expander('問い合わせ：Ⅲ')
# expandar.write('つくしちゃん')
# expandar = st.expander('問い合わせ：Ⅳ')
# expandar.write('つくしちゃん')


# if st.checkbox('Show Image'):
#   img = Image.open('産後写真.jpg')
#   st.image(img, caption='つくしちゃん', use_column_width=True)
## 
st.write('プログレスバーの表示')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i + 1}')
  bar.progress(i)
  time.sleep(0.1)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
  right_column.write("ここは右カラムです。")

expandar = st.expander('問い合わせ：Ⅰ')
expandar.write('つくしちゃん')
expandar = st.expander('問い合わせ：Ⅱ')
expandar.write('つくしちゃん')
expandar = st.expander('問い合わせ：Ⅲ')
expandar.write('つくしちゃん')
expandar = st.expander('問い合わせ：Ⅳ')
expandar.write('つくしちゃん')
