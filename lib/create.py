def create_link(page_number, query) -> str:
    base_url = "https://stockx.com"
    link = base_url + query + "&page=" + str(page_number)
    return link

def create_query(filters) -> str:
    query = "/api/browse?productCategory=sneakers"
    for filter in filters:
        query = query + "&" + filter.name + "=" + filter.value
    return query

def create_sales_link(page_number,product_id) -> str:
    link = f"https://stockx.com/api/products/{product_id}/activity?state=480&limit=1000&page={page_number}"
    return link

if __name__ == "__main__":
    product_id = "f33dca85-0dd3-46a9-aec9-352f54fbbac1"
    page = 3
    link = create_sales_link(page, product_id)