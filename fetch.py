from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
def ChromeDriver(playlist_url,search_year):
    """
    Télécharge des images pour chaque série de mots clés

    Args:
    - userprompts (str) : tableau de mots clés
    - initialprompt (str): prompt initiale
    -file_path (str) : chemin du dossier images
    - file_name (str) : nom que l'on veut donner aux images
    Returns:
    None
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    driver=webdriver.Chrome()
    driver.get(playlist_url)
    #driver.implicitly_wait(30)
    bouton_refuser=driver.find_element('xpath',"/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]/div/div/button/span")
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(bouton_refuser, 0, 0)
    action.click()
    action.perform()
    driver.execute_script("window.open('about;blank','secondtab');")
    driver.switch_to.window("secondtab")
    window_handles = driver.window_handles
    driver.get("https://web.archive.org/")
    driver.switch_to.window(window_handles[0])
    video_nb=int(driver.find_element('xpath','/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[1]/div[1]/ytd-playlist-byline-renderer/div/yt-formatted-string[1]/span[1]').text)        
    print(video_nb,"vidéos trouvées")
    print("Vidéos archivées:")
    for i in range(video_nb):
        time.sleep(3)
        video_element=driver.find_element('xpath',"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video-renderer[%s]/div[2]/div[1]/ytd-thumbnail/a" % (i+1))
        video_link=str(video_element.get_attribute("href")).split("&")[0]
        driver.switch_to.window(window_handles[1])
        input=driver.find_element('xpath',"/html/body/div[4]/div[1]/div[3]/form/div/div/input[1]")
        input.send_keys(video_link)
        input.send_keys(Keys.RETURN)
        time.sleep(3)
        page_content=driver.page_source
        if "Wayback Machine has not archived that URL." in page_content:
            pass
        else:
            try:   
                date=int(driver.find_element('xpath','/html/body/div[4]/div[2]/span/a[1]').text.split(" ")[2])
                #date2=int(driver.find_element('xpath','/html/body/div[4]/div[2]/span/a[2]').text.split(" ")[2])

            except:
                date=int(driver.find_element('xpath','/html/body/div[4]/div[2]/a').text.split(" ")[2].rstrip("."))
                
            if int(search_year)>=int(date):
                print(i,".",video_link)
        driver.get("https://web.archive.org/")        
        driver.switch_to.window(window_handles[0])  

            
            
        

    """
    for i in urls:
                  
        for j in i:
            query+=j
            query+=" "
        query=query.replace(' ','+')
        driver.get("https://www.google.com/search?q="+initialprompt+"+"+query+"+"+''.join(s for s in domain_url_exception)+"+-site%3Ashutterstock.com&sxsrf=AOaemvJeytcKjM5D8gP9-5q5XyK6WZD2qg:1631292824077&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiJyJ6Y9Iz8AhVQhmEKHdOBDlQQ_AUoAXoECAEQAw&biw=1366&bih=657")
        driver.implicitly_wait(30)
        first_image=driver.find_element('xpath','//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
        action.move_to_element_with_offset(first_image, 0, 0)
        action.click()
        action.perform()
        time.sleep(3)
        print('image:'+str(i))
        driver.implicitly_wait(30)
        try:
            my_url=driver.find_element("xpath",'//*[@id="islrg"]/div[1]/div[1]/a[2]')
            domain_url_exception.insert(c,"-site%3A"+urlparse(my_url.get_attribute('href')).netloc+"+")
            my_image=driver.find_element("xpath",'//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]')
            print(my_image.get_attribute("src"))
            urls.insert(c,my_image.get_attribute("src"))
        except:
            urls.insert(c,urls[c-1])
        c+=1
    c=0    
    for i in urls:
        try:
            reponse = requests.get(i,headers=headers)
            with open(os.path.join(file_path+file_name+str(c)+".jpg"), 'wb') as file:
                file.write(reponse.content)
                   
        except:    
            first=os.path.join(file_path+file_name+str(c-1)+".jpg")
            second=os.path.join(file_path+file_name+str(c)+".jpg")
            shutil.copyfile(first,second)
        c+=1 
        
        
        
    """
url=input("Playlist URL:")
year=0
year=input("Recherche avant:")
ChromeDriver(url,year)