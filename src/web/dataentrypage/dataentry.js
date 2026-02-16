window.onload = function () {

    document.body.style.overflow = "hidden";
  

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
      document.body.style.overflow = "auto"; 
    
    } else {
      document.getElementById("login-error").style.display = "block";
    }
  }


  
  
  document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("patientForm");
  
    form.addEventListener("submit", async (e) => {
      e.preventDefault(); 
  
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

      
      let patients = JSON.parse(localStorage.getItem("patients")) || [];

      patients.push(patientData);
      
      localStorage.setItem("patients", JSON.stringify(patients));
      
      alert("Patient saved locally!");
      form.reset();
    });
  });
  
  document.addEventListener("DOMContentLoaded", function () {

    const med1 = document.querySelector(".med1");
    const med2 = document.querySelector(".med2");
    const med3 = document.querySelector(".med3");
    const med4 = document.querySelector(".med4");
    const med5 = document.querySelector(".med5");
  
    const second = document.querySelector(".second-mid");
    const third = document.querySelector(".third-mid");
    const fourth = document.querySelector(".fourth-mid");
    const fifth = document.querySelector(".fifth-mid");
    const sixth = document.querySelector(".sixth-mid");
  
    med1.addEventListener("change", function () {
      if (med1.value !== "") {
        second.style.display = "flex";
      }
    });
  
    med2.addEventListener("change", function () {
      if (med2.value !== "") {
        third.style.display = "flex";
      }
    });
  
    med3.addEventListener("change", function () {
      if (med3.value !== "") {
        fourth.style.display = "flex";
      }
    });
  
    med4.addEventListener("change", function () {
      if (med4.value !== "") {
        fifth.style.display = "flex";
      }
    });
  
    med5.addEventListener("change", function () {
      if (med5.value !== "") {
        sixth.style.display = "flex";
      }
    });
  
  });
  
  fetch("http://127.0.0.1:8000/add_patient", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        name: name,
        age: age,
        phone: phone
    })
})
.then(response => response.json())
.then(data => {
    alert("Patient saved successfully!");
});
