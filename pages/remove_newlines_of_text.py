import streamlit as st
import pyperclip

def remove_newlines(text):
    return text.replace('\n', '').replace('\r', '')

def main():
    st.title("Remove newlines and copy to clipboard")

    # テキスト入力フォーム
    input_text = st.text_area("Input text")

    # 改行文字を除去したテキストの表示
    output_text = remove_newlines(input_text)
    st.write("Output text:")
    st.code(output_text)

    # コピーするボタン
    if st.button("Copy to clipboard"):
        pyperclip.copy(output_text)
        st.success("Copied to clipboard!")

if __name__ == "__main__":
    main()
