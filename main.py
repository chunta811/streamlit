import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')

# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# st.write('Display Image')

# img = Image.open('buckslogo.jpg')
# st.image(img, caption='Logo of The Bucks', use_column_width=True)

# st.write('Interactive Widgets')

# if st.checkbox('Show Image'):
#     img = Image.open('buckslogo.jpg')
#     st.image(img, caption='Logo of The Bucks', use_column_width=True)

# option = st.selectbox(
#     'あなたの好きな数字を教えてください。',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は', option, 'です。'

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味: ', text

# condition = st.slider('あなたの今の調子を教えてください。', 0, 100, 50)
# 'コンディション: ', condition

# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子を教えてください。', 0, 100, 50)
# 'あなたの趣味: ', text
# 'コンディション: ', condition

# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# expander = st.beta_expander('問い合わせ')
# expander.write('問い合わせの回答')

st.write('プログレスバーの表示')
'Start!!'
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!'







