from flask import Flask, render_template, request, jsonify
import dmPython

import config

connect = dmPython.Connection(host=config.host, port=config.port, user=config.user, password=config.password)
cursor = connect.cursor()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('shaixuan2.html')


@app.route('/departments')
def departments():
    cursor.execute('select orgname from "XXCX"."PERSONS" group by orgname')
    departments = []
    try:
        # 获取查询结果
        rows = cursor.fetchall()
        # 将结果添加到列表中
        for row in rows:
            departments.append(row[0])
        # print(departments)
    except Exception as e:
        # 如果有错误发生，返回错误信息
        return jsonify({"error": str(e)}), 500
        # 使用jsonify将Python列表转换为JSON格式的响应
    print(departments)
    return jsonify(departments)


@app.route('/department')
def department():
    persons = []
    department_name = request.args.get('department', '')
    print(department_name)
    cursor.execute(
        'select id, personname, orgname, duty, gender, birthday, nation, nativeplace, joinworktime, joinpartytime, shortintroduction, resume, picurl, photo, edulevel from "XXCX"."PERSONS" where orgname = ?',
        (department_name,))
    datas = cursor.fetchall()
    for data in datas:
        leader = {
            'id': data[0],
            'personname': data[1],
            'orgname': data[2],
            'duty': data[3],
            'gender': data[4],
            'birthday': data[5],
            'nation': data[6],
            'nativeplace': data[7],
            'joinworktime': data[8],
            'joinpartytime': data[9],
            'shortintroduction': data[10],
            'resume': data[11],
            'picurl': data[12],
            'photo': data[13],
            'edulevel': data[14]
        }
        persons.append(leader)
    # for num in range(0, 5):
    #     try:
    #         print(persons[num])
    #     except:
    #         continue
    return jsonify(persons)  # 将领导信息以JSON格式返回


@app.route('/person')
def leader():
    persons = []
    person_name = request.args.get('person', '')
    print(person_name)
    cursor.execute(
        'select id, personname, orgname, duty, gender, birthday, nation, nativeplace, joinworktime, joinpartytime, shortintroduction, resume, picurl, photo, edulevel from "XXCX"."PERSONS" where personname like ? ',
        ('%' + person_name + '%',))
    datas = cursor.fetchall()
    for data in datas:
        leader = {
            'id': data[0],
            'personname': data[1],
            'orgname': data[2],
            'duty': data[3],
            'gender': data[4],
            'birthday': data[5],
            'nation': data[6],
            'nativeplace': data[7],
            'joinworktime': data[8],
            'joinpartytime': data[9],
            'shortintroduction': data[10],
            'resume': data[11],
            'picurl': data[12],
            'photo': data[13],
            'edulevel': data[14]
                  }
        persons.append(leader)
    # for num in range(0, 5):
    #     try:
    #         print(persons[num])
    #     except:
    #         continue
    return jsonify(persons)


@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    dataId = data['dataId']
    index = data['index']
    updateStr = data['updateStr']
    print(data)
    if index == 2:
        cursor.execute('update "XXCX"."PERSONS" set personname = ? where id = ? ', (updateStr, dataId))
    elif index == 3:
        cursor.execute('update "XXCX"."PERSONS" set orgname = ? where id = ? ', (updateStr, dataId))
    elif index == 4:
        cursor.execute('update "XXCX"."PERSONS" set duty = ? where id = ? ', (updateStr, dataId))
    elif index == 5:
        cursor.execute('update "XXCX"."PERSONS" set gender = ? where id = ? ', (updateStr, dataId))
    elif index == 6:
        cursor.execute('update "XXCX"."PERSONS" set birthday = ? where id = ? ', (updateStr, dataId))
    elif index == 7:
        cursor.execute('update "XXCX"."PERSONS" set nation = ? where id = ? ', (updateStr, dataId))
    elif index == 8:
        cursor.execute('update "XXCX"."PERSONS" set nativeplace = ? where id = ? ', (updateStr, dataId))
    elif index == 9:
        cursor.execute('update "XXCX"."PERSONS" set joinworktime = ? where id = ? ', (updateStr, dataId))
    elif index == 10:
        cursor.execute('update "XXCX"."PERSONS" set joinpartytime = ? where id = ? ', (updateStr, dataId))
    elif index == 11:
        cursor.execute('update "XXCX"."PERSONS" set shortintroduction = ? where id = ? ', (updateStr, dataId))
    elif index == 12:
        cursor.execute('update "XXCX"."PERSONS" set resume = ? where id = ? ', (updateStr, dataId))
    elif index == 13:
        cursor.execute('update "XXCX"."PERSONS" set edulevel = ? where id = ? ', (updateStr, dataId))
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
