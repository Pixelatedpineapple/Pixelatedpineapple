document.getElementById('login-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent page reload

    const username = document.getElementById('username').value;
    if (username) {
        localStorage.setItem('username', username); // Store the username
        window.location.href = 'main.html'; // Redirect to the main page
    }
});