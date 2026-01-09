def LatLongBinning(latitude: float, longitude: float, grid_size_latitude: int = 0.01, grid_size_longitude: int = 0.01):
    """
    A function that is used to bin latitude and longitude into different groups

    Parameters
    ----------
    latitude : float
        Latitude in degrees (-90 to 90)
    longitude : float
        Longitude in degrees (-180 to 180)
    grid_size_latitude (optional) : int
        Grid size of latitude in meters 
    grid_size_longitude (optional) : int
        Grid size of longitude in meters 

    Returns
    -------
    binned_lat_long : str
        Binned group based on latitude and longitude
    """