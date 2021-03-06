CREATE TABLE dry_season_crops_products (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_321 VARCHAR(255),
  ward_321 VARCHAR(255),
  village_321 VARCHAR(255),
  hhid_321 VARCHAR(255),
  dry_rains_crops_products VARCHAR(255),
  dry_rains_production_Quantity INT,
  dry_rains_production_Quantity_units VARCHAR(255),
  dry_rains_Hhfood_consumption_Qty VARCHAR(255),
  dry_rains_Hhfood_consumption_Qty_units VARCHAR(255),
  dry_rains_Payment_in_kind_quantity VARCHAR(255),
  dry_rains_Payment_in_kind_quantity_units VARCHAR(255),
  dry_rains_other_Qty VARCHAR(255),
  dry_rains_other_Qty_units VARCHAR(255),
  dry_rains_Livestock_feeding_Qty VARCHAR(255),
  dry_rains_Livestock_feeding_Qty_units VARCHAR(255),
  dry_rains_kept_as_seed_Qty VARCHAR(255),
  dry_rains_kept_as_seed_Qty_units VARCHAR(255),
  dry_rains_sales_Qnty VARCHAR(255),
  dry_rains_Sales_quantity VARCHAR(255),
  dry_rains_Sales_units VARCHAR(255),
  dry_rains_Sales_total_value VARCHAR(255),
  dry_rains_Sales_income_control VARCHAR(255),
  dry_rains_main_buyer VARCHAR(255),
  dry_rains_stored_for_Dry_Season VARCHAR(255)
);