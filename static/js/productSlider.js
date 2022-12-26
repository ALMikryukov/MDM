
// (НЕ РАБОТАЕТ САМ СЛАЙДЕР
// СОЗДАВАТЬ- УДАЛЯТЬ ПРИ НАЖАТИИ КНОПКИ)
/*Slider-product*/
const openBtn = document.querySelectorAll('.product-more button');
const closeBtn = document.querySelector('.button-close');
const slider = document.querySelectorAll('.overlay');
console.log("ASDASD");
const product = document.querySelectorAll('.product');
product.forEach(item =>{
		const openBtn = document.querySelectorAll('.product-more button');
		const slider = document.querySelectorAll('.overlay');
		console.log(123);
		openBtn.forEach(item =>{
			item.onclick = function() {
				console.log('wer');
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
					observe: true,
					observeParents: true,
					observeSliderChildren: true,
					spaceBetween: 10,
					navigation: {
					  nextEl: ".swiper-button-next",
					  prevEl: ".swiper-button-prev",
					},
					thumbs: {
					  swiper: swiper,
					},
				  });
				slider.forEach(el =>{
					el.classList.add('active');
				})
				
			};
			
		})
	
	

	
})


closeBtn.onclick = function() {
	slider.forEach(el =>{
		el.innerHTML = '';
	})
};
/*Slider-product-info*/
const openBtnInfo = document.querySelector('.slider-product-info__close');
const closeBtnInfo = document.querySelector('.slider-product-info__close.active');
const sliderInfo = document.querySelector('.slider-product-info__body');


closeBtnInfo.onclick =  function() {
	closeBtnInfo.classList.toggle('active');
	sliderInfo.classList.toggle('active');
}

closeBtn.onclick = function() {
	slider.forEach(el =>{
		el.classList.remove('active');
	})
};