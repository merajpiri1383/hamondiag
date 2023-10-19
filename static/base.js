const brand = $("#brand-section");
const barSection = $("#btn-hambur-section");
const linkSection = $("#navbar-links-section");
const showAndHide = ()=>{
    if(window.innerWidth <= 768){
        barSection.removeClass("hide")
        brand.addClass("hide")
        linkSection.addClass("hide")
    }if(window.innerWidth > 768){
        barSection.addClass("hide");
        brand.removeClass("hide");
        linkSection.removeClass("hide");
    }
};
barSection.click(()=>{
    linkSection.toggle(1000);
})
showAndHide();
window.addEventListener("resize",()=>{
    showAndHide();
})