from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="eduSelect">Какое у Вас образование ?</label>
                                        <select class="form-control" id="eduSelect" name="education">
                                          <option>Дошкольное</option>
                                          <option>Начальное общее</option>
                                          <option>Основное общее</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее I степени</option>
                                          <option>Высшее II степени</option>
                                          <option>Высшее III степени</option>
                                        </select>
                                    </div>
                                    <br>
                                    <label for="professions">Какие у Вас есть профессии ?</label>
                                    <div class="form-group">
                                        <label>
                                            <input type="checkbox" class="form-check-input" name="professions">
                                            Инженер-исследователь
                                        </label>
                                        <br>
                                        <label>
                                            <input type="checkbox" class="form-check-input" name="professions">
                                            Инженер-строитель
                                        </label>
                                        <br>
                                        <label>
                                            <input type="checkbox" class="form-check-input" name="professions">
                                            Пилот
                                        </label>
                                        <br>
                                        <label>
                                            <input type="checkbox" class="form-check-input" name="professions">
                                            Метеоролог
                                        </label>
                                        <br>
                                        <label>
                                            <input type="checkbox" class="form-check-input" name="professions">
                                            Инженер по радиационной защите
                                        </label>
                                        <br>
                                        <label>
                                            <input type="checkbox" class="form-check-input" name="professions">
                                            Bpaч
                                        </label>
                                        <br>
                                        <label>
                                            <input type="checkbox" class="form-check-input" name="professions">
                                            Экзобиолог
                                        </label>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                            <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                            <label class="form-check-label" for="female">
                                            Женский
                                            </label>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии ?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе ?</label>
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
