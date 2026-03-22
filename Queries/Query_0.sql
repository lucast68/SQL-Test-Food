-- TABLE FOR USERS
CREATE TABLE Users (
	user_id INT UNSIGNED NOT NULL PRIMARY KEY, -- Users unique identifier
    country VARCHAR(50), -- Users country identifier saved in max length of 50 characters
    device_id VARCHAR(255), -- Devices identifier saved in max length of 255 characters
    registration_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of users registration
    first_purchase_timestamp TIMESTAMP -- Timestamp of user's first purchase
);

-- TABLE FOR SALES
CREATE TABLE Sales (
	purchase_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    user_id INT UNSIGNED NOT NULL,
    venue_id INT UNSIGNED,
    timestamp_utc TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_number_units INT UNSIGNED NOT NULL,
    value_eur DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- TABLE FOR USER PURCHASES
CREATE TABLE Purchases (
	purchase_id INT UNSIGNED NOT NULL,
    product_id INT UNSIGNED NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INT UNSIGNED NOT NULL,
    PRIMARY KEY (purchase_id, product_id),
    FOREIGN KEY (purchase_id) REFERENCES Sales(purchase_id)
);
    
SHOW TABLES;
DESC purchases
