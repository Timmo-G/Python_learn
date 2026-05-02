distance_mi = 10
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

if not distance_mi:
    print('False')
# 距离小于1
elif distance_mi <= 1:
    if not is_raining:
        print('True')
    else:
        print('False')
# 距离大于1 小于6
elif 1 < distance_mi and distance_mi <= 6:
    if  has_bike and not is_raining:
        print('True')
    else:
        print('False')
# 距离大于6
elif distance_mi > 6:
    if  has_car or has_ride_share_app:
        print('True')
    else:
        print('False')
