# class TestIncidenceRate:
#   def test_incidence_rate_result(self, conn, test_incidence_rate_id):
#     conn.get_incidence_rate_result(test_incidence_rate_id)

#   def test_incidence_rate_raw(self, conn, test_incidence_rate_id):
#     stream = conn.get_incidence_rate_raw(test_incidence_rate_id)
#     obj = stream.fetchone()
#     assert obj
#     stream.close()
