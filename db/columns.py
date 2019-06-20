MAIN = ["starttime","endtime","today","const","Demographics_count","district_02","ward_02","village_02","hhid_02","hhid_confirmed","Seasons_count","hh_type","hhh_marital","hhh_read_write","hhh_indigenous","hhh_move_here","hh_no","hh_position_dummy","offfarm_desc_dummy","hh_members_count","age_num","bigger_plots","type_of_tenure_dummy","subplots_info_count","other_plots_planning_forages","other_plots_planning_forages_codes","other_plots_planning_forages_year","other_plots_planning_forages_season","non_ruminant_livestock_no","non_ruminant_livestock_count","ruminant_yesno","categories_no","species9_dummy","breed9_dummy","sex9_dummy","ageclass9_dummy","ruminants_count","notes9","livestock1","livestock2","livestock3","livestock4","livestock5","livestock6","livestock7","livestock8","livestock9","livestock10","livestock11","livestock12","livestock13","livestock14","livestock15","livestock16","livestock17","livestock18","livestock19","livestock20","feeding_seasons_no","Typical_Livestock_Feedbasket_count","lactation_supplements","additional_supplements_no","dairy_additional_supplements_count","confirm_no_of_all_livestock","livestock_products_utilization_count","value_addition","value_addition_prdct","value_addition_frqncy","value_addition_ltrs","value_addition_other","vol_produced","vol_consumed","vol_sold","vol_gift","product_sale_price","milk_purchases_count","livestock_activity_ID_dummy","livestock_activity_breed_dummy","Livestock_activity_dummy","management_practicesA_count","management_practicesB_count","feed_conservation_profitable","reducing_area_under_fodder","use_fresh_manure_profitable","use_fresh_manure_plants","natural_env_compared_10_yrs","believe","believe_explanation","manure_production_comments","long_term_dairy_credit","num_dairy_credit","loans_count","access_to_credit_comments","Food_insecurity_count","HDDS_count","gpsloc"]
DEMOGRAPHIC = ["enum","country","region","district","sector","ward","village","hhid","respname","respgender","respphone","Hhposition","other_Hhposition"]
SEASONS = ["district_01","ward_01","village_01","hhid_01","Long_rain_season","Short_rain_season","Long_Dry_season","short_Dry_season"]
HH_MEMBERS = ["hh_member_no","district_1","ward_1","village_1","hhid_1","hh_position","hhposition_name","hh_position_other","hh_age","hh_age_1","hh_gender","Highest_completed_education","labour_availability","work_calendar","activmain","activshort","dry_season","offfarm_desc","offfarmwork_name","offfarmwork_other","experience","hh_notes"]
SUBPLOT_DETAILS = ["sub_plot","district_2","ward_2","village_2","hhid_2","subplot_ID","subplot_acreas","tenant_owner","decision_maker","other_tenant_owner","land_type","long_rain_utilization","long_rain_utilization_crop","long_rains_croppedA_count","long_rains_croppedB_count","short_rain_utilization","short_rain_utilization_crop","short_rains_croppedA_count","short_rains_croppedB_count","dry_season_utilization","dry_season_utilization_crop","dry_season_croppedA_count","dry_season_croppedB_count","long_rain_season_count","long_rains_Number_Intercrop_components","long_rains_Intercrops_components_count","short_rain_season_count","dry_rain_season_count","dry_rains_Number_Intercrop_components","dry_rains_Intercrops_components_count","planted_with_forages","if_not_planted_sub_plotID","if_not_planted_percentage","plot_ID_forage_area","forage__Tractor_ploughing_note_summary_of_farming_activities"]
LONG_RAINS_CROPPEDA = ["district_221","ward_221","village_221","hhid_221","long_rain_utilization_cropsA","long_rain_utilization_otherCropsA"]
LONG_RAINS_CROPPEDB = ["district_222","ward_222","village_222","hhid_222","long_rain_utilization_cropsB","long_rain_utilization_otherCropsB"]
SHORT_RAINS_CROPPEDA = ["district_223","ward_223","village_223","hhid_223","short_rain_utilization_cropsA","short_rain_utilization_otherCropsA"]
SHORT_RAINS_CROPPEDB = ["district_224","ward_224","village_224","hhid_224","short_rain_utilization_cropsB","short_rain_utilization_otherCrops"]
DRY_SEASON_CROPPEDA = ["district_225","ward_225","village_225","hhid_225","dry_season_utilization_cropsA","dry_season_utilization_otherCropsA"]
DRY_SEASON_CROPPEDB = ["district_226","ward_226","village_226","hhid_226","dry_season_utilization_cropsB","dry_season_utilization_otherCropsB"]
LONG_RAIN_SEASON = ["district_21,ward_21,village_21,hhid_21,long_rain_crops,long_rain_types_variety,long_rain_start_month,long_rain_end_month,long_rain_if_intercropped,otherlong_rain_crops,long_rain_crop_products_count"]
LONG_RAIN_ACT = ["district_22","ward_22","village_22","hhid_22","long_rain_act_pos","long_rain_activity_type","long_rain_activity_other","long_rain_activity_date","long_rain_activity_Hh_male_no","long_rain_activity_Hh_male_days","long_rain_activity_Hh_male_hrs_days","long_rain_activity_Hh_female_no","long_rain_activity_Hh_female_days","long_rain_activity_Hh_female_hrs_day","long_rain_activity_Hh_child_no","long_rain_activity_Hh_child_days","long_rain_activity_Hh_child_hrs_day","long_rain_activity_Permantly_employed_worker_no","long_rain_activity_Permntly_employed_days","long_rain_activity_Permntly_employed_hrs_day","long_rain_activity_Unpaid_labour_no","long_rain_activity_Unpaid_labour_days","long_rain_activity_Unpaid_labour_hrs_day","long_rain_activity_hired_no","long_rain_activity_hired_hours","long_rain_activity_hired_hours_day","long_rain_activity_other_Total_costs"]
LONG_RAIN_INPUT = ["district_23,ward_23,village_23,hhid_23,long_rain_input_pos,long_rain_input_type,long_rain_input_other_fertilizer,long_rain_input_other_type,long_rain_input_quantity,long_rain_input_units,long_rain_input_total_costs"]
LONG_RAIN_CROP_PRODUCT = ["district_24,ward_24,village_24,hhid_24,Long_rains_Crop_products_count,long_rains_residue_type,long_rains_residue_other,long_rains_left_in_share,long_rains_grazing_share,long_rains_burnt_share,long_rains_residue_sales_share,long_rains_residue_sales_total_value,long_rains_residue_sales_income_control,long_rains_residue_sales_main_buyer,long_rains_residue_feed_stall,long_rains_residue_feed_own_graze,long_rains_residue_livestock_bedding,long_rains_residue_fuel,long_rains_residue_other,long_rains_crop_residues_notes"]
LONG_RAINS_CROPS_PRODUCT = ["district_241,ward_241,village_241,hhid_241,long_rains_crops_products,long_rains_production_Quantity,long_rains_production_Quantity_units,long_rains_Hhfood_consumption_Qty,long_rains_Hhfood_consumption_Qty_units,long_rains_Payment_in_kind_quantity,long_rains_Payment_in_kind_quantity_units,long_rains_other_Qty,long_rains_other_Qty_units,long_rains_Livestock_feeding_Qty,long_rains_Livestock_feeding_Qty_units,long_rains_kept_as_seed_Qty,long_rains_kept_as_seed_Qty_units,long_rains_sales_Qnty,long_rains_Sales_quantity,long_rains_Sales_units,long_rains_Sales_total_value,long_rains_Sales_income_control,long_rains_main_buyer,long_rains_crop_products_notes,long_rains_stored_for_Dry_Season"]
LONG)_RAINS_INTERCROP_COMP = ["long_rains_Intercrop_components","district_5","ward_5","village_5","hhid_5","long_rains_types_of_intercrop","long_rains_interCrop_products","long_rains_interCrop_production_Quantity","long_rains_interCrop_production_Quantity_units","long_rains_interCrop_Hhfood_consumption_Qty","long_rains_interCrop_Hhfood_consumption_Qty_units","long_rains_interCrop_Payment_in_kind_quantity","long_rains_interCrop_Payment_in_kind_quantity_units","long_rains_interCrop_other_Qty","long_rains_interCrop_other_Qty_units","long_rains_interCrop_Livestock_feeding_Qty","long_rains_interCrop_Livestock_feeding_Qty_units","long_rains_interCrop_kept_as_seed_Qty","long_rains_interCrop_kept_as_seed_Qty_units","long_rains_interCrop_sales_Qnty","long_rains_interCrop_Sales_quantity","long_rains_interCrop_Sales_units","long_rains_interCrop_Sales_total_value","long_rains_interCrop_Sales_income_control","long_rains_interCrop_main_buyer","long_rains_intercrop_products_notes","Long_rains_interCrop_Residue_utilisation_count"]
LONG_RAINS_INTERCROP_RESIDUE = ["district_51,ward_51,village_51,hhid_51,long_rains_interCrop_residue_type,long_rains_interCrop_residue_other,long_rains_interCrop_left_in_share,long_rains_interCrop_grazing_share,long_rains_interCrop_burnt_share,long_rains_interCrop_residue_sales_share,long_rains_interCrop_residue_sales_total_value,long_rains_interCrop_residue_sales_income_control,long_rains_interCrop_residue_sales_main_buyer,long_rains_interCrop_residue_feed_stall,long_rains_interCrop_residue_feed_own_graze,long_rains_interCrop_residue_livestock_bedding,long_rains_interCrop_residue_fuel,long_rains_interCrop_residue_other,long_rains_interCrop_residues_notes"]
SHORT_RAIN_SEASON = ["district_25","ward_25","village_25","hhid_25","short_rain_crops","short_rain_types_variety","short_rain_start_month","short_rain_end_month","short_rain_if_intercropped","othershort_rain_crops","short_rain_season_activity_notes","short_rain_crop_products_count","short_rains_Number_Intercrop_components","short_rains_Intercrops_components_count"]
SHORT_RAIN_ACT = ["district_26","ward_26","village_26","hhid_26","short_rain_act_pos","short_rain_activity_type","short_rain_activity_other","short_rain_activity_date","short_rain_activity_Hh_male_no","short_rain_activity_Hh_male_days","short_rain_activity_Hh_male_hrs_days","short_rain_activity_Hh_female_no","short_rain_activity_Hh_female_days","short_rain_activity_Hh_female_hrs_day","short_rain_activity_Hh_child_no","short_rain_activity_Hh_child_days","short_rain_activity_Hh_child_hrs_day","short_rain_activity_Permantly_employed_worker_no","short_rain_activity_Permntly_employed_days","short_rain_activity_Permntly_employed_hrs_day","short_rain_activity_Unpaid_labour_no","short_rain_activity_Unpaid_labour_days","short_rain_activity_Unpaid_labour_hrs_day","short_rain_activity_hired_no","short_rain_activity_hired_hours","short_rain_activity_hired_hours_day","short_rain_activity_other_Total_costs","short_rain_activity_notes"]
SHORT_RAIN_INPUT = ["district_27","ward_27","village_27","hhid_27","short_rain_input_pos","short_rain_input_type","short_rain_input_other_fertilizer","short_rain_input_other_type","short_rain_input_quantity","short_rain_input_units","short_rain_input_total_costs","short_rain_input_notes"]
SHORT_RAIN_CROP_PRODUCTS = ["district_28","ward_28","village_28","hhid_28","short_rains_Crop_products_count","short_rains_crop_products_notes","short_rains_residue_type","short_rains_residue_other","short_rains_left_in_share","short_rains_grazing_share","short_rains_burnt_share","short_rains_residue_sales_share","short_rains_residue_sales_total_value","short_rains_residue_sales_income_control","short_rains_residue_sales_main_buyer","short_rains_residue_feed_stall","short_rains_residue_feed_own_graze","short_rains_residue_livestock_bedding","short_rains_residue_fuel","short_rains_residue_other","short_rains_crop_residues_notes"]
SHORT_RAINS_CROPS_PRODUCTS = ["district_281","ward_281","village_281","hhid_281","short_rains_crops_products","short_rains_production_Quantity","short_rains_production_Quantity_units","short_rains_Hhfood_consumption_Qty","short_rains_Hhfood_consumption_Qty_units","short_rains_Payment_in_kind_quantity","short_rains_Payment_in_kind_quantity_units","short_rains_other_Qty","short_rains_other_Qty_units","short_rains_Livestock_feeding_Qty","short_rains_Livestock_feeding_Qty_units","short_rains_kept_as_seed_Qty","short_rains_kept_as_seed_Qty_units","short_rains_sales_Qnty","short_rains_Sales_quantity","short_rains_Sales_units","short_rains_Sales_total_value","short_rains_Sales_income_control","short_rains_main_buyer","short_rains_stored_for_Dry_Season"]
SHORT_RAINS_INTERCROP_COMP = ["short_rains_Intercrop_components","district_6","ward_6","village_6","hhid_6","short_rains_types_of_intercrop","short_rains_interCrop_products","short_rains_interCrop_production_Quantity","short_rains_interCrop_production_Quantity_units","short_rains_interCrop_Hhfood_consumption_Qty","short_rains_interCrop_Hhfood_consumption_Qty_units","short_rains_interCrop_Payment_in_kind_quantity","short_rains_interCrop_Payment_in_kind_quantity_units","short_rains_interCrop_other_Qty","short_rains_interCrop_other_Qty_units","short_rains_interCrop_Livestock_feeding_Qty","short_rains_interCrop_Livestock_feeding_Qty_units","short_rains_interCrop_kept_as_seed_Qty","short_rains_interCrop_kept_as_seed_Qty_units","short_rains_interCrop_sales_Qnty","short_rains_interCrop_Sales_quantity","short_rains_interCrop_Sales_units","short_rains_interCrop_Sales_total_value","short_rains_interCrop_Sales_income_control","short_rains_interCrop_main_buyer","short_rains_intercrop_products_notes","short_rains_inter_residue_count"]
SHORT_RAINS_INTERCROP_RESIDUE = ["district_61","ward_61","village_61","hhid_61","short_rains_interCrop_residue_type","short_rains_interCrop_residue_other","short_rains_interCrop_left_in_share","short_rains_interCrop_grazing_share","short_rains_interCrop_burnt_share","short_rains_interCrop_residue_sales_share","short_rains_interCrop_residue_sales_total_value","short_rains_interCrop_residue_sales_income_control","short_rains_interCrop_residue_sales_main_buyer","short_rains_interCrop_residue_feed_stall","short_rains_interCrop_residue_feed_own_graze","short_rains_interCrop_residue_livestock_bedding","short_rains_interCrop_residue_fuel","short_rains_interCrop_residue_other","short_rains_interCrop_residues_notes"]
DRY_SEASON = ["district_29","ward_29","village_29","hhid_29","dry_rain_crops","dry_rain_types_variety","dry_rain_start_month","dry_rain_end_month","dry_rain_if_intercropped","otherdry_season_crops","dry_rain_season_activity_comments","dry_rain_Tractor_ploughing_note_summary_of_farming_activities","dry_rain_crop_products_count"]
DRY_SEASON_ACT = ["district_30","ward_30","village_30","hhid_30","dry_rain_act_pos","dry_rain_activity_type","dry_rain_activities_other","dry_rain_activity_Activity_date","dry_rain_activity_Hh_male_no","dry_rain_activity_Hh_male_days","dry_rain_activity_Hh_male_hrs_days","dry_rain_activity_Hh_female_no","dry_rain_activity_Hh_female_days","dry_rain_activity_Hh_female_hrs_day","dry_rain_activity_Hh_child_no","dry_rain_activity_Hh_child_days","dry_rain_activity_Hh_child_hrs_day","dry_rain_activity_Permantly_employed_worker_no","dry_rain_activity_Permntly_employed_days","dry_rain_activity_Permntly_employed_hrs_day","dry_rain_activity_Unpaid_labour_no","dry_rain_activity_Unpaid_labour_days","dry_rain_activity_Unpaid_labour_hrs_day","dry_rain_activity_hired_no","dry_rain_activity_hired_hours","dry_rain_activity_hired_hours_day","dry_rain_activity_other_Total_costs"]
DRY_SEASON_INPUTS = ["district_31","ward_31","village_31","hhid_31","dry_rain_input_pos","dry_rain_input_type","dry_rain_input_other_fertilizer","dry_rain_input_other_type","dry_rain_input_quantity","dry_rain_input_units","dry_rain_input_total_costs"]
DRY_SEASON_CROP_PRODUCTS = ["district_32","ward_32","village_32","hhid_32","dry_rains_Crop_products_count","dry_rains_crop_products_notes","dry_rains_residue_type","dry_rains_residue_other","dry_rains_left_in_share","dry_rains_grazing_share","dry_rains_burnt_share","dry_rains_residue_sales_share","dry_rains_residue_sales_total_value","dry_rains_residue_sales_income_control","dry_rains_residue_sales_main_buyer","dry_rains_residue_feed_stall","dry_rains_residue_feed_own_graze","dry_rains_residue_livestock_bedding","dry_rains_residue_fuel","dry_rains_residue_other","dry_rains_crop_residues_notes"]
DRY_SEASON_CROPS_PRODUCT = ["district_321","ward_321","village_321","hhid_321","dry_rains_crops_products","dry_rains_production_Quantity","dry_rains_production_Quantity_units","dry_rains_Hhfood_consumption_Qty","dry_rains_Hhfood_consumption_Qty_units","dry_rains_Payment_in_kind_quantity","dry_rains_Payment_in_kind_quantity_units","dry_rains_other_Qty","dry_rains_other_Qty_units","dry_rains_Livestock_feeding_Qty","dry_rains_Livestock_feeding_Qty_units","dry_rains_kept_as_seed_Qty","dry_rains_kept_as_seed_Qty_units","dry_rains_sales_Qnty","dry_rains_Sales_quantity","dry_rains_Sales_units","dry_rains_Sales_total_value","dry_rains_Sales_income_control","dry_rains_main_buyer","dry_rains_stored_for_Dry_Season"]
DRY_SEASON_INTERCROP_COMP = ["dry_rains_Intercrop_components","district_7","ward_7","village_7","hhid_7","dry_rains_types_of_intercrop","dry_rains_interCrop_products","dry_rains_interCrop_production_Quantity","dry_rains_interCrop_production_Quantity_units","dry_rains_interCrop_Hhfood_consumption_Qty","dry_rains_interCrop_Hhfood_consumption_Qty_units","dry_rains_interCrop_Payment_in_kind_quantity","dry_rains_interCrop_Payment_in_kind_quantity_units","dry_rains_interCrop_other_Qty","dry_rains_interCrop_other_Qty_units","dry_rains_interCrop_Livestock_feeding_Qty","dry_rains_interCrop_Livestock_feeding_Qty_units","dry_rains_interCrop_kept_as_seed_Qty","dry_rains_interCrop_kept_as_seed_Qty_units","dry_rains_interCrop_sales_Qnty","dry_rains_interCrop_Sales_quantity","dry_rains_interCrop_Sales_units","dry_rains_interCrop_Sales_total_value","dry_rains_interCrop_Sales_income_control","dry_rains_interCrop_main_buyer","dry_rains_intercrop_products_notes","dry_rains_interCrop_residue_type","dry_rains_interCrop_residue_other","dry_rains_interCrop_left_in_share","dry_rains_interCrop_grazing_share","dry_rains_interCrop_burnt_share","dry_rains_interCrop_residue_sales_share","dry_rains_interCrop_residue_sales_total_value","dry_rains_interCrop_residue_sales_income_control","dry_rains_interCrop_residue_sales_main_buyer","dry_rains_interCrop_residue_feed_stall","dry_rains_interCrop_residue_feed_own_graze","dry_rains_interCrop_residue_livestock_bedding","dry_rains_interCrop_residue_fuel","dry_rains_interCrop_residue_other","dry_rains_interCrop_residues_notes"]
FORAGE_ACT = ["district_33","ward_33","village_33","hhid_33","forage_act_pos","forage__activity_type","forage__activity_other_type","forage__activity_date","forage__activity_Hh_male_no","forage__activity_Hh_male_days","forage__activity_Hh_male_hrs_days","forage__activity_Hh_female_no","forage__activity_Hh_female_days","forage__activity_Hh_female_hrs_day","forage__activity_Hh_child_no","forage__activity_Hh_child_days","forage__activity_Hh_child_hrs_day","forage__activity_Permantly_employed_worker_no","forage__activity_Permntly_employed_days","forage__activity_Permntly_employed_hrs_day","forage__activity_Unpaid_labour_no","forage__activity_Unpaid_labour_days","forage__activity_Unpaid_labour_hrs_day","forage__activity_hired_no","forage__activity_hired_hours","forage__activity_hired_hours_day","forage__activity_other_Total_costs"]
FORAGE_INPUT = ["district_34,ward_34,village_34,hhid_34,forage_inputs_pos,forage__input_type,forage__input_other_fertilizer,forage__input_other_type,forage__input_quantity,forage__input_units,forage__input_total_costs"]
NON_RUMINANT = ["non_ruminant_no","district_81","ward_81","village_81","hhid_81","non_ruminant_type","gender_ownership","Total_kept","Adult_females","Adult_males","Young","newly_acquired","no_added","way_acquired","other_way_acquired","if_purchased","notes_non_ruminant_livestock"]
RUMINANT = ["totalanimals_no","district_82","ward_82","village_82","hhid_82","species9","species_name","breed9","breed_name","sex9","sex_name","ageclass9","ageclass_name","tanimals9","Cattle_ownership_status","Cattle_gender_status","pregnant9","milked9","birthtimer9","offspring9","traction9","dairy_animals_count","ruminants_used_traction","change12mths","total12mths9","noageclass9","noborn9","giftsdowry9","purchased9","paid9","outageclass9","deaths9","outgiftsdowry9","consumed9","sold9","totalsold9","others9","livestock_lbl"]
DAIRY_ANIMALS = ["district_821","ward_821","village_821","hhid_821","reasons_for_cows_local","Other_reasons_for_cows_local","reasons_for_cows_local_rank2","Other_reasons_for_cows_local_rank2","reasons_for_cows_local_rank3","Other_reasons_for_cows_local_rank3","reasons_for_cows_improved","Other_reasons_for_cows_improved","reasons_for_cows_improved_rank2","Other_reasons_for_cows_improved_rank2","reasons_for_cows_improved_rank3","Other_reasons_for_cows_improved_rank3","reasons_for_cows_exotic","Other_reasons_for_cows_exotic","reasons_for_cows_exotic_rank2","Other_reasons_for_cows_exotic_rank2","reasons_for_cows_exotic_rank3","Other_reasons_for_cows_exotic_rank3","local_milk_times_day","improved_milk_times_day","exotic_milk_times_day","local_dry_days","improved_dry_days","exotic_dry_days","local_dry_currently","improved_dry_currently","exotic_dry_currently","local_Lactation_length","improved_Lactation_length","exotic_Lactation_length","local_milk_yield_max","improved_milk_yield_max","exotic_milk_yield_max","local_milk_yield_min","improved_milk_yield_min","exotic_milk_yield_min","local_milk_sulked","improved_milk_sulked","exotic_milk_sulked"]
FEEDBASKET = ["Typical_Feedbasket","district_9","ward_9","village_9","hhid_9","name_Typical_Livestock_Feedbasket","feed_bst_months_count","adequacy_count","Ruminants_fed","Feed_items","feed_items_types_count","other_Crop_residue_dry","other_Green_crop_by_products","other_Supplements_Concentrates","percentage_Natural_grasses_fresh","percentage_Crop_residue_dry","percentage_Planted_Fodder","percentage_Green_crop_by_products","percentage_Supplements_Concentrates","Feed_item_source_count","Purchased_Natural_grasses_fresh","Natural_grasses_fresh_units","Natural_grasses_fresh_total_costs","Purchased_Crop_residue_dry","Purchased_Crop_residue_dry_units","Purchased_Crop_residue_dry_total_costs","Purchased_Planted_Fodder","Purchased_Planted_Fodder_units","Purchased_Planted_Fodder_costs","Purchased_Green_crop_by_products","Purchased_Green_crop_by_products_units","Purchased_Green_crop_by_products_costs","Purchased_Supplements_Concentrates","Purchased_Supplements_Concentrates_units","Purchased_Supplements_Concentrates_costs","other_feed_basket_costs","notes_feed_basket_costs"]
FEEDBASKET_MONTHS = ["District_901","ward_901","village_901","hhid_901","feed_basket_months"]
FEEDBASKET_ADEQUECY = ["district_91","ward_91","village_91","hhid_91","January_1st_half","January_2nd_half","February_1st_half","February_2nd_half","March_1st_half","March_2nd_half","April_1st_half","April_2nd_half","May_1st_half","May_2nd_half","June_1st_half","June_2nd_half","July_1st_half","July_2nd_half","August_1st_half","August_2nd_half","September_1st_half","September_2nd_half","October_1st_half","October_2nd_half","November_1st_half","November_2nd_half","December_1st_half","December_2nd_half"]
FEEDBASKET_ITEM_TYPES = ["district_911","ward_911","village_911","hhid_911","Natural_grasses_fresh","Crop_residue_dry","Planted_Fodder","Green_crop_by_products","Supplements_Concentrates"]
FEEDBASKET_ITEM_SOURCE = ["district_912","ward_912","village_912","hhid_912","Source_Natural_grasses_fresh","Source_Crop_residue_dry","Source_Planted_Fodder","Source_Green_crop_by_products","Source_Supplements_Concentrates"]
ADDITIONAL_SUPPLEMENTS = ["dairy_additional_supplements_no","district_10","ward_10","village_10","hhid_10","dairy_additional_supplements_type_of_feed","Same_quantity_throughout","Qty_begining","Qty_begining_units","Qty_middle","Qty_middle_units","Qty_End","Qty_End_units","Qty_throughout_lactation","Qty_throughout_lactation_units"]
LIVESTOCK_PROD_UTILIZATION = ["confirmed_livestock_no","district_11","ward_11","village_11","hhid_11","livestock_ID","livestock_prdct_codes","livestock_product_breed","livestock_product_data_period","production_Qty","production_Qty_units","livestock_products_Qty_sold","production_Qty_HH","production_Qty_HH_units","production_Qty_other","production_Qty_other_units","other_buyer","production_Qty_sales","production_Qty_sales_value","production_Qty_sales_gender","production_Qty_sales_buyer","production_buyer_reasons"]
MILK_PURCHASES = ["district_011","ward_011","village_011","hhid_011","hh_buy_milk_buyers","hh_buy_packaged_milk","hh_buy_processed_other_milk_products"]
LIVESTOCK_ACT_INPUTS = ["district_12,ward_12,village_12,hhid_12,livestock_activity_ID,livestock_activity_ID_name,livestock_activity_breed,livestock_activity_breed_name,Livestock_activity,Livestock_activity_name,Livestock_activity_other,livestock_Hh_male_no,livestock_Hh_male_Days,livestock_Hh_male_hrs_day,livestock_Hh_female_no,livestock_Hh_female_Days,livestock_Hh_female_hours,livestock_Hh_child_no,livestock_Hh_child_Days,livestock_Hh_child_hours,livestock_Permantly_employed_worker_no,livestock_Permantly_Days,livestock_Permantly_hours,livestock_Unpaid_labour_no,livestock_Unpaid_labour_days,livestock_Unpaid_labour_hours,livestock_hired_no,livestock_hired_days,livestock_hired_hours"]
LIVESTOCK_INPUTS = ["district_13","ward_13","village_13","hhid_13","livestock_activity_ID_1","livestock_activity_breed_name_1","Livestock_activity_name_1","livestock_input_type","livestock_input_type_quantity","livestock_input_type_units","livestock_input_type_total_costs","notes_livestock_inputs_details"]
MANAGEMENT_PRACTICES_A = ["district_131","ward_131","village_131","hhid_131","conserve_feed","store_feed","access_water","separate_animals","animals_insurance","manure_collect","manure_apply","apply_manure"]
MANAGEMENT_PRACTICES_B = ["district_1311","ward_1311","village_1311","hhid_1311","health_main_challenges","other_health_main_challenges","feeding_main_challenges","other_feeding_main_challenges","manure_main_challenges","other_manure_main_challenges","husbandry_main_challenges","other_husbandry_main_challenges","genetic_main_challenges","other_genetic_main_challenges"]
MANURE_PRODUCT_DETAILS_A = ["district_14","ward_14","village_14","hhid_14","livestock_manure_type","roofed_Shed","roofed_Shed_hrs_day","Non_roofed","Non_roofed_hrs_day","crop_fields","crop_fields_hrs_day","on_farm_grazing","on_farm_grazing_hrs_day","off_farm_grazing","off_farm_grazing_hrs_day","notes_manure_production","Shed_total_collected","Shed_total_units","Shed_firedwood","Shed_fertilizer","Shed_constrction","Shed_biogas","Shed_sold","Shed_revenues","Shed_wasted","Shed_notes","non_roof_total_collected","non_roof_total_units","non_roof_firedwood","non_roof_fertilizer","non_roof_constrction","non_roof_biogas","non_roof_sold","non_roof_revenues","non_roof_wasted","non_roof_notes","manure_utilization2_count"]
MANURE_PRODUCT_DETAILS_B = ["district_142","ward_142","village_142","hhid_142","crop_fields_total_collected","crop_fields_total_units","crop_fields_firedwood","crop_fields_fertilizer","crop_fields_constrction","crop_fields_biogas","crop_fields_sold","crop_fields_revenues","crop_fields_wasted","crop_fields_notes","on_farm_total_collected","on_farm_total_units","on_farm_firedwood","on_farm_fertilizer","on_farm_constrction","on_farm_biogas","on_farm_sold","on_farm_revenues","on_farm_wasted","on_farm_notes","off_farm_total_collected","off_farm_total_units","off_farm_firedwood","off_farm_fertilizer","off_farm_constrction","off_farm_biogas","off_farm_sold","off_farm_revenues","off_farm_wasted","off_farm_notes"]
CREDIT_ACCESS = ["loan_pos","district_15","ward_15","village_15","hhid_15","loan_type","loan_when","loan_amount","loan_interest","loan_repayment_duration","loan_source","loan_source_other","loan_purpose","loan_purpose_other","loan_satisfied"]
FOOD_SECURITY = ["district_151","ward_151","village_151","hhid_151","less_food","less_food_months","worst_month","best_month","HH_worry","HH_worry_often","not_able_to_eat","not_able_to_eat_often","limited_variety","limited_variety_often","did_not_want","did_not_want_often","not_enough","not_enough_often","fewer_meals","fewer_meals_often","no_food_to_eat","no_food_to_eat_often","sleep_hungry","sleep_hungry_often","whole_day_night","whole_day_night_often"]
HDDS = ["district_152","ward_152","village_152","hhid_152","yesterday_celebration_feast","took_cereals","took_vitamin_rich_veges_tubers","took_white_tubers_roots","took_dark_green_leafy_veges","took_other_veges","took_vit_a_rich_fruits","took_other_fruits","took_organ_meat","took_flesh_meats","took_eggs","took_fish","took_legumes_nuts_seeds","took_milk_products","took_oils_fats","took_sweets","took_spices_condiments_beverages","eat_outside_home_yesterday","hdds_comments"]