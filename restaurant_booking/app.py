from datetime import date

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    booking = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        phone = request.form.get("phone", "").strip()
        booking_date = request.form.get("date", "")
        booking_time = request.form.get("time", "")
        guests_text = request.form.get("guests", "")

        if not name or not phone or not booking_date or not booking_time:
            error = "กรุณากรอกข้อมูลให้ครบทุกช่อง"
        else:
            try:
                guests = int(guests_text)
                selected_date = date.fromisoformat(booking_date)
            except ValueError:
                error = "กรุณาเลือกวันที่และจำนวนผู้เข้าที่ถูกต้อง"
            else:
                if selected_date < date.today():
                    error = "ไม่สามารถจองวันที่ผ่านมาแล้วได้"
                elif not 1 <= guests <= 20:
                    error = "จำนวนผู้เข้าต้องอยู่ระหว่าง 1 ถึง 20 คน"
                else:
                    booking = {
                        "name": name,
                        "phone": phone,
                        "date": booking_date,
                        "time": booking_time,
                        "guests": guests,
                    }

    return render_template("index.html", error=error, booking=booking)


if __name__ == "__main__":
    app.run(debug=True)
