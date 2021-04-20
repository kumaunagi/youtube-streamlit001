import streamlit as st
import pandas as pd
from sklearn import datasets
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!'
latest_iteration= st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'

def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target_names[iris.target]
    return df

df = load_data()
targets = list(df.target.unique())
selected_targets = st.multiselect('select targets', targets, default=targets)
df = df[df.target.isin(selected_targets)]

st.dataframe(df)

"""
# 章
# 節
### 項
```python
import streamlit as st
import pandas as pd
from sklearn import datasets
from PIL import Image
```
"""
st.write('Disply Image')

if st.checkbox('Show Image'):
    img=Image.open('marron.jpg')
    st.image(img,caption='にゃんこ',use_columns_width=True)

option=st.selectbox(
    'あなたの年齢は',
        list(range(1,51))
)
'あなたの年齢は、',option,'歳で間違いありませんか？'

text=st.sidebar.text_input('どこに住んでいますか？')
if text!='':
    'そうですか！',text,'は、いいところですね。'

condision=st.slider('本日の体調は何点ですか？',0, 100, 40)
'なるほど！あなたの体調は',condision,'なのですね'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右ボタンに文字を表示する')
if button:
    right_column.write('ここは右カラムです')

expander = st.beta_expander('問い合わせ内容')
expander.write('問い合わせ内容を書く1')
expander.write('問い合わせ内容を書く2')
expander.write('問い合わせ内容を書く3')

#py37仮装で起動し
#streamlit run streamlit_example.py　　で実行出来る
#cntl + C で閉じる
# com / でコメントアウト