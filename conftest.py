import pytest
import time

timestamp = int(time.time())
# menyimpan data user
@pytest.fixture(scope="session")
def user_payload():
    return {
        "name": "Achmad Fachturrohman",
        "email": f"achmadfachturrohman{timestamp}@example.com",
        "gender": "male",
        "status": "active"
    }

# menyimpan data user_id
@pytest.fixture(scope="session")
def user_holder():
    return {}