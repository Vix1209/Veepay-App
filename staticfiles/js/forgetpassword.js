const firstPassword = document.getElementById("validationServer01");
const secondPassword = document.getElementById("validationServer02");
const forgetSubmitBtn = document.querySelector(".forget-submit");

var form = document.querySelector("form");

function handleForm(event) { event.preventDefault(); }
form.addEventListener('submit', handleForm);
let validateCreatePasswordForm = () => {
    if (firstPassword.value === "" || secondPassword.value === "" || firstPassword.value != secondPassword.value) {
        document.getElementById("validationServer02Feedback").style.display = "block";
        secondPassword.classList.add("is-invalid");
        document.getElementById("basic-addon2").style.borderColor = "#dc3545";
        forgetSubmitBtn.classList.add("disabled");
        forgetSubmitBtn.innerHTML = `Submit`;
    } else {
        document.getElementById("validationServer02Feedback").style.display = "none";
        secondPassword.classList.remove("is-invalid");
        document.getElementById("basic-addon2").style.borderColor = "rgba(115, 126, 145, 0.7)";
        forgetSubmitBtn.innerHTML = `<a class="w-75 py-2 text-white" href="./forget-password4.html" id="">Submit</a>`;
    }
}
const selects = document.querySelectorAll(".selects");

selects.forEach(select => {
    let removeDisabledSelect = () => {
        if (select === document.activeElement && forgetSubmitBtn.classList.contains("disabled")) {
            forgetSubmitBtn.classList.remove("disabled");
            document.getElementById("validationServer01Feedback").style.display = "none";
        }
    };
    select.addEventListener("focus", removeDisabledSelect);
});

const eyeIcon1 = document.querySelector(".password1");
let togglePassword1 = () => {
    const firstPassword = document.getElementById("validationServer01");

    if (firstPassword.type == "password") {
        firstPassword.setAttribute("type", "text");
        eyeIcon1.classList.remove("bi-eye");
        eyeIcon1.classList.add("bi-eye-slash");
    } else {
        firstPassword.setAttribute("type", "password");
        eyeIcon1.classList.add("bi-eye");
        eyeIcon1.classList.remove("bi-eye-slash");
    }
};

eyeIcon1.addEventListener("click", togglePassword1);


const eyeIcon2 = document.querySelector(".password2");
let togglePassword2 = () => {
    const secondPassword = document.getElementById("validationServer02");

    if (secondPassword.type == "password") {
        secondPassword.setAttribute("type", "text");
        eyeIcon2.classList.remove("bi-eye");
        eyeIcon2.classList.add("bi-eye-slash");
    } else {
        secondPassword.setAttribute("type", "password");
        eyeIcon2.classList.add("bi-eye");
        eyeIcon2.classList.remove("bi-eye-slash");
    }
};

eyeIcon2.addEventListener("click", togglePassword2);