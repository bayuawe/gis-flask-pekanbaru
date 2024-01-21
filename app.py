from flask import Flask, render_template
import folium
import pandas as pd

app = Flask(__name__)

@app.route('/')
def map():
    # Load GeoJSON data for city
    kota_pekanbaru_geojson = 'data/pekanbaru_districts/kota_pekanbaru.geojson'
    
    # Load GeoJSON data for city
    bukit_raya_geojson = 'data/pekanbaru_districts/bukit_raya.geojson'
    limapuluh_geojson = 'data/pekanbaru_districts/limapuluh.geojson'
    marpoyan_damai_geojson = 'data/pekanbaru_districts/marpoyan_damai.geojson'
    payung_sekaki_geojson = 'data/pekanbaru_districts/payung_sekaki.geojson'
    pekanbaru_kota_geojson = 'data/pekanbaru_districts/pekanbaru_kota.geojson'
    rumbai_pesisir_geojson = 'data/pekanbaru_districts/rumbai_pesisir.geojson'
    rumbai_geojson = 'data/pekanbaru_districts/rumbai.geojson'
    sail_geojson = 'data/pekanbaru_districts/sail.geojson'
    senapelan_geojson = 'data/pekanbaru_districts/senapelan.geojson'
    sukajadi_geojson = 'data/pekanbaru_districts/sukajadi.geojson'
    tampan_geojson = 'data/pekanbaru_districts/tampan.geojson'
    tenayan_raya_geojson = 'data/pekanbaru_districts/tenayan_raya.geojson'
    
    # Load GeoJSON data for coffee shops from CSV
    coffee_shop_csv = 'data/coffeeshop/coffee_shops.csv'
    coffee_shop_df = pd.read_csv(coffee_shop_csv)

    # Convert CSV data to GeoJSON
    coffee_shop_geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    # Add coffee shop data to GeoJSON
    for index, row in coffee_shop_df.iterrows():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [row['longitude'], row['latitude']]
            },
            "properties": {
                "name": row['name'],
                "address": row['address'],
                "category": '',
                "district": row['district']
            }
        }
        coffee_shop_geojson['features'].append(feature)

    # Create a Folium Map centered at Pekanbaru
    m = folium.Map(location=[0.5394, 101.4431], zoom_start=13)

    # Add GeoJSON layer for city
    folium.GeoJson(kota_pekanbaru_geojson, name='Kota Pekanbaru').add_to(m)
    
    # Add GeoJSON layer for districts
    folium.GeoJson(bukit_raya_geojson, name='Kecamatan Tampan').add_to(m)
    folium.GeoJson(limapuluh_geojson, name='Kecamatan Limapuluh').add_to(m)
    folium.GeoJson(marpoyan_damai_geojson, name='Kecamatan Marpoyan Damai').add_to(m)
    folium.GeoJson(payung_sekaki_geojson, name='Kecamatan Payung Sekaki').add_to(m)
    folium.GeoJson(pekanbaru_kota_geojson, name='Kecamatan Pekanbaru Kota').add_to(m)
    folium.GeoJson(rumbai_pesisir_geojson, name='Kecamatan Rumbai Pesisir').add_to(m)
    folium.GeoJson(rumbai_geojson, name='Kecamatan Rumbai').add_to(m)
    folium.GeoJson(sail_geojson, name='Kecamatan Sail').add_to(m)
    folium.GeoJson(senapelan_geojson, name='Kecamatan Senapelan').add_to(m)
    folium.GeoJson(sukajadi_geojson, name='Kecamatan Sukajadi').add_to(m)
    folium.GeoJson(tampan_geojson, name='Kecamatan Tampan').add_to(m)
    folium.GeoJson(tenayan_raya_geojson, name='Kecamatan Tenayan Raya').add_to(m)

    # Add GeoJSON layer for coffee shops
    folium.GeoJson(coffee_shop_geojson, name='Coffee Shops').add_to(m)

    # Add Layer Control to toggle district and coffee shop layers
    folium.LayerControl().add_to(m)

    # Save the map to an HTML file
    map_file_path = 'templates/map.html'
    m.save(map_file_path)

    # Render the HTML file
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
