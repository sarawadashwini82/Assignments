function bookCab() {
  let name = document.getElementById("name").value.trim();
  let pickup = document.getElementById("pickup").value.trim();
  let drop = document.getElementById("drop").value.trim();
  let cabType = document.getElementById("cabType").value;
  let distance = document.getElementById("distance").value;
  let result = document.getElementById("result");

  if (name === "" || pickup === "" || drop === "" || cabType === "" || distance <= 0) {
    alert("Please fill all details correctly 🚫");
    return false;
  }

  let rate = cabType === "Mini" ? 10 : cabType === "Sedan" ? 15 : 20;
  let fare = rate * distance;

  result.style.display = "block";
  result.innerHTML = `
    ✅ <b>Booking Confirmed!</b><br><br>
    👤 <b>Name:</b> ${name}<br>
    🚕 <b>Cab:</b> ${cabType}<br>
    📍 <b>Distance:</b> ${distance} km<br>
    💰 <b>Fare:</b> ₹${fare}
  `;

  return false;
}
