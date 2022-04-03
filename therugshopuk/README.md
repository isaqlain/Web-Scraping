# Hello

In this scrapy 🧹 project I scraped the products which was listed on the website.

### First I created virtual environment on my local computer. using the command 

python -m venv venv

### Then I installed scrapy

pip install scrapy

### To start the project with basic functionalities

scrapy genspider allrugs https://www.therugshopuk.co.uk/ 

### Create a new file under spiders folder called info.md to store our css selectors

## Now we need to make use of scrapy shell to interrogate the page

scrapy shell https://www.therugshopuk.co.uk/rugs-by-type/rugs.html

We are finding mainly 3 elements of each product i.e Name,Price and the Link

## CSS Selectors

### all_products = response.css('div.product-item-info') 
### price = response.css('div.price-box.price-final_price::text').get()
### link = response.css('a.product-item-link::attr(href)').get()
### product_name = response.css('img.product-image-photo.image::attr(alt)').get()


## Let's start our spider 🕷

### scrapy crawl allrugs -O allrugs.json



