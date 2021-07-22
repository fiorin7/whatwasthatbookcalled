formGroupOne = document.querySelector(".create-form .group-one");
formGroupTwo = document.querySelector(".create-form .group-two");
formGroupThree = document.querySelector(".create-form .group-three");

[formNavOne, formNavTwo, formNavThree] =
    document.querySelectorAll(".form-nav ul li");

continueButtonGroupOne = formGroupOne.querySelector(".continue-btn");
continueButtonGroupTwo = formGroupTwo.querySelector(".continue-btn");

backButtonGroupTwo = formGroupTwo.querySelector(".back-btn");
backButtonGroupThree = formGroupThree.querySelector(".back-btn");

continueButtonGroupOne.addEventListener("click", () => {
    updateCarousel(2);
});

continueButtonGroupTwo.addEventListener("click", () => {
    updateCarousel(3);
});

backButtonGroupTwo.addEventListener("click", () => {
    updateCarousel(1);
});

backButtonGroupThree.addEventListener("click", () => {
    updateCarousel(2);
});

const updateCarousel = (activeGroup) => {
    formGroupOne.style.display = "none";
    formGroupTwo.style.display = "none";
    formGroupThree.style.display = "none";

    formNavOne.classList.remove("selected");
    formNavTwo.classList.remove("selected");
    formNavThree.classList.remove("selected");

    switch (activeGroup) {
        case 1:
            formGroupOne.style.display = "block";
            formNavOne.classList.add("selected");
            break;
        case 2:
            formGroupTwo.style.display = "block";
            formNavTwo.classList.add("selected");
            break;
        case 3:
            formGroupThree.style.display = "block";
            formNavThree.classList.add("selected");
            break;

        default:
            break;
    }
};
