import pandas as pd
import unicodedata
import streamlit as st

# 全角を半角に変換する関数
def to_half_width(s):
    if isinstance(s, str):  # 文字列の場合のみ変換
        return unicodedata.normalize('NFKC', s)
    return s

# Streamlitアプリのタイトル
st.title("名簿検索システム")

# CSVファイルの読み込み

import os
import pandas as pd

df = pd.read_csv('meibo.csv', encoding='utf-8')
print(df.columns)



# 必要に応じて、期列を文字列型に変換
df['期'] = df['期'].astype(str)

# 検索条件入力フォーム
st.sidebar.header("検索条件　期は第xx期　xxは半角入力")
ki = st.sidebar.text_input("期", "").strip()
name = st.sidebar.text_input("名前", "").strip()


# フィルタリング処理（部分一致対応 & 結果を限定表示）
# 'ki'カラムを数値型へ変換
df["ki"] = pd.to_numeric(df["ki"], errors='coerce')

# ユーザー入力
search_value = st.text_input("検索する番号を入力")

if search_value.isdigit():
    search_value = int(search_value)
    result = df[df["ki"] == search_value]
    st.write(result)
else:
    st.write("数字のみ入力してください")

    # 結果を限定した列のみ表示
    selected_columns = ['期', '名前','学部学科']  # 必要な列を選択
    if not filtered_df.empty:
        if all(col in df.columns for col in selected_columns):  # 必要な列が存在するか確認
            st.subheader("検索結果")
            st.dataframe(filtered_df.loc[:, selected_columns])  # 必要な列のみ抽出して表示
        else:
            st.error(f"必要な列がデータにありません: {selected_columns}")
    else:
        st.warning("該当するデータがありません。")
else:
    st.info("検索条件を入力してください。")



