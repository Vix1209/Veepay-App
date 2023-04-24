var form = document.querySelector("form");

function handleForm(event) { event.preventDefault(); }
form.addEventListener('submit', handleForm);

const signupBtn = document.querySelector("#signup-btn");

let validateSignUpForm = () => {

    const emailNo = document.querySelector(".email-no");
    const emailNoValue = emailNo.value;
    const emailposition = emailNoValue.indexOf("@");
    const emaildotposition = emailNoValue.lastIndexOf(".");
    const mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    const signupPassword = document.querySelector(".password-input");
    const signupPasswordValue = signupPassword.value;

    if (!emailNoValue && !signupPasswordValue) {
        document.getElementById("remember").style.display = "none";
        document.getElementById("flexCheckDefault").style.display = "none";
        document.getElementById("forget").style.color = "#dc3545";
        emailNo.classList.add("is-invalid");
        document.getElementById("validationServer03Feedback").style.display = "block";
        signupPassword.classList.add("is-invalid");
        document.getElementById("validationServer04Feedback").style.display = "block";
        document.getElementById("basic-addon1").style.borderColor = "#dc3545";
        return false;
    }

    if (emailNoValue === "" || !emailNo.value.match(mailformat) && signupPasswordValue != "") {
        emailNo.classList.add("is-invalid");
        document.getElementById("validationServer03Feedback").style.display = "block";
        signupPassword.classList.remove("is-invalid");
        document.getElementById("validationServer04Feedback").style.display = "none";
        document.getElementById("basic-addon1").style.borderColor = "rgba(115, 126, 145, 0.7)";
        return false;
    }

    if (signupPasswordValue === "" && emailNoValue != "") {
        signupPassword.classList.add("is-invalid");
        document.getElementById("validationServer04Feedback").style.display = "block";
        document.getElementById("forget").style.color = "#dc3545";
        document.getElementById("basic-addon1").style.borderColor = "#dc3545";
        emailNo.classList.remove("is-invalid");
        document.getElementById("validationServer03Feedback").style.display = "none";
        return false
    }

    else {
        const modalToggler = document.getElementById("modal-toggler");
        const modalLink = document.getElementById("modal-link");

        document.getElementById("remember").style.display = "block";
        document.getElementById("flexCheckDefault").style.display = "block";
        document.getElementById("forget").style.color = "black";
        emailNo.classList.remove("is-invalid");
        document.getElementById("validationServer03Feedback").style.display = "none";
        signupPassword.classList.remove("is-invalid");
        document.getElementById("validationServer04Feedback").style.display = "none";
        document.getElementById("basic-addon1").style.borderColor = "rgba(115, 126, 145, 0.7)";

        modalToggler.dataset.bsToggle = "modal";
        if (modalToggler.dataset.bsToggle = "modal") {
            modalLink.setAttribute("href", "./dashboard.html");
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
