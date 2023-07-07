Web Crawler with Scrapy Spider

This project consists of a web crawler developed using the Scrapy framework. The web crawler is designed to extract data from web pages related to quotations.

Installation:

Make sure you have Python and pip installed on your system. Then, run the following command to install the required dependencies:

pip install scrapy

Running the Crawler:

To run the web crawler, follow the steps below:

1. Navigate to the directory where the spider file is located.

2. Run the following command in the terminal to start executing the spider:

scrapy runspider spider_file_name.py

Replace 'spider_file_name.py' with the actual name of the file containing the spider code.

Code Functionality:

The spider code consists of the 'Web_scrapy' class that inherits from the Scrapy 'Spider' class. The 'Web_scrapy' class is responsible for scraping quotation data from web pages.

The spider follows the following flow:

1. Upon initialization, the spider is configured with the name "Ultima Online" and the initial URL "https://pt.wikipedia.org/wiki/Ultima_Online".

2. The 'parse' method is called to process the HTTP response from the initial page. It extracts the quotation data present on the main page.

3. Next, the spider extracts the links to secondary pages and sends HTTP requests to each of them, calling the 'parse_secondary' method as a callback to process the responses from the secondary pages.

4. The 'parse_secondary' method is responsible for extracting the quotation data from the secondary pages.

5. The extracted data is returned using the 'yield' statement, allowing Scrapy to process it.

Make sure to adjust the CSS selectors in the 'parse' and 'parse_secondary' methods according to the HTML structure of the pages you want to scrape.

Contributing:

Contributions are welcome! Feel free to submit pull requests or report issues.


