window.onscroll = function() {scrollFxn()};

// https://www.w3schools.com/howto/howto_js_scroll_indicator.asp
function scrollFxn() {
    let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let scrolled = Math.floor((winScroll / height) * 100);
    $("#myBar").css("width",`${scrolled}%`);
    $("#myBar").text(`${scrolled}%`);
}