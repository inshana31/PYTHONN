# tracker.py

def create_record(city, comment, date):
    """
    Returns a travel record as a dictionary.
    :param city: str - Name of the city visited
    :param comment: str - Comment about the visit
    :param date: str - Date of visit in format 'dd-mm-yyyy'
    :return: dict - Travel record
    """
    return {
        "city": city,
        "comment": comment,
        "date": date
    }