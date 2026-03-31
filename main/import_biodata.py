import os
import csv
import django
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pkpl_uhuy.settings') 
django.setup()

from main.models import Biodata 

def run_import():
    file_path = os.path.join(os.path.dirname(__file__), 'biodata.csv')
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} nggak ada di folder main!")
        return

    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            obj, created = Biodata.objects.update_or_create(
                npm=row['npm'],
                defaults={
                    'nama': row['nama'],
                    'peran': row['peran'],
                    'deskripsi': row['deskripsi'],
                    'foto': row.get('foto', '')
                }
            )
            print(f"{'✅ Created' if created else '🔄 Updated'}: {obj.nama}")

if __name__ == '__main__':
    run_import()