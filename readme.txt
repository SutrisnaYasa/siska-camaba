# Run XAMPP
cd /opt/lampp
sudo ./manager-linux-x64.run

#Untuk menjalankan requirements yang akan diinstall
pip3 install -r requirements.txt 

# Membuat virtual enviroment
python3 -m venv camaba-env

# Mengaktifkan virtual environment
source camaba-env/bin/activate

# Menjalankan project
uvicorn main:app --reload 

# Akses project
http://127.0.0.1:8000/docs/

# Install mysql
pip install pymysql


