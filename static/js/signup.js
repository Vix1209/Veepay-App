var form = document.querySelector("form");

function handleForm(event) { event.preventDefault(); }
form.addEventListener('submit', handleForm);

const signupBtn = document.querySelector("#signup-btn");

let validatingSignUpForm = () => {

    const firstName = document.querySelector(".first-name");
    const lastName = document.querySelector(".last-name");
    const email = document.querySelector(".email");
    const phoneNumber = document.querySelector(".p-number");
    const firstNameValue = firstName.value;
    const lastNameValue = lastName.value;
    const emailValue = email.value;
    const phoneNumberValue = phoneNumber.value;
    const emailposition = emailValue.indexOf("@");
    const emaildotposition = emailValue.lastIndexOf(".");
    const signupPassword = document.querySelector(".password-input");
    const signupPasswordValue = signupPassword.value;


    if (!firstNameValue && !lastNameValue && !emailValue && !phoneNumberValue && !signupPasswordValue) {
        document.getElementById("error").style.display = "flex";
        document.querySelector("#error p").textContent = "No information added";
        setTimeout(hideError, 1000)
        function hideError() {
            document.getElementById("error").style.display = "none";
            document.querySelector("#error p").textContent = "";
        }
        return false;
    }

    if (firstNameValue == "") {
        document.getElementById("error").style.display = "flex";
        document.querySelector("#error p").textContent = "No FirstName added";
        setTimeout(hideError, 1000)
        function hideError() {
            document.getElementById("error").style.display = "none";
            document.querySelector("#error p").textContent = "";
        }
        return false;
    }

    if (lastNameValue == "") {
        document.getElementById("error").style.display = "flex";
        document.querySelector("#error p").textContent = "No LastName added";
        setTimeout(hideError, 1000)
        function hideError() {
            document.getElementById("error").style.display = "none";
            document.querySelector("#error p").textContent = "";
        }
        return false;
    }

    if (emailValue == "") {
        document.getElementById("error").style.display = "flex";
        document.querySelector("#error p").textContent = "Add email address";
        setTimeout(hideError, 1000)
        function hideError() {
            document.getElementById("error").style.display = "none";
            document.querySelector("#error p").textContent = "";
        }
        return false;
    }

    if (emailposition < 1 || emaildotposition < emailposition + 2 || emaildotposition + 2 >= email.length) {
        document.getElementById("error").style.display = "flex";
        document.querySelector("#error p").textContent = "Enter valid email";
        setTimeout(hideError, 1000)
        function hideError() {
            document.getElementById("error").style.display = "none";
            document.querySelector("#error p").textContent = "";
        }
        return false;
    }

    if (phoneNumberValue == "") {
        document.getElementById("error").style.display = "flex";
        document.querySelector("#error p").textContent = "No Phone number added";
        setTimeout(hideError, 1000)
        function hideError() {
            document.getElementById("error").style.display = "none";
            document.querySelector("#error p").textContent = "";
        }
        return false;
    }

    if (signupPasswordValue == "") {
        document.getElementById("error").style.display = "flex";
        document.querySelector("#error p").textContent = "No password added";
        setTimeout(hideError, 1000)
        function hideError() {
            document.getElementById("error").style.display = "none";
            document.querySelector("#error p").textContent = "";
        }
        return false;
    }

    else {
        const modalToggler = document.getElementById("modal-toggler");
        const modalLink = document.getElementById("modal-link");

        modalToggler.dataset.bsToggle = "modal";
        if (modalToggler.dataset.bsToggle = "modal") {
            modalLink.setAttribute("href", "./index.html");
        }
    }
};


const eyeIcon = document.querySelector(".bi-eye");
let togglePassword = () => {
    const signupPassword = document.querySelector(".password-input");

    if (signupPassword.type == "password") {
        signupPassword.setAttribute("type", "text");
        eyeIcon.classList.remove("bi-eye");
        eyeIcon.classList.add("bi-eye-slash");
    } else {
        signupPassword.setAttribute("type", "password");
        eyeIcon.classList.add("bi-eye");
        eyeIcon.classList.remove("bi-eye-slash");
    }
};

eyeIcon.addEventListener("click", togglePassword);
