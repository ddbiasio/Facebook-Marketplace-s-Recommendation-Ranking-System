
# Facebook-Marketplace-s-Recommendation-Ranking-System

## Exploratory Data Analysis Findings

### Products
- There are no records with actual Nan / Null values
- Price is an object due to currency symbol so will need converted to float
- Price has 0 values in 92 records however this is generally valid e.g. items offered for free, open to offers, PM for price, its an ad for services where price can vary so these records should be left in the data set
- Product name has location details and source as well as a product name (separated by pipe (|) symbol) - these additional details can be removed
- Product description can have lots of emoji and special characters - these characters should be removed
- Category is a hierarchy of sub-categories, separate by '/' (430 distinct values)
- Category appears to have all valid data
- Product description appears to have all valid data.  Noted that vgc sometimes used - assumed to mean very good condition

### Images

### Search Filters
Facebook Marketplace offers the following search parameters:
- Basic description search e.g. bed
- Location Filter:
    - Select a location (town, city, neighbourhood or postal code) (Mandatory)
    - Select a radius (list options)
- Categories: 
    - each of these have their own options e..g Vehicles allows for options such as make, model, engine size
    - also to note you can select a category without entering a basic search term and Facebook presents options that match the category / location
    - category can be drilled down into a specific sub-category e.g. Clothes / Baby Clothes / Baby Shoes  
    - There may be other options presented within a category which presumably is dynamically generated from results e.g. Brand andif these have been specified when a listing is created
- Condition (All, New, Used)
- Price (Min to Max - both optional)

From the information currently available in the products data set we will therefore be interested in:
- Product Name
- Product Description
- Price
- Category
- Location


## Data Cleaning
- Remove £ from price and convert to float
- Remove emojis from product description
- Convert text to lowercase
- Extract product name from text before the first | symbol

## Image Cleaning
- Resize all images to a maximum of 512x512, ensuring the aspect ration is maintained
- Save images to a blank image created using RGB channels so all images have the same channels
- Images which are smaller either in width or height will haver a black border
- Cleaned images are saved with the same filename in a different folder

## Project Structure

## Data Cleaning
Classes 
- CleanTabular
    - Usage:
        ct = CleanTabular('/path/to/products.csv', '\n')

- CleanImages: clean_images.py
    - Usage:
        ci = CleanImages()



