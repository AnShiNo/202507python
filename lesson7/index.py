import tkinter as tk

try:
    import wantgoo
except ImportError:
    raise ImportError("請確保已安裝 wantgoo 模組，或將 wantgoo.py 放在相同目錄下。")

class SimpleApp:
    def __init__(self, root):
        self.root = root
        try:
            self.stock_codes: list[dict] = wantgoo.get_stocks_with_twstock()
            if not isinstance(self.stock_codes, list):
                raise ValueError("wantgoo.get_stocks_with_twstock() 應回傳一個股票字典的 list。")
        except Exception as e:
            self.stock_codes = []
            print(f"取得股票資料時發生錯誤: {e}")


        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="即時股票資訊", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)        
        
        # 建立框架來包含 listbox 和 scrollbar
        frame = tk.Frame(self.root)
        frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        # 建立捲動列
        self.scrollbar = tk.Scrollbar(frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        #self.stock_listbox無法改變寬度,width=50沒有作用
        
        self.stock_listbox = tk.Listbox(frame,
                                        selectmode=tk.MULTIPLE,
                                        yscrollcommand=self.scrollbar.set,
                                        width=15,
                                        height=20)
        
        # 手動插入股票資料
        for stock in self.stock_codes:
            self.stock_listbox.insert(tk.END, f"{stock['code']} - {stock['name']}")
            
        self.stock_listbox.pack(side=tk.LEFT)
        self.scrollbar.config(command=self.stock_listbox.yview)


    


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleApp(root)
    root.mainloop()

    #非同步地從一組網址列表抓取股票資料，使用無頭的Chromium瀏覽器。

    #此函式利用非同步網頁爬蟲，搭配自訂的瀏覽器與執行設定，
    #擷取如日期時間、股票代碼、名稱、即時價格、漲跌、漲跌百分比、
    #開盤價、最高價、成交量、最低價、前一日收盤價等資訊。
    #資料擷取依據 schema 中定義的 CSS 選擇器。

    #參數:
        #urls (list[str]): 要抓取股票資料的網址列表。

    #回傳:
        #list[dict]: 每個網址對應一筆擷取到的股票資訊字典。

    #備註:
        #- 使用 SemaphoreDispatcher 控制並發數量與速率限制。
        #- 爬蟲會等待圖片載入、掃描整頁並滾動延遲。
        #- 擷取策略採用 JSON-CSS，依據 schema 設定。


        #從 twstock 套件取得所有股票清單，並篩選出股票代碼以 '2' 開頭且長度為 4 的股票。

    #回傳:
        #list[dict]: 每筆資料包含以下欄位：
            #- 'code': 股票代碼 (str)
            #- 'name': 股票名稱 (str)
            #- 'market': 市場類型 (str)
            #- 'group': 產業類別 (str)