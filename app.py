from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# API Key Here API
HERE_API_KEY = "6V6mzUA1L40nU4CMUtlJU3E3JqFjsBXvGqtnvh1ISRg"
HERE_BASE_URL = "https://router.hereapi.com/v8/routes"

# Fungsi untuk mendapatkan koordinat dari alamat (geocoding)
def geocode_address(address):
    url = "https://geocode.search.hereapi.com/v1/geocode"
    params = {"q": address, "apiKey": HERE_API_KEY}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            coords = data["items"][0]["position"]
            return coords["lat"], coords["lng"]  # (latitude, longitude)
        else:
            raise Exception("No results found for the given address.")
    else:
        raise Exception(f"Failed to fetch geocoding data: {response.status_code}, {response.text}")

# Fungsi untuk mendapatkan rute dari HERE API
def get_directions_from_here(origin_coords, destination_coords, transport_mode):
    url = HERE_BASE_URL
    headers = {"Accept": "application/json"}
    params = {
        "apiKey": HERE_API_KEY,
        "transportMode": transport_mode,
        "origin": f"{origin_coords[0]},{origin_coords[1]}",
        "destination": f"{destination_coords[0]},{destination_coords[1]}",
        "return": "polyline,summary"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch routing data: {response.status_code}, {response.text}")

# Endpoint utama
@app.route("/")
def index():
    return render_template("index.html")
    
# Fungsi untuk mengonversi detik ke menit
def seconds_to_minutes(seconds):
    return seconds / 60

# Fungsi untuk mengkonversi meter ke kilometer
def meters_to_kilometers(meters):
    return meters / 1000

# Fungsi untuk mengonversi detik ke jam dan menit
def convert_minutes_to_hours_minutes(minutes):
    hours = int(minutes // 60)  # Jam
    minutes = int(minutes % 60)  # Menit
    return hours, minutes

@app.route("/predict", methods=["POST"])
def predict():
    origin = request.form.get("origin")
    destination = request.form.get("destination")
    transport_mode = request.form.get("mode")

    if not origin or not destination or not transport_mode:
        return "All fields are required.", 400

    try:
        # Geocoding untuk origin dan destination
        origin_coords = geocode_address(origin)
        destination_coords = geocode_address(destination)

        # Mendapatkan rute dari HERE API
        directions_result = get_directions_from_here(origin_coords, destination_coords, transport_mode)

        # Mendapatkan polyline rute
        if "routes" in directions_result and len(directions_result["routes"]) > 0:
            polyline = directions_result["routes"][0]["sections"][0]["polyline"]
            summary = directions_result["routes"][0]["sections"][0]["summary"]
            
            # Mengonversi durasi dan jarak
            duration_in_minutes = seconds_to_minutes(summary["duration"])  # Durasi dalam menit
            distance_in_kilometers = meters_to_kilometers(summary["length"])  # Jarak dalam kilometer

            # Mengonversi durasi ke jam dan menit
            hours, minutes = convert_minutes_to_hours_minutes(duration_in_minutes)
            duration_formatted = f"{hours} hour(s) {minutes} minute(s)"  # Format durasi

            return render_template("result.html", origin=origin, destination=destination, 
                                   polyline=polyline, duration=duration_formatted, distance=distance_in_kilometers,
                                   origin_coords=origin_coords, destination_coords=destination_coords)
        else:
            return "No route found.", 404

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# Menjalankan aplikasi Flask
if __name__ == "__main__":
    app.run(debug=True)
