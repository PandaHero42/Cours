const pwdInput = document.getElementById("pwd");
const meter = document.getElementById("strength");
const showPwd = document.getElementById("showPwd");

const weakPassword = ["123456", "12345", "1234", "abc123", "abc",
  "pwd", "password", "mypassword", "dragon", "monkey", "shadow",
  "master", "superman", "spiderman", "batman", "god", "sex", "boobs",
  "azerty", "qwerty", "iloveyou", "computer", "welcome", "matrix",
  "secret", "login"];

function updateMeter() {
    const pwd = pwdInput.value;
    const len = pwd.length;

    if (weakPassword.includes(pwd.toLowerCase())) {
        meter.value = 1;
        return;
    }

    meter.value = Math.min(len, 15);
}

function showPassword() {
    if (showPwd.checked) {
        pwdInput.type = "text";
    } else {
        pwdInput.type = "password";
    }
}



pwdInput.addEventListener("input", updateMeter);
showPwd.addEventListener("change", showPassword);

