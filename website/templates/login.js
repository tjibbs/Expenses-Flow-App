document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    // Perform login authentication here
    var username = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    // Add your authentication logic here
    if (username === 'admin' && password === 'password') {
        alert('Login successful');
        // Redirect to the desired page after successful login
        // window.location.href = 'dashboard.html';
    } else {
        alert('Invalid username or password');
    }
});
