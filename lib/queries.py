get_all_filters = """
    SELECT * FROM Filters
"""

insert_filter_catagory ="""
    REPLACE INTO 
        FilterCatagories(name)
        VALUES(?)
"""

insert_shoe = """
    INSERT INTO shoes(id,title,brand,category,shoeType,colorway,mainAudience,releaseTime,retailPrice,shortDescription,imageUrl)
    VALUES (?,?,?,?,?,?,?,?,?,?,?)
"""

insert_sale = """
    INSERT INTO sales(id,timestamp,shoeSize,amount,product_id)
    VALUES (?,?,?,?,?)
"""

insert_filter = """
    REPLACE INTO 
        Filters(name,catagory,amount)
        VALUES(?,?,?)
"""

create_shoes_table ="""
    CREATE TABLE IF NOT EXISTS
        Shoes(
            id text PRIMARY KEY,
            title text,
            brand text,
            category text,
            shoeType text,
            colorway text,
            mainAudience text,
            releaseTime text,
            retailPrice numeric,
            shortDescription text,
            imageUrl text
        );
"""

create_sales_table ="""
    CREATE TABLE IF NOT EXISTS
        Sales(
            id text PRIMARY KEY,
            timestamp text,
            shoeSize text,
            amount numeric,
            product_id text,
            FOREIGN KEY (product_id) 
            REFERENCES shoes(id)
            ON DELETE CASCADE
        );
"""

create_filters_table = """
        CREATE TABLE IF NOT EXISTS
            Filters(
                name TEXT,
                catagory TEXT,
                amount INTEGER,
                PRIMARY KEY (name, catagory)
            );
"""


get_shoe_count = """
    SELECT 
        COUNT(*) as amount 
    FROM 
        shoes
"""

get_all_shoe_ids ="""
    SELECT id 
    FROM shoes;
"""

get_sale_count="""
    SELECT COUNT(*) 
    FROM Sales;
"""

