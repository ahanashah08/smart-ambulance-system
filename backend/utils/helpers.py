def validate_location(location):
    """Validate if location input is in the correct format."""
    return isinstance(location, str) and len(location) > 0

def format_hospital_data(hospital):
    """Format hospital data for API response."""
    if hospital:
        return {"name": hospital["name"], "lat": hospital["lat"], "lon": hospital["lon"]}
    return {"error": "No hospital found"}
