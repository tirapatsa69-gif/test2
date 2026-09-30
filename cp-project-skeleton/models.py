"""The booking class used by the booking-detail page."""


class Booking:
    def __init__(self, name, booking_date, booking_time, guests, status, zone):
        self.name = name
        self.booking_date = booking_date
        self.booking_time = booking_time
        self.guests = guests
        self.status = status
        self.zone = zone

    def describe(self):
        return (
            self.name
            + " เลือก "
            + self.zone
            + " "
            + "จองวันที่ "
            + self.booking_date
            + " เวลา "
            + self.booking_time
            + " จำนวน "
            + str(self.guests)
            + " คน สถานะ "
            + self.status
        )
