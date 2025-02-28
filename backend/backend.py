from flask import Flask, request, jsonify
from pymongo import MongoClient
from config import MONGO_URI, DATABASE_NAME

app = Flask(__name__)
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

@app.route('/find_hospital', methods=['GET'])
def find_hospital():
    location = request.args.get('location')
    # Convert location to lat/lon (mocked for now)
    lat, lon = 28.6139, 77.2090  # Example: New Delhi
    hospital = db.hospitals.find_one(
        {"location": {"$near": {"$geometry": {"type": "Point", "coordinates": [lon, lat]}}}}
    )
    if hospital:
        return jsonify({"name": hospital["name"], "lat": hospital["lat"], "lon": hospital["lon"]})
    return jsonify({"error": "No hospital found"})

if __name__ == '__main__':
    app.run(debug=True)