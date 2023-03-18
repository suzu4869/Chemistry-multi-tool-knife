import streamlit as st
import sys
sys.path.append("../")
from functions import ppm_to_mol_L

# Streamlit アプリケーションを作成する
st.title("ppm to mol/L converter")

# 入力フォームを作成する
state = st.selectbox("Select the state of substance:", ("gas", "liquid"))
ppm = float(st.number_input("Enter the concentration in ppm:"))

if state == "gas":
    molecular_weight = None
    temperature = st.number_input("Enter the temperature (K):", value=298.15)
    pressure = st.number_input("Enter the pressure (kPa):", value=101.0) * 1000
else:
    molecular_weight = st.number_input("Enter the molecular weight:")
    temperature = None
    pressure = None

# 変換を実行する
if st.button("Convert"):
    C = ppm_to_mol_L(state, ppm, molecular_weight, temperature=temperature, pressure=pressure)
    st.write(f"The concentration in umol/L is {C*1e6:.5g}")