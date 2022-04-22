def item_to_proto_name(item_file_name: str, item_type: str, slot_name: str, item_name: str) -> tuple:
    # returns array of Temple items:
    # (item_const_full_name, wear, comment)

    #fn = item_file_name.lower()
    #sname = slot_name.lower()

    result = None

    slot = None
    if slot_name[:11] == 'SLOT_WEAPON':
        slot = "toee.item_wear_weapon_primary"
        if slot_name[:11] == 'SLOT_WEAPON2':
            slot = "toee.item_wear_weapon_secondary"

    if item_type == 'LeatherArmor':
        # Leather Armor 00CIARMA is not used
        do_default = item_file_name in ('00CIARMB', '00LEAT01')
        do_default = True
            
        if do_default:
            if not slot_name == 'SLOT_ARMOR':
                result = (("const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN", None, None), )
            else:
                result = (
                    ("const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN", "toee.item_wear_armor", None),
                    ("const_proto_cloth.PROTO_CLOTH_BOOTS_LEATHER_BOOTS_FINE", "toee.item_wear_boots", None)
                )
    elif item_type == "Spears":
        do_default = item_file_name in ('00SPER01', )
        do_default = True
        if do_default:
            result = (("const_proto_weapon.PROTO_WEAPON_SHORTSPEAR", slot, None), )
    elif item_type == "Daggers":
        do_default = item_file_name in ('00DAGG01', )
        do_default = True
        if do_default:
            result = (("const_proto_weapon.PROTO_WEAPON_DAGGER", slot, None), )
    elif item_type == "Club":
        do_default = item_file_name in ('00CLUB01', )
        do_default = True
        if do_default:
            result = (("const_proto_weapon.PROTO_WEAPON_CLUB", slot, None), )


    return result