import subprocess
import sys
from token_manager import TokenManager
import webbrowser

def main():
    try:
        print("Scraping token dari GoREST...")
        token_mgr = TokenManager()
        token = token_mgr.get_token()

        if not token:
            print("Token tidak ditemukan.")
            sys.exit(1)

        print("Token berhasil didapat. Menjalankan tes...")

        subprocess.run([
            "pytest",
            "scenario.py",
            "--html=report.html",
            "--self-contained-html"
        ], check=True)
        webbrowser.open("report.html")


    except subprocess.CalledProcessError as err:
        print(f"Pytest gagal dijalankan: {err}")
        sys.exit(err.returncode)

    except Exception as e:
        import traceback
        print("Terjadi error lain:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()