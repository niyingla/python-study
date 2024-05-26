import json


class Test:

    @staticmethod
    def get_socket_response(self, browser_log_list):
        print(f'日志长度{len(browser_log_list)}')
        request_ids = []
        # 先保存到文件，利于测试，和后面的正则匹配
        for log in browser_log_list:
            message = json.loads(log['message']).get('message')
            if 'params' in message:
                params = message.get('params')
                if 'response' in params:
                    response = params.get('response')
                    if 'url' in response:
                        getUrl = response.get('url')
                    if 'type=productsPrice' in getUrl:
                        request_ids.append(params.get('requestId'))

        return request_ids

