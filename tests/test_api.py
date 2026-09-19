import requests


BASE_URL = "https://jsonplaceholder.typicode.com"
headers ={
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0"
}
def test_get_users():
    """测试获取用户列表"""
    response = requests.get(f"{BASE_URL}/users")

    #验证状态码
    assert response.status_code == 200

    #验证响应数据
    users =response.json()
    assert isinstance(users,list)
    assert len(users) >0

    #验证第一个用户的数据结构
    first_user = users[0]
    assert "id" in first_user
    assert "name" in first_user
    assert "email" in first_user

def test_get_single_user():
    """测试获取单个用户"""
    user_id = 1
    respone = requests.get(f"{BASE_URL}/users/{user_id}")
    assert respone.status_code == 200

    user = respone.json()
    assert user["id"] == user_id
    assert user["name"] is not None

def test_create_user():
    """测试创建用户"""
    new_user = {
        "name": "Test User",
        "email": "test@example.com"
    }
    response = requests.post(f"{BASE_URL}/users",json=new_user)
    assert response.status_code == 201

    created_user = response.json()
    assert created_user["name"] == new_user["name"]
    assert created_user["email"] == new_user["email"]