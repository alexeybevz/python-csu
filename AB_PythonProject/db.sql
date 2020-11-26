CREATE TABLE product (
	sku nvarchar(20) NOT NULL,
	type_product nvarchar(30) NOT NULL,
	name nvarchar(100) NOT NULL,
	qty decimal(18,5) NOT NULL,
	manufacter nvarchar(100) NOT NULL,
	price decimal(18,2) NOT NULL,
	size decimal(18,2) NULL,
	color nvarchar(50) NULL,
	type_print nvarchar(50) NULL,
	shoe_laces nvarchar(50) NULL,
	PRIMARY KEY(sku),
);
GO

CREATE NONCLUSTERED INDEX IX_name ON product (name ASC);
GO