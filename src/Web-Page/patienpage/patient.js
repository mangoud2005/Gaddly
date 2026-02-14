document.addEventListener('DOMContentLoaded', function () {
    const select = document.getElementById('disease-select');
  
    const symptomForms = document.querySelectorAll('form[class$="-dis"]');
  
    select.addEventListener('change', function () {
      const selectedOption = select.selectedOptions[0];
      const group = selectedOption.parentElement.getAttribute('data-group');
  
      // إخفاء جميع نماذج الأعراض
      symptomForms.forEach(form => {
        form.style.display = 'none';
      });
  
      // عرض النموذج المطابق للمجموعة
      const targetForm = document.querySelector(`form.${groupToClass(group)}`);
      if (targetForm) {
        targetForm.style.display = 'block';
      }
    });
  
    // تحويل group إلى اسم الكلاس
    function groupToClass(group) {
      switch (group) {
        case 'group1': return 'first-dis';
        case 'group2': return 'second-dis';
        case 'group3': return 'third-dis';
        case 'group4': return 'fourth-dis';
        case 'group5': return 'fifth-dis';
        case 'group6': return 'sixth-dis';
        case 'group7': return 'seventh-dis';
        case 'group8': return 'eighth-dis';
        case 'group9': return 'ninth-dis';
        case 'group10': return 'tenth-dis';
        case 'group11': return 'eleventh-dis';
        default: return '';
      }
    }
  
    // إخفاء كل النماذج عند بدء التشغيل
    symptomForms.forEach(form => {
      form.style.display = 'none';
    });
  });
  
// login 


  window.onload = function () {
    // امنع التمرير قبل تسجيل الدخول
    document.body.style.overflow = "hidden";

    // عرض المودال أول ما الصفحة تفتح
    document.getElementById("loginModal").style.display = "flex";
  };

  function login() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    const validUser = "patient1";
    const validPass = "1234";

    if (username === validUser && password === validPass) {
      document.getElementById("loginModal").style.display = "none";
      document.getElementById("login-error").style.display = "none";
      document.body.style.overflow = "auto"; // السماح بالتمرير بعد الدخول
    } else {
      document.getElementById("login-error").style.display = "block";
    }
  }


