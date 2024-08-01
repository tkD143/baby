const reasons = [
    "your kindness and compassion inspire me every day.",
    "you have an amazing sense of humor that always makes me laugh.",
    "your intelligence and curiosity keep me constantly learning.",
    "you are incredibly supportive and always believe in me.",
    "your smile brightens my day and makes everything better.",
    "you are my best friend, and I love sharing my life with you.",
    "you have a unique way of seeing the world that I adore.",
    "your creativity and passion for life are contagious.",
    "you make even the simplest moments special and memorable.",
    "you love me for who I am, and I love you for who you are."
];

document.getElementById("reasonForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const passcode = document.getElementById("passcode").value.trim();
    const number = parseInt(document.getElementById("reasonNumber").value.trim());

    if (passcode === "baby") {
        if (number >= 1 && number <= 10) {
            document.getElementById("result").innerText = `reason ${number}: ${reasons[number - 1]}`;
        } else {
            document.getElementById("result").innerText = "please enter a number between 1 and 10.";
        }
    } else {
        document.getElementById("result").innerText = "incorrect passcode. please try again.";
    }
});
