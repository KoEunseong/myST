import streamlit as st
import osmnx as ox
import matplotlib.pyplot as plt

# 대한민국 지도를 가져옵니다.
place_name = "대한민국"
graph = ox.graph_from_place(place_name, network_type="all")
area = ox.geocode_to_gdf(place_name)
fig, ax = ox.plot_graph(ox.project_graph(graph), show=False, close=False, figsize=(10, 8), edge_color='black')

def show_properties(district):
    # 선택한 구(district)의 속성 정보를 가져옵니다.
    properties = area[area['구(district)'] == district]
    
    # 속성 정보를 출력합니다.
    st.write(f"**{district}**의 속성 정보:")
    st.write(properties)

def main():
    # 사이드바를 만듭니다.
    st.sidebar.title("지역 선택")
    selected_district = st.sidebar.selectbox("구(district)를 선택하세요.", area['구(district)'])
    
    # 선택한 구(district)의 속성 정보를 보여줍니다.
    show_properties(selected_district)
    
    # 대한민국 지도를 출력합니다.
    st.pyplot(fig)

if __name__ == '__main__':
    main()
