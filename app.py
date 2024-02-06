from folium import IFrame
from flask import Flask, render_template
import folium
import pandas as pd
import hashlib 



app = Flask(__name__)

@app.route('/')
def map():
    # Load GeoJSON data for city
    kota_pekanbaru_geojson = 'data/pekanbaru/kota_pekanbaru.geojson'
    
    # Load GeoJSON data for district
    bukit_raya_geojson = 'data/pekanbaru/bukit_raya.geojson'
    limapuluh_geojson = 'data/pekanbaru/limapuluh.geojson'
    marpoyan_damai_geojson = 'data/pekanbaru/marpoyan_damai.geojson'
    payung_sekaki_geojson = 'data/pekanbaru/payung_sekaki.geojson'
    pekanbaru_kota_geojson = 'data/pekanbaru/pekanbaru_kota.geojson'
    rumbai_pesisir_geojson = 'data/pekanbaru/rumbai_pesisir.geojson'
    rumbai_geojson = 'data/pekanbaru/rumbai.geojson'
    sail_geojson = 'data/pekanbaru/sail.geojson'
    senapelan_geojson = 'data/pekanbaru/senapelan.geojson'
    sukajadi_geojson = 'data/pekanbaru/sukajadi.geojson'
    tampan_geojson = 'data/pekanbaru/tampan.geojson'
    tenayan_raya_geojson = 'data/pekanbaru/tenayan_raya.geojson'
    
    # Load GeoJSON data for coffee shops from CSV
    coffee_shop_csv = 'data/coffeeshop/coffee_shops.csv'
    coffee_shop_df = pd.read_csv(coffee_shop_csv)

    # Create a Folium Map centered at Pekanbaru
    m = folium.Map(location=[0.5394, 101.4431], zoom_start=13)

    # Add GeoJSON layer for city
    folium.GeoJson(kota_pekanbaru_geojson, name='Kota Pekanbaru', show=False).add_to(m)

    
    # Add GeoJSON layer for districts
    folium.GeoJson(bukit_raya_geojson, name='Kecamatan Bukit Raya', show=False).add_to(m)
    folium.GeoJson(limapuluh_geojson, name='Kecamatan Limapuluh', show=False).add_to(m)
    folium.GeoJson(marpoyan_damai_geojson, name='Kecamatan Marpoyan Damai', show=False).add_to(m)
    folium.GeoJson(payung_sekaki_geojson, name='Kecamatan Payung Sekaki', show=False).add_to(m)
    folium.GeoJson(pekanbaru_kota_geojson, name='Kecamatan Pekanbaru Kota', show=False).add_to(m)
    folium.GeoJson(rumbai_pesisir_geojson, name='Kecamatan Rumbai Pesisir', show=False).add_to(m)
    folium.GeoJson(rumbai_geojson, name='Kecamatan Rumbai', show=False).add_to(m)
    folium.GeoJson(sail_geojson, name='Kecamatan Sail', show=False).add_to(m)
    folium.GeoJson(senapelan_geojson, name='Kecamatan Senapelan', show=False).add_to(m)
    folium.GeoJson(sukajadi_geojson, name='Kecamatan Sukajadi', show=False).add_to(m)
    folium.GeoJson(tampan_geojson, name='Kecamatan Tampan', show=False).add_to(m)
    folium.GeoJson(tenayan_raya_geojson, name='Kecamatan Tenayan Raya', show=False).add_to(m)
    
    # Create a FeatureGroup for the Coffee Shop layer
    coffee_shop_layer = folium.FeatureGroup(name='Coffee Shop')

    # Loop melalui setiap baris data dan tambahkan marker dengan popup ke layer Coffee Shop
    for index, row in coffee_shop_df.iterrows():
        location = [row['latitude'], row['longitude']]

        # Logic untuk mendapatkan URL gambar berdasarkan nama kedai dan district
        image_url = row['image_url']
        
        popup_content = f'<strong>{row["name"]}</strong><br>{row["address"]}<br>{row["district"]}<br><img src="{image_url}" width="100" height="100">'
        
        marker = folium.Marker(
            location=location,
            popup=folium.Popup(IFrame(html=popup_content, width=200, height=150), max_width=300),
            icon=folium.Icon(icon="fa-coffee", prefix="fa")
        )

        # Menambahkan marker ke dalam layer Coffee Shop
        marker.add_to(coffee_shop_layer)

    # Menambahkan layer Coffee Shop ke dalam peta
    coffee_shop_layer.add_to(m)


    # Add Layer Control to toggle district and coffee shop layers
    folium.LayerControl().add_to(m)
    
    # Save the map to an HTML file
    map_file_path = 'templates/map.html'
    m.save(map_file_path)

    # Render the HTML file
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
