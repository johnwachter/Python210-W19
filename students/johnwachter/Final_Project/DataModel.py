from datetime import datetime
import re as rex

class Product(object):
    def __init__(self, product_id: int, product_name: str):
        self.__product_id = product_id
        self.__product_name = product_name
    def __str__(self):
        return("ProductID: {}, ProductName: {}".format(self.__product_id, self.__product_name))
    def __repr__(self):
        return "{i}:[{brk1}{pi}{p}, {c}:{cv}{brk2}]".format(brk1='{', i="Product",
                                            pi="'ProductID':",
                                            p=self.__product_id,
                                            c="'ProductName'",
                                            cv=self.__product_name, brk2='}')
    def __dict__(self):
        return {"ProductID": self.__product_id, "ProductName": self.__product_name}
    @property
    def product_id(self):
        return self.__product_id
    def set_product_id(self, product_id):
        if type(product_id) is not int:
            raise TypeError("Requires integer!")
        if product_id <= 0:
            raise ValueError("Requires value greater than zero!")
        else:
            self.__product_id = product_id
    @property
    def product_name(self):
        return self.__product_name
    def set_product_name(self, product_name):
        self.__product_name = str(product_name).strip()

class InventoryCount(object):
    def __init__(self, product: Product, count: int):
        self.__product = product
        self.__count = count
    def __str__(self):
        return ("Product: ({}), Number of products: {}".format(self.__product, self.__count))
    def __repr__(self):
        return "{i}:[{p}, {c}:{cv}]".format(i="InventoryCount",
                                            p=self.product.__repr__(),
                                            c="count",
                                            cv=self.count)
    def __dict__(self):
        return {"Product": self.__product, "Count": self.__count}
    @property
    def product(self):
        return self.__product
    def set_product(self, product):
        if type(product) is not Product: raise TypeError("Requires Product Object!")
        else:
            self.__product = product
    @property
    def count(self):
        return self.__count
    def set_count(self, count):
        if count < 0:
            raise ValueError("Negative counts are not possible")
        self.__count = count

class Inventory(object):
    def __init__(self, inventory_id: int, inventory_date: datetime.date, inventory_counts: InventoryCount = [None]):
        self.__inventory_id = inventory_id
        self.__inventory_date = inventory_date
        self.__inventory_counts = inventory_counts
    def __str__(self):
        return("InventoryID: {}, InventoryDate: {}, InventoryCount: {}".format(self.__inventory_id, self.__inventory_date, self.__inventory_counts))
    def __repr__(self):
        return "{d}, {i}:[{p}, {c}:{cv}]".format(d=self.__inventory_date,
                                            i="InventoryID",
                                            p=self.__inventory_id.__repr__(),
                                            c="count",
                                            cv=self.__inventory_counts.__repr__())
    def __dict__(self):
        return {"InventoryID": self.__inventory_id, "InventoryDate": self.__InventoryDate, "InventoryCount": self.__inventory_counts}
    @property
    def inventory_id(self):
        return self.__inventory_id
    def set_inventory_id(self, inventory_id):
        if inventory_id < 0:
            raise TypeError("Can't have a negative InventoryID!")
        else:
            self.__inventory_id = inventory_id
    @property
    def inventory_date(self):
        return self.__inventory_date
    def set_inventory_date(self, inventory_date):
        try:
            if rex.match("\d\d\d\d-\d\d-\d\d", str(inventory_date)) is None:
                raise TypeError("Not a Date! Use the following format: YYYY-MM-DD")
            else:
                self.__inventory_date = inventory_date
        except Exception as e:
            raise e
    @property
    def inventory_counts(self):
        return self.__inventory_counts
    def set_inventory_counts(self, inventory_counts):
        if inventory_counts is not None and type(inventory_counts) is InventoryCount:
            self.inventory_counts = inventory_counts

if __name__ == '__main__':
    p1 = Product(100, "ProdA")
    p2 = Product(200, "ProdB")
    #print("P1 str function produces:\n{}".format(p1))
    #print(p2.product_id)
    #print(repr(p1))
    p2.set_product_id(1)
    #print(p2.product_id)
    ic1 = InventoryCount(p1, 15)
    ic2 = InventoryCount(p2, 45)
    #print(repr(ic1))
    #print("ic1 str function produces:\n{}".format(ic1))
    invJan0119 = Inventory(1, '2019-01-01', [ic1,ic2])
    invFeb0119 = Inventory(2, '2020-01-01', [ic1])
    print("repr func produces: {}".format(repr(invFeb0119)))
    print("Str func produces: {}".format(invFeb0119))
    print("repr func produces: {}".format(repr(invJan0119)))
    print("Str func produces: {}".format(invJan0119))
    #for ic in invJan0119.inventory_counts:
        #print(invJan0119.inventory_date , ic.product.product_name, ' = ', ic.count)
    invJan0119.set_inventory_date('2019-09-01')
    #print(invJan0119.inventory_date)
    print(dict())

