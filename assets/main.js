// Load the username from local storage
const username = localStorage.getItem('username');
if (username) {
    document.getElementById('user-name').textContent = username;
}

// Handle button actions
document.getElementById('download-btn').addEventListener('click', function() {
    alert('The game will now be downloaded.');
    // Add your download logic here
});

document.getElementById('comment-btn').addEventListener('click', function() {
    document.getElementById('comment-section').style.display = 'block';
});

document.getElementById('submit-comment').addEventListener('click', function() {
    const comment = document.getElementById('comment').value;
    if (comment) {
        alert('Your comment has been submitted: ' + comment);
        // You can save the comment to a database or backend here
    }
});