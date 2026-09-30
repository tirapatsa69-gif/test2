from datetime import date, time

import storage

TITLE = "จองโต๊ะ"
ZONES = [
    {"value": "window", "name": "โซนริมหน้าต่าง"},
    {"value": "garden", "name": "โซนสวนด้านนอก"},
    {"value": "quiet", "name": "โซนมุมสงบ"},
    {"value": "family", "name": "โซนครอบครัว"},
]


def build(query):
    items = storage.load()
    waiting_count = 0

    for item in items:
        if item.get("status", "") == "รอยืนยัน":
            waiting_count = waiting_count + 1

    return {
        "count": len(items),
        "waiting_count": waiting_count,
        "zones": ZONES,
        "selected_zone": query.get("zone", ""),
    }


def handle(form):
    name = form.get("name", "").strip()
    phone = form.get("phone", "").strip()
    booking_date = form.get("date", "")
    booking_time = form.get("time", "")
    guests_text = form.get("guests", "")
    zone_value = form.get("zone", "")
    zone_name = ""

    for zone in ZONES:
        if zone["value"] == zone_value:
            zone_name = zone["name"]

    if name == "" or phone == "" or booking_date == "" or booking_time == "" or zone_name == "":
        return "กรุณากรอกข้อมูลให้ครบทุกช่อง"

    try:
        guests = int(guests_text)
        selected_date = date.fromisoformat(booking_date)
        time.fromisoformat(booking_time)
    except ValueError:
        return "กรุณากรอกวันที่ เวลา และจำนวนคนให้ถูกต้อง"

    if selected_date < date.today():
        return "ไม่สามารถจองวันที่ผ่านมาแล้วได้"

    if guests < 1 or guests > 20:
        return "จำนวนผู้เข้าต้องอยู่ระหว่าง 1 ถึง 20 คน"

    items = storage.load()
    items.append({
        "name": name,
        "phone": phone,
        "date": booking_date,
        "time": booking_time,
        "guests": guests,
        "zone": zone_name,
        "status": "รอยืนยัน",
    })
    storage.save(items)
    return "ส่งคำขอจองโต๊ะแล้ว"
