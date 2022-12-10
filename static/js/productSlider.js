var swiper = new Swiper(".mySwiper", {
	observe: true,
	observeParents: true,
	observeSliderChildren: true,
	spaceBetween: 10,
	slidesPerView: 4,
	freeMode: true,
	watchSlidesProgress: true,
  });
  var swiper2 = new Swiper(".mySwiper2", {
	spaceBetween: 10,
	navigation: {
	  nextEl: ".swiper-button-next",
	  prevEl: ".swiper-button-prev",
	},
	thumbs: {
	  swiper: swiper,
	},
  });
/*Slider-product*/
const openBtn = document.querySelectorAll('.product-more button');
const closeBtn = document.querySelector('.button-close');
const slider = document.querySelectorAll('.overlay');


openBtn.forEach(item =>{
	item.onclick = function() {
		slider.forEach(el =>{
			el.classList.add('active');
		})
		
	};
	
})

closeBtn.onclick = function() {
	slider.forEach(el =>{
		el.classList.remove('active');
	})
};