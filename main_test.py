from fastapi import FastAPI
from fastapi.testclient import TestClient
import unittest

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

class TestMinimalApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"Hello": "World"})

if __name__ == '__main__':
    unittest.main()