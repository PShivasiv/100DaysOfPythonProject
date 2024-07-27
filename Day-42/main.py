from selenium import webdriver 
from selenium.webdriver.common.by import By


#KEEP THE BROSWER OPEN
chrom_option = webdriver.ChromeOptions()
chrom_option.add_experimental_option("detach",True)

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX6NQMD/ref=sr_1_26?crid=1RRZCMQ0570BY&dib=eyJ2IjoiMSJ9.dVABcK2QHCS6eKC7OM7pMsz8sM3LR3CRWoYKRolMFwom4dNwa2HNimSIR7rIdyzEcREfTIXCh0LNT6FG67fFRaNOtmoamAVE_LmIX1edQTaeZVLCIf0FmPNomVNfeaJz-0t4b4qP3IC97j6HjHGHdk9ZH6cqwU8XTffpuq8DMkb06UFwNGDlgt0h63j0PDE3argCtDmb6QxKMTsy1xmMv4gAq8ep00lKleg9265keAgCBxAm6hTVX19lpbLTXTPW6X2eahba2rvpBYKqsquTe6GYWjHtwjFxSRrMg52ZB7Y.5UhIJ2Od3ca0f9iwRotImPMTz5od82PxxZwYkpC4Y9Y&dib_tag=se&keywords=iphone+15+pro+max&qid=1719218726&sprefix=iphone%2Caps%2C306&sr=8-26")

price = driver.find_element(By.XPATH , value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]')
print(f"The price is {price.text}")

# driver.close()  #is to close one tab at the time 
driver.quit()  # is to close the broswer in once 

