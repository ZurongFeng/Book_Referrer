import pandas as pd
import json

def assign_tags(book):
    mood_map = {
        '愉悦': ['温暖', '幸福', '喜悦', '阳光', '笑', '爱', '甜', '美好', '童话'],
        '轻松': ['轻松', '惬意', '悠闲', '散步', '简单', '有趣', '生活', '日常'],
        '平静': ['平静', '宁静', '思考', '淡定', '安宁', '智慧', '禅', '深邃', '哲学'],
        '振奋': ['力量', '梦想', '拼搏', '热血', '勇气', '奋斗', '改变', '希望', '英雄'],
        '思念': ['思念', '故乡', '回忆', '怀念', '往事', '信', '远方', '故人'],
        '悲伤': ['痛苦', '悲伤', '离别', '沉重', '泪', '死', '葬', '哀', '残缺'],
        '忧郁': ['忧郁', '孤独', '彷徨', '忧伤', '深沉', '夜', '秋', '冷'],
        '倦怠': ['治愈', '休息', '慢生活', '温暖', '停留', '发呆', '安静'],
        '迷茫': ['意义', '寻找', '自我', '迷茫', '困惑', '路', '灯塔', '真实'],
        '孤单': ['陪伴', '灵魂', '对话', '独自', '寂寞', '一个', '影']
    }
    
    weather_map = {
        '晴': ['灿烂', '明媚', '晴朗', '阳光', '夏', '热', '光'],
        '云': ['云', '阴天', '沉静', '天空', '灰', '朦胧'],
        '雨': ['雨', '湿润', '伞', '潮湿', '水', '泪', '洗礼'],
        '雪': ['雪', '冬', '洁白', '寒冷', '冰', '纯净'],
        '风': ['风', '自由', '飞翔', '旷野', '流浪', '远行', '远方']
    }
    
    text = f"{book.get('title', '')} {book.get('sentence', '')} {book.get('author', '')}"
    
    book['moods'] = [m for m, keywords in mood_map.items() if any(k in text for k in keywords)]
    book['weathers'] = [w for w, keywords in weather_map.items() if any(k in text for k in keywords)]
    
    # Ensure at least one random tag if none match to avoid empty pools
    import random
    if not book['moods']:
        book['moods'] = [random.choice(list(mood_map.keys()))]
    if not book['weathers']:
        book['weathers'] = [random.choice(list(weather_map.keys()))]
    
    return book

def convert_excel_to_json(book_path, quote_path, output_path):
    try:
        # Read books and quotes
        df_books = pd.read_excel(book_path).fillna("")
        df_quotes = pd.read_excel(quote_path).fillna("")
        
        books = df_books.to_dict(orient='records')
        quotes = df_quotes.to_dict(orient='records')
        
        # Fill empty sentences with random quotes
        import random
        for book in books:
            if not book.get('sentence') or str(book.get('sentence')).strip() == "":
                if quotes:
                    q = random.choice(quotes)
                    book['sentence'] = f"{q['Quote']}<br>——{q['Author']}"
                else:
                    book['sentence'] = "读书足以怡情，足以博彩，足以长才。<br>——培根"
            
            # Assign mood and weather tags
            assign_tags(book)
                
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(books, f, ensure_ascii=False, indent=2)
        print(f"Successfully converted {len(books)} books with tags to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    convert_excel_to_json('book_250.xlsx', 'Quote.xlsx', 'books.json')
