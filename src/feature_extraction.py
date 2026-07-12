# src/feature_extraction.py
import re
from urllib.parse import urlparse

def extract_lexical_features(url_string):
    """
    Mengekstrak fitur leksikal dan struktural dari sebuah string URL
    untuk kebutuhan input model Machine Learning klasik (RF & XGBoost).
    """
    if not isinstance(url_string, str):
        url_string = str(url_string)
        
    features = {}
    
    # Standardisasi penanganan skema untuk urlparse
    if not url_string.startswith(('http://', 'https://')):
        parsed_url = urlparse('http://' + url_string)
    else:
        parsed_url = urlparse(url_string)
        
    # 1. Fitur Panjang Karakter (Length Features)
    features['url_len'] = len(url_string)
    features['domain_len'] = len(parsed_url.netloc)
    features['path_len'] = len(parsed_url.path)
    
    # 2. Fitur Penghitung Karakter Khusus (Special Character Counts)
    features['count_dot'] = url_string.count('.')
    features['count_hyphen'] = url_string.count('-')
    features['count_underline'] = url_string.count('_')
    features['count_slash'] = url_string.count('/')
    features['count_question'] = url_string.count('?')
    features['count_equal'] = url_string.count('=')
    features['count_at'] = url_string.count('@')
    
    # 3. Fitur Penghitung Digit Numerik
    features['count_digits'] = sum(c.isdigit() for c in url_string)
    
    # 4. Fitur Forensik Keamanan (Cek apakah domain menggunakan IP Address mentah)
    ip_pattern = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
    features['is_ip_address'] = 1 if ip_pattern.match(parsed_url.netloc) else 0
    
    return features