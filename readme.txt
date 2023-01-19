# Run XAMPP
cd /opt/lampp
sudo ./manager-linux-x64.run

#Untuk menjalankan requirements yang akan diinstall
pip3 install -r requirements.txt 

# Membuat virtual enviroment
python3 -m venv baak-env

# Mengaktifkan virtual environment
source baak-env/bin/activate

# Menjalankan project
uvicorn main:app --reload 

# Install mysql
pip install pymysql

