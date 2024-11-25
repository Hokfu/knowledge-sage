def extract_payload(response):
    payload = {}
    if isinstance(response, dict):
        for key, value in response.items():
            if key != "response":
                payload[key] = value
    return payload
