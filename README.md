
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
- Convert Product Category to a coded value (based on top-level category only)

## Image Cleaning
- Resize all images to a maximum of 512x512, ensuring the aspect ration is maintained
- Save images to a blank image created using RGB channels so all images have the same channels
- Images which are smaller either in width or height will haver a black border
- Cleaned images are saved with the same filename in a different folder

## Model for Predicting Price
Create a Linear Regression model for predicting price based on Product Name, Product Description and Location.  The first attempt was made using CountVectorise, to create features from the product name based on the count of words in the data.  This resulted in very low prediction rates, so used TF-IDF Vectoriser.  This provides a better analysis of content as it not only considers frequencies of word in one 'document', but also their frequency across all 'documents'.  Perfomed a grid search to tune the hyperparameters.  Again, the results were not impressive, althiugh considerably better than the model using CountVectorizer. It is worth considering that within the second hand market place, product details and location are probably not enough to obtain a good prediction.  For example, a dining table could range from being offered for free, to being 1000s of pounds if it were antique.  It could also be a dolls house dining table which would have a very different price.  Category and condition of item would help with better predictions.  Location I would assume has very little impact on most items for sale.  Additionally, pricing data has some anomalies, items offered for free, or listed with a zero price but 'PM me for price' will skew the results, so it may be better to exclude items with 0 price.

## Model for classifying images by category
The image and product data was combined so that a category could be linked to each image.  This was used to loop through each of the images and load them into an array, and the image data and catgeiry saved as a Pickle file to persist the numerical representations.  
I then created a pipeline which first loaded the images into an array structure transformed the images to grayscale, then transformed this using HOG to reduce the number of features but hopefully retain as much variation as possible.  The final transformed wasusing StandardScaler to standardise the features.  I selected to use the SGDClassifier, and trained it with the preprocessed data. The test data was also passed through the transformers and predictions made.

I had a lot of issues with the kernel crashing, so I reduced the data set, and also the size of the images to 128x128 (originally 512x512).  I just took the first 1/2 of the data set so this resulted in some categories not being represented, and poor distribution of samples across train and test.
The results were poor, about 28% predicted correctly.

I decided using the full data set may offer better results, however memory issues prevented this atthe current image size, so these were further reduced to 80x80.  This did result in a much better distribution of data, but unfortunately worse model performance with around 17% correct predictions, presumably since many 'features' i.e. pixels are lost by reducing the image size.

Ultimately, a machine learning model is not the optimal solution for image classification, and so the next steps will hopefully attain better results using neural networks.


 

## Project Structure

## Data Cleaning
Classes 
- CleanTabular
    - Usage:
        ct = CleanTabular('/path/to/products.csv', '\n')

- CleanImages: clean_images.py
    - Usage:
        ci = CleanImages()



