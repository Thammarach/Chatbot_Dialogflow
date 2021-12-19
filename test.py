a = {'a': 10, 'b': 20, 'c': 30, 'd': {'f': 40}}
print(a['d']['f'])

# k = {'responseId': 'ec2c31cb-e170-4813-8aa3-3832c7f51242-87a8b854',
#      'queryResult': {'queryText': 'เดี๋ยวกลับมาสั่ง', 'action': 'Intent-.Intent--no', 'parameters': {},
#                      'allRequiredParamsPresent': True, 'fulfillmentText': 'โอเครครับ คุณลูกค้า',
#                      'fulfillmentMessages': [{'text': {'text': ['โอเครครับ คุณลูกค้า']}}], 'outputContexts': [{
#              'name': 'projects/kratom-shop-tuiu/agent/sessions/8931f2b6-4c5f-3432-bb61-58adb0a68457/contexts/intent--no-followup',
#              'lifespanCount': 999},
#              {
#                  'name': 'projects/kratom-shop-tuiu/agent/sessions/8931f2b6-4c5f-3432-bb61-58adb0a68457/contexts/intent--followup',
#                  'lifespanCount': 994},
#              {
#                  'name': 'projects/kratom-shop-tuiu/agent/sessions/8931f2b6-4c5f-3432-bb61-58adb0a68457/contexts/__system_counters__',
#                  'parameters': {
#                      'no-input': 0.0,
#                      'no-match': 0.0}}],
#                      'intent': {'name': 'projects/kratom-shop-tuiu/agent/intents/df2425d8-f9a3-46d1-8353-8b5d30793c4e',
#                                 'displayName': 'Intent-สั่งสินค้า - no'}, 'intentDetectionConfidence': 1.0,
#                      'languageCode': 'th'}, 'originalDetectIntentRequest': {'source': 'line', 'payload': {
#         'data': {'replyToken': '9bfa4779c73f48b18931a3a7b8e4fd79', 'timestamp': '1639284406785',
#                  'source': {'type': 'user', 'userId': 'Uc53a82e111fc8f5c991ebc7ab2313795'}, 'type': 'message',
#                  'message': {'type': 'text', 'id': '15233659892106', 'text': 'เดี๋ยวกลับมาสั่ง'}}}},
#      'session': 'projects/kratom-shop-tuiu/agent/sessions/8931f2b6-4c5f-3432-bb61-58adb0a68457'}




# Workshop Buy Order
j = {'responseId': '1a6a622f-b10e-445f-a509-825fb4d18664-87a8b854',
     'queryResult': {'queryText': '001 10', 'action': 'Intent-Buy.Intent-Buy-custom',
                     'parameters': {'id_item': 1.0, 'count_number': 10.0}, 'allRequiredParamsPresent': True,
                     'fulfillmentMessages': [{'text': {'text': ['']}}], 'outputContexts': [{
                                                                                               'name': 'projects/kratom-shop-tuiu/agent/sessions/8931f2b6-4c5f-3432-bb61-58adb0a68457/contexts/intent-buy-followup',
                                                                                               'lifespanCount': 1,
                                                                                               'parameters': {
                                                                                                   'id_item': 1.0,
                                                                                                   'id_item.original': '001',
                                                                                                   'count_number': 10.0,
                                                                                                   'count_number.original': '10'}},
                                                                                           {
                                                                                               'name': 'projects/kratom-shop-tuiu/agent/sessions/8931f2b6-4c5f-3432-bb61-58adb0a68457/contexts/intent--followup',
                                                                                               'lifespanCount': 996,
                                                                                               'parameters': {
                                                                                                   'id_item': 1.0,
                                                                                                   'id_item.original': '001',
                                                                                                   'count_number': 10.0,
                                                                                                   'count_number.original': '10'}},
                                                                                           {
                                                                                               'name': 'projects/kratom-shop-tuiu/agent/sessions/8931f2b6-4c5f-3432-bb61-58adb0a68457/contexts/__system_counters__',
                                                                                               'parameters': {
                                                                                                   'no-input': 0.0,
                                                                                                   'no-match': 0.0,
                                                                                                   'id_item': 1.0,
                                                                                                   'id_item.original': '001',
                                                                                                   'count_number': 10.0,
                                                                                                   'count_number.original': '10'}}],
                     'intent': {'name': 'projects/kratom-shop-tuiu/agent/intents/fb8d0f95-ae2a-4cc2-8748-8780cc80804a',
                                'displayName': 'Intent-Buy - custom'}, 'intentDetectionConfidence': 1.0,
                     'languageCode': 'th'}, 'originalDetectIntentRequest': {'source': 'line', 'payload': {
        'data': {'source': {'userId': 'Uc53a82e111fc8f5c991ebc7ab2313795', 'type': 'user'},
                 'message': {'text': '001 10', 'id': '15234106272429', 'type': 'text'}, 'type': 'message',
                 'replyToken': 'df7eff2f254b42188b9865650be6901a', 'timestamp': '1639291519087'}}},
     'session': 'projects/kratom-shop-tuiu/agent/sessions/8931f2b6-4c5f-3432-bb61-58adb0a68457'}

#print(j['queryResult']['outputContexts'][0]['parameters']['id_item.original']) # data have list module give 0
id_user = j['originalDetectIntentRequest']['payload']['data']['source']['userId']
print(id_user)

