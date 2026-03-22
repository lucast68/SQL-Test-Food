SELECT
	product_id,
    price AS most_recent_price
FROM (
	SELECT
		p.product_id,
        p.price,
        ROW_NUMBER() OVER(PARTITION BY p.product_id ORDER BY s.timestamp_utc DESC) AS rn
	FROM
		Purchases p
	JOIN
		Sales s ON p.purchase_id = s.purchase_id
) AS ranked_purchases
WHERE
	rn = 1
ORDER BY
	product_id;
