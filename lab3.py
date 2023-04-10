def palindrom(text):
  
    words = text.split()
    
    palindromes = []
   
    for word in words:
        if word == word[::-1]:  
            palindromes.append(word) 
    return palindromes
  
  
  
  
  def validate_ip(ip_address):
   
    parts = ip_address.split('.')
 
    if len(parts) != 4:
        return False
 
    for part in parts:
        try:
            num = int(part)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
  
    return True
  
  
  
  
  import platform

def get_os():
    system = platform.system()
    if system == 'Darwin':
        return 'Mac'
    elif system == 'Windows':
        return 'Windows'
    elif system == 'Linux':
        return 'Linux'
    else:
        return 'Unknown'
