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


// const product = document.querySelectorAll('.product');


// product.forEach(element =>{
// 	const openBtn = element.querySelector('.product-more button');

// 	const sliderContainer = element.querySelector('.overlay');
	
// 	openBtn.onclick = function() {
		
// 		sliderContainer.classList.add('active');
		
// 				var swiper = new Swiper(".mySwiper", {
// 					observe: true,
// 					observeParents: true,
// 					observeSliderChildren: true,
// 					spaceBetween: 10,
// 					slidesPerView: 4,
// 					freeMode: true,
// 					watchSlidesProgress: true,
// 				  });
// 				  var swiper2 = new Swiper(".mySwiper2", {
// 					observe: true,
// 					observeParents: true,
// 					observeSliderChildren: true,
// 					spaceBetween: 10,
// 					navigation: {
// 					  nextEl: ".swiper-button-next",
// 					  prevEl: ".swiper-button-prev",
// 					},
// 					thumbs: {
// 					  swiper: swiper,
// 					},
// 				  });
			
			
// 		}
		
	
// })


	
// 	document.querySelector('.swiper-wrapper').innerHTML = '';
// 	document.querySelector('.mySwiper2').innerHTML = '';

// }

/*Slider-product-info*/
// const openBtnInfo = document.querySelector('.slider-product-info__close');
// const closeBtnInfo = document.querySelector('.slider-product-info__close.active');
// const sliderInfo = document.querySelector('.slider-product-info__body');


// closeBtnInfo.onclick =  function() {
// 	closeBtnInfo.classList.toggle('active');
// 	sliderInfo.classList.toggle('active');
// }

// closeBtn.onclick = function() {
// 	slider.forEach(el =>{
// 		el.classList.remove('active');
// 	})
// };

