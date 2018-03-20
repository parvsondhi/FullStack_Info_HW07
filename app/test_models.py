import models as m

m.create_user('jim@gmail.com', 'test')
m.create_user('wynd07@gmail.com', 'test')
assert not m.create_user('wynd07@gmail.com', 'test')
assert m.check_login('wynd07@gmail.com', 'test')
assert not m.check_login('wynd07@gmail.com', 'testa')
assert not m.check_login('wynd07@gmail.co', 'test')

print([x['email'] for x in m.get_users()])

m.add_trip('eecs vs wild', 'aryo seco', 'jim@gmail.com', 'wynd07@gmail.com')
m.add_trip('eecs vs wild2', 'aryo seco', 'wynd07@gmail.com', 'jim@gmail.com')

print(m.get_trips('jim@gmail.com'))
print(m.get_trips('wynd07@gmail.com'))

m.remove_trip(m.get_trips('wynd07@gmail.com')[0]['trip_id'])

print(m.get_trips('jim@gmail.com'))
print(m.get_trips('wynd07@gmail.com'))

m.remove_trip(m.get_trips('wynd07@gmail.com')[0]['trip_id'])

print(m.get_trips('jim@gmail.com'))
print(m.get_trips('wynd07@gmail.com'))