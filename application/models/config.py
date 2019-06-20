import web

db_host = 'd5x4ae6ze2og6sjo.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'tbrbsew4oxpusjq5'
db_user = 'e0vm3eyg1zui6b5e'
db_pw = 'yc1pzpj3t0mptnt9'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )