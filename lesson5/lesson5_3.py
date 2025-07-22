import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    #建立一個AsyncWebCrawler的實體
    async with AsyncWebCrawler() as crawler:
        #Run the crawler on a URL
        url = 'https://tw.news.yahoo.com/%E4%BD%8E%E5%A3%93%E5%B8%B6%E6%8C%81%E7%BA%8C%E5%BD%B1%E9%9F%BF%E5%8F%B0%E7%81%A3%E8%87%B3%E4%B8%8B%E9%80%B1-%E9%A2%B1%E9%A2%A8-%E8%8C%83%E6%96%AF%E9%AB%98-%E6%9C%AC%E9%80%B1%E5%8F%AF%E6%81%90%E7%94%9F%E6%88%90%E4%B8%8D%E6%8E%92%E9%99%A4%E9%9B%99%E9%A2%B1-235304436.html?guccounter=1&guce_referrer=aHR0cHM6Ly9uZXdzLmdvb2dsZS5jb20v&guce_referrer_sig=AQAAAFduxk0ZvDH-BFCy8ow7RCP6l90cS7aXN-kCczV3Tz1lK8tQqcgaconMfYiMm7X-J0Q4Opebhx0K74KlZLmmVpe9At0dhhnzns-zr08r6YH9GKRFwh1oiq1Hu6zx6mdphyF_v81pImJJCtago6zOOKhCp52dG5QAimBBR7LhVpVj'
        result = await crawler.arun(url=urldue)
        print(type(result))
        print("=" * 20)        

        #列印取出的結果
        
        print(result.markdown.raw_markdown[:200])
        

if __name__ == "__main__":
    asyncio.run(main())