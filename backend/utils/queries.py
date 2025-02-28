def insert_hospital(name, lat, lon):
    db.hospitals.insert_one({"name": name, "lat": lat, "lon": lon, "location": {"type": "Point", "coordinates": [lon, lat]}})

def get_all_hospitals():
    return list(db.hospitals.find({}, {"_id": 0, "name": 1, "lat": 1, "lon": 1}))