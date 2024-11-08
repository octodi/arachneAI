import argparse
import re
import requests
#from cms import CMSDetector
import ssl
import socket
from lxml import html
from urllib.parse import urlparse, parse_qs,urljoin
import os
import time
import concurrent.futures


desc = "Web Vulnerability Scanner"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument("action", help="Action: full xss sql fuzzing e-mail credit-card whois links portscanner urlEncode cyberthreatintelligence commandInjection directoryTraversal fileInclude headerCheck certificate method IP2Location FileInputAvailable")
parser.add_argument("web_URL", help="URL")
args = parser.parse_args()

url = ""


def commandInjection(url, dosyaAdi):
    try:
        deger = url.find("=")
        istek = url[:deger + 1] + ";cat%20/etc/passwd"
        sonuc = requests.get(istek, verify=False)
        if "www-data" in sonuc.content:
            print("[+]Command injection possible, payload: ;cat%20/etc/passwd")
            print("Response: ", sonuc.content)
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[+]Command injection possible, payload: ;cat%20/etc/passwd\n"
            raporIcerik += "Response: " + sonuc.content + "\n"
            rapor.write(raporIcerik)
            rapor.close()
        else:
            print("[-]Command injection isn't possible, payload: ;cat%20/etc/passwd")
            print("Response: ", sonuc.content)
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[-]Command injection isn't possible, payload: ;cat%20/etc/passwd\n"
            raporIcerik += "Response: " + sonuc.content + "\n"
            rapor.write(raporIcerik)
            rapor.close()
    except Exception as e:
        print(f"Error in commandInjection: {e}")
        pass

def directoryTraversal(url, dosyaAdi):
    try:
        deger = url.find("=")
        istek = url[:deger + 1] + "../../../../../../etc/passwd"
        sonuc = requests.get(istek, verify=False)
        if "www-data" in sonuc.content:
            print("[+]Directory traversal possible, payload: ../../../../../../etc/passwd")
            print("Response: ", sonuc.content)
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[+]Directory traversal possible, payload: ../../../../../../etc/passwd\n"
            raporIcerik += "Response: " + sonuc.content + "\n"
            rapor.write(raporIcerik)
            rapor.close()
        else:
            print("[-]Directory traversal isn't possible, payload: ../../../../../../etc/passwd")
            print("Response: ", sonuc.content)
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[-]Directory traversal isn't possible, payload: ../../../../../../etc/passwd\n"
            raporIcerik += "Response: " + sonuc.content + "\n"
            rapor.write(raporIcerik)
            rapor.close()
    except Exception as e:
        print(f"Error in directoryTraversal: {e}")
        pass

def fileInclude(url, dosyaAdi):
    try:
        deger = url.find("=")
        istek = url[:deger + 1] + "../../../../../../etc/passwd"
        sonuc = requests.get(istek, verify=False)
        if "www-data" in sonuc.content:
            print("[+]File include possible, payload: ../../../../../../etc/passwd")
            print("Response: ", sonuc.content)
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[+]File include possible, payload: ../../../../../../etc/passwd\n"
            raporIcerik += "Response: " + sonuc.content + "\n"
            rapor.write(raporIcerik)
            rapor.close()
        else:
            print("[-]File include isn't possible, payload: ../../../../../../etc/passwd")
            print("Response: ", sonuc.content)
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[-]File include isn't possible, payload: ../../../../../../etc/passwd\n"
            raporIcerik += "Response: " + sonuc.content + "\n"
            rapor.write(raporIcerik)
            rapor.close()
    except Exception as e:
        print(f"Error in fileInclude: {e}")
        pass

def headerInformation(url, dosyaAdi):
    try:
        sonuc = requests.get(url, verify=False)
        headers = sonuc.headers
        print("[+] HTTP headers: \n", headers)
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[+] HTTP headers: \n " + str(headers) + "\n"
        rapor.write(raporIcerik)
        rapor.close()
    except Exception as e:
        print(f"Error in headerInformation: {e}")
        pass

def portScanner(url, dosyaAdi):
    try:
        deger = url.find("/")
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(1)
        for port in range(79, 85):
            if soket.connect_ex((url[:deger], port)) == 0:
                print("[+]Port open: ", port)
                rapor = open(dosyaAdi, "a")
                raporIcerik = "[+]Port open: " + str(port) + "\n"
                rapor.write(raporIcerik)
                rapor.close()
            else:
                print("[-]Port closed: ", port)
                rapor = open(dosyaAdi, "a")
                raporIcerik = "[-]Port closed: " + str(port) + "\n"
                rapor.write(raporIcerik)
                rapor.close()
        soket.close()
    except Exception as e:
        print(f"Error in portScanner: {e}")
        pass

def robotstxtAvailable(url, dosyaAdi):
    try:
        response = requests.get(f"{url}/robots.txt", verify=False)

        if response.status_code == 200:
            print("[+] robots.txt is available")
            domain = urlparse(url).netloc
            rbts = f"./report/robots_{domain}.txt"
            ss=f"Content: {response.text}\n"

            rbtstxt = open(rbts, "a")
            rbtstxt.write(ss)


            with open(dosyaAdi, "a") as rapor:
                rapor_icerik = f"[+] robots.txt is available\n "

                rapor.write(rapor_icerik)
        else:
            print("[-] robots.txt is not available")

            with open(dosyaAdi, "a") as rapor:
                rapor_icerik = "[-] robots.txt is not available\n"
                rapor.write(rapor_icerik)

    except requests.exceptions.RequestException as e:
        print(f"Error in robotstxt_available: {e}")


def urlEncode(url, dosyaAdi):
    try:
        sonuc = requests.get(url, verify=False)
        urlKod = sonuc.url
        print("[+]Encoded URL: ", urlKod)
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[+]Encoded URL: " + urlKod + "\n"
        rapor.write(raporIcerik)
        rapor.close()
    except Exception as e:
        print(f"Error in urlEncode: {e}")
        pass

def certificateInformation(url, dosyaAdi):
    try:
        ctx = ssl.create_default_context()
        s = ctx.wrap_socket(socket.socket(), server_hostname=url)
        s.connect((url, 443))
        cert = s.getpeercert()
        print("[+]Certificate information: ", cert)
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[+]Certificate information: " + str(cert) + "\n"
        rapor.write(raporIcerik)
        rapor.close()
    except Exception as e:
        print(f"Error in certificateInformation: {e}")
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[+]NO Certificate information: "  + "\n"
        rapor.write(raporIcerik)
        rapor.close()


def method(url, dosyaAdi):
    try:
        sonuc = requests.options(url, verify=False)
        allowed_methods = sonuc.headers.get('allow')
        print("[+]Allowed methods: ", allowed_methods)
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[+]Allowed methods: " + str(allowed_methods) + "\n"
        rapor.write(raporIcerik)
        rapor.close()
    except Exception as e:
        print(f"Error in method: {e}")

def FileInputAvailable(url, dosyaAdi):
    page = requests.get(url, verify=False)
    tree = html.fromstring(page.content)
    inputs = tree.xpath('//input[@name]')
    file_upload_available = False
    with open(dosyaAdi, "a") as rapor:
        for input in inputs:
            startPoint = int(str(input).find("'")) + 1
            stopPoint = int(str(input).find("'", startPoint))
            print(str(input)[startPoint:stopPoint])
            if "type='file'" in str(input):
                file_upload_available = True
    if file_upload_available:
        print("[+]File Upload Function available")
        rapor.write("[+]File Upload Function available\n")
    else:
        print("[+]File Upload Function NOT available")
        rapor.write("[+]File Upload Function NOT available\n")

def sql(url, dosyaAdi):
    sqlDosya = open("wordlists/sql.txt", "r")
    sqlPayload = sqlDosya.readlines()
    sqlDosya.close()
    if "=" in url:
        deger = str(url).find('=')
        for i in sqlPayload:
            try:
                i = i.split("\n")[0]
                yazi = str(url[0:deger + 1]) + str(i)
                sonuc = requests.get(yazi)
                if int(sonuc.status_code) == 200:
                    print("[+]Sqli payload: ", str(i))
                    print("[+]Sqli URL: ", yazi)
                    rapor = open(dosyaAdi, "a")
                    raporIcerik = "[+]Sqli payload: " + str(i) + "\n"
                    raporIcerik += "[+]Sqli URL: " + yazi + "\n"
                    rapor.write(raporIcerik)
                    rapor.close()
                else:
                    print("[-]Sqli payload: ", str(i))
                    print("[-]Sqli URL: ", yazi)
                    rapor = open(dosyaAdi, "a")
                    raporIcerik = "[-]Sqli payload: " + str(i) + "\n"
                    raporIcerik += "[-]Sqli URL: " + yazi + "\n"
                    rapor.write(raporIcerik)
                    rapor.close()
            except:
                pass
    else:
        print("[-]Sqli isn't available")
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[-]Sqli isn't available\n"
        rapor.write(raporIcerik)
        rapor.close()





def xss(url, dosyaAdi):
    xssDosya = open("wordlists/xss2.txt", "r", encoding="utf-8")
    xssPayload = xssDosya.readlines()
    xssDosya.close()

    def check_xss(test_url, payload):
        try:
            sonuc = requests.get(test_url)
            if payload in sonuc.text:
                print("[+]XSS payload: ", str(payload))
                print("[+]XSS URL: ", test_url)
                rapor = open(dosyaAdi, "a")
                raporIcerik = f"[+]XSS payload: {payload}\n[+]XSS URL: {test_url}\n"
                rapor.write(raporIcerik)
                rapor.close()
            else:
                print("[-]XSS payload: ", str(payload))
                print("[-]XSS URL: ", test_url)
                rapor = open(dosyaAdi, "a")
                raporIcerik = f"[-]XSS payload: {payload}\n[-]XSS URL: {test_url}\n"
                rapor.write(raporIcerik)
                rapor.close()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # Check for XSS in URL parameters
    if "=" in url:
        deger = str(url).find('=')
        for i in xssPayload:
            i = i.strip()
            yazi = str(url[:deger + 1]) + str(i)
            check_xss(yazi, i)

    # Check for XSS by appending to the end of the URL
    for i in xssPayload:
        i = i.strip()
        yazi = url + i
        check_xss(yazi, i)

    if "=" not in url:
        print("[-]XSS in URL parameters isn't available")
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[-]XSS in URL parameters isn't available\n"
        rapor.write(raporIcerik)
        rapor.close()

def crawl(url):
    crawl_dosya_path = "./wordlists/crawler2.txt"
    links_file_name = f"./crawler/crawl_{urlparse(url).netloc}.txt"

    if os.path.exists(links_file_name):
        os.remove(links_file_name)

    with open(crawl_dosya_path, "r") as crawl_dosya:
        crawl_icerik = crawl_dosya.readlines()

    for index, path in enumerate(crawl_icerik, start=1):
        try:
            path = path.strip()
            crawl_site = urljoin(url, path)
            response = requests.get(crawl_site, verify=False)

            if response.status_code == 200:
                print("[+] Url:", crawl_site)

                with open(links_file_name, "a") as links_file:
                    print("[+] Links:", crawl_site)
                    links_file.write("[+] Links:" + crawl_site + "\n")

            if index % 10 == 0:  # Check if 10 requests have been processed
                time.sleep(1)  # Introduce a 1-second delay
        except Exception as e:
            print(f"Error processing URL {crawl_site}: {e}")

def mail(url, dosyaAdi):
    istek = requests.get(url, verify=False)
    content_str = istek.content.decode('utf-8')  # Convert content to string

    sonuc = re.findall(r'[\w.-]+@[\w.-]+\.\w+', content_str)

    for i in sonuc:
        print("[+] E-mail: ", str(i))
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[+] E-mail: " + str(i) + "\n"
        rapor.write(raporIcerik)
        rapor.close()


def credit(url, dosyaAdi):
    istek = requests.get(url, verify=False)
    icerik = str(istek).split()
    icerikSon = str("".join(icerik))
    AMEX = re.match(r"^3[47][0-9]{13}$", icerikSon)
    VISA = re.match(r"^4[0-9]{12}(?:[0-9]{3})?$", icerikSon)
    MASTERCARD = re.match(r"^5[1-5][0-9]{14}$", icerikSon)
    DISCOVER = re.match(r"^6(?:011|5[0-9]{2})[0-9]{12}$", icerikSon)
    try:
        if MASTERCARD.group():
            print("Website has a Master Card!")
            print(MASTERCARD.group())
            rapor = open(dosyaAdi, "a")
            raporIcerik = "Website has a Master Card!\n"
            raporIcerik += MASTERCARD.group() + "\n"
            rapor.write(raporIcerik)
            rapor.close()

    except:
        print("Website hasn't a Mastercard!")

    try:
        if VISA.group():
            print("Website has a VISA card!")
            print(VISA.group())
            rapor = open(dosyaAdi, "a")
            raporIcerik = "Website has a VISA card!\n"
            raporIcerik += VISA.group() + "\n"
            rapor.write(raporIcerik)
            rapor.close()
    except:
        print("Website hasn't a VISA card!")

    try:
        if AMEX.group():
            print("Website has a AMEX card!")
            print(AMEX.group())
            rapor = open(dosyaAdi, "a")
            raporIcerik = "Website has a AMEX card!\n"
            raporIcerik += AMEX.group() + "\n"
            rapor.write(raporIcerik)
            rapor.close()
    except:
        print("Website hasn't a AMEX card!")

    try:
        if DISCOVER.group():
            print("Website has a payment methode!")
            print(DISCOVER.group())
            rapor = open(dosyaAdi, "a")
            raporIcerik = "[+] Website has a payment methode!\n"
            raporIcerik += DISCOVER.group() + "\n"
            rapor.write(raporIcerik)
            rapor.close()
    except:
        print("Website has no credit card!")
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[+] Website has no credit card payment methode!\n"
        rapor.write(raporIcerik)
        rapor.close()



def link(url):
    isimSayi1 = url.find(".")
    isim = url[isimSayi1 + 1:]
    isimSayi2 = isim.find(".")
    isim = isim[:isimSayi2]

    istek = requests.get(url, verify=False)
    content_str = istek.content.decode('utf-8')  # Convert content to string

    sonuc = re.findall(
        r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))""",
        content_str)

    domain = urlparse(url).netloc
    links_file_name = f"./links/links_{domain}.txt"

    with open(links_file_name, "w") as links_file:
        for link in sonuc:
            if isim in link:
                print("[+]Links:", link)
                links_file.write("[+]Links:" + link + "\n")


def cloudflare_detect(url,dosyaAdi):
    url_hh = f"http://api.hackertarget.com/httpheaders/?q={url}"
    resulthh = requests.get(url_hh).text

    if 'cloudflare' in resulthh.lower():
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[+] Cloudfare Detected !\n"
        rapor.write(raporIcerik)
        rapor.close()

    else:
        rapor = open(dosyaAdi, "a")
        raporIcerik = "[-] Cloudfare Not Detected !\n"
        rapor.write(raporIcerik)
        rapor.close()


def read_contents(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"Error reading contents from {url}: {e}")
        return None

# def cms_detect(url):
#     cmssc = read_contents(url)

#     if '/wp-content/' in cmssc:
#         tcms = "WordPress"
#     else:
#         if 'Joomla' in cmssc:
#             tcms = "Joomla"
#         else:
#             drpurl = url + "/misc/drupal.js"
#             drpsc = read_contents(drpurl)

#             if 'Drupal' in drpsc:
#                 tcms = "Drupal"
#             else:
#                 if '/skin/frontend/' in cmssc:
#                     tcms = "Magento"
#                 else:
#                     if 'content="WordPress' in cmssc:
#                         tcms = "WordPress"
#                     else:
#                         tcms = "Could Not Detect"

#     return tcms

# def result_cms(dosyaAdi,url):
#     resulthh = cms_detect(url)
#     if 'cloudflare' in resulthh.lower():
#         str = resulthh
#         rapor = open(dosyaAdi, "a")
#         raporIcerik = "[+]Detected "+ str +"!\n"
#         rapor.write(raporIcerik)
#         rapor.close()

#     else:
#         rapor = open(dosyaAdi, "a")
#         raporIcerik = "[+]CMS Not Detected !\n"
#         rapor.write(raporIcerik)
#         rapor.close()

if args:
    url = getattr(args, 'web_URL')
    print (str(url).split("/")[2])
    dosyaAdi="./report/"+str(url).split("/")[2]+"_report.txt"

    rapor=open(dosyaAdi,"w")
    raporIcerik=url+"\n"
    rapor.write(raporIcerik)
    rapor.close()
    print ("URL:", url, "\n==========")
    if args.action=="sql":
        sql(url,dosyaAdi)



    elif args.action=="portscanner":
        if str(url).split("/")[2]:
            url=str(url).split("/")[2]
        elif str(url).split("/")[3]:
            url = str(url).split("/")[2]

        print (url)
        portScanner(url,dosyaAdi)

    elif args.action=="urlEncode":
        urlEncode(url,dosyaAdi)


    elif args.action=="xss":
        xss(url,dosyaAdi)

    #elif args.action=="crawl":
      #  crawl(url,dosyaAdi)

    elif args.action=="e-mail":
        mail(url,dosyaAdi)

    elif args.action=="credit":
        credit(url,dosyaAdi)

    elif args.action=="links":
        link(url)

    elif args.action=="commandInjection":
        commandInjection(url,dosyaAdi)

    elif args.action=="directoryTraversal":
        directoryTraversal(url,dosyaAdi)

    elif args.action=="fileInclude":
        fileInclude(url,dosyaAdi)

    elif args.action=="headerCheck":
        headerInformation(url,dosyaAdi)

    elif args.action=="certificate":
        if str(url).split("/")[2]:
            url=str(url).split("/")[2]
        elif str(url).split("/")[3]:
            url = str(url).split("/")[2]

        print (url)
        certificateInformation(url,dosyaAdi)

    elif args.action=="method":
        if str(url).split("/")[2]:
            url=str(url).split("/")[2]
        elif str(url).split("/")[3]:
            url = str(url).split("/")[2]
        print (url)
        method(url,dosyaAdi)

    elif args.action=="FileInputAvailable":
        FileInputAvailable(url,dosyaAdi)

    elif args.action=="full":

        urlEncode(url,dosyaAdi)
        method(url, dosyaAdi)
        certificateInformation(url,dosyaAdi)
        link(url)
        # crawl(url)
        robotstxtAvailable(url, dosyaAdi)
        headerInformation(url,dosyaAdi)
        portScanner(url,dosyaAdi)
        mail(url,dosyaAdi)
        cloudflare_detect(url,dosyaAdi)
        #result_cms(dosyaAdi,url)


        #FileInputAvailable(url,dosyaAdi)
        credit(url,dosyaAdi)
        sql(url,dosyaAdi)
        xss(url,dosyaAdi)
        commandInjection(url,dosyaAdi)
        directoryTraversal(url,dosyaAdi)
        fileInclude(url,dosyaAdi)
        #detector = CMSDetector(url="https://emsi.ma", webinfo=True, cmsinfo=True)

    else:
        exit()
