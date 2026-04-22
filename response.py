class Response:
    def __init__(self, request=None):
        self.status_code = 200
        self.reason = "OK"
        self.cookies = {}
        self.request = request

    def set_cookie(self, key, value):
        self.cookies[key] = value

    def build_header(self, content_length):
        headers = [
            f"HTTP/1.1 {self.status_code} {self.reason}",
            f"Content-Length: {content_length}",
            "Connection: close"
        ]
        
        # Thêm các header cài đặt Cookie nếu có
        for k, v in self.cookies.items():
            headers.append(f"Set-Cookie: {k}={v}; Path=/")
            
        # Dòng trắng cuối cùng để ngăn cách Headers với Body
        return "\r\n".join(headers) + "\r\n\r\n"

    def build_response(self, body: bytes):
        # Lấy kích thước body tính theo byte
        content_length = len(body)
        
        # Xây dựng chuỗi header
        header_str = self.build_header(content_length)
        
        # Chuyển header về byte string và ghép cùng body
        return header_str.encode("utf-8") + body

    def build_notfound(self):
        return (
            b"HTTP/1.1 404 Not Found\r\n"
            b"Content-Type: text/plain\r\n"
            b"Content-Length: 13\r\n"
            b"Connection: close\r\n\r\n"
            b"404 Not Found"
        )