const formGroupOne = document.querySelector(".create-form .group-one");
const formGroupTwo = document.querySelector(".create-form .group-two");
const formGroupThree = document.querySelector(".create-form .group-three");

const [formNavOne, formNavTwo, formNavThree] =
    document.querySelectorAll(".form-nav ul li");

const continueButtonGroupOne = formGroupOne.querySelector(".continue-btn");
const continueButtonGroupTwo = formGroupTwo.querySelector(".continue-btn");

const backButtonGroupTwo = formGroupTwo.querySelector(".back-btn");
const backButtonGroupThree = formGroupThree.querySelector(".back-btn");

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

const defaultPage = document.getElementById("error_page").value;
if (defaultPage != "None" && defaultPage != 1) {
    updateCarousel(Number(defaultPage));
}
