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
df = pd.read_csv('meibo.csv', encoding='utf-8')

# 必要に応じて、期列を文字列型に変換
df['期'] = df['期'].astype(str)

# 検索条件入力フォーム
st.sidebar.header("検索条件　期は半角入力")
ki = st.sidebar.text_input("期", "").strip()
name = st.sidebar.text_input("名前", "").strip()


# 全データ表示オプション
# if st.sidebar.checkbox("全データを表示"):
#     st.subheader("名簿全データ")
#     st.dataframe(df)

# フィルタリング処理（部分一致対応 & 結果を限定表示）
if ki or name :
    filtered_df = df[
        ((df['期'].str.contains(ki, na=False, case=False)) if ki else True) &
        ((df['名前'].str.contains(name, na=False, case=False)) if name else True) 
    ]

    # 結果を限定した列のみ表示
    selected_columns = ['期', '名前', 'メアド１','電話番号','プロフィール']  # 必要な列を選択
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



