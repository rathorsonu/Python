state_of_india = ["Gujarat", "Maharashtra", "Rajasthan", "Bihar", "Punjab", "Haryana",
                   "Uttar Pradesh", "Madhya Pradesh", "Kerala", "Tamil Nadu",
                   "Karnataka", "Andhra Pradesh", "Telangana", "West Bengal", 
                  "Odisha", "Assam", "Sikkim", "Arunachal Pradesh", "Nagaland", 
                  "Manipur", "Mizoram", "Tripura", "Meghalaya", "Jharkhand", "Chhattisgarh",
                  "Goa", "Himachal Pradesh", "Uttarakhand", "Jammu and Kashmir", "Ladakh", "Delhi", 
                  "Puducherry", "Andaman and Nicobar Islands", "Lakshadweep", "Dadra and Nagar Haveli"
                  "and Daman and Diu", "Chandigarh", "Telangana", "Andhra Pradesh", ]

print(state_of_india[0])
state_of_india.append("New State")
print(state_of_india)
print("========================================================")
state_of_india.remove("New State")
print(state_of_india)

print("********************************************************************")
state_of_india.insert(0, "New State")
print(state_of_india)