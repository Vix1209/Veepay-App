
const network = document.getElementById("network");
const dataValue = document.getElementById("datavalue");


let changeValue = () => {
    if (network.value == "select-network") {
        dataValue.innerHTML = ""
    } else if (network.value == "mtn") {
        dataValue.innerHTML = `
        <option value="datavalue ">500mb-30 Days</option>
        <option value="datavalue ">1gb-30 Days</option>
        <option value="datavalue ">2gb-30 Days</option>
        <option value="datavalue ">3gb-30 Days</option>
        <option value="datavalue ">5gb-30 Days</option>
        <option value="datavalue ">6gb-7 Days</option>
        <option value="datavalue ">10gb-30 Days</option>
        <option value="datavalue ">20gb-30 Days</option>
        <option value="datavalue ">40gb-30 Days</option>
        <option value="datavalue ">120gb-60 Days</option>
        `
    } else if (network.value == "glo") {
        dataValue.innerHTML = `
        <option value="datavalue ">1.3gb-14 Days</option>
        <option value="datavalue ">2.9gb-30 Days</option>
        <option value="datavalue ">4.1gb-30 Days</option>
        <option value="datavalue ">5.8gb-30 Days</option>
        <option value="datavalue ">7.7gb-30 Days</option>
        <option value="datavalue ">11gb-30 Days</option>
        <option value="datavalue ">12gb-30 Days</option>
        <option value="datavalue ">29.5gb-30 Days</option>
        <option value="datavalue ">50gb-30 Days</option>
        <option value="datavalue ">93gb-60 Days</option>
        `
    } else if (network.value == "airtel" || network.value == "9mobile") {
        dataValue.innerHTML = `
        <option value="datavalue ">500mb-30 Days</option>
        <option value="datavalue ">1.5gb-30 Days</option>
        <option value="datavalue ">4.5gb-30 Days</option>
        <option value="datavalue ">11gb-30 Days</option>
        <option value="datavalue ">15gb-30 Days</option>
        <option value="datavalue ">40gb-30 Days</option>
        <option value="datavalue ">75gb-30 Days</option>
        `
    }
}

network.addEventListener("change", changeValue);

var form = document.querySelector("form");

function handleForm(event) { event.preventDefault(); }
form.addEventListener('submit', handleForm);


const phoneNumber = document.querySelector(".phonenumber");
const phoneNumberValue = document.querySelector(".phonenumber").value;
const amount = document.querySelector(".amount");
const submitBtn = document.querySelector("button");
const inputs = document.querySelectorAll(".input-group input");
const selects = document.querySelectorAll(".input-group select");

inputs.forEach(input => {
    let removeDisabledInput = () => {
        if (input === document.activeElement && submitBtn.classList.contains("disabled")) {
            submitBtn.classList.remove("disabled");
            phoneNumber.classList.remove("is-invalid");
            document.getElementById("validationServer01Feedback").style.display = "none";
        }
    }
    input.addEventListener("focus", removeDisabledInput);
});

selects.forEach(select => {
    let removeDisabledSelect = () => {
        if (select === document.activeElement && submitBtn.classList.contains("disabled")) {
            submitBtn.classList.remove("disabled");
            phoneNumber.classList.remove("is-invalid");
            document.getElementById("validationServer01Feedback").style.display = "none";
        }
    };
    select.addEventListener("focus", removeDisabledSelect);
});

let validateSmePurchase = () => {
    const phoneNumber = document.querySelector(".phonenumber");
    const phoneNumberValue = document.querySelector(".phonenumber").value;
    const amount = document.querySelector(".amount");
    const dataValue = document.getElementById("datavalue");
    const submitBtn = document.querySelector("button");

    if (dataValue.value === "") {
        return false
    }

    if (phoneNumber.value === "") {
        phoneNumber.classList.add("is-invalid")
        document.getElementById("validationServer01Feedback").style.display = "block"
        submitBtn.classList.add("disabled")
        return false
    }

    if (isNaN(phoneNumber.value)) {
        phoneNumber.classList.add("is-invalid")
        document.getElementById("validationServer01Feedback").style.display = "block"
        submitBtn.classList.add("disabled")
        return false
    }

    if (phoneNumberValue.length !== 11) {
        phoneNumber.classList.add("is-invalid")
        document.getElementById("validationServer01Feedback").style.display = "block"
        submitBtn.classList.add("disabled")
        return false
    }

    if (isNaN(amount)) {
        return false
    }
}