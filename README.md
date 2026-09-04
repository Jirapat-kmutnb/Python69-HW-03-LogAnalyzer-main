# 🧪 Python-68-HW03-LogAnalyze

วัตถุประสงค์:  
พัฒนาโปรแกรมวิเคราะห์พฤติกรรมผู้ใช้งานจากไฟล์ Log ที่มีรูปแบบมาตรฐาน โดยใช้ฟังก์ชัน `analyze_user_activity(log_file_path: str) -> dict` ในการวิเคราะห์

---

## 📂 โครงสร้างไฟล์ที่ใช้

- `loganalyze.py` — ฟังก์ชันหลักสำหรับวิเคราะห์ Log
- `test_lognalyze.py` — ไฟล์ทดสอบอัตโนมัติด้วย `unittest`
- `activity.log` — ไฟล์ตัวอย่าง Log สำหรับการทดสอบ

---

## 📜 รูปแบบข้อมูลในไฟล์ Log

แต่ละบรรทัดประกอบด้วยข้อมูล:

```
<timestamp> <user_id> <action> <duration>
```

ตัวอย่าง:
```
2025-08-01T10:00:00 u001 login 120
2025-08-01T10:02:05 u002 login 200
2025-08-01T10:04:00 u001 view 0
...
```

---

## 🔧 วิธีใช้งานฟังก์ชัน

### โค้ดหลัก (ใน `loganalyze.py`):

```python
def analyze_user_activity(log_file_path: str) -> dict:
    #your code here
    pass

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)
```

### ตัวอย่างผลลัพธ์:

```python
{
  "total_users": 2,
  "action_counts": {"login": 2, "view": 2, "submit": 1, "logout": 2},
  "most_active_user": "u002",
  "average_session_time": 160.0
}
```

---

## ✅ วิธีรันทดสอบด้วย `unittest`

1. เปิด Terminal หรือ Command Prompt ในไดเรกทอรีที่มีไฟล์ทั้งสอง
2. รันคำสั่ง:

```bash
python -m unittest test_loganalyze.py
```

---


## 📌 หมายเหตุ

- หากมีบรรทัดผิดรูปแบบใน Log ให้ข้าม
- รองรับไฟล์ Log ที่มีหลายพันรายการ
- ทดสอบทั้งกรณี: ข้อมูลปกติ / ไฟล์ว่าง / ข้อมูลไม่สมบูรณ์

---


