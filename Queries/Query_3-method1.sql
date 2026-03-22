SELECT
	p.product_id,
    p.price AS most_recent_price
FROM
	Purchases p
JOIN
	Sales s ON p.purchase_id = s.purchase_id
WHERE
	(p.product_id, s.timestamp_utc) IN (
		SELECT
			pp.product_id,
            MAX(ss.timestamp_utc)
		FROM
			Purchases pp
		JOIN
			Sales ss ON pp.purchase_id = ss.purchase_id
		GROUP BY
			pp.product_id
	)
ORDER BY
	p.product_id;
