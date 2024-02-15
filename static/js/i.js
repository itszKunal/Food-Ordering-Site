document.getElementById('search-icon').addEventListener('click',function(){
  document.getElementById('search').classList.remove('hide')
})
document.getElementById('close').addEventListener('click',function(){
  document.getElementById('search').classList.add('hide')
})

var swiper = new Swiper(".home-slider", {
  spaceBetween: 30,
  centeredSlides: true,
  autoplay: {
    delay: 4500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  loop:true,
});



var swiper = new Swiper(".review-slider", {
  spaceBetween: 20,
  centeredSlides: true,
  autoplay: {
    delay: 7500,
    disableOnInteraction: false,
  },
  loop:true,
  breakpoints: {
    0:{
      slidesPerView:1,
    },
    640:{
      slidesPerView:2,
    },
    768:{
      slidesPerView:2,
    },
    1024:{
      slidesPerView:3,
    }, 
  }
});
