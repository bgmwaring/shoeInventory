# Shoe Inventory
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A simple python command line program allowing the editing and viewing of an inventory for a shoe shop.

### Status
This was part of a HyperionDEV software engineering course. The main purpose of this program was to practice the basics of OOP, and so this is unlikely to be updated into a more useful publication.

## Installation

You can clone the repository to use. The program is just one python file.

## Usage

Upon running the program, users will see the following command line interface.

```Python
Select one of the following option below:
                    cs - Capture shoe
                    va - View all
                    rs - Re-stock
                    s - Search
                    v - Value per item
                    hq - Highest quantity
                    q - Quit
                    : 
```

### Capture Shoe
By entering, ```cs``` users can add a shoe to the inventory. You will be prompted to enter the country, code, product, cost, and quantity of the item.

### View All
By entering ```va``` users will see a table of all items in the inventory.

### Re-Stock
By entering, ```rs``` users can re-stock the shoe with the lowest quantity. They will have an amount requested in the command line and the inventory will be updated based off of that.

### Search
By entering, ```s``` users will be prompted to enter a shoe code. The program will then output the inventory information of this product.

### Highest Quantity
By entering, ```hq``` the program will output the inventory information of the product with the highest stock quantity.

### Quit
By entering ```q``` the program will be stopped.

## Licence

[MIT](https://choosealicense.com/licenses/mit/)
