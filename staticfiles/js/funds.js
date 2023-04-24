const eyeIcon = document.querySelector(".bi-eye");
let togglePassword = () => {
    const signupPassword = document.querySelector(".new-password-input");

    if (signupPassword.type == "password") {
        signupPassword.setAttribute("type", "text");
        eyeIcon.classList.remove("bi-eye");
        eyeIcon.classList.add("bi-eye-slash");
    } else {
        signupPassword.setAttribute("type", "password");
        eyeIcon.classList.add("bi-eye");
        eyeIcon.classList.remove("bi-eye-slash");
    }

    if (signupPassword.type == "text") {
        console.log("yttyty")
    }
};

eyeIcon.addEventListener("click", togglePassword);