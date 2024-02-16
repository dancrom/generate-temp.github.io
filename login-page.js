const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "pbtc" && password === "PbTc150224!") {
        alert('logged in')
        window.location.href = 'generate.html'
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})
