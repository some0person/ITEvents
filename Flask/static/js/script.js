document.addEventListener("DOMContentLoaded", () => {

    Array.from(document.getElementsByClassName("sourceImg")).forEach(elem => {
        elem.style.height = elem.parentElement.clientHeight.toString() + "px";
    })
})