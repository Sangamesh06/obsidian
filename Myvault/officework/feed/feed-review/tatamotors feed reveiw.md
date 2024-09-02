
| attribute    | value in csv                                                                                                                                                                                                                                 | value in website                                                                                                                                                                                                                             |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Product_Path | [https://buytrucknbus.tatamotors.com/product-details/buses/buses/m&hcv-buses/lpo-1620-58-para-air-ac-bs6-phase-2/1376](https://buytrucknbus.tatamotors.com/product-details/buses/buses/m&hcv-buses/lpo-1620-58-para-air-ac-bs6-phase-2/1376) | [https://buytrucknbus.tatamotors.com/product-details/buses/buses/m&hcv-buses/lpo-1620-58-para-air-ac-bs6-phase-2/1376](https://buytrucknbus.tatamotors.com/product-details/buses/buses/m&hcv-buses/lpo-1620-58-para-air-ac-bs6-phase-2/1376) |
| image_url    |                                                                                                                                                                                                                                              | https://d3bslevwxw022c.cloudfront.net/buytrucknbus-tatamotors-com/cv/cv_online/VehicleImages/21960158000R/8728.webp                                                                                                                          |

[https://pim-assets.unbxd.com/images/b0368e8acc34c3fdf4deca33187111bb/1713430217886_8728.webp](https://pim-assets.unbxd.com/images/b0368e8acc34c3fdf4deca33187111bb/1713430217886_8728.webp)
https://d3bslevwxw022c.cloudfront.net/buytrucknbus-tatamotors-com/cv/cv_online/VehicleImages/21960158000R/8728.webp



value i did not get
breadcrumbs
buses and vans in bread crumbs(2nd value)
LPO 1620/58 PARA AIR AC( i got this value indescription but it is used in breadcrumbs)
 BS6 PHASE 2(it is present in vc_ddescription ut not as seperae attribute value)


Title
logic for creation of title

BS6 Phase 2(it is given as emission_norm)
LPO 1620/58 Para Air AC BS6 Phase 2(title present in vc_description)

ex showroom price is not present(but actual price is given)
is down payment same as book_now price

images
for image url they do have diffrent url but they point to same image

https://d3bslevwxw022c.cloudfront.net/buytrucknbus-tatamotors-com/cv/cv_online/VehicleImages/21960158000R/8728.webp


https://d3bslevwxw022c.cloudfront.net/buytrucknbus-tatamotors-com/cv/cv_online/VehicleImages/21960158000R/8728.webp


both the images beside main image are same

they have same url as main product 

in vehicle specification there is price but it is not present in csv file


in vehicle specification there is attribute called gearbox but it is not present in csv file
example : GB 750 6 speed

##  design and build
in design and build vehicle specification in first row
there is 16-t but i was unable to find the same in csv file

### wheel base
not found
is width considered as overall width

### emi calculator

loan amount : ex showroom price
interest rate for loan



//vehicle id is n/a in previous feed file
//for some of the vehicles overview is empty
//emission norms slightly diffrent(added ph-2 , ph2, phase 2)
//there are some value in clutch type that have value just as push_type but in feed most of have //some specification behind them
//product_type is slightly diffrent
//in max-power and max_torque the unit is diffrent r/min in feed but in csv it is rpm
//fuel tank capacity type of tank is added in csv but not in feed





correct
//rear_overhang format for empty is NA In csv but it is empty in feed
//front_overhang format for empty is NA In csv but it is empty in feed
// is slightly diffrent
//warranty is slightly diffrent
//engine_oil_change_interval is 
//kerb_weight  is 
//load_body_length does not have length in ft for some of the values
//some load_body_dimensions does not have length units in csv
//telematics in csv : 4g available 
		  in feed : YES OR NO or available
//engine_type_s has some time emission_norms attached to the same
//fuel_tank_capacity_s unit is slightly diffrent from feed along with type of tank attached
//max_power has additional rpm mentioned
//cabin_type is slightly diffrent
 


video_url_s for empty it is {} in feed but it is empty in csv  file sent bhy pim	
vc_title is slightly diffrent compared to earlier feed.  (pipe with tata motors)
actual_price data type in csv is float but it in feed it is int
Number of Seats	 data type in csv is float but it in feed it is int
max speed is not available in feed
year is float in csv but int in feed
gear box value structure is diffrent compared to  feed in csv
power steering is yes or no in feed but it is power or empty in csv. it was not present in prod search api
product_category is slightly diffrent
no_wheels we need to add spare for extra wheel
  csv : 6 Wheels + 1 Wheel
 feed : 6 Wheels + 1 Spare wheel 
 tyre type is diffrent compared to feed but it is not in dev site searchapi or prod search api
 
 

/Users/unbxd/Desktop/Screenshot 2024-07-16 at 10.53.51 AM.png
ppl_seo
is_top
lob_seo
is_home_brand
is_new_launch
is_popular
viewed_count
gst
Model_Cluster_1
Model_Cluster_2
Product Line
Parent Product Line
battery
alternator
body type 
front_axel 
rear_axel 
created_date   
updated_date 
status 
created_by_id 
updated_by_id 
**video_url** is 
 hotspot is 
column_three 
column_four 
column_five  
keywords 
is_active 
price_range 
retail_price 
esp_with gst 
frontbreaks 
rear_breaks 
exterior_color 
interior_color 


these are also some of the feilds in csv that are empty but not empty in feed_file
turning radius
ground_clearance
chassis type
test_drive
cargo_box_dimensions



		  
export PATH="$PATH:/downloads/Visual Studio Code 2.app/contents/resources/app/bin"
to run any application using command line you need to add path fro the same
go to folder where appln is there 
	cd to application
		cd to content
			cd to resources
				cd to bin
			 		add path to zshrc
			 if there is no directory named bin in resources
			 cd to macos
				 cd appln name
					 add path to zshrc	

|          |                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                            |                        |         |         |           |           |       |       |     |              |              |     |                                      |                 |     |     |                                    |     |     |     |     |             |             |     |                                          |              |         |         |         |     |     |                 |     |     |     |     |                           |                           |     |     |     |     |                                           |        |     |     |      |     |     |     |          |                           |                             |                                               |     |                                                |               |         |     |         |     |         |                             |                             |     |     |     |     |     |     |     |     |     |     |     |                                |     |     |     |     |     |     |             |     |     |     |     |     |     |      |     |                     |     |     |                 |     |         |                                      |     |     |     |     |     |     |     |     |     |                               |                               |          |     |     |     |                                                |               |         |                           |     |     |     |      |     |     |       |       |         |     |     |                |       |       |       |     |     |     |     |     |        |     |     |     |                           |                                                       |           |       |      |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- | ------- | ------- | --------- | --------- | ----- | ----- | --- | ------------ | ------------ | --- | ------------------------------------ | --------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- | ----------- | ----------- | --- | ---------------------------------------- | ------------ | ------- | ------- | ------- | --- | --- | --------------- | --- | --- | --- | --- | ------------------------- | ------------------------- | --- | --- | --- | --- | ----------------------------------------- | ------ | --- | --- | ---- | --- | --- | --- | -------- | ------------------------- | --------------------------- | --------------------------------------------- | --- | ---------------------------------------------- | ------------- | ------- | --- | ------- | --- | ------- | --------------------------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | ---- | --- | ------------------- | --- | --- | --------------- | --- | ------- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | ----------------------------- | -------- | --- | --- | --- | ---------------------------------------------- | ------------- | ------- | ------------------------- | --- | --- | --- | ---- | --- | --- | ----- | ----- | ------- | --- | --- | -------------- | ----- | ----- | ----- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ------------------------- | ----------------------------------------------------- | --------- | ----- | ---- |
| **1886** | [https://buytrucknbus.tatamotors.com/product-details/scv-pickups/pickups/intra/intra-v20-gold-bi-fuel-5l-nac-bs6-phase-2/1886](https://buytrucknbus.tatamotors.com/product-details/scv-pickups/pickups/intra/intra-v20-gold-bi-fuel-5l-nac-bs6-phase-2/1886) | [https://d3bslevwxw022c.cloudfront.net/buytrucknbus-tatamotors-com/cv/cv_online/VehicleImages/55459825AJSR/6466.webp](https://d3bslevwxw022c.cloudfront.net/buytrucknbus-tatamotors-com/cv/cv_online/VehicleImages/55459825AJSR/6466.webp) | 4b10-8843-77354a907020 | Pickups | Pickups | Intra V20 | Intra V20 | Intra | Intra |     | 55459825AJSR | 55459825AJSR |     | TITANIUM_WH-INTRA V20 PICKUP CNG+ LX | CABIN LOAD BODY |     |     | 25 %(CNG Mode), 27 % (Petrol Mode) |     |     |     |     | BS6 Phase 2 | 2 Cylinders |     | Single plate dry friction diaphragm type | GBS 65-5/5.6 | 1692 mm | 1921 mm | 4460 mm |     |     | Cabin Load Body |     |     | 4x2 |     | 165 R14 LT 8PR (Tubeless) | 165 R14 LT 8PR (Tubeless) |     | D+1 |     |     | INTRA V20 GOLD BI-FUEL 5L NAC BS6 phase 2 | 850048 |     |     | 5000 |     |     |     | 4 Wheels | Petrol: 43 kW CNG : 39 kW | P:106Nm C:95Nm@1800-2200RPM | Front - Disc Brakes<br><br>Rear - Drum Brakes |     | 1.2L, Three Cylinder, NGNA Bi-fuel CNG Engine. | P:5L + C:110L | Bi-Fuel |     | 2505 Kg |     | 2450 mm | Semi-elliptical leaf spring | Semi-elliptical leaf spring |     |     |     |     |     |     |     |     |     |     |     | Electric Power Steering (EPAS) |     |     | D+1 |     |     |     | SCV Pickups |     |     |     |     |     |     | TRUE | NO  | 2 Years / 72000 Kms |     |     | Cabin Load Body |     | 2620 mm | 2.62 X 1.56 X 0.3 (inner Dimensions) |     |     |     |     |     | N   |     |     |     | 2023-12-08 17:25:35.092 +0530 | 2024-01-30 17:30:13.123 +0530 | APPROVED |     | 18  | 18  | 1.2L, Three Cylinder, NGNA Bi-fuel CNG Engine. | P:5L + C:110L | 2505 Kg | Petrol: 43 kW CNG : 39 kW | {}  |     |     | TRUE |     |     | intra | FALSE | pickups |     |     | Titanium White | FALSE | FALSE | FALSE |     |     |     |     | 185 | 845248 | 28  |     |     | INTRA V20 GOLD BI-FUEL 5L | INTRA V20 GOLD CNG LX TITANIUM_WHITE_W/o GDCU TCU_PH2 | Intra V20 | Intra | Live |
