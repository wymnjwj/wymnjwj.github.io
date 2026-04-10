import requests
from typing import Optional, Dict, Any

"""""
curl https://musachat-red-api.mthreads.com/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
  "model": "DeepSeek-R1-Distill-Llama-70B",
  "messages": [
    {
      "role": "user",
      "content": "你是谁啊?"
    }
  ],
  "stream": false
}'
"""

def http_request(
    method: str,
    url: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 10
) -> Dict[str, Any]:
    """
    发送 HTTP 请求的简单接口。

    :param method: 请求方法，如 'GET', 'POST'
    :param url: 请求 URL
    :param params: URL 查询参数（字典）
    :param data: 请求体数据（字典，对于 POST 请求）
    :param headers: 请求头（字典）
    :param timeout: 超时时间（秒）
    :return: 包含状态码、响应头和响应内容的字典
    """
    try:
        method = method.upper()
        if method == 'GET':
            resp = requests.get(url, params=params, headers=headers, timeout=timeout)
        elif method == 'POST':
            resp = requests.post(url, params=params, data=data, headers=headers, timeout=timeout)
        else:
            raise ValueError(f"不支持的请求方法: {method}")

        return {
            'status_code': resp.status_code,
            'headers': dict(resp.headers),
            'content': resp.text  # 如需二进制内容可使用 resp.content
        }
    except requests.RequestException as e:
        return {'error': str(e)}

# 使用示例
if __name__ == '__main__':
    # GET 请求示例
    result = http_request('GET', 'https://httpbin.org/get', params={'key': 'value'})
    print(result)

    # POST 请求示例
    result = http_request('POST', 'https://httpbin.org/post', data={'name': 'test'})
    print(result)