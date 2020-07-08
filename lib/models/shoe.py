product_id = "id"
product_title = "title"
product_brand = "brand"
product_category = "category"
product_shoe_type = "shoe"
product_color = "colorway"
product_gender = "gender"
product_release_date = "releaseTime"
product_retail_price = "retailPrice"
product_short_discription = "shortDescription"
product_media = "media"
product_image_url = "imageUrl" 

attribute_names = [
    product_title,
    product_brand,
    product_category,
    "shoeType", #for product_shoe
    product_color,
    "mainAudience", # for gender
    product_release_date,
    product_retail_price,
    product_short_discription,
    product_image_url
]

class Shoe:
    def __init__(self, json):
        self.id = json[product_id]
        self.title = json[product_title]
        self.brand = json[product_brand]
        self.category = json[product_category]
        self.shoe_type = json[product_shoe_type]
        self.color = json[product_color]
        self.gender = json[product_gender]
        self.release_time = json[product_release_date]
        self.retail_price = json[product_retail_price]
        self.short_discription = json[product_short_discription]
        media = json[product_media]
        if(media != None):
            self.image_url = media[product_image_url]
        else:
            self.image_url = None

    def get_attributes_tuple(self):
            return (
                self.id,
                self.title,
                self.brand,
                self.shoe_type,
                self.category,
                self.color,
                self.gender,
                self.release_time,
                self.retail_price,
                self.short_discription,
                self.image_url
            )