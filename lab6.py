def get_text_info(filepath):
    with open(filepath, 'r') as f:
        text = f.read().lower()
        words = ''.join(c if c.isalpha() else ' ' for c in text).split()
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        for word, freq in word_freq.items():
            print(f"{word} - {freq}")
            
            
            
import csv
import requests

def download_csv(https://support.staffbase.com/hc/en-us/article_attachments/360009
197031/username.csv):
    filename = urlpath.split("/")[-1]
    response = requests.get(urlpath)
    data = response.content.decode('utf-8')
    lines = data.split('\n')
    lines = lines[:-1]
    with open('source_data/' + filename, 'w') as f:
        writer = csv.writer(f)
        for line in lines:
            row = line.split(',')
            writer.writerow(row)
    print('Completed!')
    
    
    
    
    import os
import csv
import requests

def download_csv(urlpath):
    if not os.path.exists("source_data"):
        os.makedirs("source_data")

    response = requests.get(urlpath)

    with open("source_data/username.csv", "wb") as f:
        f.write(response.content)

    with open("source_data/username.csv", "r") as f:
        lines = f.readlines()
    with open("source_data/username.csv", "w") as f:
        f.writelines(lines[:-1])

    print("Completed!")
