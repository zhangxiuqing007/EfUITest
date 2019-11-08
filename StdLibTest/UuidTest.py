import uuid

for _ in range(100):
    uid = uuid.uuid4().__str__()
    print(uid)
    print(uid[-8:])
