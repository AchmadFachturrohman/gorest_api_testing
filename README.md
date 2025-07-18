# gorest_api_testing

dalam repositori ini terdapat 5 file .py dan file lainnya
1. `token_manager.py`
   - this code for:
     - Login otomatis ke GitHub menggunakan Selenium.
     - Scraping token dari halaman tertentu (kemungkinan halaman akses token GoREST).
     - Menyimpan token ke file .env agar bisa digunakan oleh automation pipeline.
     - Menyediakan header Authorization untuk API request.
2. `login_manager.py`
   - this code for:
     - Login otomatis ke GitHub menggunakan Selenium.
     - Scraping token dari halaman web (kemungkinan halaman akses token GoREST).
     - Menyimpan token ke file .env.
     - Menyediakan header Authorization untuk digunakan dalam API testing.
3. `scenario.py`
   - this code for:
     Melakukan pengujian otomatis terhadap endpoint https://gorest.co.in/public-api/users menggunakan pytest, dengan skenario:
     - Create user (positif & negatif)
     - Get user (positif & negatif)
     - Update user (positif & negatif)
     - Delete user (positif & negatif)
4. `conftest.py`
   - Kode ini mendefinisikan dua fixture untuk digunakan dalam pengujian API GoREST:
     - user_payload: Menyediakan data user yang valid untuk test create user.
     - user_holder: Menyimpan user_id dari user yang berhasil dibuat, agar bisa digunakan di test berikutnya (get, update, delete).
6. `main.py`
   - Script ini berfungsi sebagai entry point otomatis untuk:
     - Scraping token dari GoREST menggunakan TokenManager.
     - Menjalankan test pytest pada file scenario.py.
     - Menghasilkan report HTML (report.html) dari hasil test.
     - Membuka report tersebut di browser secara otomatis.

How to run this code:
1. Pull this repo to your local computer
2. Open the folder to visual studio code or your favorite code editor
3. Open the terminal
4. Run the main using `python run.py`

or

1. Pull this repo to your local computer
2. Open CMD and copy the `path` directory of the downloaded repo
3. Run the code by using `python run.py`
