from flask import Flask, render_template
import folium
import pandas as pd

app = Flask(__name__)

@app.route('/')
def map():
    # Load GeoJSON data for districts
    binawidya_geojson = 'data/kecamatan/binawidya.geojson'
    bukitraya_geojson = 'data/kecamatan/bukitraya.geojson'
    kulim_geojson = 'data/kecamatan/kulim.geojson'
    limapuluh_geojson = 'data/kecamatan/limapuluh.geojson'
    marpoyandamai_geojson = 'data/kecamatan/marpoyandamai.geojson'
    payungsekaki_geojson = 'data/kecamatan/payungsekaki.geojson'
    pekanbarukota_geojson = 'data/kecamatan/pekanbarukota.geojson'
    rumbai_geojson = 'data/kecamatan/rumbai.geojson'
    rumbaibarat_geojson = 'data/kecamatan/rumbaibarat..geojson'
    rumbaitimur_geojson = 'data/kecamatan/rumbaitimur.geojson'
    sail_geojson = 'data/kecamatan/sail.geojson'
    senapelan_geojson = 'data/kecamatan/senapelan.geojson'
    sukajadi_geojson = 'data/kecamatan/sukajadi.geojson'
    tenayanraya_geojson = 'data/kecamatan/tenayanraya.geojson'
    tuahmadani_geojson = 'data/kecamatan/tuahmadani.geojson'

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

    # Add GeoJSON layer for districts
    folium.GeoJson(binawidya_geojson, name='Binawidya').add_to(m)
    folium.GeoJson(bukitraya_geojson, name='Bukit Raya').add_to(m)
    folium.GeoJson(kulim_geojson, name='Kulim').add_to(m)
    folium.GeoJson(limapuluh_geojson, name='Lima Puluh').add_to(m)
    folium.GeoJson(marpoyandamai_geojson, name='Marpoyan Damai').add_to(m)
    folium.GeoJson(payungsekaki_geojson, name='Payung Sekaki').add_to(m)
    folium.GeoJson(pekanbarukota_geojson, name='Pekanbaru Kota').add_to(m)
    folium.GeoJson(rumbaibarat_geojson, name='Rumbai Barat').add_to(m)
    folium.GeoJson(rumbai_geojson, name='Rumbai').add_to(m)
    folium.GeoJson(rumbaitimur_geojson, name='Rumbai Timur').add_to(m)
    folium.GeoJson(sail_geojson, name='Sail').add_to(m)
    folium.GeoJson(senapelan_geojson, name='Senapelan').add_to(m)
    folium.GeoJson(sukajadi_geojson, name='Sukajadi').add_to(m)
    folium.GeoJson(tuahmadani_geojson, name='Tuah Madani').add_to(m)
    folium.GeoJson(tenayanraya_geojson, name='Tenayan Raya').add_to(m)

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
