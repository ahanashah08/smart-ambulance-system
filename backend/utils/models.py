def create_hospital_model():
    """Define the MongoDB schema for hospitals."""
    db.hospitals.create_index([("location", "2dsphere")])
    return "Hospital collection indexed for geospatial queries."
