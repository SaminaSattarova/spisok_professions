from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/list_prof/<list>')
def index(list):
    return render_template('base.html', title='Заготовка', list=list, sp=['Инженер-исследователь', 'Пилот',
                                                                          'Строитель', 'Экзобиолог', 'Врач',
                                                                          'Инженер по терраформированию', 'Климатолог',
                                                                          'Специалист по радиационной защите',
                                                                          'Астрогеолог', 'Гляциолог',
                                                                          'Инженер жизнеобеспечения', 'Метеоролог',
                                                                          'Оператор марсохода', 'Киберинженер',
                                                                          'Штурман', 'Пилот дронов'])


if __name__ == '__main__':
    app.run(port=8065, host='127.0.0.1')