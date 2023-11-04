const barSection = $("#btn-hambur-section");
const linkSection = $("#navbar-links-section");
const iconMobile = $("#user-icon-section-mobile");
const linkSectionMobile = $("#link-section-mobile");
const categorys = $("#categorys");
const btnCategory = $("#btn-category");
const showAndHide = ()=>{
    if(window.innerWidth <= 768){
        barSection.removeClass("hide")
        linkSection.addClass("hide")
        iconMobile.removeClass("hide")
        linkSectionMobile.removeClass("hide-important")
        btnCategory.removeClass("hide")
        categorys.addClass("hide")
    }if(window.innerWidth > 768){
        barSection.addClass("hide");
        linkSection.removeClass("hide");
        iconMobile.addClass("hide");
        linkSectionMobile.addClass("hide");
        linkSectionMobile.addClass("hide-important");
        btnCategory.addClass("hide");
        categorys.removeClass("hide")
    }
};
btnCategory.click(()=>{
    categorys.toggle(800);
})
barSection.click(()=>{
    linkSectionMobile.toggle(800);
})
showAndHide();
window.addEventListener("resize",()=>{
    showAndHide();
})