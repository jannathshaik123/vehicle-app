# vehicle-app

**Purpose:**  
This repository is for learning the working of signals in Django.

---

## Overview

This project demonstrates how to use Django signals to automate interactions between models such as `User`, `Buyer`, `Car`, `Order`, and `Sale`.

---

## Key Concepts

- There are two ways to set up signals:  
   **Check the Django documentation for details.**
- The main steps are:
  1. Import signals in the `apps.py` file.
  2. Set `default_app_config = '<app_name>.apps.<ConfigClassName>'`.

---

## Signal Setups

### 1. User &rarr; Buyer

- **Goal:** Create a `Buyer` instance when a `User` is created.
- **How:**
  - Use a post-save signal.
  - Sender: `User`
  - Receiver: `Buyer`
  - The signal triggers only once, during user creation.

---

### 2. Buyer &rarr; Car

- **Goal:** Assign a unique code to a `Car` when saved.
- **Methods:**
  1. **Override the `save` method:**
     ```python
     def save(self, *args, **kwargs):
             if self.code is None or self.code == "":
                     self.code = str(uuid.uuid4()).replace("-", "").upper()[:10]  # Generate a unique code if not provided
             return super().save(*args, **kwargs)
     ```
     _Traditional approach using the save method._
  2. **Use `pre_save` signals:** - The `Car` model acts as both sender and receiver. - `pre_save` is triggered right before the `save` function is executed.
  3. **Use `post_save` signals:** - More popular for updating instances after saving. - Use `save` if you need to modify an existing instance.

---

### 3. Orders Signal Setup

- **Goal:** Update `Sale` when an `Order` changes.
- **How:**
  - The sender is the many-to-many field (not the `Order` itself).
  - Example:
    ```python
    @receiver(m2m_changed, sender=Order.cars.through)
    ```
  - Use both `post` and `pre` signals, but add a condition to avoid duplicate triggers:
    ```python
    if action == "post_add" or action == "post_remove":
            # Your logic here
    ```
  - Use `get_or_create` to ensure the order instance exists.
  - Set up a sale when an order is created.

---

### 4. Sales Pre-Delete

- **Goal:** When a `Sale` is deleted, update the related `Order`.
- **How:**
  - Get the instance of the related order (`sale.order`).
  - Set the `active` status in the order to `False`.

---
