from datetime import datetime
from guns import ak47, bazooka, deserteagle, glock, mk16, scar

dt = datetime.now()
print(dt)

ak = ak47.AK47(60)
bazooka = bazooka.Bazooka()
deserteagle = deserteagle.DesertEagle()
glock = glock.Glock(20)
mk16 = mk16.MK16()
scar = scar.Scar()

print('Bazooka: ')
bazooka.shoot()
bazooka.reload()
bazooka.grenade_exists()

scar.shoot()