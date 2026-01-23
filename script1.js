let employees = JSON.parse(localStorage.getItem("employees")) || [];
const form = document.getElementById("empForm");
const table = document.getElementById("empTable");

form.addEventListener("submit", function(e){
  e.preventDefault();

  const empId = document.getElementById("empId").value.trim();
  const name = document.getElementById("name").value.trim();
  const dept = document.getElementById("dept").value.trim();
  const email = document.getElementById("email").value.trim();
  const salary = document.getElementById("salary").value.trim();

  // Validation
  if(!empId || !name || !dept || !email || !salary){
    alert("All fields are mandatory!");
    return;
  }

  if(isNaN(salary)){
    alert("Salary must be numeric!");
    return;
  }

  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if(!emailPattern.test(email)){
    alert("Invalid Email Format!");
    return;
  }

  const emp = { empId, name, dept, email, salary };
  employees.push(emp);
  localStorage.setItem("employees", JSON.stringify(employees));

  form.reset();
  displayEmployees();
});

function displayEmployees(){
  table.innerHTML = "";
  employees.forEach((emp, index) => {
    const row = `
      <tr>
        <td>${index + 1}</td>
        <td>${emp.empId}</td>
        <td>${emp.name}</td>
        <td>${emp.dept}</td>
        <td>${emp.email}</td>
        <td>${emp.salary}</td>
        <td>
          <button class="delete-btn" onclick="deleteEmp(${index})">Delete</button>
        </td>
      </tr>
    `;
    table.innerHTML += row;
  });
}

function deleteEmp(index){
  if(confirm("Are you sure you want to delete this employee?")){
    employees.splice(index, 1);
    localStorage.setItem("employees", JSON.stringify(employees));
    displayEmployees();
  }
}

// Load data on refresh
displayEmployees();
