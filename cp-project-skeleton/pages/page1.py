TITLE = "แนะนำโซนโต๊ะ"


def build():
    spots = [
        {
            "code": "window",
            "name": "โซนริมหน้าต่าง",
            "description": "รับแสงธรรมชาติ เหมาะกับการนั่งทานอาหารและถ่ายรูป",
            "recommendation": "เหมาะสำหรับ 2–4 คน",
        },
        {
            "code": "garden",
            "name": "โซนสวนด้านนอก",
            "description": "บรรยากาศเปิดโล่ง เหมาะกับคนที่ชอบนั่งรับลม",
            "recommendation": "เหมาะสำหรับครอบครัว",
        },
        {
            "code": "quiet",
            "name": "โซนมุมสงบ",
            "description": "อยู่มุมร้าน บรรยากาศเป็นส่วนตัว เหมาะกับการพูดคุย",
            "recommendation": "เหมาะสำหรับนั่งคุย",
        },
        {
            "code": "family",
            "name": "โซนครอบครัว",
            "description": "พื้นที่นั่งสบายสำหรับกลุ่มเพื่อนหรือครอบครัว",
            "recommendation": "เหมาะสำหรับ 4–6 คน",
        },
    ]

    for spot in spots:
        spot["booking_url"] = "/page2?zone=" + spot["code"]

    return {"spots": spots}
