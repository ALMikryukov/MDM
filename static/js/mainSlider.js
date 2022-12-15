new Swiper('.main-slider', {
	observe: true,
	observeParents: true,
	observeSliderChildren: true,
	navigation:{
		nextEl: '.swiper-button-next',
		prevEl: '.swiper-button-prev'
	},
	pagination: {
		el: ".swiper-pagination",
		clickable: true,
	},
});



