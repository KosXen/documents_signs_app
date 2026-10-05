// index.js
const correctPassword = 'pass123';
const passwordEnteredKey = 'passwordEntered';

document.addEventListener('DOMContentLoaded', function() {
  // Check if the password has already been entered
  const passwordEntered = sessionStorage.getItem(passwordEnteredKey);

  if (passwordEntered) {
    // If the password has been entered before, display the web app content
    document.getElementById('passwordPrompt').style.display = 'none';
    document.getElementById('webAppContent').style.display = 'block';
  } else {
    // If the password has not been entered before, display the password prompt
    document.getElementById('passwordPrompt').style.display = 'block';
    document.getElementById('webAppContent').style.display = 'none';
  }
});

document.getElementById('passwordInput').addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    checkPassword();
  }
});

document.getElementById('submitButton').addEventListener('click', function() {
  checkPassword();
});

function checkPassword() {
  const passwordInput = document.getElementById('passwordInput').value;

  if (passwordInput === correctPassword) {
    sessionStorage.setItem(passwordEnteredKey, true);
    document.getElementById('passwordPrompt').style.display = 'none';
    document.getElementById('webAppContent').style.display = 'block';
  } else {
    document.getElementById('errorMessage').textContent = 'Λάθος κωδικός, δοκιμάστε ξανά.';
  }
}