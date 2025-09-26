window.onload = function () {
    // امنع التمرير قبل تسجيل الدخول
    document.body.style.overflow = "hidden";
  
    // عرض المودال أول ما الصفحة تفتح
    document.getElementById("loginModal").style.display = "block";
  };
  
  function login() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
  
    const validUser = "dataentry1";
    const validPass = "1234";
  
    if (username === validUser && password === validPass) {
      document.getElementById("loginModal").style.display = "none";
      document.getElementById("login-error").style.display = "none";
      document.body.style.overflow = "auto"; // السماح بالتمرير بعد الدخول
    } else {
      document.getElementById("login-error").style.display = "block";
    }
  }
  