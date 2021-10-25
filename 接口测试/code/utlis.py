
def common_assert(case,response,status_code,success):
                case.assertEqual(200, response.status_code)
                case.assertEqual(True, response.json().get("success"))