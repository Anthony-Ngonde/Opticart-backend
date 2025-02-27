from db import cursor, conn


class Glass:
    TABLE_NAME = 'glasses'
    
    def __init__(self, name):
        self.id = None
        self.name = name
    
    def save(self):
        sql = f"""
            INSERT INTO {self.TABLE_NAME} (name)
            VALUES (?)
        """
        cursor.execute(sql, (self.name,))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"{self.name} saved")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name":self.name

        }
    
    @classmethod
    def find_all(cls):
        sql = f"""
            SELECT * FROM {cls.TABLE_NAME}
        """
        rows = cursor.execute(sql).fetchall()

        return [
            cls.row_to_instance(row).to_dict() for row in rows
        ]
    
    @classmethod
    def row_to_instance(cls, row):
        if row == None:
            return None
        
        glass = cls(row[1])
        glass.id = row[0]

        return glass

    @classmethod
    def drop_table(cls):
        sql = f"DROP TABLE IF EXISTS {cls.TABLE_NAME}"
        cursor.execute(sql)
        conn.commit()
        print(f"{cls.TABLE_NAME} table dropped")

    @classmethod
    def create_table(cls):
        sql = f"""
            CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"{cls.TABLE_NAME} table created")



Glass.drop_table()
Glass.create_table()


glasses = [
    "Large Round Circle Frame", "Small Round Circle Frame", "Retro Round Sunglasses", 
    "Timeless Round Eyewear", "Minimalist Eyewear", "Rimless Rectangular Sunglasses",
    "Tortoiseshell Wayfarer Glasses", "Minimalist Frameless Glasses", "Wayfarer Frame Glasses",
    "Clear Frame Angular Sunglasses", "Gold-Rimmed Round Glasses", "Clear Square Fashion Glasses",
    "CatEye-Framed Sunglasses", "Purple Cat-Eye Glasses", "Feline Chic Frames", 
    "CatEye Geometric Glasses"
]

for name in glasses:
    glass = Glass(name)
    glass.save()



class Order:
    TABLE_NAME = 'orders'

    def __init__(self, name, email, address, item_purchased, total_price):
        self.id = None
        self.name = name
        self.email = email
        self.address = address
        self.item_purchased = item_purchased
        self.total_price = total_price

    def save(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (name, email, address, item_purchased, total_price)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.name, self.email, self.address, self.item_purchased, self.total_price))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Order {self.id} saved")

    @classmethod
    def create_table(cls):
        sql = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            item_purchased TEXT NOT NULL,
            total_price REAL NOT NULL
        )
        """
        cursor.execute(sql)
        conn.commit()
        print(f"Table {cls.TABLE_NAME} created")


Order.create_table()

