CREATE TABLE dry_season_crop_products (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  district_32 VARCHAR(255),
  ward_32 VARCHAR(255),
  village_32 VARCHAR(255),
  hhid_32 VARCHAR(255),
  dry_rains_Crop_products_count INT,
  dry_rains_crop_products_notes VARCHAR(255),
  dry_rains_residue_type VARCHAR(255),
  dry_rains_residue_other VARCHAR(255),
  dry_rains_left_in_share VARCHAR(255),
  dry_rains_grazing_share VARCHAR(255),
  dry_rains_burnt_share VARCHAR(255),
  dry_rains_residue_sales_share VARCHAR(255),
  dry_rains_residue_sales_total_value VARCHAR(255),
  dry_rains_residue_sales_income_control VARCHAR(255),
  dry_rains_residue_sales_main_buyer VARCHAR(255),
  dry_rains_residue_feed_stall VARCHAR(255),
  dry_rains_residue_feed_own_graze VARCHAR(255),
  dry_rains_residue_livestock_bedding VARCHAR(255),
  dry_rains_residue_fuel VARCHAR(255),
  dry_rains_crop_residues_notes VARCHAR(255)
);