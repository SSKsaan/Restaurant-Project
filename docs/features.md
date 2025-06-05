# ✨ Features Overview

This document provides a detailed breakdown of the major features of the project. Each section outlines the user interface and interactive behavior of different pages and components to help users and contributors understand how the system is structured and functions.

## 📚 Table of Contents
- [🏠 Home](#-home)
- [🍽️ Menu](#%EF%B8%8F-menu)
- [📑 Item Details](#-item-details)
- [🛒 Cart](#-cart)
- [💳 Checkout](#-checkout)
- [🔐 Authentication](#-authentication)
- [👤 Profile](#-profile)
- [📃 Others](#-invoice)

---

### 🏠 Home

- Hero banner with animated text and responsive image
- **Featured Items Carousel**:
  - 3 items visible at a time
  - Manual navigation with left-right arrow buttons
  - Item images have Hover overlays with minimal item info
- **Featured Reviews Carousel**:
  - 3 items visible at a time
  - Smooth infinite scroll
  - Center-focused item
  - Navigated through clicking on the faded side items
- Google Map embed with CTA
- Opposite-direction sliding image strips

![Homepage][home]

---

### 🍽️ Menu

- Collapsible category filter with active highlighting
- Responsive cards grid for menu items
    - Large name and image with featured (star icon) indicator
    - price with availability indicators
    - Truncated description 
    - View Details & AJAX-based Add to cart Buttons per item

![Menu][menu]

---

### 📑 Item Details

- **Main Section**:
  - Image and content arranged side-by-side or stacked based on viewport
  - availability indicator in price and add-to-cart button
- **Recommendations**:
  - Same carousel as Featured Items on homepage.
  - Hover overlay also has 2 icon buttons for view-details and add-to-cart
  - Has 6 random **available** items
- **Reviews**:
  - Collapsible section toggle with animated width
  - Reviews styled with:
    - Header: username | datetime (left), ratings as stars (right)
    - Body: content (left-aligned), optional image (right-aligned)
  - Button for adding/editing (if logged in) through Modal form
  - JS-based star rating selector

![Item Details with Recommendations and Reviews][item]
  
---

### 🛒 Cart

- Itemized list of names & prices with per-item:
  - Quantity selector (AJAX update)
  - Remove button 
- Footer:
  - Clear cart button with confirmaion modal
  - Responsive Payment method dropdown + Checkout button

![Cart][cart]

---

### 💳 Checkout

- Collapsible Bootstrap accordion order summary, styled like an invoice
- Shows subtotal and delivery charge (only for delivery)
- Form section includes:
  - Contact number 
  - Address (only for delivery)
  - Optional note
  - Payment method dropdown and “Place Order” button
- Confirmation email sent on successful order

![Checkout][checkout]

---

### 🔐 Authentication

- Shared template for login/register with context-based variation
- Full-screen responsive background and animated rotating image 
- Smooth side change animation between login and register page
- Blured form card with page switching prompt 

![Login / Register][auth]

---

### 👤 Profile

  - Non-editable Username and Editable email fields
  - Toggleable password change section
  - “Update” and “Logout” buttons
  - Order History (list) with:
    - Order ID (button-like), Timestamp, Amount and Details button

![Profile][profile]

---

### 📃 Invoice

- Order metadata table with aligned labels + values styled like formfields
- Structured item list and aligned billing section

![Invoice style Order history][invoice]

---

### 📨 Notifications

- Django messages and JS alerts appear bottom-right
- Styled using Bootstrap alert classes with dismiss icon

---

### 🔼 Navbar

- Logo on the left, navigation icons on the right
- Icon buttons with tooltip-like text on hover
- Responsive mobile layout with a toggle menu

---

### 🔽 Footer

- **Left side**: Phone, Email, Address, Hours
- **Right side**: Social media buttons, Brand logo, Copyright info

[home]: https://SSKsaan.github.io/Restaurant-Project/assets/home.gif
[menu]: https://SSKsaan.github.io/Restaurant-Project/assets/menu.png
[item]: https://SSKsaan.github.io/Restaurant-Project/assets/item-details.gif
[auth]: https://SSKsaan.github.io/Restaurant-Project/assets/auth.gif
[cart]: https://SSKsaan.github.io/Restaurant-Project/assets/cart.gif
[checkout]: https://SSKsaan.github.io/Restaurant-Project/assets/checkout.png
[profile]: https://SSKsaan.github.io/Restaurant-Project/assets/profile.png
[invoice]: https://SSKsaan.github.io/Restaurant-Project/assets/invoice.png