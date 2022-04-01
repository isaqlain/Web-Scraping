## Scrapy Project to extract the data from the website and export it into json

Step 1 : Setup a virtual environment called whiskyscraper.

Step 2: install scrapy in another subfolder named same as the project name i.e **pip install scrapy**

Step 3: Go to project folder type **dir** and then **cd** **project_folder** and then **tree** to list the structure of the project.

Step 4: Make use of **scrapy shell** to just interrogate the page before starting the .

fetch(’[url](https://www.fnp.com/flowers-bestsellers?promo=desk_hp_row1_pos_3)’)

**response**  When using scrapy everything is saved under this variable.

**response.css(’div.product-item-info’)** // It will return all the div blocks having class ‘product-item-info’

**response.css(’div.product-item-info’).get()**  // It return only the first occurring element

**products =** **response.css(’div.product-item-info’)**   // Storing all the product information into single variable

**len(products)**  // it will return the number of elements present in the current variable

**products.css(’a.product-item-link).get()** // Get the first item link

**products.css(’a.product-item-link::text’).get()**  // It will return the text from the link

**products.css(’a.product-item-link::text’).getall()**  // It will return the list of names of all the products

**products.css('span.price').get()  // Getting the price of the first element**

**products.css('span.price::text').get() // Extracting the text from it**

**products.css('span.price::text').getall() // Extracting the prices from all the objects.**

Result : '£71.00’ replacing the ‘£’ with nothing  **products.css('span.price::text').get().replace('£','')**

**products.css('a.product-item-link').attrib['href']  //** Getting the link

After getting all the elements we need to assemble our final file.

### Assembling [spider.py](http://spider.py) file

Add folder to VSCode and create new .py file under the spiders folder.

class WhiskySpider(scrapy.Spider):
name = 'whisky'   // name of the spider
start_urls = ['[https://www.whiskyshop.com/single-malt-scotch-whisky](https://www.whiskyshop.com/single-malt-scotch-whisky)']

**scrapy crawl whisky  //** Before executing this command make sure you under the scrapy project

**scrapy crawl whisky -O whisky.json  //**  It will produce the output file
