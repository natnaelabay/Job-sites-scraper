import os
from colorama import init, Fore, Back, Style


print(
    Fore.GREEN
    + """
    _____            __               ______                                                    
   /     |          /  |             /      \                                                   
   $$$$$ |  ______  $$ |____        /$$$$$$  |  _______   ______    ______    ______   __    __ 
      $$ | /      \ $$      \       $$ \__$$/  /       | /      \  /      \  /      \ /  |  /  |
 __   $$ |/$$$$$$  |$$$$$$$  |      $$      \ /$$$$$$$/ /$$$$$$  | $$$$$$  |/$$$$$$  |$$ |  $$ |
/  |  $$ |$$ |  $$ |$$ |  $$ |       $$$$$$  |$$ |      $$ |  $$/  /    $$ |$$ |  $$ |$$ |  $$ |
$$ \__$$ |$$ \__$$ |$$ |__$$ |      /  \__$$ |$$ \_____ $$ |      /$$$$$$$ |$$ |__$$ |$$ \__$$ |
$$    $$/ $$    $$/ $$    $$/       $$    $$/ $$       |$$ |      $$    $$ |$$    $$/ $$    $$ |
 $$$$$$/   $$$$$$/  $$$$$$$/         $$$$$$/   $$$$$$$/ $$/        $$$$$$$/ $$$$$$$/   $$$$$$$ |
                                                                            $$ |      /  \__$$ |
                                                                            $$ |      $$    $$/ 
                                                                            $$/        $$$$$$/  
"""
)


# choose from the different sites

print("Scraping Jobs(Please Wait while we find your dream job!)..🚀🚀🚀🚀")
os.system("scrapy crawl linkedin")
print("Done scraping🏁🏁✅✅")
print()
print("Check http://144.126.247.24 for the results.")
print()
print()