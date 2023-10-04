import arcpy

arcpy.env.overwriteOutput = True

# Path of the original Geodatabase table storing the 9 demographic datasets participating in the relationship class:
ori_table = r"C:\LPA\Projects\RelationshipClassProject\RelationshipClassProject.gdb\OC_Demograhic_Data"
# List of field's names for fields storing demographic attributes that required updates (Except for the GEOID field):
ori_table_fields = ['GEOID_1K', 'DP02_0064P', 'DP02_0065P', 'DP03_0002P', 'DP03_0004P',
                    'DP04_0096P', 'DP04_0111P', 'DP05_0010P', 'DP05_0014P']
# Path of the new geodatabase table storing demographic attribute data used for update:
new_table = r"C:\LPA\Projects\RelationshipClassProject\RelationshipClassProject.gdb\OC_Demographic_Data_Updated_2020"
# List of field's names for fields with corresponding demographic attributes used for update (Except for the GEOID field):
new_table_fields = ['GEO_ID_1J', 'F2020_DP02_0064PE', 'F2020_DP02_0065PE', 'F2020_DP03_0002PE', 'F2020_DP03_0004PE',
                    'F2020_DP04_0096PE', 'F2020_DP04_0111PE', 'F2020_DP05_0010PE', 'F2020_DP05_0014PE']

# The Search Cursor used for returning row records from fields of the new Geodatabase table:
cursor1 = arcpy.da.SearchCursor(new_table, new_table_fields)
# Dictionary storing the row records of the new table as key-value pairs:
new_table_dict = {row[0]: [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]] for row in cursor1}
# Delete the Search Cursor's object:
del cursor1

# The path of the Geodatabase storing the data:
workspace = r"C:\LPA\Projects\RelationshipClassProject\RelationshipClassProject.gdb"
# Start an edit session:
with arcpy.da.Editor(workspace) as edit:
    # The Update Cursor used for updating the row records in the original table participated in the Relationship Class:
    cursor2 = arcpy.da.UpdateCursor(ori_table, ori_table_fields)
    # The outer loop for iterating each row record in the original table:
    for rc in cursor2:
        # Print out the GEOID of the row record in the original table in the current iteration of the outer loop:
        print(f"\nThe geo_id of the original table in the current iteration of the outer loop: {rc[0]}")
        # The Inner loop for iterating the dictionary storing the row records of the new table:
        for k, v in new_table_dict.items():
            # If the GEOID of the row record in the original table in the current iteration of the outer loop matched with the GEOID of the row record in the new table of the current iteration of the inner loop, the demographic attribute in the corresponding fields in the new Table will be assigned and updated as the new field value of the original table:
            if rc[0] == k:
                print(f"The geo_id for both the inner loop and outer loop matched, records will be updated.")
                rc[1] = v[0]
                rc[2] = v[1]
                rc[3] = v[2]
                rc[4] = v[3]
                rc[5] = v[4]
                rc[6] = v[5]
                rc[7] = v[6]
                rc[8] = v[7]
                cursor2.updateRow(rc)
                break
    # Delete the Update Cursor's object:
    del cursor2

print(f"\nScript complete.")