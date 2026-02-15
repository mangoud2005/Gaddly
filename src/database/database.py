import json
import os
from datetime import datetime

DB_FILENAME = 'patients_database.json'

def load_database():
    if not os.path.exists(DB_FILENAME):
        return {}
    with open(DB_FILENAME, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_database(data):
    with open(DB_FILENAME, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def check_and_update_subscriptions():
    """
    تقوم هذه الدالة بالمرور على جميع المرضى، وحساب الأيام المتبقية لاشتراكاتهم.
    إذا انتهت المدة (الأيام = 0)، يتم تحويلهم تلقائياً إلى الخطة المجانية.
    """
    db = load_database()
    today = datetime.now().date()
    database_updated = False # لمعرفة ما إذا احتجنا لحفظ تعديلات جديدة

    print("⏳ جاري فحص وتحديث اشتراكات المرضى...")

    for patient_id, patient_data in db.items():
        subscription = patient_data.get("Subscription", {})
        expiry_str = subscription.get("Expiry_Date", "غير محدد")

        # نتخطى المرضى الذين ليس لديهم تاريخ انتهاء أو هم بالفعل على الخطة المجانية
        if expiry_str != "غير محدد":
            # تحويل نص التاريخ المحفوظ إلى كائن تاريخ (Date Object)
            expiry_date = datetime.strptime(expiry_str, '%Y-%m-%d').date()
            
            # حساب الأيام المتبقية
            remaining_days = (expiry_date - today).days

            if remaining_days <= 0:
                # انتهى الاشتراك: يتم تصفير الأيام وتفعيل الخطة المجانية
                subscription["Plan"] = "خطة مجانية"
                subscription["Status"] = "منتهي"
                subscription["Expiry_Date"] = "غير محدد"
                subscription["Remaining_Days"] = 0
                
                database_updated = True
                print(f"🔄 المريض '{patient_data['Name']}' (هوية: {patient_id}): انتهى الاشتراك. تم التحويل للخطة المجانية.")
            else:
                # الاشتراك ما زال سارياً: نقوم بتحديث الأيام المتبقية فقط في قاعدة البيانات
                if subscription.get("Remaining_Days") != remaining_days:
                    subscription["Remaining_Days"] = remaining_days
                    database_updated = True

    # حفظ قاعدة البيانات فقط إذا حدثت تغييرات
    if database_updated:
        save_database(db)
        print("✅ تم تحديث قاعدة البيانات بنجاح.")
    else:
        print("✅ جميع الاشتراكات سارية ولا تحتاج إلى تغيير.")
