import json
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILENAME = os.path.join(BASE_DIR, 'patients_database.json')


def load_database():
    """قراءة قاعدة البيانات من ملف JSON"""
    if not os.path.exists(DB_FILENAME):
        return {}
    with open(DB_FILENAME, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_database(data):
    """حفظ قاعدة البيانات في ملف JSON"""
    with open(DB_FILENAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def add_customer(name, id_number, medical_number, age, clinic, diagnosis, medicine, prescription_images, subscription_plan="بدون اشتراك", subscription_days=0):
    """
    إضافة مريض جديد من خلال البيانات القادمة من HTML عبر FastAPI.
    تُرجع الدالة (True, رسالة) في حال النجاح، أو (False, رسالة) في حال الفشل.
    """
    db = load_database()
    id_str = str(id_number)
    
    # 1. التحقق من رقم الهوية (Primary Key)
    if id_str in db:
        return False, f"فشل الإضافة: المريض صاحب رقم الهوية '{id_str}' مسجل بالفعل."
        
    # 2. التحقق من الرقم الطبي (Unique)
    for existing_id, patient_data in db.items():
        if patient_data.get("Medical_Number") == medical_number:
            return False, f"فشل الإضافة: الرقم الطبي '{medical_number}' مستخدم بالفعل."

    # 3. إعداد بيانات الاشتراك الافتراضية
    if subscription_days > 0:
        expiry_date = (datetime.now() + timedelta(days=subscription_days)).strftime('%Y-%m-%d')
        status = "فعال"
        remaining_days = subscription_days
    else:
        expiry_date = "غير محدد"
        status = "غير فعال"
        remaining_days = 0

    # إضافة المريض لقاعدة البيانات
    db[id_str] = {
        "Name": name,
        "ID_Number": id_str,
        "Medical_Number": medical_number,
        "Age": age,
        "Clinic": clinic,
        "Diagnosis": diagnosis,
        "Medicine": medicine,
        "Prescription_Images": prescription_images,
        "Subscription": {
            "Plan": subscription_plan,
            "Status": status,
            "Expiry_Date": expiry_date,
            "Remaining_Days": remaining_days # أضفنا هذا الحقل ليتوافق مع دالة التحديث الخاصة بك
        }
    }
    
    save_database(db)
    return True, "تمت إضافة المريض بنجاح!"

def check_and_update_subscriptions():
    """
    تقوم هذه الدالة بالمرور على جميع المرضى، وحساب الأيام المتبقية لاشتراكاتهم.
    إذا انتهت المدة (الأيام = 0)، يتم تحويلهم تلقائياً إلى الخطة المجانية.
    """
    db = load_database()
    today = datetime.now().date()
    database_updated = False 

    print("⏳ جاري فحص وتحديث اشتراكات المرضى...")

    for patient_id, patient_data in db.items():
        subscription = patient_data.get("Subscription", {})
        expiry_str = subscription.get("Expiry_Date", "غير محدد")

        if expiry_str != "غير محدد":
            expiry_date = datetime.strptime(expiry_str, '%Y-%m-%d').date()
            remaining_days = (expiry_date - today).days

            if remaining_days <= 0:
                subscription["Plan"] = "خطة مجانية"
                subscription["Status"] = "منتهي"
                subscription["Expiry_Date"] = "غير محدد"
                subscription["Remaining_Days"] = 0
                
                database_updated = True
                print(f"🔄 المريض '{patient_data['Name']}': انتهى الاشتراك. تم التحويل للخطة المجانية.")
            else:
                if subscription.get("Remaining_Days") != remaining_days:
                    subscription["Remaining_Days"] = remaining_days
                    database_updated = True

    if database_updated:
        save_database(db)
        print("✅ تم تحديث قاعدة البيانات بنجاح.")
    else:
        print("✅ جميع الاشتراكات سارية ولا تحتاج إلى تغيير.")