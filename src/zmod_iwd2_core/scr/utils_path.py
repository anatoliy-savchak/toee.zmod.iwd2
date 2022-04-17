import math
import toee
import tpdp

def rot_from_locs(loc1, loc2):
	""" Returns angle (rad) between two full locations. rot_from_locs(npc1.location_full, npc2.location_full) """
	assert isinstance(loc1, tpdp.LocAndOffsets)
	assert isinstance(loc2, tpdp.LocAndOffsets)
	ax, ay = loc1.get_overall_offset()
	bx, by = loc2.get_overall_offset()
	angle = angle_from_points(ax, ay, bx, by)
	return angle - 0.7853981633974483 # -45 grad

def angle_from_points(ax, ay, bx, by):
	return math.atan2(ax-bx, ay-by)

def angle_align_with(angle_rad, aliquot_degr):
	angle_grad = math.degrees(angle_rad) % 360
	angle_grad_aligned = round(float(angle_grad) / aliquot_degr) * aliquot_degr
	return math.radians(angle_grad_aligned)

def radius_align_with_side(radius_ft, angle_rad, aliquot_degr):
	angle_grad = math.degrees(angle_rad) % 360
	det = angle_grad // aliquot_degr
	den = angle_grad % aliquot_degr
	result = radius_ft
	if (det % 2 == 0):
		result = math.sqrt(radius_ft**2 + radius_ft**2)

	#print('radius_align_with_side radius_ft: {}, angle_grad: {}, det: {}, result: {}'.format(radius_ft, angle_grad, det, result))
	return result