const barSection = $("#btn-hambur-section");
const linkSection = $("#navbar-links-section");
const iconMobile = $("#user-icon-section-mobile");
const linkSectionMobile = $("#link-section-mobile");
const categorys = $("#categorys");
const btnCategory = $("#btn-category");
const categorysMobile = $("#categorys-mobile");
const showAndHide = ()=>{
    if(window.innerWidth <= 768){
        barSection.removeClass("hide")
        linkSection.addClass("hide")
        categorysMobile.removeClass("hide-important");
        iconMobile.removeClass("hide")
        linkSectionMobile.removeClass("hide-important")
        btnCategory.removeClass("hide-important");
        categorys.addClass("hide-important");
    }if(window.innerWidth > 768){
        barSection.addClass("hide");
        linkSection.removeClass("hide");
        iconMobile.addClass("hide");
        linkSectionMobile.addClass("hide");
        linkSectionMobile.addClass("hide-important");
        btnCategory.addClass("hide-important");
        categorys.removeClass("hide-important");
        categorysMobile.addClass("hide-important");
    }
};
btnCategory.click(()=>{
    categorysMobile.toggle(800);
})
barSection.click(()=>{
    linkSectionMobile.toggle(800);
})
showAndHide();
window.addEventListener("resize",()=>{
    showAndHide();
})