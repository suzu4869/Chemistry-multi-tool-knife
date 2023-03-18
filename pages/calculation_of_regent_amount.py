import streamlit as st
import sys
sys.path.append("../")
from functions import calculate_molar_mass

st.title("Calculation of regent amount")

regent = st.text_input("Please input regent", value="HAuCl4")
st.write("as")
loaded_formation = st.text_input("loaded formation", value="Au")
st.write("of")
loading_amount = st.text_input("Please enter the number", value=0.1)
if loading_amount: loading_amount = float(loading_amount)
unit_of_amount = st.selectbox("", ("wt%", "mol%"))
st.write("on")
support = st.text_input("Please input support name as molecular formula", value="Al2O3")
# TODO: 載せたい形1molに対し試薬が何mol必要か計算。（今は1:1）
# TODO: 試薬が濃度を持った液体か固体かを判断

names = (regent, loaded_formation, support)
for name in names:
    if name:
        st.write(f"{name}: {calculate_molar_mass(name)}")
if all(names) and loading_amount and unit_of_amount:
    M_regent = calculate_molar_mass(regent)
    M_l = calculate_molar_mass(loaded_formation)
    M_s = calculate_molar_mass(support)
    if unit_of_amount == "wt%":
        st.write(f"{loading_amount/100 * M_regent/M_l} g/g_support of {regent} is needed")
    else:
        st.write(f"{loading_amount/100 * M_regent/M_s} g/g_support of {regent} is needed")