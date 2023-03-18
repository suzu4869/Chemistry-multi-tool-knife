import streamlit as st
import sys
sys.path.append("../")
from functions import conversion_rate

# Streamlit アプリケーションを作成する
st.title("mol to conversion rate converter")

# 入力フォームを作成する
moles = float(st.number_input("Number of mols consumed (mmol):", value=0.00)) * 1e-3
st.write("in")
volume = float(st.number_input("Total volume (L):", value=1.00))
partial_pressure = float(st.number_input("Initial partial pressure (atm):", value=1.00))

# 変換を実行する
if all((moles, volume, partial_pressure)):
    conversion = conversion_rate(moles, volume, partial_pressure)
    st.write(f"The conversion is {conversion:.5g}")