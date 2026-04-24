// Show/Hide Password
const passwordInput = document.getElementById('password');
const togglePassword = document.getElementById('togglePassword');
togglePassword.addEventListener('click', () => {
    if(passwordInput.type === 'password'){
        passwordInput.type = 'text';
        togglePassword.textContent = 'Hide Password';
    } else {
        passwordInput.type = 'password';
        togglePassword.textContent = 'Show Password';
    }
});

// Form validation
const form = document.getElementById('loginForm');
form.addEventListener('submit', (e) => {
    const email = document.getElementById('email').value.trim();
    const password = passwordInput.value.trim();
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if(!emailRegex.test(email)){
        alert('Please enter a valid email.');
        e.preventDefault();
        return;
    }

    if(password.length < 6){
        alert('Password must be at least 6 characters.');
        e.preventDefault();
    }
});