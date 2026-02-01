import math

AB = int(input())

BC = int(input())

m_angle = math.atan(AB/BC) # tan(theta) = AB/BC

final_m_degree = math.degrees(m_angle) # (AB/BC) in degree

print(round(final_m_degree), chr(176), sep = '') # Rounding up and ASCii value for degree sign is 176 + space
