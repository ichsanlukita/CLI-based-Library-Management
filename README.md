Here's your improved **README** with better **styling, formatting, and structure** to make it more engaging and readable. 🚀

---

# 📚 Library Management CLI (Simulation Game)

## 📝 Overview
This project is a **Library Management System** implemented as a **Command-Line Interface (CLI) simulation game**. It is **not a real application** but serves as a demonstration of my ability to code in **Python**. 

The purpose of this project is to **showcase my programming skills** in:
✅ Handling **user input**  
✅ **Data storage** and retrieval  
✅ Implementing **CRUD (Create, Read, Update, Delete) operations**  

⚠️ Limitations
❌ No database – Data resets when the script is restarted.
❌ No user authentication – Anyone can perform all operations.
❌ Basic error handling – Input validation is implemented but limited.

---

## ✨ Features  

### 🔹 **1. User Roles**
👤 **System Administrator (Librarian)**  
- Full control over book management and user transactions.

👥 **Library Visitor**  
- Limited access: Can view, borrow, and return books.

### 📖 **2. Book Management**
🔍 **View Books** – List all available books or search by book ID.  
➕ **Add Books** – Librarians can add new books with **ID, title, year, author, and stock information**.  
📝 **Edit Books** – Update book details such as **title, year, author, and stock**.  
🗑️ **Delete Books** – Remove books from the system.  

### 🔄 **3. Borrow & Return System**
📥 **Borrow Books** – Check availability and borrow books, reducing stock accordingly.  
📤 **Return Books** – Increase stock upon return.  

### 🔑 **4. Authentication**
🔹 Users choose their role upon login (**Admin** or **Visitor**).  
🔹 Access to features is **role-based**.  

---

## ⚙️ Installation & Usage

### 🔹 **Prerequisites**
- **Python 3.x** installed on your system  

### 🚀 **Running the Application**
1️⃣ **Clone** the repository or **download** the script.  
2️⃣ Open a **terminal** or **command prompt**.  
3️⃣ Navigate to the script’s directory.  
4️⃣ Run the script using:  
   ```sh
   python Simple_LibraryManagement_CLI.py
   ```
5️⃣ Follow the on-screen instructions to log in and navigate the menu options.  

---

## 🎮 Menu Navigation  

### 🔹 **Login Page**
```
1️⃣ Login as System Administrator (Librarian)  
2️⃣ Login as Library Visitor  
3️⃣ Exit  
```

### 🔹 **System Administrator Menu**
```
1️⃣ View Book Availability  
2️⃣ Add New Book  
3️⃣ Edit Book Information  
4️⃣ Delete Book  
5️⃣ Borrow Book  
6️⃣ Return Book  
7️⃣ Exit  
```

### 🔹 **Library Visitor Menu**
```
1️⃣ View Book Availability  
2️⃣ Borrow Book  
3️⃣ Return Book  
4️⃣ Exit  
```

---

## 🏗️ Code Structure  

📌 **Global Variables** – Stores book data and login status.  
📌 **Menu Functions** – Manages user inputs and menu navigation.  
📌 **Helper Functions** – Performs tasks such as searching, updating, and validating book records.  

---

## 📚 Example Book Data  
```python
list_book = [
    {'ID': '001', 'Title': 'Doraemon', 'Year': '1980', 'Author': 'Nobita', 'Stock': 2},
    {'ID': '002', 'Title': 'NatGeo', 'Year': '1976', 'Author': 'Johnson', 'Stock': 1},
    {'ID': '003', 'Title': 'Product Book', 'Year': '2000', 'Author': 'Product', 'Stock': 5},
]
```

---

## 🚀 Future Enhancements  
✨ **Implement a database** for persistent storage  
✨ **Add user authentication** with username and password  
✨ **Enhance the interface** with a graphical UI  

---

## 👤 Author  
💡 **Muhammad Ichsan Lukita**  

---

Now, this **README** is more visually appealing and structured in a way that is easier to read! Let me know if you need further refinements. 🚀🔥
