import json
import os

DB_FILENAME = 'patients_database.json'

def load_database():
    """تقرأ قاعدة البيانات وترجع قاموساً (Dictionary) بدلاً من قائمة."""
    if not os.path.exists(DB_FILENAME):
        return {}
    
    with open(DB_FILENAME, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_database(data):
    """تحفظ القاموس في ملف JSON."""
    with open(DB_FILENAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_customer(name, id_number, medical_number, age, clinic, diagnosis, medicine, prescription_images):
    """تضيف مريضاً جديداً مع التأكد من تفرد رقم الهوية والرقم الطبي."""
    db = load_database()
    
    # تحويل رقم الهوية إلى نص لضمان توافقه كمفتاح في JSON
    id_str = str(id_number)
    
    # 1. التحقق من المفتاح الأساسي (رقم الهوية)
    if id_str in db:
        print(f"❌ فشل الإضافة: المريض صاحب رقم الهوية '{id_str}' مسجل بالفعل في قاعدة البيانات.")
        return False
        
    # 2. التحقق من تفرد الرقم الطبي
    for existing_id, patient_data in db.items():
        if patient_data.get("Medical_Number") == medical_number:
            print(f"❌ فشل الإضافة: الرقم الطبي '{medical_number}' مستخدم بالفعل لمريض آخر (رقم هويته: {existing_id}).")
            return False

    # إضافة المريض (رقم الهوية هو المفتاح الأساسي للسجل)
    db[id_str] = {
        "Name": name,
        "ID_Number": id_str,
        "Medical_Number": medical_number,
        "Age": age,
        "Clinic": clinic,
        "Diagnosis": diagnosis,
        "Medicine": medicine,
        "Prescription_Images": prescription_images
    }
    
    save_database(db)
    print(f"✅ تمت إضافة بيانات المريض '{name}' بنجاح!")
    return True
