// var swiper = new Swiper(".mySwiper", {
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


const product = document.querySelectorAll('.product');


product.forEach(element =>{
	const openBtn = element.querySelector('.product-more button');

	const sliderContainer = element.querySelector('.overlay');
	
	openBtn.onclick = function() {
		
		sliderContainer.classList.add('active');
		sliderContainer.innerHTML = `
		
		 <div class="slider-product">
                              <div style="--swiper-navigation-color: #fff; --swiper-pagination-color: #fff"
                              class="swiper mySwiper2">
                              <div class="button-close">
                                <img src="src/img/CloseSlider.svg" alt="">
                              </div>
                              <div class="slider-product-info">
                                <div class="slider-product-info__close active ">
                      
                                </div>
                                <div class="slider-product-info__body">
                                  <div class="slider-product-info__about">
                                    <div class="slider-product__title">
                                      Описание товара:
                                    </div>
                                    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam molestias ad sit adipisci architecto asperiores unde voluptatum quisquam exercitationem veritatis, placeat, delectus repellat aliquid ullam quas omnis quasi illo vitae.
                                    Voluptatibus odio enim inventore natus sunt, sint neque omnis asperiores ratione iusto! Itaque unde quasi maiores eveniet ad quas, minima laudantium. Beatae tenetur ducimus magni nemo unde minus inventore culpa.
                                    ullam a laboriosam. Ad, totam numquam!</p>
                                  </div>
                                  <div class="slider-product-info__price">
                                    <div class="slider-product__title">
                                      Гарантия: <p>60 дней</p> 
                                    </div>
                                    <div class="slider-product__title">
                                      Вес: <p>0.7 кг</p>
                                    </div>
                                    <div class="slider-product__title">
                                      Цена: <p>500 р</p>
                                    </div>
                                    <div class="product-info__button">
                                      <button>Добавить в корзину</button>
                                  </div>
                                  </div>
                                </div>
                              
                              </div>
                              <div class="swiper-wrapper">
                                <div class="swiper-slide">
                                  <img src="{{ app.featured_image.url }}" />
                                </div>
                                <div class="swiper-slide">
                                  <img src="{{ app.featured_image.url }}" />
                                </div>
                                <div class="swiper-slide">
                                  <img src="{{ app.featured_image.url }}" />
                                </div>
                                <div class="swiper-slide">
                                  <img src="{{ app.featured_image.url }}" />
                                </div> 
                              </div>
                              <div class="swiper-buttons">
                                <div class="swiper-button-next"></div>
                                <div class="swiper-button-prev"></div>
                              </div>
                              
                            </div>
                            <div thumbsSlider="" class="swiper mySwiper">
                              <div class="swiper-wrapper">
                                <div class="swiper-slide">
                                  <img src="{{ app.featured_image.url }}" />
                                </div>
                                <div class="swiper-slide">
                                  <img src="{{ app.featured_image.url }}" />
                                </div>
                                <div class="swiper-slide">
                                  <img src="{{ app.featured_image.url }}" />
                                </div>
                                <div class="swiper-slide">
                                  <img src="{{ app.featured_image.url }}" />
                                </div> 
                              </div>
                            </div>
                            </div>
		`
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
			
			
		}

	
})

function deleteSlider() {
	sliderContainer.classList.remove('active');
	document.querySelector('.mySwiper').remove();
	document.querySelector('.mySwiper2').remove();

}

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