"""
How to create a gem:
Given: gem_name, gem_icon_name, gem_value, gem_desc
1. Produce inventory icon (gem_inventory_id) in toee from gem_icon_name:
    a. Look for gem_bam (png) file from gem_icon_name. There are many for some reason, pick largest by file size.
    b. Convert gem_bam into gem_tga.
    c. Copy into core\art\interface\Inventory 
    d. open inventory.mes and decide new gem_inventory_id
    e. save result into inventory.json for further lookups and produce of inventory.mes
2. Look for available proto_id => gem_proto_id
3. Take gem template, replace proto fields and store into protos.json
4. Store proto_id as const into the lookup. Also save producer class for that one.
"""