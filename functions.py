import datetime
import pandas as pd
import re

# TODO: かっこに対応
def split_elements(text):
    elements_dic = {}
    for elem_num in re.findall(r"[A-Z][^A-Z]*", text):
        elem = re.match(r"\D+", elem_num).group()
        num_str = elem_num.replace(elem, "")
        num = int(num_str) if num_str else 1
        elements_dic[elem] = elements_dic[elem] + num if elem in elements_dic else num
    return elements_dic

def calculate_molar_mass(text):
    molar_mass = 0
    elements_dic = split_elements(text)
    elements_df = pd.read_csv("pTable.csv")
    for elem in elements_dic:
        molar_mass += elements_df.atomic_mass[elements_df.symbol == elem].to_list()[0] * elements_dic[elem]
    return molar_mass

def calculate_area_from_spectra(df, x_name, y_name, init_x, end_x):
    tmp_df = df[[x_name, y_name]]
    tmp_df = tmp_df[(init_x < tmp_df[x_name]) & (tmp_df[x_name] < end_x)]
    peak_init, abs_init = tmp_df.iloc[0]
    peak_end, abs_end = tmp_df.iloc[-1]
    p1, p2 = (peak_init, abs_init), (peak_end, abs_end)
    a = p2[1]-p1[1]
    b = p1[0]-p2[0]
    c = p1[1]*p2[0]-p1[0]*p2[1]
    diff_df = tmp_df.diff()
    area = 0
    for i in range(len(tmp_df.index)):
        try:    
            area1 = (tmp_df[y_name].iloc[i+1]+tmp_df[y_name].iloc[i])/2*diff_df[x_name].iloc[i]
            y1 = (-c-a*tmp_df[x_name].iloc[i])/b
            y2 = (-c-a*tmp_df[x_name].iloc[i+1])/b
            area2 = (y1+y2)/2*diff_df[x_name].iloc[i+1]
            if not pd.isna(area1-area2):
                    area += abs(area1-area2)
        except:
            pass
    return area

def change_hour_under_24(time_str):
    time_str = time_str.strip()
    m = re.match(r"(\d+):(\d+):(\d+)", time_str)
    days = int(m[1]) // 24
    hours = int(m[1]) % 24
    minutes = int(m[2])
    seconds = int(m[3])
    return datetime.timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

def change_time_to_seconds(time_str):
    time_str = time_str.strip()
    m = re.match(r"(\d+):(\d+):(\d+)", time_str)
    hours = int(m[1])
    minutes = int(m[2])
    seconds = int(m[3])
    return hours * 3600 + minutes * 60 + seconds

if __name__ == "__main__":
    ir_data_path = r"G:\共有ドライブ\CatEC\DATA\Takuya Suguro\Data\data\microwave_ammonia_synthesis\raw\exp1040\IR\exp1040 IR-5.csv"
    tmp_df = pd.read_csv(ir_data_path, header=20, names=["Wavenumber", "Absorbance"])
    tmp_df = tmp_df[pd.to_numeric(tmp_df.Wavenumber, errors="coerce").notna()]
    tmp_df = tmp_df.astype("float64")
    area = calculate_area_from_spectra(tmp_df, "Wavenumber", "Absorbance", 3325, 3342)
    print(area)
    print(split_elements("CH3CH2OH"))
    print(calculate_molar_mass("HAuCl4"))