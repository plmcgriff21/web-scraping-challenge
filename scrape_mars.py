{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import Dependencies\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from splinter import Browser\n",
    "import requests\n",
    "import pymongo\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Initialize PyMongo to work with MongoDBs\n",
    "conn='mongodb://localhost:27017'\n",
    "client= pymongo.MongoClient(conn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Define DB and Collection \n",
    "db=client.nasa_db\n",
    "collection=db.articles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<div class=\"image_and_description_container\">\n",
       " <a href=\"/news/8749/nasa-readies-perseverance-mars-rovers-earthly-twin/\">\n",
       " <div class=\"rollover_description\">\n",
       " <div class=\"rollover_description_inner\">\n",
       " Did you know NASA's next Mars rover has a nearly identical sibling on Earth for testing? Even better, it's about to roll for the first time through a replica Martian landscape.\n",
       " </div>\n",
       " <div class=\"overlay_arrow\">\n",
       " <img alt=\"More\" src=\"/assets/overlay-arrow.png\"/>\n",
       " </div>\n",
       " </div>\n",
       " <img alt=\"NASA Readies Perseverance Mars Rover's Earthly Twin \" class=\"img-lazy\" data-lazy=\"/system/news_items/list_view_images/8749_PIA23964-320.jpg\" src=\"/assets/loading_320x240.png\"/>\n",
       " </a>\n",
       " </div>,\n",
       " <div class=\"image_and_description_container\">\n",
       " <a href=\"/news/8716/nasa-to-broadcast-mars-2020-perseverance-launch-prelaunch-activities/\">\n",
       " <div class=\"rollover_description\">\n",
       " <div class=\"rollover_description_inner\">\n",
       " Starting July 27, news activities will cover everything from mission engineering and science to returning samples from Mars to, of course, the launch itself.\n",
       " </div>\n",
       " <div class=\"overlay_arrow\">\n",
       " <img alt=\"More\" src=\"/assets/overlay-arrow.png\"/>\n",
       " </div>\n",
       " </div>\n",
       " <img alt=\"NASA to Broadcast Mars 2020 Perseverance Launch, Prelaunch Activities\" class=\"img-lazy\" data-lazy=\"/system/news_items/list_view_images/8716_PIA23499-320x240.jpg\" src=\"/assets/loading_320x240.png\"/>\n",
       " </a>\n",
       " </div>,\n",
       " <div class=\"image_and_description_container\">\n",
       " <a href=\"/news/8695/the-launch-is-approaching-for-nasas-next-mars-rover-perseverance/\">\n",
       " <div class=\"rollover_description\">\n",
       " <div class=\"rollover_description_inner\">\n",
       " The Red Planet's surface has been visited by eight NASA spacecraft. The ninth will be the first that includes a roundtrip ticket in its flight plan. \n",
       " </div>\n",
       " <div class=\"overlay_arrow\">\n",
       " <img alt=\"More\" src=\"/assets/overlay-arrow.png\"/>\n",
       " </div>\n",
       " </div>\n",
       " <img alt=\"The Launch Is Approaching for NASA's Next Mars Rover, Perseverance\" class=\"img-lazy\" data-lazy=\"/system/news_items/list_view_images/8695_24732_PIA23499-226.jpg\" src=\"/assets/loading_320x240.png\"/>\n",
       " </a>\n",
       " </div>,\n",
       " <div class=\"image_and_description_container\">\n",
       " <a href=\"/news/8692/nasa-to-hold-mars-2020-perseverance-rover-launch-briefing/\">\n",
       " <div class=\"rollover_description\">\n",
       " <div class=\"rollover_description_inner\">\n",
       " Learn more about the agency's next Red Planet mission during a live event on June 17.\n",
       " </div>\n",
       " <div class=\"overlay_arrow\">\n",
       " <img alt=\"More\" src=\"/assets/overlay-arrow.png\"/>\n",
       " </div>\n",
       " </div>\n",
       " <img alt=\"NASA to Hold Mars 2020 Perseverance Rover Launch Briefing\" class=\"img-lazy\" data-lazy=\"/system/news_items/list_view_images/8692_PIA23920-320x240.jpg\" src=\"/assets/loading_320x240.png\"/>\n",
       " </a>\n",
       " </div>,\n",
       " <div class=\"image_and_description_container\">\n",
       " <a href=\"/news/8659/alabama-high-school-student-names-nasas-mars-helicopter/\">\n",
       " <div class=\"rollover_description\">\n",
       " <div class=\"rollover_description_inner\">\n",
       " Vaneeza Rupani's essay was chosen as the name for the small spacecraft, which will mark NASA's first attempt at powered flight on another planet.\n",
       " </div>\n",
       " <div class=\"overlay_arrow\">\n",
       " <img alt=\"More\" src=\"/assets/overlay-arrow.png\"/>\n",
       " </div>\n",
       " </div>\n",
       " <img alt=\"Alabama High School Student Names NASA's Mars Helicopter\" class=\"img-lazy\" data-lazy=\"/system/news_items/list_view_images/8659_1-PIA23883-MAIN-320x240.jpg\" src=\"/assets/loading_320x240.png\"/>\n",
       " </a>\n",
       " </div>,\n",
       " <div class=\"image_and_description_container\">\n",
       " <a href=\"/news/8645/mars-helicopter-attached-to-nasas-perseverance-rover/\">\n",
       " <div class=\"rollover_description\">\n",
       " <div class=\"rollover_description_inner\">\n",
       " The team also fueled the rover's sky crane to get ready for this summer's history-making launch.\n",
       " </div>\n",
       " <div class=\"overlay_arrow\">\n",
       " <img alt=\"More\" src=\"/assets/overlay-arrow.png\"/>\n",
       " </div>\n",
       " </div>\n",
       " <img alt=\"Mars Helicopter Attached to NASA's Perseverance Rover\" class=\"img-lazy\" data-lazy=\"/system/news_items/list_view_images/8645_PIA23824-RoverWithHelicopter-32x24.jpg\" src=\"/assets/loading_320x240.png\"/>\n",
       " </a>\n",
       " </div>]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Second URL to be scraped \n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "#Retrieve page with requests module\n",
    "response=requests.get(url)\n",
    "#Create BS object class_='content_title'\n",
    "soup=bs(response.text,'html.parser')\n",
    "results=soup.find_all('div',class_='image_and_description_container')\n",
    "results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "headers=[]\n",
    "teasers=[]\n",
    "\n",
    "for result in results:\n",
    "    headers.append(result.text)\n",
    "    teasers.append(result.find_all('div','rollover_description_inner'))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[\"\\n\\n\\n\\nDid you know NASA's next Mars rover has a nearly identical sibling on Earth for testing? Even better, it's about to roll for the first time through a replica Martian landscape.\\n\\n\\n\\n\\n\\n\\n\\n\",\n",
       " '\\n\\n\\n\\nStarting July 27, news activities will cover everything from mission engineering and science to returning samples from Mars to, of course, the launch itself.\\n\\n\\n\\n\\n\\n\\n\\n',\n",
       " \"\\n\\n\\n\\nThe Red Planet's surface has been visited by eight NASA spacecraft. The ninth will be the first that includes a roundtrip ticket in its flight plan. \\n\\n\\n\\n\\n\\n\\n\\n\",\n",
       " \"\\n\\n\\n\\nLearn more about the agency's next Red Planet mission during a live event on June 17.\\n\\n\\n\\n\\n\\n\\n\\n\",\n",
       " \"\\n\\n\\n\\nVaneeza Rupani's essay was chosen as the name for the small spacecraft, which will mark NASA's first attempt at powered flight on another planet.\\n\\n\\n\\n\\n\\n\\n\\n\",\n",
       " \"\\n\\n\\n\\nThe team also fueled the rover's sky crane to get ready for this summer's history-making launch.\\n\\n\\n\\n\\n\\n\\n\\n\"]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "headers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[<div class=\"rollover_description_inner\">\n",
       "  Did you know NASA's next Mars rover has a nearly identical sibling on Earth for testing? Even better, it's about to roll for the first time through a replica Martian landscape.\n",
       "  </div>],\n",
       " [<div class=\"rollover_description_inner\">\n",
       "  Starting July 27, news activities will cover everything from mission engineering and science to returning samples from Mars to, of course, the launch itself.\n",
       "  </div>],\n",
       " [<div class=\"rollover_description_inner\">\n",
       "  The Red Planet's surface has been visited by eight NASA spacecraft. The ninth will be the first that includes a roundtrip ticket in its flight plan. \n",
       "  </div>],\n",
       " [<div class=\"rollover_description_inner\">\n",
       "  Learn more about the agency's next Red Planet mission during a live event on June 17.\n",
       "  </div>],\n",
       " [<div class=\"rollover_description_inner\">\n",
       "  Vaneeza Rupani's essay was chosen as the name for the small spacecraft, which will mark NASA's first attempt at powered flight on another planet.\n",
       "  </div>],\n",
       " [<div class=\"rollover_description_inner\">\n",
       "  The team also fueled the rover's sky crane to get ready for this summer's history-making launch.\n",
       "  </div>]]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "teasers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Second URL to be scraped \n",
    "url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "#Retrieve page with requests module\n",
    "response2=requests.get(url2)\n",
    "#Create BS object class_='content_title'\n",
    "soup2=bs(response2.text,'html.parser')\n",
    "results2=soup2.find_all('a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "browser.visit(url2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "full_image_elem = browser.find_by_id('full_image')\n",
    "full_image_elem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "more_info = browser.links.find_by_partial_text('more info')\n",
    "more_info.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create BS object class_='content_title'\n",
    "html=browser.html\n",
    "soup=bs(html,'html.parser')\n",
    "#results3=soup.find_all('div',class_='image_and_description_container')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'/spaceimages/images/largesize/PIA16239_hires.jpg'"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "results3 = soup.select_one('div article figure a img').get('src')\n",
    "results3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url3 = 'https://space-facts.com/mars/'\n",
    "browser.visit(url3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\porti\\anaconda3\\lib\\site-packages\\bs4\\__init__.py:389: UserWarning: \"https://space-facts.com/mars/\" looks like a URL. Beautiful Soup is not an HTTP client. You should probably use an HTTP client like requests to get the document behind the URL, and feed that document to Beautiful Soup.\n",
      "  ' that document to Beautiful Soup.' % decoded_markup\n"
     ]
    }
   ],
   "source": [
    "soup3=bs(url3,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Mars</th>\n",
       "      <th>Earth</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mars - Earth Comparison</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Diameter:</th>\n",
       "      <td>6,779 km</td>\n",
       "      <td>12,742 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.39 × 10^23 kg</td>\n",
       "      <td>5.97 × 10^24 kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Distance from Sun:</th>\n",
       "      <td>227,943,824 km</td>\n",
       "      <td>149,598,262 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Length of Year:</th>\n",
       "      <td>687 Earth days</td>\n",
       "      <td>365.24 days</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Temperature:</th>\n",
       "      <td>-87 to -5 °C</td>\n",
       "      <td>-88 to 58°C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                    Mars            Earth\n",
       "Mars - Earth Comparison                                  \n",
       "Diameter:                       6,779 km        12,742 km\n",
       "Mass:                    6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       "Moons:                                 2                1\n",
       "Distance from Sun:        227,943,824 km   149,598,262 km\n",
       "Length of Year:           687 Earth days      365.24 days\n",
       "Temperature:                -87 to -5 °C      -88 to 58°C"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_html(url3)\n",
    "new_df=df[1]\n",
    "new_df.set_index(\"Mars - Earth Comparison\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Cerberus Region\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Response [200]>"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Retrieve page with requests module\n",
    "response4=requests.get(url4)\n",
    "response4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\porti\\anaconda3\\lib\\site-packages\\bs4\\__init__.py:389: UserWarning: \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\" looks like a URL. Beautiful Soup is not an HTTP client. You should probably use an HTTP client like requests to get the document behind the URL, and feed that document to Beautiful Soup.\n",
      "  ' that document to Beautiful Soup.' % decoded_markup\n"
     ]
    }
   ],
   "source": [
    "#Create BS object class_='content_title'\n",
    "soup4=bs(url4,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<h3>Cerberus Hemisphere Enhanced</h3>"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "image4_title = soup4.find_all('h3')\n",
    "new_image4_title = image4_title[0]\n",
    "new_image4_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "more_info_cerberus_hem = browser.find_by_text(\"Cerberus Hemisphere Enhanced\")\n",
    "more_info_cerberus_hem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "cerberus_hem_full = browser.find_by_text(\"Sample\")\n",
    "full_cerberus_image = cerberus_hem_full.click()\n",
    "full_cerberus_image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Schiaparelli Region\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<h3>Schiaparelli Hemisphere Enhanced</h3>"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "image5_title = soup4.find_all('h3')\n",
    "new_image5_title = image4_title[1]\n",
    "new_image5_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "more_info_schiaparelli_hem = browser.find_by_text(\"Schiaparelli Hemisphere Enhanced\")\n",
    "more_info_schiaparelli_hem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "schiaparelli_hem_full = browser.find_by_text(\"Sample\")\n",
    "full_schiaparelli_image = schiaparelli_hem_full.click()\n",
    "full_schiaparelli_image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Syrtis Major Region\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<h3>Syrtis Major Hemisphere Enhanced</h3>"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "image5_title = soup4.find_all('h3')\n",
    "new_image5_title = image4_title[2]\n",
    "new_image5_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "more_info_syrtis_hem = browser.find_by_text(\"Syrtis Major Hemisphere Enhanced\")\n",
    "more_info_syrtis_hem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "syrtis_hem_full = browser.find_by_text(\"Sample\")\n",
    "full_syrtis_image = syrtis_hem_full.click()\n",
    "full_syrtis_image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Valles Marineris Hemisphere Enhanced\n",
    "executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<h3>Valles Marineris Hemisphere Enhanced</h3>"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "image5_title = soup4.find_all('h3')\n",
    "new_image5_title = image4_title[3]\n",
    "new_image5_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "more_info_valles_hem = browser.find_by_text(\"Valles Marineris Hemisphere Enhanced\")\n",
    "more_info_valles_hem.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "valles_hem_full = browser.find_by_text(\"Sample\")\n",
    "full_valles_image = valles_hem_full.click()\n",
    "full_valles_image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
