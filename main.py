import inmem


s: inmem.Session = inmem.Session()

# s.set("demo_1")

print(s.get("demo_1"))

# s = inmem.Session()
# s.add(session_id1) # +1
# s.add(session_id2) # +2
# s.tot() # 2
# s.get(session_id1) # True
# s.del(session_id1) # ok
# s.get(session_id1) # False
