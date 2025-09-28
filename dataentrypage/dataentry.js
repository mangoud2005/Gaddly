// window.onload = function () {
//     // امنع التمرير قبل تسجيل الدخول
//     document.body.style.overflow = "hidden";
  
//     // عرض المودال أول ما الصفحة تفتح
//     document.getElementById("loginModal").style.display = "block";
//   };
  
//   function login() {
//     const username = document.getElementById("username").value.trim();
//     const password = document.getElementById("password").value.trim();
  
//     const validUser = "dataentry1";
//     const validPass = "1234";
  
//     if (username === validUser && password === validPass) {
//       document.getElementById("loginModal").style.display = "none";
//       document.getElementById("login-error").style.display = "none";
//       document.body.style.overflow = "auto"; // السماح بالتمرير بعد الدخول
//     } else {
//       document.getElementById("login-error").style.display = "block";
//     }
//   }

  /////
  
  
  document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("patientForm");
  
    form.addEventListener("submit", async (e) => {
      e.preventDefault(); // prevent reload
  
      const patientData = {
        name: document.querySelector(".name").value,
        idNumber: document.querySelector(".idnumber").value,
        medicalNumber: document.querySelector(".mednumber").value,
        age: document.querySelector(".age").value,
        clinic: document.querySelector(".clinic").value,
        diagnosis: document.querySelector(".diagnosis").value,
        medicine: document.querySelector(".med1").value,
        regimen: document.querySelector(".reg1").value,
        duration: document.querySelector(".dura1").value,
      };
  
      try {
        const res = await fetch("http://localhost:5000/api/patients", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(patientData),
        });
  
        if (res.ok) {
          alert("Patient added successfully!");
          form.reset();
        } else {
          alert("Failed to save patient.");
        }
      } catch (err) {
        console.error("Error:", err);
        alert("Something went wrong.");
      }
    });
  });
  
  