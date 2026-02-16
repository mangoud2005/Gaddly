import os
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager

# استدعاء دوال قاعدة البيانات من ملفك
from database import add_customer, check_and_update_subscriptions

# ---------------------------------------------------------
# 1. إعداد مهام الخلفية (تحديث الاشتراكات)
# ---------------------------------------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    """هذه ال
    دالة تعمل أوتوماتيكياً مرة واحدة عند تشغيل السيرفر"""
    print("🚀 جاري تشغيل السيرفر...")
    # استدعاء دالتك لفحص وتحديث الاشتراكات قبل أن يبدأ الموقع في استقبال الزوار
    check_and_update_subscriptions()
    
    yield # هنا السيرفر يعمل ويستقبل الطلبات
    
    print("🛑 تم إيقاف السيرفر.")

# إنشاء تطبيق FastAPI وربطه بدالة بدء التشغيل
app = FastAPI(lifespan=lifespan)

# ---------------------------------------------------------
# 2. إعداد المسارات (توجيه السيرفر لمجلد الواجهات الأمامية)
# ---------------------------------------------------------
# تحديد مسار مجلد web الموجود خارج مجلد الباك إند
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(BASE_DIR,"..", "web")


# ربط الملفات الثابتة (مثل CSS والصور)
app.mount("/", StaticFiles(directory=WEB_DIR), name="static")

# ربط مجلد قوالب HTML
templates = Jinja2Templates(directory=WEB_DIR)

# ---------------------------------------------------------
# 3. روابط عرض صفحات الـ HTML (Frontend)
# ---------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def read_main(request: Request):
    """يعرض الصفحة الرئيسية (main.html)"""
    return templates.TemplateResponse("main.html", {"request": request})

@app.get("/doctor", response_class=HTMLResponse)
async def read_doctor_page(request: Request):
    """يعرض صفحة الطبيب"""
    return templates.TemplateResponse("doctor/index.html", {"request": request})

@app.get("/receptionist", response_class=HTMLResponse)
async def read_receptionist_page(request: Request):
    """يعرض صفحة موظف الاستقبال"""
    return templates.TemplateResponse("receptionist/index.html", {"request": request})

# ---------------------------------------------------------
# 4. روابط معالجة البيانات (Backend API)
# ---------------------------------------------------------
@app.post("/submit_patient")
async def submit_patient(
    request: Request,
    name: str = Form(...),            
    id_number: str = Form(...),
    medical_number: str = Form(...),
    age: int = Form(0),               # أضفنا العمر، وقيمته الافتراضية 0 إذا ترك فارغاً
    clinic: str = Form("غير محدد"),
    diagnosis: str = Form("غير محدد"),
    medicine: str = Form("غير محدد")
):
    """يستقبل بيانات المريض من نموذج الـ HTML الخاص بموظف الاستقبال ويحفظها"""
    
    # استدعاء دالتك التي كتبناها في ملف db_functions.py
    success, message = add_customer(
        name=name,
        id_number=id_number,
        medical_number=medical_number,
        age=age,
        clinic=clinic,
        diagnosis=diagnosis,
        medicine=medicine,
        prescription_images=[],  # مجهزة كقائمة فارغة حالياً
        subscription_plan="بدون اشتراك", 
        subscription_days=0
    )
    
    # إعادة رسالة للمستخدم بناءً على نتيجة الحفظ

    if success:
         return templates.TemplateResponse("receptionist/index.html", {
        "request": request,
        "success_message": message
    })
    else:
        return templates.TemplateResponse("receptionist/index.html", {
             "request": request,
             "error_message": message
    })


# ---------------------------------------------------------
# 5. كود التشغيل
# ---------------------------------------------------------
if __name__ == "__main__":
    # تشغيل السيرفر على جهازك المحلي
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)