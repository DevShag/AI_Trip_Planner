import os
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSeachTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv


class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get('GPLACES_API_KEY')
        #self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSeachTool()
        self.place_search_tool_list = self._setup_tools()


    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""

        @tool
        def search_attractions(place:str) -> str:
            """Search attanctions of a place"""
            try:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Following are the attractions of {place} suggested by tavily : {tavily_result}"

            except Exception as e:
                return f"Google cannot find the details due to {e}"

        @tool
        def search_restaurancts(place : str) -> str:
            """Search restaurants of a place"""
            try:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                if tavily_result:
                    return f"Following are the restaurants of {place} as suggested by google: {tavily_result}"
            except Exception as e:
                return f"Tavily cannot find the details due to {e}."


        @tool
        def search_activities(place:str) -> str:
            "Search activities of a place"
            try:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Following are the mode of transportation available in {place} as suggested by tavily : {tavily_result}"
            except Exception as e:
                return f"Tavily can not find the details due to {e} "


        @tool
        def search_transportation(place : str) -> str:
            """Search transportation of a place"""
            try:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                if tavily_result:
                    return f"Following are the modes of transportation available in {place} as suggested by tavily : {tavily_result}"
            except Exception as e:
                return f"Tavily cannot find the details due to {e}."


        return [search_attractions, search_restaurancts, search_activities, search_transportation]
            

            