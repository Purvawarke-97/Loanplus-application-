// REPLACE THIS WITH YOUR BACKEND EC2 PUBLIC IP OR PUBLIC DNS
// Example: 'http://54.210.12.34:5000'
const BACKEND_API_URL = 'http://YOUR_BACKEND_EC2_PUBLIC_IP:5000';

document.getElementById('loanForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const alertBox = document.getElementById('alert-box');
  alertBox.style.display = 'none';

  const payload = {
    fullName: document.getElementById('fullName').value.trim(),
    email: document.getElementById('email').value.trim(),
    mobileNumber: document.getElementById('mobileNumber').value.trim(),
    uidNumber: document.getElementById('uidNumber').value.trim(),
    panNumber: document.getElementById('panNumber').value.trim(),
    cibilScore: document.getElementById('cibilScore').value.trim(),
    loanType: document.getElementById('loanType').value
  };

  try {
    const response = await fetch(`${BACKEND_API_URL}/api/apply`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    const result = await response.json();

    if (response.ok) {
      alertBox.className = 'alert-success';
      alertBox.textContent = result.message || 'Application submitted successfully!';
      alertBox.style.display = 'block';
      document.getElementById('loanForm').reset();
    } else {
      alertBox.className = 'alert-error';
      alertBox.textContent = result.error || 'Failed to submit application.';
      alertBox.style.display = 'block';
    }
  } catch (error) {
    alertBox.className = 'alert-error';
    alertBox.textContent = 'Could not connect to backend server. Please verify backend state.';
    alertBox.style.display = 'block';
    console.error('Error:', error);
  }
});
