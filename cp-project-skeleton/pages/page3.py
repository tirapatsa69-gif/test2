import models
import storage

TITLE = "รายละเอียดการจอง"


def build(query):
    items = storage.load()

    if len(items) == 0:
        return {
            "booking": None,
            "sentence": "",
            "index": 0,
            "prev": None,
            "next": None,
            "count": 0,
        }

    index = 0
    requested_index = query.get("i", "")
    if requested_index.isdigit():
        index = int(requested_index)

    if index >= len(items):
        index = len(items) - 1

    row = items[index]
    booking = models.Booking(
        row.get("name", ""),
        row.get("date", ""),
        row.get("time", ""),
        row.get("guests", 0),
        row.get("status", ""),
        row.get("zone", "ไม่ระบุ"),
    )

    previous_index = None
    next_index = None
    if index > 0:
        previous_index = index - 1
    if index < len(items) - 1:
        next_index = index + 1

    return {
        "booking": row,
        "sentence": booking.describe(),
        "index": index,
        "prev": previous_index,
        "next": next_index,
        "count": len(items),
    }
