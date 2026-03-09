# LOCACAR – Car Rental Database System

LOCACAR is a database-driven application developed for managing a **vehicle rental system**.
The project integrates **MySQL**, **Python**, and **PySimpleGUI** to provide a graphical interface for managing customers, vehicles, rentals, and pricing policies.

The system was designed following a complete **database development workflow**, including:

* Conceptual modeling (EER)
* Relational schema mapping
* Database implementation
* Application integration with a graphical interface

---

# System Overview

The system manages three main entities:

* **Clients**
* **Cars**
* **Rentals**

It allows the user to register customers, manage vehicles, create rental reservations, and process vehicle returns while automatically calculating rental costs.

The project ensures **data consistency and integrity** through database constraints, triggers, stored procedures, and transactional control.

---

# Main Interface
<img width="1544" height="742" alt="Screenshot_69" src="https://github.com/user-attachments/assets/297f2a15-8fa6-4c8d-b81d-4a4be39382f7" />

 
<img width="1513" height="723" alt="Screenshot_68" src="https://github.com/user-attachments/assets/1d4e38b9-1b2c-416e-b26b-f45e45f30613" />
 
# Conceptual Modeling (EER)

The database model was designed based on the requirements of a **vehicle rental company**.
The EER model was mapped to a relational schema implemented in **MySQL**.

Main entities:

```
CLIENT
CAR
ALUGA (RENTAL)
```
 
<img width="1367" height="693" alt="Screenshot_66" src="https://github.com/user-attachments/assets/e52194db-5581-4e25-9ac3-7179d55ae3cd" />

# Relational Model Diagram
After mapping the EER model to the relational model, the schema was defined as follows.
 
<img width="1387" height="640" alt="Screenshot_67" src="https://github.com/user-attachments/assets/bcf8f337-a224-4194-b972-63b5c110d68b" />

# Database Implementation

The database was implemented using **MySQL**.

Main features used:

* Primary Keys
* Foreign Keys
* Triggers
* Stored Procedures
* Transactions
* Isolation Level Control

---

# Transactions and Concurrency Control

The system uses the **Repeatable Read** isolation level.

This level ensures:

* consistent reads during transactions
* protection against non-repeatable reads
* good balance between performance and consistency

Transactions are handled using **MySQL Connector for Python**, ensuring:

* atomicity
* rollback in case of failure
* database consistency

---

# Triggers and Stored Procedures

The system uses **two triggers** and **three stored procedures** to enforce business rules.

Examples include:

### Car validation

A trigger verifies whether the car ID exists before inserting a rental.

### Client validation

A trigger verifies whether the client exists before allowing a rental.

### Phone number validation

A stored procedure checks whether a phone number already exists in the system before allowing a new client registration.

This prevents duplicate customer contacts.

---

# Graphical Interface

The application interface was built using **PySimpleGUI**.

Main features available in the GUI:

### Client Management

* register new clients
* list existing clients

---

### Vehicle Management

* register new cars
* list registered vehicles
* manage car categories and rental rates

---

### Rental Management

Users can:

* create a rental reservation
* select client and vehicle
* specify rental period
* verify vehicle availability

---

### Return Processing

When returning a car, the system:

* calculates the total rental cost
* applies weekly discounts when applicable
* updates the rental status
* records whether the payment is finalized or still open

---

# Pricing Calculation

Rental values are calculated using:

```
Daily Rate × Number of Days
```

If the rental period exceeds one week, the system applies the **weekly rate discount**.

Example:

```
Daily Rate = 120
7 days = 840
Weekly discount = 100

Total = 740
```

---

# Technologies Used

* Python
* MySQL
* mysql-connector-python
* PySimpleGUI

---

# Educational Context

This project was developed for the **Database Laboratory course** at the Federal University of Mato Grosso (UFMT).

It demonstrates the integration between **database design, SQL programming, and application development**.




