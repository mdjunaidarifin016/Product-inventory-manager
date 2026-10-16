# 📦 Inventory & Sales Analytics System

## 📌 About This Project

I researched inventory management and learned how difficult it can be to keep track of product stock and sales records. To practice solving this problem, I built this Inventory & Sales Analytics System using Python.

This application allows users to manage inventory, process sales, view sales history, and check the sales summary of individual products. It uses JSON files to store inventory data and sales records persistently.

## ✨ Features

- **Process Sales:** Sell products by entering their product ID and quantity.
- **Inventory Management:** View current inventory and available stock.
- **Sales Analytics:** Calculate total revenue, total profit, and the number of successful sales for a particular product.
- **Sales History:** Store and review previous sales records.
- **Input Validation:** Handle invalid quantities and insufficient stock.
- **Error Handling:** Handle missing files, invalid JSON data, and other common errors.
- **Persistent Storage:** Save inventory and sales records in JSON files.

## 🛠️ Technologies Used

- **Python 3.12.10**
- **JSON** for data storage
- Python concepts used:
  - Loops and conditional statements
  - Lists and dictionaries
  - Functions
  - File handling
  - Exception handling
  - Custom exceptions
  - Data processing and calculations

## 📂 Project Structure

- `main.py` — Contains the main application logic, including sales processing, inventory updates, and sales analytics.
- `inventory.json` — Stores product information, including product IDs, names, purchase costs, selling prices, and available stock.
- `sales_history.json` — Stores sales records, including product IDs, quantities sold, revenue, profit, and remaining stock.
- `README.md` — Provides information about the project, its features, and instructions for using it.

## ⚙️ Requirements

- Python 3.12.10 or a compatible Python 3 version.
- A code editor, such as VS Code, or a terminal.
- No external Python packages are required; the project uses Python's built-in `json` module.

## 🚀 How to Run

1. Clone or download this repository.
2. Open the project folder in your code editor or terminal.
3. Make sure `main.py` and the required JSON files are in the correct location.
4. Run the application using:

   `python main.py`

5. Follow the menu displayed in the terminal.

## 💻 How to Use

When you run the application, a menu appears with the available options.

1. **Process a Sale:** Select option `1`, enter the product ID, and provide the quantity you want to sell.
2. **View Sales Summary:** Select option `2` and enter a product ID to view its sales analytics and current stock.
3. **View Sales History:** Select option `3` to view previous sales records.
4. **View Inventory:** Select option `4` to view the current inventory.
5. **Exit:** Select option `5` to close the application.

## 📊 Sales Analytics

The application calculates sales statistics for individual products.

- **Total Revenue:** The total amount earned from selling a particular product.
- **Total Profit:** The total profit earned from sales of that product, calculated using the difference between its selling price and purchase cost.
- **Successful Sales:** The number of recorded sales transactions for that product.
- **Available Stock:** The quantity of that product currently remaining in inventory.

The application loads the required data, processes sales, updates stock, records sales transactions, and calculates the requested statistics.

## 🗃️ Data Storage

The application uses two JSON files to maintain data between program runs.

- `inventory.json` stores product details and the current stock of each product.
- `sales_history.json` stores the details of recorded sales transactions.

When a sale is processed successfully, the application updates the inventory and records the transaction in the sales history.

**Note:** Because the application uses two separate JSON files, a failure while saving data can affect consistency between inventory and sales history.

## ⚠️ Limitations

- The application uses local JSON files rather than a database.
- It is designed as a command-line application.
- Saving inventory and sales history in separate files does not provide fully atomic transactions.

## 🔮 Future Improvements

- Add product creation, editing, and deletion.
- Introduce a database such as SQLite.
- Generate sales reports for multiple products.
- Add a graphical user interface.

## 👨‍💻 Author

**Md Junaid Arifin**


