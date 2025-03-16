import cart from "./cart.js";
import products from "./products.js";

let app = document.getElementById('homeApp');
let temporaryContent = document.getElementById('homeTemporaryContent');

//load tempelate file
const loadTemplate = () => {
    fetch('/template.html')
    .then(resposne => resposne.text())
    .then(html => {
      app.innerHTML = html;
      let contentTab = document.getElementById('contentTab');
      contentTab.innerHTML = temporaryContent.innerHTML;
      temporaryContent.innerHTML = null;
      cart();
      initApp();
    })
  }
  loadTemplate();
  
  const initApp = () => {
    let listProduct = document.querySelector('.listProduct');
    listProduct.innerHTML = null;
    Product.innerHTML = `
        <main id="hero-section">
            <!-- hero content -->
            <div class="hero-content">
                <h1 class="hero-heading"> Eat the best </h1>
                <p class="hero-line">Explore and understand the culture more by tasting this amazing cuisine</p>
                <!-- Search menu available -->
                

                <div class="hero-action-btn-container">
                    <button class="btn"> View menu/Order Food </button>
                    <p class='or'> or </p>
                    <button class="btn transparent"> View Profile </button>
                </div>
            </div>

            <!-- hero image container -->
            <div class="hero-img-container">
                <div class="background-ele">
                    <div class="ellipse"></div>
                    <div class="ellipse"></div>
                    <div class="ellipse"></div>
                </div>
                <div class="forground-elements">
                    <img src="img/meatpie.jpeg" class="hero-img" alt="">
                    <img src="img/meatpie.jpeg" class="hero-img" alt="">
                    <img src="img/meatpie.jpeg" class="hero-img" alt="">
                </div>
            </div>
        </main>
      `;

    // products.forEach(product => {
    //     let newProduct = document.createElement('div');
    //     newProduct.classList.add('item');
    //     newProduct.innerHTML = `
    //       <img src="${product.image}"/>
    //       <h2>${product.name}</h2>
    //       <div class="price">$${product.price}</div>
    //       <button class='addCart'>
    //         Add To Cart
    //       </button
    //     `;
    //     listProduct.appendChild(newProduct);
    //   })
  }