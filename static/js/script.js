/*Burger */
const burger = document.querySelector('.header__burger');
const headerBody = document.querySelector('.header-body');

burger.onclick = function() {
    burger.classList.toggle('active');
    headerBody.classList.toggle('active');
    document.body.classList.toggle('lock');
}

/*mainSlider */
$(document).ready(function(){
	$('.mainSlider').slick({
		arrows:true,
		dots:true,
		slidesToShow:1,
	});
});

/*categories-choice*/
const choiceGategory = document.querySelectorAll('.choice');

choiceGategory.onclick = function() {
    choiceGategory.classList.toggle('active');
}

/*choice*/

let choice = document.querySelectorAll('.choice');

choice.forEach((item) => {
	item.onclick = function () {
		item.addEventListener('click', (e) =>{
			choice.forEach(el=>{ el.classList.remove('active'); });
			item.classList.add('active')
		})
	}
})

/*Accordion*/
$(function() {
	var Accordion = function(el, multiple) {
		this.el = el || {};
		this.multiple = multiple || false;
		var links = this.el.find('.link');
		links.on('click', {el: this.el, multiple: this.multiple}, this.dropdown)
	}
	Accordion.prototype.dropdown = function(e) {
		var $el = e.data.el,
			$this = $(this),
			$next = $this.next();

		$next.slideToggle();
		$this.parent().toggleClass('open');

		if (!e.data.multiple) {
			$el.find('.submenu').not($next).slideUp().parent().removeClass('open');
		};
	}

	var accordion = new Accordion($('#accordion'), false);
});
/*sliderProduct*/
$('.slider-for').slick({
	speed: 400,
	slidesToShow: 1,
	slidesToScroll: 1,
	arrows: false,

  });
  $('.slider-nav').slick({
	slidesToShow: 9,
	slidesToScroll: 1,
	asNavFor: '.slider-for',
	focusOnSelect: true,
	arrows: false
  });
  //   $('.slider-nav').slick('slickGoTo', index, [, dontAnimate]);
/*sliderProductFull*/
const  productSlider = document.querySelectorAll('.slider-for__img');
const  productSliderFull = document.querySelector('.overlay');
const  closeSliderFull = document.querySelector('.slider-forFull__close');


Array.from(productSlider).forEach(item => {
   item.onclick = function () {
	productSliderFull.classList.add('active');
   }
})
closeSliderFull.onclick = function () {
	productSliderFull.classList.remove('active');
   }
$('.slider-forFull').slick({
	speed: 400,
	slidesToShow: 1,
	slidesToScroll: 1,
	arrows: false,

  });
  $('.slider-navFull').slick({
	slidesToShow: 9,
 	slidesToScroll: 1,
  	asNavFor: '.slider-forFull',
  	centerMode: true,
  	focusOnSelect: true
  });