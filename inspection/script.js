function validateForm() {
  // Get values from the form fields
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  // Simple validation
  if (email === "" || password === "") {
    alert("Please enter both email and password.");
    return false; // Prevent form submission
  }

  // Further validation
  var validUsername = "Flaguser";
  var validPassword = atob("RmdINF8="); //third part

  if (email !== validUsername || password !== validPassword) {
    alert("Invalid username or password.");
    return false; // Prevent form submission
  }

  // Authentication successful
  alert("Login successful!");
  return true; // Allow form submission
}
