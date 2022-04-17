import const_proto_armor, utils_const

PROTO_ARMOR_PADDED_ARMOR_TAN_MAP = {"proto": const_proto_armor.PROTO_ARMOR_PADDED_ARMOR_TAN, "xp": 0 \
	, "mwp": const_proto_armor.PROTO_ARMOR_PADDED_ARMOR_MASTERWORK, "mwxp": 6 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 0 \
	, "adp": 0, "adxp": 0 \
	}
PROTO_ARMOR_PADDED_ARMOR_RED_MAP = {"proto": const_proto_armor.PROTO_ARMOR_PADDED_ARMOR_RED, "xp": 0 \
	, "mwp": const_proto_armor.PROTO_ARMOR_PADDED_ARMOR_MASTERWORK, "mwxp": 6 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 0 \
	, "adp": 0, "adxp": 0 \
	}

PROTOS_ARMOR_LIGHT_PADDED_MAP = {\
	const_proto_armor.PROTO_ARMOR_PADDED_ARMOR_TAN : PROTO_ARMOR_PADDED_ARMOR_TAN_MAP \
	, const_proto_armor.PROTO_ARMOR_PADDED_ARMOR_RED : PROTO_ARMOR_PADDED_ARMOR_RED_MAP \
	}

PROTO_ARMOR_LEATHER_ARMOR_BROWN_MAP = {"proto": const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN, "xp": 0 \
	, "mwp": const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_MASTERWORK, "mwxp": 6 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 44 \
	, "adp": 0, "adxp": 0 \
	}
PROTO_ARMOR_LEATHER_ARMOR_BLACK_MAP = {"proto": const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BLACK, "xp": 0 \
	, "mwp": const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_MASTERWORK, "mwxp": 6 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 44 \
	, "adp": 0, "adxp": 0 \
	}
PROTO_ARMOR_LEATHER_ARMOR_TAN_MAP = {"proto": const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_TAN, "xp": 0 \
	, "mwp": const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_MASTERWORK, "mwxp": 6 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 44 \
	, "adp": 0, "adxp": 0 \
	}
PROTO_ARMOR_LEATHER_ARMOR_GREY_MAP = {"proto": const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_GREY, "xp": 0 \
	, "mwp": const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_MASTERWORK, "mwxp": 6 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 44 \
	, "adp": 0, "adxp": 0 \
	}

PROTOS_ARMOR_LIGHT_LEATHER_MAP = {\
	const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BROWN : PROTO_ARMOR_LEATHER_ARMOR_BROWN_MAP \
	, const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_BLACK : PROTO_ARMOR_LEATHER_ARMOR_BLACK_MAP \
	, const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_TAN : PROTO_ARMOR_LEATHER_ARMOR_TAN_MAP \
	, const_proto_armor.PROTO_ARMOR_LEATHER_ARMOR_GREY : PROTO_ARMOR_LEATHER_ARMOR_GREY_MAP \
	}

PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MAP = {"proto": const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR, "xp": 1 \
	, "mwp": const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MASTERWORK, "mwxp": 7 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 45 \
	, "adp": 0, "adxp": 0 \
	}

PROTOS_ARMOR_LIGHT_STUDDED_MAP = {\
	const_proto_armor.PROTO_ARMOR_STUDDED_LEATHER_ARMOR : PROTO_ARMOR_STUDDED_LEATHER_ARMOR_MAP \
	}

PROTO_ARMOR_CHAIN_SHIRT_MAP = {"proto": const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT, "xp": 4 \
	, "mwp": const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT_MASTERWORK, "mwxp": 11 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": const_proto_armor.PROTO_ARMOR_MITHRAL_SHIRT, "mixp": 48 \
	, "adp": 0, "adxp": 0 \
	}

PROTOS_ARMOR_LIGHT_CHAIN_SHIRT_MAP = {\
	const_proto_armor.PROTO_ARMOR_CHAIN_SHIRT : PROTO_ARMOR_CHAIN_SHIRT_MAP \
	}


PROTOS_ARMOR_LIGHT_MAP = utils_const.dmerge(PROTOS_ARMOR_LIGHT_PADDED_MAP, PROTOS_ARMOR_LIGHT_LEATHER_MAP, PROTOS_ARMOR_LIGHT_STUDDED_MAP, PROTOS_ARMOR_LIGHT_CHAIN_SHIRT_MAP)

PROTO_ARMOR_HIDE_MAP = {"proto": const_proto_armor.PROTO_ARMOR_HIDE, "xp": 2 \
	, "mwp": const_proto_armor.PROTO_ARMOR_HIDE_MASTERWORK, "mwxp": 8 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 0 \
	, "adp": 0, "adxp": 0 \
	}

PROTOS_ARMOR_MEDIUM_HIDE_MAP = {\
	const_proto_armor.PROTO_ARMOR_HIDE : PROTO_ARMOR_HIDE_MAP \
	}

PROTO_ARMOR_SCALE_MAIL_MAP = {"proto": const_proto_armor.PROTO_ARMOR_SCALE_MAIL, "xp": 2 \
	, "mwp": const_proto_armor.PROTO_ARMOR_SCALE_MAIL_MASTERWORK, "mwxp": 8 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 178 \
	, "adp": 0, "adxp": 442 \
	}
PROTO_ARMOR_SCALE_MAIL_FINE_MAP = {"proto": const_proto_armor.PROTO_ARMOR_SCALE_MAIL_FINE, "xp": 2 \
	, "mwp": const_proto_armor.PROTO_ARMOR_SCALE_MAIL_MASTERWORK, "mwxp": 8 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 178 \
	, "adp": 0, "adxp": 442 \
	}

PROTOS_ARMOR_MEDIUM_SCALE_MAP = {\
	const_proto_armor.PROTO_ARMOR_SCALE_MAIL : PROTO_ARMOR_SCALE_MAIL_MAP \
	, const_proto_armor.PROTO_ARMOR_SCALE_MAIL_FINE : PROTO_ARMOR_SCALE_MAIL_FINE_MAP \
	}

PROTO_ARMOR_CHAINMAIL_MAP = {"proto": const_proto_armor.PROTO_ARMOR_CHAINMAIL, "xp": 6 \
	, "mwp": const_proto_armor.PROTO_ARMOR_CHAINMAIL_MASTERWORK_FINE, "mwxp": 13 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": const_proto_armor.PROTO_ARMOR_CHAINMAIL_MITHRAL, "mixp": 182 \
	, "adp": 0, "adxp": 446 \
	}
PROTO_ARMOR_CHAINMAIL_FINE_MAP = {"proto": const_proto_armor.PROTO_ARMOR_CHAINMAIL_FINE, "xp": 6 \
	, "mwp": const_proto_armor.PROTO_ARMOR_CHAINMAIL_MASTERWORK_FINE, "mwxp": 13 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": const_proto_armor.PROTO_ARMOR_CHAINMAIL_MITHRAL, "mixp": 182 \
	, "adp": 0, "adxp": 446 \
	}
PROTO_ARMOR_CHAINMAIL_RED_MAP = {"proto": const_proto_armor.PROTO_ARMOR_CHAINMAIL_RED, "xp": 6 \
	, "mwp": const_proto_armor.PROTO_ARMOR_CHAINMAIL_MASTERWORK_RED, "mwxp": 13 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": const_proto_armor.PROTO_ARMOR_CHAINMAIL_MITHRAL, "mixp": 182 \
	, "adp": 0, "adxp": 446 \
	}
PROTO_ARMOR_CHAINMAIL_GOLD_MAP = {"proto": const_proto_armor.PROTO_ARMOR_CHAINMAIL_GOLD, "xp": 6 \
	, "mwp": const_proto_armor.PROTO_ARMOR_CHAINMAIL_MASTERWORK_FINE, "mwxp": 13 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": const_proto_armor.PROTO_ARMOR_CHAINMAIL_MITHRAL, "mixp": 182 \
	, "adp": 0, "adxp": 446 \
	}

PROTOS_ARMOR_MEDIUM_CHAINMAIL_MAP = {\
	const_proto_armor.PROTO_ARMOR_CHAINMAIL : PROTO_ARMOR_CHAINMAIL_MAP \
	, const_proto_armor.PROTO_ARMOR_CHAINMAIL_FINE : PROTO_ARMOR_CHAINMAIL_FINE_MAP \
	, const_proto_armor.PROTO_ARMOR_CHAINMAIL_RED : PROTO_ARMOR_CHAINMAIL_RED_MAP \
	, const_proto_armor.PROTO_ARMOR_CHAINMAIL_GOLD : PROTO_ARMOR_CHAINMAIL_GOLD_MAP \
	}

PROTO_ARMOR_BREASTPLATE_MAP = {"proto": const_proto_armor.PROTO_ARMOR_BREASTPLATE, "xp": 8 \
	, "mwp": const_proto_armor.PROTO_ARMOR_BREASTPLATE_MASTERWORK, "mwxp": 15 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 184 \
	, "adp": 0, "adxp": 448 \
	}
PROTO_ARMOR_BREASTPLATE_BLACK_MAP = {"proto": const_proto_armor.PROTO_ARMOR_BREASTPLATE_BLACK, "xp": 8 \
	, "mwp": const_proto_armor.PROTO_ARMOR_BREASTPLATE_MASTERWORK, "mwxp": 15 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 184 \
	, "adp": 0, "adxp": 448 \
	}
PROTO_ARMOR_BREASTPLATE_GOLD_MAP = {"proto": const_proto_armor.PROTO_ARMOR_BREASTPLATE_GOLD, "xp": 8 \
	, "mwp": const_proto_armor.PROTO_ARMOR_BREASTPLATE_MASTERWORK, "mwxp": 15 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 184 \
	, "adp": 0, "adxp": 448 \
	}

PROTOS_ARMOR_MEDIUM_BREASTPLATE_MAP = {\
	const_proto_armor.PROTO_ARMOR_BREASTPLATE : PROTO_ARMOR_BREASTPLATE_MAP \
	, const_proto_armor.PROTO_ARMOR_BREASTPLATE_BLACK : PROTO_ARMOR_BREASTPLATE_BLACK_MAP \
	, const_proto_armor.PROTO_ARMOR_BREASTPLATE_GOLD : PROTO_ARMOR_BREASTPLATE_GOLD_MAP \
	}


PROTOS_ARMOR_MEDIUM_MAP = utils_const.dmerge(PROTOS_ARMOR_MEDIUM_HIDE_MAP, PROTOS_ARMOR_MEDIUM_SCALE_MAP, PROTOS_ARMOR_MEDIUM_CHAINMAIL_MAP, PROTOS_ARMOR_MEDIUM_BREASTPLATE_MAP)

PROTO_ARMOR_SPLINT_MAIL_MAP = {"proto": const_proto_armor.PROTO_ARMOR_SPLINT_MAIL, "xp": 8 \
	, "mwp": const_proto_armor.PROTO_ARMOR_SPLINT_MAIL_MASTERWORK, "mwxp": 15 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 404 \
	, "adp": 0, "adxp": 668 \
	}

PROTOS_ARMOR_HEAVY_SPLINT_MAIL_MAP = {\
	const_proto_armor.PROTO_ARMOR_SPLINT_MAIL : PROTO_ARMOR_SPLINT_MAIL_MAP \
	}

PROTO_ARMOR_BANDED_MAIL_MAP = {"proto": const_proto_armor.PROTO_ARMOR_BANDED_MAIL, "xp": 11 \
	, "mwp": const_proto_armor.PROTO_ARMOR_BANDED_MAIL_MASTERWORK, "mwxp": 17 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 407 \
	, "adp": 0, "adxp": 671 \
	}

PROTO_ARMOR_BANDED_MAIL_BLACK_MAP = {"proto": const_proto_armor.PROTO_ARMOR_BANDED_MAIL_BLACK, "xp": 11 \
	, "mwp": const_proto_armor.PROTO_ARMOR_BANDED_MAIL_MASTERWORK, "mwxp": 17 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 407 \
	, "adp": 0, "adxp": 671 \
	}

PROTOS_ARMOR_HEAVY_BANDED_MAIL_MAP = {\
	const_proto_armor.PROTO_ARMOR_SPLINT_MAIL : PROTO_ARMOR_SPLINT_MAIL_MAP \
	, const_proto_armor.PROTO_ARMOR_BANDED_MAIL_BLACK : PROTO_ARMOR_BANDED_MAIL_BLACK_MAP \
	}

PROTO_ARMOR_HALF_PLATE_MAP = {"proto": const_proto_armor.PROTO_ARMOR_HALF_PLATE, "xp": 26 \
	, "mwp": const_proto_armor.PROTO_ARMOR_HALF_PLATE_MASTERWORK, "mwxp": 33 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": 0, "mixp": 422 \
	, "adp": 0, "adxp": 686 \
	}

PROTOS_ARMOR_HEAVY_HALF_PLATE_MAP = {\
	const_proto_armor.PROTO_ARMOR_HALF_PLATE : PROTO_ARMOR_HALF_PLATE_MAP \
	}

PROTO_ARMOR_FULL_PLATE_MAP = {"proto": const_proto_armor.PROTO_ARMOR_FULL_PLATE, "xp": 66 \
	, "mwp": const_proto_armor.PROTO_ARMOR_FULL_PLATE_MASTERWORK, "mwxp": 72 \
	, "svp": 0, "svxp": 0 \
	, "cip": 0, "cixp": 0 \
	, "mip": const_proto_armor.PROTO_ARMOR_FULL_PLATE_MITHRAL, "mixp": 462 \
	, "adp": 0, "adxp": 726 \
	}

PROTOS_ARMOR_HEAVY_FULL_PLATE_MAP = {\
	const_proto_armor.PROTO_ARMOR_FULL_PLATE : PROTO_ARMOR_FULL_PLATE_MAP \
	}


PROTOS_ARMOR_HEAVY_MAP = utils_const.dmerge(PROTOS_ARMOR_HEAVY_SPLINT_MAIL_MAP, PROTOS_ARMOR_HEAVY_BANDED_MAIL_MAP, PROTOS_ARMOR_HEAVY_HALF_PLATE_MAP, PROTOS_ARMOR_HEAVY_FULL_PLATE_MAP)


PROTOS_ARMOR_MAP = utils_const.dmerge(PROTOS_ARMOR_LIGHT_MAP, PROTOS_ARMOR_MEDIUM_MAP, PROTOS_ARMOR_HEAVY_MAP)

