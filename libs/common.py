from bs4 import BeautifulSoup
import requests
DROP_DOWN_ID = {"product" : "dropdown-products", "updateType" : "dropdown-updatetype", "platform" : "dropdown-platform"}
AZURE_BASEURL = "https://azure.microsoft.com/"
SERVICE_UPDATE_BASEURL = "https://azure.microsoft.com/en-us/updates/"

def parse_drop_downlist():
    '''
    ドロップダウンリストの解析 
    '''
    html = requests.get(SERVICE_UPDATE_BASEURL).text
    soup = BeautifulSoup(html, "html.parser")

    # ドロップダウンのハッシュ
    option_list = {}

    for dropdownId in DROP_DOWN_ID.values():
        select_html = soup.find_all("select", attrs={"id":dropdownId})[0].find_all("option")
        option_list[dropdownId] = {}
        for option in select_html:
            # ALL は除く
            if(option.get("value") == ''):
                continue
            #print(option.text.strip())
            option_list[dropdownId].update({option.text.strip():option.get("value")})

    return option_list


if __name__ == "__main__":
    print(parse_drop_downlist())    
