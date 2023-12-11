from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymysql

from pydantic import BaseModel
app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MySQL 연결 설정
db = pymysql.connect(
    host="db",
    user="april0ys",
    password="0560",
    database="grocery_shopping_guessing_game",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)
cursor = db.cursor()


# Model

class Bulletin(BaseModel):
    title: str
    cooking: str
    ingredients: str
    
class Note(BaseModel):
    bulletin_id: int
    user: str
    ingredient: str
    re_ingredient: str
    state: int

# 게시판 조회 API
@app.get('/bulletins')
async def get_bulletins():
    cursor.execute("SELECT * FROM bulletins")
    bulletins = cursor.fetchall()
    return bulletins

# 게시판 작성 API
@app.post('/bulletins')
async def create_bulletin(bulletin: Bulletin):
    cursor.execute("INSERT INTO bulletins (title, cooking, ingredients) VALUES (%s, %s, %s)", (bulletin.title, '', ''))
    db.commit()
    return {'message': '게시판이 만들어졌습니다.'}

# 게시판 수정 API
@app.put('/bulletins/{bulletin_id}')
async def update_bulletin(bulletin_id: int, bulletin: Bulletin):
    cursor.execute("UPDATE bulletins SET title = %s, cooking = %s, ingredients = %s WHERE id = %s", (bulletin.title, bulletin.cooking, bulletin.ingredients, bulletin_id))
    db.commit()
    return {'message': '게시판이 업데이트되었습니다.'}

# 게시판 삭제 API
@app.delete('/bulletins/{bulletin_id}')
async def delete_bulletin(bulletin_id: int):
    cursor.execute("DELETE FROM bulletins WHERE id = %s", bulletin_id)
    db.commit()
    return {'message': '게시판이 삭제되었습니다.'}


# 게시물 조회 API
@app.get('/bulletins/{bulletin_id}')
async def get_note(bulletin_id: int):
    cursor.execute("SELECT * FROM notes WHERE bulletin_id = %s", (bulletin_id))
    bulletin = cursor.fetchall()
    return bulletin

# 게시물 작성 API
@app.post('/bulletins/{bulletin_id}')
async def create_note(bulletin_id: int, note: Note):
    cursor.execute("INSERT INTO notes (bulletin_id, user, ingredient, re_ingredient, state) VALUES (%s, %s, %s, %s, %s)", (bulletin_id, note.user, note.ingredient, '', 0))
    db.commit()
    return {'message': '게시물이 만들어졌습니다.'}

# 게시물 수정 API
@app.put('/notes/{note_id}')
async def update_note(note_id: int, note: Note):
    cursor.execute("UPDATE notes SET user = %s, ingredient = %s, re_ingredient = %s, state = %s WHERE id = %s", (note.user, note.ingredient, note.re_ingredient, note.state, note_id))
    db.commit()
    return {'message': '게시물이 업데이트되었습니다.'}

# 게시물 삭제 API
@app.delete('/note/{bulletin_id}')
async def delete_note(note_id: int):
    cursor.execute("DELETE FROM notes WHERE id = %s", note_id)
    db.commit()
    return {'message': '게시판이 삭제되었습니다.'}

# FastAPI 종료 시 MySQL 연결 닫기
@app.on_event("shutdown")
def shutdown_event():
    db.close()