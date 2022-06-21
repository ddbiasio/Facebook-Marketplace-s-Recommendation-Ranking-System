from clean_tabular import CleanTabular
from clean_images import CleanImages

def clean_products():

    ct = CleanTabular("./products.csv", '\n')

    # ensure price is numeric
    ct.clean_currency("price")
    # remove emojis from product description
    ct.clean_emojis("product_description")
    # make text values lower case
    ct.make_lower_case("product_description")
    ct.make_lower_case("product_name")
    ct.make_lower_case("location")
    # extract product name
    ct.split_data("product_name", '|', 0)

def clean_images():
    ci = CleanImages()
    ci.clean_image_folder('images/', 'images_clean/')

if __name__ == "__main__":

    clean_products()
    clean_images()
