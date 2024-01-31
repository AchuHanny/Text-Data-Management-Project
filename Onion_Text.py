# -*- coding: utf-8 -*-
"""NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XpX90JsgSox6hy3Ykyt1yqYEnejzvOxf
"""

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

urls =['https://www.theonion.com/marvel-fans-blast-martin-scorsese-as-hypocrite-for-dead-1850941991',
       'https://www.theonion.com/biggest-revelations-from-jada-pinkett-smith-s-memoir-1850939851',
       'https://www.theonion.com/biden-urges-americans-not-to-let-dangerous-online-rheto-1850941897',
       'https://www.theonion.com/woman-claiming-she-from-chicago-technically-from-magica-1850925840',
       'https://www.theonion.com/white-house-tour-group-shrinks-down-to-molecular-size-f-1850925288',
       'https://www.theonion.com/amazon-river-records-lowest-water-level-in-over-a-centu-1850942673',
       'https://www.theonion.com/humane-meat-company-hires-assassins-to-quietly-slaughte-1850929503',
       'https://www.theonion.com/israel-military-reports-it-was-you-the-reader-who-ble-1850939156',
       'https://www.theonion.com/encouraging-study-finds-there-still-a-bunch-of-kids-who-1850925603',
       'https://www.theonion.com/helpful-passengers-in-tsa-line-let-airplane-running-lat-1850925291',
       'https://www.theonion.com/sen-menendez-s-wife-offers-to-hit-anyone-with-her-car-1850925749',
       'https://www.theonion.com/mar-a-lago-members-reveal-what-secrets-trump-shared-wit-1850928831',
       'https://www.theonion.com/liberal-woman-genuinely-fascinated-by-man-s-experience-1850925294',
       'https://www.theonion.com/the-onion-stands-with-israel-because-it-seems-like-yo-1850922505',
       'https://www.theonion.com/senator-darkness-appears-on-cnn-to-call-for-thousand-ye-1850922319']


def article(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    paragraphs = soup.find_all('p')
    return "\n".join(paragraph.get_text() for paragraph in paragraphs)


def get():
    return [article(url) for url in urls]
        
      
      # with open('OnionText.txt', 'a') as file:
      #   file.write("\n")
      #   if len(paragraphs)>1:
      #     for paragraph in paragraphs[:-1]:
      #       file.write(paragraph.get_text())
      #       file.write("\n")
      #   else:
      #     for paragraph in paragraphs:
      #       file.write(paragraph.get_text())
      #       file.write("\n")


