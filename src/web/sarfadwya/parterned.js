window.onload = function () {
    document.getElementById("loginPopup").classList.remove("hidden");
    document.body.style.overflow = "hidden";
  };
  
  function login() {
    const area = document.getElementById("dArea").value;
  
    if (!area) {
      alert("Please select area");
      return;
    }
  
    filterOrders(area);
  
    document.getElementById("loginPopup").classList.add("hidden");
    document.body.style.overflow = "auto";
  }
  
  function filterOrders(area) {
    const cards = document.querySelectorAll(".order-card");
  
    cards.forEach(card => {
      if (card.getAttribute("data-area") === area) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });
  }
  
  function openOrder(id) {
    document.getElementById("orderNumber").innerText = "Order Number: #" + id;
    document.getElementById("orderPopup").classList.remove("hidden");
    document.body.style.overflow = "hidden";
  }
  
  function closeOrder() {
    document.getElementById("orderPopup").classList.add("hidden");
    document.body.style.overflow = "auto";
  }
  