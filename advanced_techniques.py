#Task 1

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))
catalog3 = (("Television", 350), ("HDMI Cables", 25))
catalog4 = (("Speaker", 250), ("Monitor", 400))

def display_catalogs(*catalog):
    big_catalog = ()
    for cat in catalog:
        big_catalog += cat
    for item in big_catalog:
        print(f"Item: {item[0]} costs ${item[1]} ")

display_catalogs(catalog1, catalog2, catalog4)